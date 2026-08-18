"""Canonical category / keyword rules for Asterisk Quarto posts."""

from __future__ import annotations

# casefold(input) -> canonical category label
CATEGORY_CANON: dict[str, str] = {
    "g+ archive": "G+ archive",
    "teaching": "teaching",
    "organizations": "organizations",
    "politics": "politics",
    "misc": "misc",
    "nt criticism": "NT criticism",
    "bible criticism": "Bible criticism",
    "open source": "open source",
    "open-source": "open source",
    "free software": "free software",
    "data science": "data science",
    "education": "education",
    "information": "information",
    "coding": "coding",
    "code": "coding",
    "management": "management",
    "programming": "programming",
    "history": "History",
    "china": "China",
    "culture": "culture",
    "literature": "literature",
    "academia": "Academia",
}

# Labels that should never be site categories (former Pelican Tags, etc.)
KEYWORD_ONLY: set[str] = {
    "julia",
    "python",
    "matlab",
    "r",
    "thinking",
    "epistemology",
    "xfree86",
    "xorg",
    "bsd",
    "netbsd",
    "core",
    "scientific python",
}


def as_list(value) -> list[str]:
    if value is None:
        return []
    if isinstance(value, list):
        return [str(v).strip() for v in value if str(v).strip()]
    return [p.strip() for p in str(value).split(",") if p.strip()]


def split_taxonomy(
    categories: list[str] | None = None,
    keywords: list[str] | None = None,
    tags: list[str] | None = None,
) -> tuple[list[str], list[str]]:
    """Return (canonical categories, keywords) with stable order and no dupes."""
    cats_out: list[str] = []
    keys_out: list[str] = []
    seen_cat: set[str] = set()
    seen_key: set[str] = set()

    def add_cat(label: str) -> None:
        if label not in seen_cat:
            seen_cat.add(label)
            cats_out.append(label)

    def add_key(label: str) -> None:
        key = label.casefold()
        if key not in seen_key:
            seen_key.add(key)
            keys_out.append(label)

    for raw in list(categories or []) + list(tags or []):
        text = str(raw).strip()
        if not text:
            continue
        folded = text.casefold()
        if folded in KEYWORD_ONLY:
            # Prefer a tidy keyword spelling
            add_key(CATEGORY_CANON.get(folded, text))
            continue
        if folded in CATEGORY_CANON:
            add_cat(CATEGORY_CANON[folded])
            continue
        # Unknown: keep as category with original spelling (rare)
        add_cat(text)

    for raw in keywords or []:
        text = str(raw).strip()
        if not text:
            continue
        folded = text.casefold()
        if folded in CATEGORY_CANON and folded not in KEYWORD_ONLY:
            add_cat(CATEGORY_CANON[folded])
        else:
            add_key(CATEGORY_CANON.get(folded, text) if folded in KEYWORD_ONLY else text)

    return cats_out, keys_out
