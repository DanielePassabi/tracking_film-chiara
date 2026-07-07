from __future__ import annotations

import csv
import argparse
import json
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_EXPORT_DIR = ROOT / "data" / "raw"
EXPORT_DIR = DEFAULT_EXPORT_DIR
PROCESSED_DIR = ROOT / "data" / "processed"
DOC_PATH = ROOT / "docs" / "DATA_AUDIT.md"
JSON_PATH = PROCESSED_DIR / "export_profile.json"

ENCODINGS = ("utf-8-sig", "utf-8", "cp1252", "utf-16")
DATE_FORMATS = (
    "%Y-%m-%d",
    "%Y-%m-%d %H:%M:%S",
    "%Y-%m-%dT%H:%M:%S",
    "%Y-%m-%dT%H:%M:%SZ",
    "%d/%m/%Y",
    "%d/%m/%Y %H:%M:%S",
    "%m/%d/%Y",
    "%m/%d/%Y %H:%M:%S",
)

SENSITIVE_NAME_RE = re.compile(
    r"(token|email|mail|password|secret|ip|address|advertising|ad_identifier|"
    r"appsflyer|facebook|device|session|auth|login|refresh|access|idfa|gaid)",
    re.IGNORECASE,
)


@dataclass
class LoadedCsv:
    path: Path
    encoding: str
    delimiter: str
    rows: list[dict[str, str]]
    headers: list[str]


def read_text(path: Path) -> tuple[str, str]:
    for encoding in ENCODINGS:
        try:
            return path.read_text(encoding=encoding), encoding
        except UnicodeDecodeError:
            continue
    return path.read_text(errors="replace"), "unknown"


def sniff_delimiter(text: str) -> str:
    sample = text[:8192]
    try:
        dialect = csv.Sniffer().sniff(sample, delimiters=",;\t|")
        return dialect.delimiter
    except csv.Error:
        return ","


def load_csv(path: Path) -> LoadedCsv:
    text, encoding = read_text(path)
    delimiter = sniff_delimiter(text)
    reader = csv.DictReader(text.splitlines(), delimiter=delimiter)
    headers = list(reader.fieldnames or [])
    rows = [
        {key or "": (value or "").strip() for key, value in row.items()}
        for row in reader
    ]
    return LoadedCsv(path=path, encoding=encoding, delimiter=delimiter, rows=rows, headers=headers)


def parse_date(value: str) -> datetime | None:
    raw = value.strip()
    if not raw:
        return None

    normalized = raw.replace("Z", "+00:00")
    try:
        return datetime.fromisoformat(normalized)
    except ValueError:
        pass

    for fmt in DATE_FORMATS:
        try:
            return datetime.strptime(raw, fmt)
        except ValueError:
            continue
    return None


def parse_number(value: str) -> float | None:
    raw = value.strip().replace(",", ".")
    if not raw or not re.fullmatch(r"-?\d+(\.\d+)?", raw):
        return None
    try:
        return float(raw)
    except ValueError:
        return None


def display_value(column_name: str, value: str) -> str:
    if not value:
        return value
    if SENSITIVE_NAME_RE.search(column_name):
        return "[redacted]"
    if re.fullmatch(r"[\w.+-]+@[\w-]+(\.[\w-]+)+", value):
        return "[redacted-email]"
    if re.fullmatch(r"\d{1,3}(\.\d{1,3}){3}", value):
        return "[redacted-ip]"
    if len(value) > 80 and re.fullmatch(r"[A-Za-z0-9._~+/=-]+", value):
        return "[redacted-long-token]"
    return value


def guess_entity(filename: str, headers: list[str]) -> str:
    haystack = " ".join([filename, *headers]).lower()
    checks = [
        ("episodes", ("episode", "season", "aired")),
        ("series", ("show", "series", "season_count")),
        ("movies", ("movie", "film", "runtime")),
        ("ratings", ("rating", "vote", "score", "stars")),
        ("watch history", ("watched", "seen", "viewed", "completed")),
        ("watchlist", ("watchlist", "to watch", "later")),
        ("comments", ("comment", "message", "review")),
        ("people/social", ("friend", "follower", "following", "user")),
    ]
    for label, terms in checks:
        if any(term in haystack for term in terms):
            return label
    return "unknown"


def profile_file(csv_file: LoadedCsv) -> dict[str, Any]:
    row_count = len(csv_file.rows)
    column_profiles = []

    for header in csv_file.headers:
        values = [row.get(header, "") for row in csv_file.rows]
        non_empty = [value for value in values if value != ""]
        unique_count = len(set(non_empty))
        samples = []
        for value in non_empty:
            sample = display_value(header, value)
            if sample not in samples:
                samples.append(sample)
            if len(samples) == 5:
                break

        parsed_dates = [parsed for value in non_empty if (parsed := parse_date(value))]
        parsed_numbers = [parsed for value in non_empty if (parsed := parse_number(value)) is not None]

        column_profile: dict[str, Any] = {
            "name": header,
            "non_empty": len(non_empty),
            "completeness": round((len(non_empty) / row_count) * 100, 2) if row_count else 0,
            "unique": unique_count,
            "samples": samples,
        }

        if parsed_dates and len(parsed_dates) / max(len(non_empty), 1) >= 0.6:
            column_profile["date_range"] = {
                "min": min(parsed_dates).isoformat(),
                "max": max(parsed_dates).isoformat(),
            }

        if parsed_numbers and len(parsed_numbers) / max(len(non_empty), 1) >= 0.8:
            column_profile["number_range"] = {
                "min": min(parsed_numbers),
                "max": max(parsed_numbers),
            }

        column_profiles.append(column_profile)

    return {
        "file": csv_file.path.name,
        "relative_path": relative_path(csv_file.path),
        "encoding": csv_file.encoding,
        "delimiter": csv_file.delimiter,
        "entity_guess": guess_entity(csv_file.path.name, csv_file.headers),
        "rows": row_count,
        "columns": len(csv_file.headers),
        "headers": csv_file.headers,
        "column_profiles": column_profiles,
    }


def build_profile() -> dict[str, Any]:
    csv_paths = sorted(EXPORT_DIR.rglob("*.csv"))
    files = []
    column_frequency: Counter[str] = Counter()
    columns_by_name: defaultdict[str, list[str]] = defaultdict(list)

    for path in csv_paths:
        loaded = load_csv(path)
        file_profile = profile_file(loaded)
        files.append(file_profile)
        for header in loaded.headers:
            normalized = header.strip().lower()
            column_frequency[normalized] += 1
            columns_by_name[normalized].append(path.name)

    shared_columns = [
        {"column": column, "count": count, "files": columns_by_name[column]}
        for column, count in column_frequency.most_common()
        if count > 1
    ]

    entity_counts = Counter(file_profile["entity_guess"] for file_profile in files)
    return {
        "generated_at": datetime.now().isoformat(timespec="seconds"),
        "export_dir": str(EXPORT_DIR),
        "csv_count": len(files),
        "total_rows": sum(file_profile["rows"] for file_profile in files),
        "entity_counts": dict(entity_counts),
        "shared_columns": shared_columns,
        "files": files,
    }


def relative_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def md_table(rows: list[list[str]]) -> str:
    if not rows:
        return ""
    widths = [max(len(row[index]) for row in rows) for index in range(len(rows[0]))]
    lines = []
    for row_index, row in enumerate(rows):
        line = "| " + " | ".join(value.ljust(widths[index]) for index, value in enumerate(row)) + " |"
        lines.append(line)
        if row_index == 0:
            lines.append("| " + " | ".join("-" * widths[index] for index in range(len(row))) + " |")
    return "\n".join(lines)


def render_markdown(profile: dict[str, Any]) -> str:
    lines = [
        "# Data Audit",
        "",
        f"Generato: `{profile['generated_at']}`",
        "",
        "## Sintesi",
        "",
        f"- CSV trovati: **{profile['csv_count']}**",
        f"- Righe totali: **{profile['total_rows']}**",
        f"- Cartella export: `{profile['export_dir']}`",
        "",
    ]

    if profile["csv_count"] == 0:
        lines.extend(
            [
                "Nessun file CSV trovato. Verifica che l'export TV Time sia in `data/raw/` e riesegui:",
                "",
                "```powershell",
                "python .\\scripts\\profile_export.py",
                "```",
                "",
            ]
        )
        return "\n".join(lines)

    entity_rows = [["Tipo ipotizzato", "File"]]
    entity_rows.extend(
        [[entity, str(count)] for entity, count in sorted(profile["entity_counts"].items())]
    )
    lines.extend(["## Tipi di file ipotizzati", "", md_table(entity_rows), ""])

    file_rows = [["File", "Tipo", "Righe", "Colonne", "Encoding", "Separatore"]]
    for file_profile in profile["files"]:
        file_rows.append(
            [
                file_profile["file"],
                file_profile["entity_guess"],
                str(file_profile["rows"]),
                str(file_profile["columns"]),
                file_profile["encoding"],
                repr(file_profile["delimiter"]),
            ]
        )
    lines.extend(["## File", "", md_table(file_rows), ""])

    if profile["shared_columns"]:
        shared_rows = [["Colonna", "File", "Presente in"]]
        for shared in profile["shared_columns"][:30]:
            shared_rows.append(
                [
                    shared["column"],
                    str(shared["count"]),
                    ", ".join(shared["files"][:6]) + ("..." if len(shared["files"]) > 6 else ""),
                ]
            )
        lines.extend(["## Colonne condivise", "", md_table(shared_rows), ""])

    lines.append("## Dettaglio colonne")
    lines.append("")
    for file_profile in profile["files"]:
        lines.extend(
            [
                f"### {file_profile['file']}",
                "",
                f"- Tipo ipotizzato: `{file_profile['entity_guess']}`",
                f"- Righe: `{file_profile['rows']}`",
                f"- Colonne: `{file_profile['columns']}`",
                "",
            ]
        )

        column_rows = [["Colonna", "Piena", "Unici", "Range", "Esempi"]]
        for column in file_profile["column_profiles"]:
            value_range = ""
            if "date_range" in column:
                value_range = f"{column['date_range']['min']} -> {column['date_range']['max']}"
            elif "number_range" in column:
                value_range = f"{column['number_range']['min']} -> {column['number_range']['max']}"
            samples = ", ".join(str(sample)[:60] for sample in column["samples"])
            column_rows.append(
                [
                    column["name"],
                    f"{column['completeness']}%",
                    str(column["unique"]),
                    value_range,
                    samples,
                ]
            )
        lines.extend([md_table(column_rows), ""])

    lines.extend(
        [
            "## Prime domande per il sito",
            "",
            "- Quali file contengono le azioni personali, non solo il catalogo?",
            "- Esistono date di visione affidabili per costruire una timeline?",
            "- I voti/commenti sono completi abbastanza per una vista dei preferiti?",
            "- Ci sono ID comuni per collegare episodi, serie e film senza ambiguita?",
        ]
    )
    return "\n".join(lines)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Profile a TV Time GDPR CSV export.")
    parser.add_argument(
        "export_dir",
        nargs="?",
        default=str(DEFAULT_EXPORT_DIR),
        help="Folder containing TV Time CSV files. Defaults to data/raw/.",
    )
    return parser.parse_args()


def main() -> None:
    global EXPORT_DIR
    args = parse_args()
    EXPORT_DIR = Path(args.export_dir).expanduser().resolve()

    PROCESSED_DIR.mkdir(parents=True, exist_ok=True)
    DOC_PATH.parent.mkdir(parents=True, exist_ok=True)
    if EXPORT_DIR == DEFAULT_EXPORT_DIR:
        EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    elif not EXPORT_DIR.exists():
        raise SystemExit(f"Cartella export non trovata: {EXPORT_DIR}")

    profile = build_profile()
    JSON_PATH.write_text(json.dumps(profile, indent=2, ensure_ascii=False), encoding="utf-8")
    DOC_PATH.write_text(render_markdown(profile), encoding="utf-8")

    print(f"CSV trovati: {profile['csv_count']}")
    print(f"Righe totali: {profile['total_rows']}")
    print(f"Report: {DOC_PATH}")
    print(f"JSON: {JSON_PATH}")


if __name__ == "__main__":
    main()
