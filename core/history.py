from datetime import datetime

import pandas as pd

from core.config import HISTORY_FILE


def save_history(course_name, url, target, age, look, azul_text, verde_text):
    row = pd.DataFrame([{
        "fecha": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "curso": course_name,
        "link": url,
        "target": target,
        "edad_visual": age,
        "look_feel": look,
        "azul": azul_text,
        "verde": verde_text,
    }])
    if HISTORY_FILE.exists():
        old = pd.read_excel(HISTORY_FILE)
        df = pd.concat([old, row], ignore_index=True)
    else:
        df = row
    df.to_excel(HISTORY_FILE, index=False)
