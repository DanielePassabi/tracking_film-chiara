from __future__ import annotations

import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
SITE_DATA = ROOT / "site" / "data" / "polpetta-data.json"
POSTERS_DIR = ROOT / "site" / "assets" / "movie-posters"
POSTERS_JSON = ROOT / "site" / "data" / "movie-posters.json"
MATCH_REPORT = ROOT / "docs" / "MOVIE_POSTER_MATCHES.md"

WIKIPEDIA_API = "https://en.wikipedia.org/w/api.php"
OMDB_API = "https://www.omdbapi.com/"
OMDB_API_KEY = "trilogy"

QUERY_OVERRIDES = {
    "기생충": "Parasite 2019 film",
    "(500) Days of Summer": "500 Days of Summer film",
    "Harry Potter 20th Anniversary: Return to Hogwarts": "Harry Potter 20th Anniversary Return to Hogwarts film",
    "All Too Well: The Short Film": "All Too Well The Short Film",
    "Taylor Swift: The 1989 World Tour - Live": "The 1989 World Tour Live Taylor Swift film",
    "Marvel Studios Assembled: The Making of She-Hulk: Attorney at Law": "Marvel Studios Assembled She-Hulk Attorney at Law",
    "Taylor Swift City of Lover Concert": "Taylor Swift City of Lover concert film",
    "Miley Cyrus – Endless Summer Vacation (Backyard Sessions)": "Miley Cyrus Endless Summer Vacation Backyard Sessions",
}

OMDB_TITLE_OVERRIDES = {
    "기생충": "Parasite",
    "(500) Days of Summer": "500 Days of Summer",
    "Birds of Prey (and the Fantabulous Emancipation of One Harley Quinn)": "Birds of Prey and the Fantabulous Emancipation of One Harley Quinn",
    "Dark Phoenix": "X-Men: Dark Phoenix",
    "Le Fabuleux destin d'Amélie Poulain": "Amelie",
    "Harry Potter and the Philosopher's Stone": "Harry Potter and the Sorcerer's Stone",
    "Star Wars: The Rise of Skywalker": "Star Wars: Episode IX - The Rise of Skywalker",
    "Hotel Transylvania: Transformania": "Hotel Transylvania 4: Transformania",
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "movie"


def normalize(value: str) -> str:
    value = value.lower()
    value = value.replace("&", "and")
    value = re.sub(r"\([^)]*\)", "", value)
    value = re.sub(r"[^a-z0-9]+", "", value)
    return value


def omdb_title(item: dict[str, Any]) -> str:
    return OMDB_TITLE_OVERRIDES.get(item["name"], item["name"])


def acceptable_omdb_match(item: dict[str, Any], payload: dict[str, Any]) -> bool:
    target = normalize(omdb_title(item))
    matched = normalize(payload.get("Title", ""))
    return bool(target and matched == target)


def movie_query(item: dict[str, Any]) -> str:
    name = item["name"]
    if name in QUERY_OVERRIDES:
        return QUERY_OVERRIDES[name]
    year = item.get("releaseYear")
    if year:
        return f"{name} {year} film"
    return f"{name} film"


def fetch_json(params: dict[str, str | int]) -> Any:
    query = urllib.parse.urlencode(params)
    request = urllib.request.Request(
        f"{WIKIPEDIA_API}?{query}",
        headers={
            "User-Agent": "polpetta-movie-poster-fetch/1.0",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def download(url: str, out_path: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "polpetta-movie-poster-fetch/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        out_path.write_bytes(response.read())


def fetch_omdb(item: dict[str, Any]) -> tuple[dict[str, Any] | None, str]:
    title = omdb_title(item)
    attempts = []
    if item.get("releaseYear"):
        attempts.append(("omdb-year", {"apikey": OMDB_API_KEY, "t": title, "y": item["releaseYear"]}))
    attempts.append(("omdb-title", {"apikey": OMDB_API_KEY, "t": title}))

    for match_type, params in attempts:
        request = urllib.request.Request(
            f"{OMDB_API}?{urllib.parse.urlencode(params)}",
            headers={
                "User-Agent": "polpetta-movie-poster-fetch/1.0",
                "Accept": "application/json",
            },
        )
        with urllib.request.urlopen(request, timeout=20) as response:
            payload = json.loads(response.read().decode("utf-8"))
        poster = payload.get("Poster", "")
        if payload.get("Response") == "True" and poster and poster != "N/A" and acceptable_omdb_match(item, payload):
            return payload, match_type

    return None, "omdb-not-found"


def extension_from_url(url: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    return ".jpg"


def search_pages(query: str) -> list[dict[str, Any]]:
    payload = fetch_json(
        {
            "action": "query",
            "list": "search",
            "srsearch": query,
            "srlimit": 6,
            "format": "json",
        }
    )
    return payload.get("query", {}).get("search", [])


def page_images(page_ids: list[int]) -> dict[int, dict[str, Any]]:
    if not page_ids:
        return {}
    payload = fetch_json(
        {
            "action": "query",
            "pageids": "|".join(str(page_id) for page_id in page_ids),
            "prop": "pageimages|info",
            "pithumbsize": 520,
            "inprop": "url",
            "format": "json",
        }
    )
    pages = payload.get("query", {}).get("pages", {})
    return {int(page_id): page for page_id, page in pages.items()}


def choose_match(item: dict[str, Any], search_results: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, str]:
    if not search_results:
        return None, "not-found"

    target = normalize(item["name"])
    year = str(item.get("releaseYear") or "")
    images = page_images([result["pageid"] for result in search_results])
    candidates = [
        {**result, **images.get(result["pageid"], {})}
        for result in search_results
        if images.get(result["pageid"], {}).get("thumbnail", {}).get("source")
    ]
    if not candidates:
        return None, "no-image"

    for candidate in candidates:
        title_norm = normalize(candidate.get("title", ""))
        if title_norm == target or title_norm == f"{target}film":
            return candidate, "exact"

    for candidate in candidates:
        if target in normalize(candidate.get("title", "")):
            return candidate, "title"

    return None, "ambiguous"


def build() -> dict[str, Any]:
    data = json.loads(SITE_DATA.read_text(encoding="utf-8"))
    movies = data.get("movies", {}).get("items", [])
    POSTERS_DIR.mkdir(parents=True, exist_ok=True)
    POSTERS_JSON.parent.mkdir(parents=True, exist_ok=True)
    MATCH_REPORT.parent.mkdir(parents=True, exist_ok=True)

    records = []
    for index, item in enumerate(movies, start=1):
        name = item["name"]
        query = movie_query(item)
        status = "ok"
        match_type = ""
        matched_name = ""
        page_id = None
        poster_url = ""
        local_path = ""
        source_url = ""

        try:
            omdb_match, match_type = fetch_omdb(item)
            match = None
            if omdb_match:
                matched_name = omdb_match.get("Title", "")
                page_id = omdb_match.get("imdbID")
                source_url = f"https://www.imdb.com/title/{page_id}/" if page_id else ""
                poster_url = omdb_match.get("Poster", "")
                out_path = POSTERS_DIR / f"{slugify(name)}{extension_from_url(poster_url)}"
                download(poster_url, out_path)
                local_path = f"./assets/movie-posters/{out_path.name}"
            else:
                results = search_pages(query)
                match, match_type = choose_match(item, results)

            if not local_path and match:
                matched_name = match.get("title", "")
                page_id = match.get("pageid")
                source_url = match.get("fullurl", "")
                poster_url = match.get("thumbnail", {}).get("source", "")
                if poster_url:
                    out_path = POSTERS_DIR / f"{slugify(name)}{extension_from_url(poster_url)}"
                    download(poster_url, out_path)
                    local_path = f"./assets/movie-posters/{out_path.name}"
                else:
                    status = "no-image"
            elif not local_path:
                status = match_type
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            status = f"error: {exc.__class__.__name__}"

        records.append(
            {
                "name": name,
                "query": query,
                "status": status,
                "matchType": match_type,
                "matchedName": matched_name,
                "wikipediaPageId": page_id,
                "posterUrl": poster_url,
                "localPath": local_path,
                "sourceUrl": source_url,
            }
        )

        print(f"[{index:03}/{len(movies)}] {name} -> {matched_name or status} ({match_type or status})")
        time.sleep(0.08)

    payload = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "source": "OMDb + Wikipedia fallback",
        "sourceApi": f"{OMDB_API} / {WIKIPEDIA_API}",
        "records": records,
    }
    POSTERS_JSON.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")
    MATCH_REPORT.write_text(render_report(payload), encoding="utf-8")
    return payload


def render_report(payload: dict[str, Any]) -> str:
    records = payload["records"]
    with_images = [item for item in records if item["localPath"]]
    needs_review = [
        item
        for item in records
        if not item["localPath"] or item["matchType"] not in {"omdb-year", "omdb-title", "exact", "title"}
    ]

    lines = [
        "# Movie Poster Matches",
        "",
        f"Fonte: OMDb API con fallback Wikipedia (`{payload['sourceApi']}`).",
        "",
        f"- Film totali: {len(records)}",
        f"- Poster locali trovati: {len(with_images)}",
        f"- Da rivedere: {len(needs_review)}",
        "",
        "## Match da rivedere",
        "",
        "| Film | Query | Match | Stato |",
        "| --- | --- | --- | --- |",
    ]
    for item in needs_review:
        lines.append(
            f"| {item['name']} | {item['query']} | {item['matchedName'] or '-'} | {item['status']} / {item['matchType']} |"
        )

    lines.extend(["", "## Tutti i match", "", "| Film | Match | Tipo | Poster |", "| --- | --- | --- | --- |"])
    for item in records:
        poster = "si" if item["localPath"] else "no"
        lines.append(f"| {item['name']} | {item['matchedName'] or '-'} | {item['matchType']} | {poster} |")

    return "\n".join(lines) + "\n"


def main() -> None:
    payload = build()
    with_images = sum(1 for item in payload["records"] if item["localPath"])
    print(f"Poster locali: {with_images}/{len(payload['records'])}")
    print(f"Report: {MATCH_REPORT}")


if __name__ == "__main__":
    main()
