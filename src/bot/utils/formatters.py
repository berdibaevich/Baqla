

def format_group_name(days: str, time: str) -> str:
    translations = {
        "ODD": "Taq kúnler",
        "EVEN": "Jup kúnler"
    }
    day_name = translations.get(days.upper(), days)
    return f"{day_name} | 🕒 {time}"