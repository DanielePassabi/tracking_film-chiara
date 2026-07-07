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
POSTERS_DIR = ROOT / "site" / "assets" / "posters"
POSTERS_JSON = ROOT / "site" / "data" / "posters.json"
MATCH_REPORT = ROOT / "docs" / "POSTER_MATCHES.md"

TVMAZE_SEARCH_URL = "https://api.tvmaze.com/search/shows?q="

QUERY_OVERRIDES = {
    "Mercoledì": "Wednesday",
    "The Office (US)": "The Office US",
    "Once Upon a Time (2011)": "Once Upon a Time",
    "Euphoria (US)": "Euphoria",
    "The Tomorrow People (US)": "The Tomorrow People",
    "Celebrity Hunted: Manhunt (IT)": "Celebrity Hunted",
    "What If…?": "What If...?",
    "Mickey Mouse: Disney Animated Shorts": "Mickey Mouse",
    "Raven's Home": "Raven's Home",
    "Le fate ignoranti - La serie": "Le fate ignoranti",
    "The O.C.": "The O.C.",
}

REJECT_MATCHES = {
    "Love Bugs": {"Un gars, une fille", "Herbie the Love Bug"},
    "Mickey Mouse: Disney Animated Shorts": {"Mickey Mouse Clubhouse"},
}


def slugify(value: str) -> str:
    value = value.lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    return value.strip("-") or "show"


def normalize(value: str) -> str:
    value = value.lower()
    value = value.replace("&", "and")
    value = re.sub(r"\([^)]*\)", "", value)
    value = re.sub(r"[^a-z0-9]+", "", value)
    return value


def cleaned_query(name: str) -> str:
    if name in QUERY_OVERRIDES:
        return QUERY_OVERRIDES[name]
    return re.sub(r"\s*\([^)]*\)\s*", " ", name).strip()


def fetch_json(url: str) -> Any:
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": "film-polpetta-poster-fetch/1.0",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(request, timeout=20) as response:
        return json.loads(response.read().decode("utf-8"))


def download(url: str, out_path: Path) -> None:
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "film-polpetta-poster-fetch/1.0"},
    )
    with urllib.request.urlopen(request, timeout=30) as response:
        out_path.write_bytes(response.read())


def choose_match(name: str, results: list[dict[str, Any]]) -> tuple[dict[str, Any] | None, str]:
    if not results:
        return None, "not-found"

    target = normalize(name)
    query = normalize(cleaned_query(name))
    rejected = REJECT_MATCHES.get(name, set())
    allowed_results = [
        item
        for item in results
        if item.get("show", {}).get("name", "") not in rejected
    ]
    if not allowed_results:
        return None, "rejected"

    with_images = [
        item
        for item in allowed_results
        if ((item.get("show", {}).get("image") or {}).get("medium"))
    ]
    candidates = with_images or allowed_results

    for item in candidates:
        show = item["show"]
        show_norm = normalize(show.get("name", ""))
        if show_norm == target or show_norm == query:
            return item, "exact"

    for item in candidates:
        show = item["show"]
        show_norm = normalize(show.get("name", ""))
        if target and (target in show_norm or show_norm in target):
            return item, "close"

    return candidates[0], "best-score"


def extension_from_url(url: str) -> str:
    suffix = Path(urllib.parse.urlparse(url).path).suffix.lower()
    if suffix in {".jpg", ".jpeg", ".png", ".webp"}:
        return ".jpg" if suffix == ".jpeg" else suffix
    return ".jpg"


def build() -> dict[str, Any]:
    data = json.loads(SITE_DATA.read_text(encoding="utf-8"))
    shows = [item["name"] for item in data["series"]]
    POSTERS_DIR.mkdir(parents=True, exist_ok=True)
    POSTERS_JSON.parent.mkdir(parents=True, exist_ok=True)
    MATCH_REPORT.parent.mkdir(parents=True, exist_ok=True)

    records = []
    for index, name in enumerate(shows, start=1):
        query = cleaned_query(name)
        url = TVMAZE_SEARCH_URL + urllib.parse.quote(query)
        status = "ok"
        match_type = ""
        matched_name = ""
        tvmaze_id = None
        poster_url = ""
        local_path = ""
        source_url = ""

        try:
            results = fetch_json(url)
            match, match_type = choose_match(name, results)
            if match:
                show = match["show"]
                matched_name = show.get("name", "")
                tvmaze_id = show.get("id")
                source_url = show.get("url", "")
                image = show.get("image") or {}
                poster_url = image.get("medium") or image.get("original") or ""
                if poster_url:
                    out_path = POSTERS_DIR / f"{slugify(name)}{extension_from_url(poster_url)}"
                    if not out_path.exists():
                        download(poster_url, out_path)
                    local_path = f"./assets/posters/{out_path.name}"
                else:
                    status = "no-image"
            else:
                status = "not-found"
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            status = f"error: {exc.__class__.__name__}"

        records.append(
            {
                "name": name,
                "query": query,
                "status": status,
                "matchType": match_type,
                "matchedName": matched_name,
                "tvmazeId": tvmaze_id,
                "posterUrl": poster_url,
                "localPath": local_path,
                "sourceUrl": source_url,
            }
        )

        print(f"[{index:03}/{len(shows)}] {name} -> {matched_name or status} ({match_type or status})")
        time.sleep(0.18)

    payload = {
        "generatedAt": time.strftime("%Y-%m-%dT%H:%M:%S"),
        "source": "TVMaze",
        "sourceApi": "https://www.tvmaze.com/api",
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
        if not item["localPath"] or item["matchType"] not in {"exact", "close"}
    ]

    lines = [
        "# Poster Matches",
        "",
        f"Fonte: TVMaze API (`{payload['sourceApi']}`).",
        "",
        f"- Serie totali: {len(records)}",
        f"- Poster locali trovati: {len(with_images)}",
        f"- Da rivedere: {len(needs_review)}",
        "",
        "## Match da rivedere",
        "",
        "| Serie | Query | Match | Stato |",
        "| --- | --- | --- | --- |",
    ]
    for item in needs_review:
        lines.append(
            f"| {item['name']} | {item['query']} | {item['matchedName'] or '-'} | {item['status']} / {item['matchType']} |"
        )

    lines.extend(["", "## Tutti i match", "", "| Serie | Match | Tipo | Poster |", "| --- | --- | --- | --- |"])
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
