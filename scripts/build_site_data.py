from __future__ import annotations

import csv
import json
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
SITE_DATA_DIR = ROOT / "site" / "data"
PROCESSED_OUT = PROCESSED_DIR / "site_data.json"
SITE_OUT = SITE_DATA_DIR / "polpetta-data.json"
ARCHIVE_MONTH_KEY = "2018-04"


def read_csv(name: str) -> list[dict[str, str]]:
    path = RAW_DIR / name
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        return [
            {key: (value or "").strip() for key, value in row.items()}
            for row in csv.DictReader(handle)
        ]


def parse_dt(value: str) -> datetime | None:
    if not value:
        return None
    for candidate in (value, value.replace("Z", "+00:00")):
        try:
            return datetime.fromisoformat(candidate)
        except ValueError:
            pass
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    return None


def as_int(value: str) -> int:
    try:
        return int(float(value or "0"))
    except ValueError:
        return 0


def month_key(dt: datetime) -> str:
    return f"{dt.year:04d}-{dt.month:02d}"


def month_label(key: str) -> str:
    year, month = key.split("-")
    names = [
        "Gen",
        "Feb",
        "Mar",
        "Apr",
        "Mag",
        "Giu",
        "Lug",
        "Ago",
        "Set",
        "Ott",
        "Nov",
        "Dic",
    ]
    return f"{names[int(month) - 1]} {year}"


def valid_release_dt(value: str) -> datetime | None:
    dt = parse_dt(value)
    if dt is None or dt.year <= 1900:
        return None
    return dt


def build() -> dict[str, Any]:
    tracking = read_csv("tracking-prod-records-v2.csv")
    movie_tracking = read_csv("tracking-prod-records.csv")
    user_show_data = read_csv("user_tv_show_data.csv")
    followed = read_csv("followed_tv_show.csv")
    rewatched = read_csv("rewatched_episode.csv")
    movie_ratings = read_csv("ratings-live-votes.csv") + read_csv("ratings-v2-prod-votes.csv")
    movie_emotions = read_csv("emotions-live-votes.csv")

    series: dict[str, dict[str, Any]] = {}
    months: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "key": "",
            "label": "",
            "records": 0,
            "bulkRecords": 0,
            "episodeRecords": 0,
            "runtimeSeconds": 0,
            "series": Counter(),
        }
    )
    years: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "year": "",
            "records": 0,
            "bulkRecords": 0,
            "runtimeSeconds": 0,
        }
    )

    first_seen: datetime | None = None
    last_seen: datetime | None = None
    distinct_episodes = set()
    bulk_records = 0
    runtime_seconds = 0

    for row in tracking:
        name = row.get("series_name") or row.get("movie_name")
        if not name:
            continue
        dt = parse_dt(row.get("created_at", ""))
        runtime = as_int(row.get("runtime", ""))
        bulk_type = row.get("bulk_type", "")
        episode_id = row.get("ep_id") or row.get("episode_id")

        entry = series.setdefault(
            name,
            {
                "name": name,
                "trackingRecords": 0,
                "trackingEpisodes": 0,
                "episodesSeen": 0,
                "runtimeSeconds": 0,
                "runtimeHours": 0,
                "firstSeen": None,
                "lastSeen": None,
                "followed": False,
                "favorited": False,
                "rewatchedEpisodes": 0,
                "bulkRecords": 0,
                "topMonth": None,
            },
        )

        entry["trackingRecords"] += 1
        entry["runtimeSeconds"] += runtime
        runtime_seconds += runtime
        if episode_id:
            distinct_episodes.add(episode_id)
            entry["trackingEpisodes"] += 1
        if bulk_type:
            bulk_records += 1
            entry["bulkRecords"] += 1

        if dt:
            if first_seen is None or dt < first_seen:
                first_seen = dt
            if last_seen is None or dt > last_seen:
                last_seen = dt

            existing_first = parse_dt(entry["firstSeen"] or "")
            existing_last = parse_dt(entry["lastSeen"] or "")
            if existing_first is None or dt < existing_first:
                entry["firstSeen"] = dt.isoformat(sep=" ")
            if existing_last is None or dt > existing_last:
                entry["lastSeen"] = dt.isoformat(sep=" ")

            key = month_key(dt)
            months[key]["key"] = key
            months[key]["label"] = month_label(key)
            months[key]["records"] += 1
            months[key]["runtimeSeconds"] += runtime
            months[key]["series"][name] += 1
            if bulk_type:
                months[key]["bulkRecords"] += 1
            else:
                months[key]["episodeRecords"] += 1

            year = str(dt.year)
            years[year]["year"] = year
            years[year]["records"] += 1
            years[year]["runtimeSeconds"] += runtime
            if bulk_type:
                years[year]["bulkRecords"] += 1

    followed_names = {row.get("tv_show_name", "") for row in followed if row.get("active") == "1"}
    for row in user_show_data:
        name = row.get("tv_show_name", "")
        if not name:
            continue
        entry = series.setdefault(
            name,
            {
                "name": name,
                "trackingRecords": 0,
                "trackingEpisodes": 0,
                "episodesSeen": 0,
                "runtimeSeconds": 0,
                "runtimeHours": 0,
                "firstSeen": None,
                "lastSeen": None,
                "followed": False,
                "favorited": False,
                "rewatchedEpisodes": 0,
                "bulkRecords": 0,
                "topMonth": None,
            },
        )
        entry["episodesSeen"] = as_int(row.get("nb_episodes_seen", ""))
        entry["followed"] = row.get("is_followed") == "1" or name in followed_names
        entry["favorited"] = row.get("is_favorited") == "1"

    rewatch_counter = Counter(row.get("tv_show_name", "") for row in rewatched if row.get("tv_show_name"))
    for name, count in rewatch_counter.items():
        if name in series:
            series[name]["rewatchedEpisodes"] = count

    month_list = []
    for item in sorted(months.values(), key=lambda value: value["key"]):
        top_series = item["series"].most_common(1)
        month_list.append(
            {
                "key": item["key"],
                "label": item["label"],
                "records": item["records"],
                "bulkRecords": item["bulkRecords"],
                "episodeRecords": item["episodeRecords"],
                "runtimeHours": round(item["runtimeSeconds"] / 3600, 1),
                "topSeries": top_series[0][0] if top_series else "",
                "topSeriesRecords": top_series[0][1] if top_series else 0,
                "isArchiveImport": item["key"] == ARCHIVE_MONTH_KEY,
            }
        )

    for entry in series.values():
        entry["runtimeHours"] = round(entry["runtimeSeconds"] / 3600, 1)
        del entry["runtimeSeconds"]
        series_months = [
            month
            for month in month_list
            if month["topSeries"] == entry["name"]
        ]
        if series_months:
            entry["topMonth"] = max(series_months, key=lambda value: value["records"])["label"]

    series_list = sorted(
        series.values(),
        key=lambda item: (item["episodesSeen"], item["trackingRecords"], item["runtimeHours"]),
        reverse=True,
    )

    likely_import_records = next(
        (month["records"] for month in month_list if month["key"] == ARCHIVE_MONTH_KEY),
        0,
    )
    archive_month = next((month for month in month_list if month["key"] == ARCHIVE_MONTH_KEY), None)
    chart_months = [month for month in month_list if not month["isArchiveImport"]]

    year_list = []
    for item in sorted(years.values(), key=lambda value: value["year"]):
        archive_records_for_year = likely_import_records if item["year"] == "2018" else 0
        year_list.append(
            {
                "year": item["year"],
                "records": item["records"],
                "chartRecords": item["records"] - archive_records_for_year,
                "bulkRecords": item["bulkRecords"],
                "runtimeHours": round(item["runtimeSeconds"] / 3600, 1),
            }
        )

    movies: dict[str, dict[str, Any]] = {}
    movie_months: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "key": "",
            "label": "",
            "records": 0,
            "runtimeSeconds": 0,
            "movies": Counter(),
        }
    )
    movie_years: dict[str, dict[str, Any]] = defaultdict(
        lambda: {
            "year": "",
            "records": 0,
            "runtimeSeconds": 0,
        }
    )

    def movie_entry(name: str) -> dict[str, Any]:
        return movies.setdefault(
            name,
            {
                "name": name,
                "trackingRecords": 0,
                "watchRecords": 0,
                "followRecords": 0,
                "watchlistRecords": 0,
                "runtimeSeconds": 0,
                "runtimeHours": 0,
                "firstTracked": None,
                "lastTracked": None,
                "firstWatched": None,
                "lastWatched": None,
                "releaseDate": None,
                "releaseYear": None,
                "watched": False,
                "followed": False,
                "watchlist": False,
                "rewatchCount": 0,
                "ratingVotes": 0,
                "emotionVotes": 0,
                "topMonth": None,
            },
        )

    first_movie_watch: datetime | None = None
    last_movie_watch: datetime | None = None
    movie_records = 0
    movie_watch_records = 0
    movie_follow_records = 0
    movie_watchlist_records = 0

    for row in movie_tracking:
        if row.get("entity_type") != "movie" and not row.get("movie_name"):
            continue
        name = row.get("movie_name", "")
        if not name:
            continue

        action = row.get("type", "")
        dt = parse_dt(row.get("created_at", ""))
        release_dt = valid_release_dt(row.get("release_date", ""))
        runtime = as_int(row.get("runtime", ""))
        entry = movie_entry(name)

        movie_records += 1
        entry["trackingRecords"] += 1
        if runtime:
            entry["runtimeSeconds"] = max(entry["runtimeSeconds"], runtime)
        if release_dt and not entry["releaseDate"]:
            entry["releaseDate"] = release_dt.date().isoformat()
            entry["releaseYear"] = release_dt.year

        if dt:
            existing_first = parse_dt(entry["firstTracked"] or "")
            existing_last = parse_dt(entry["lastTracked"] or "")
            if existing_first is None or dt < existing_first:
                entry["firstTracked"] = dt.isoformat(sep=" ")
            if existing_last is None or dt > existing_last:
                entry["lastTracked"] = dt.isoformat(sep=" ")

        if action == "watch":
            movie_watch_records += 1
            entry["watchRecords"] += 1
            entry["watched"] = True
            entry["rewatchCount"] = max(entry["rewatchCount"], as_int(row.get("rewatch_count", "")))
            if dt:
                if first_movie_watch is None or dt < first_movie_watch:
                    first_movie_watch = dt
                if last_movie_watch is None or dt > last_movie_watch:
                    last_movie_watch = dt

                existing_first = parse_dt(entry["firstWatched"] or "")
                existing_last = parse_dt(entry["lastWatched"] or "")
                if existing_first is None or dt < existing_first:
                    entry["firstWatched"] = dt.isoformat(sep=" ")
                if existing_last is None or dt > existing_last:
                    entry["lastWatched"] = dt.isoformat(sep=" ")

                key = month_key(dt)
                movie_months[key]["key"] = key
                movie_months[key]["label"] = month_label(key)
                movie_months[key]["records"] += 1
                movie_months[key]["runtimeSeconds"] += runtime
                movie_months[key]["movies"][name] += 1

                year = str(dt.year)
                movie_years[year]["year"] = year
                movie_years[year]["records"] += 1
                movie_years[year]["runtimeSeconds"] += runtime
        elif action == "follow":
            movie_follow_records += 1
            entry["followRecords"] += 1
            entry["followed"] = True
        elif action == "towatch":
            movie_watchlist_records += 1
            entry["watchlistRecords"] += 1
            entry["watchlist"] = True

    rating_counter = Counter(row.get("movie_name", "") for row in movie_ratings if row.get("movie_name"))
    for name, count in rating_counter.items():
        movie_entry(name)["ratingVotes"] = count

    emotion_counter = Counter(row.get("movie_name", "") for row in movie_emotions if row.get("movie_name"))
    for name, count in emotion_counter.items():
        movie_entry(name)["emotionVotes"] = count

    movie_month_list = []
    for item in sorted(movie_months.values(), key=lambda value: value["key"]):
        top_movies = item["movies"].most_common(1)
        movie_month_list.append(
            {
                "key": item["key"],
                "label": item["label"],
                "records": item["records"],
                "runtimeHours": round(item["runtimeSeconds"] / 3600, 1),
                "topMovie": top_movies[0][0] if top_movies else "",
                "topMovieRecords": top_movies[0][1] if top_movies else 0,
            }
        )

    movie_year_list = []
    for item in sorted(movie_years.values(), key=lambda value: value["year"]):
        movie_year_list.append(
            {
                "year": item["year"],
                "records": item["records"],
                "chartRecords": item["records"],
                "bulkRecords": 0,
                "runtimeHours": round(item["runtimeSeconds"] / 3600, 1),
            }
        )

    release_decades = Counter()
    for entry in movies.values():
        entry["runtimeHours"] = round(entry["runtimeSeconds"] / 3600, 1)
        del entry["runtimeSeconds"]
        movie_specific_months = [
            month
            for month in movie_month_list
            if month["topMovie"] == entry["name"]
        ]
        if movie_specific_months:
            entry["topMonth"] = max(movie_specific_months, key=lambda value: value["records"])["label"]
        if entry["watched"] and entry["releaseYear"]:
            release_decades[f"{entry['releaseYear'] // 10 * 10}s"] += 1

    movie_list = sorted(
        movies.values(),
        key=lambda item: (
            item["watched"],
            item["lastWatched"] or item["lastTracked"] or "",
            item["runtimeHours"],
        ),
        reverse=True,
    )
    watched_movies = [item for item in movie_list if item["watched"]]
    known_movie_runtime = sum(item["runtimeHours"] for item in watched_movies)
    movie_release_decades = [
        {
            "label": decade,
            "records": count,
        }
        for decade, count in sorted(release_decades.items(), key=lambda item: item[0])
    ]

    return {
        "generatedAt": datetime.now().isoformat(timespec="seconds"),
        "title": "Polpetta TV Diary",
        "subtitle": "Una memoria interattiva delle serie viste su TV Time.",
        "source": {
            "rawDir": str(RAW_DIR),
            "trackingFile": "tracking-prod-records-v2.csv",
            "notes": [
                "Aprile 2018 e' trattato come archivio recuperato: record inseriti in massa che rappresentano visioni precedenti.",
                "I record con bulk_type sono batch di stagione o import, non visioni minuto per minuto.",
                "Dati tecnici e personali del GDPR export non sono inclusi nel JSON del sito.",
            ],
        },
        "stats": {
            "csvFiles": len(list(RAW_DIR.glob("*.csv"))),
            "trackingRecords": len(tracking),
            "seriesCount": len(series_list),
            "distinctEpisodes": len(distinct_episodes),
            "episodesSeen": sum(item["episodesSeen"] for item in series_list),
            "runtimeHours": round(runtime_seconds / 3600, 1),
            "followedShows": sum(1 for item in series_list if item["followed"]),
            "rewatchedEpisodes": sum(rewatch_counter.values()),
            "bulkRecords": bulk_records,
            "firstSeen": first_seen.isoformat(sep=" ") if first_seen else None,
            "lastSeen": last_seen.isoformat(sep=" ") if last_seen else None,
            "likelyImportRecords": likely_import_records,
        },
        "archiveImport": {
            "key": ARCHIVE_MONTH_KEY,
            "label": archive_month["label"] if archive_month else "Apr 2018",
            "records": likely_import_records,
            "topSeries": archive_month["topSeries"] if archive_month else "",
            "note": "Archivio recuperato: record inseriti in massa che probabilmente rappresentano serie viste prima dell'uso continuativo di TV Time.",
        },
        "top": {
            "episodes": sorted(series_list, key=lambda item: item["episodesSeen"], reverse=True)[:12],
            "hours": sorted(series_list, key=lambda item: item["runtimeHours"], reverse=True)[:12],
            "rewatchedEpisodes": sorted(series_list, key=lambda item: item["rewatchedEpisodes"], reverse=True)[:8],
            "months": sorted(chart_months, key=lambda item: item["records"], reverse=True)[:12],
        },
        "years": year_list,
        "months": month_list,
        "series": series_list,
        "movies": {
            "stats": {
                "trackingRecords": movie_records,
                "movieCount": len(movie_list),
                "watchedMovies": len(watched_movies),
                "watchRecords": movie_watch_records,
                "followedMovies": sum(1 for item in movie_list if item["followed"]),
                "watchlistMovies": sum(1 for item in movie_list if item["watchlist"]),
                "followRecords": movie_follow_records,
                "watchlistRecords": movie_watchlist_records,
                "runtimeHours": round(known_movie_runtime, 1),
                "ratedMovies": len(rating_counter),
                "emotionMovies": len(emotion_counter),
                "firstSeen": first_movie_watch.isoformat(sep=" ") if first_movie_watch else None,
                "lastSeen": last_movie_watch.isoformat(sep=" ") if last_movie_watch else None,
            },
            "top": {
                "hours": sorted(watched_movies, key=lambda item: item["runtimeHours"], reverse=True)[:12],
                "months": sorted(movie_month_list, key=lambda item: item["records"], reverse=True)[:12],
                "releaseDecades": sorted(movie_release_decades, key=lambda item: item["records"], reverse=True),
            },
            "years": movie_year_list,
            "months": movie_month_list,
            "items": movie_list,
        },
    }


def main() -> None:
    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    SITE_DATA_DIR.mkdir(parents=True, exist_ok=True)
    data = build()
    rendered = json.dumps(data, indent=2, ensure_ascii=False)
    PROCESSED_OUT.write_text(rendered, encoding="utf-8")
    SITE_OUT.write_text(rendered, encoding="utf-8")
    print(f"Site data: {SITE_OUT}")
    print(f"Series: {data['stats']['seriesCount']}")
    print(f"Movies: {data['movies']['stats']['movieCount']}")
    print(f"Records: {data['stats']['trackingRecords']}")


if __name__ == "__main__":
    main()
