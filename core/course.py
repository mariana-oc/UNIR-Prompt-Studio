import re

import requests
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    return re.sub(r"\s+", " ", text or "").strip()


def fetch_course(url: str) -> tuple[str, str]:
    if not url:
        return "Curso UNIR", ""
    try:
        r = requests.get(url, timeout=12, headers={"User-Agent": "Mozilla/5.0"})
        soup = BeautifulSoup(r.text, "lxml")
        h1 = soup.find("h1")
        title = clean_text(h1.get_text()) if h1 else "Curso UNIR"
        meta = soup.find("meta", attrs={"name": "description"})
        desc = meta.get("content", "") if meta else ""
        body = clean_text(soup.get_text(" "))[:3500]
        return title, f"{title}. {desc}. {body}"
    except Exception:
        return "Curso UNIR", ""
