

def format_group_name(days: str, time: str) -> str:
    translations = {
        "ODD": "Taq kúnler",
        "EVEN": "Jup kúnler"
    }
    day_name = translations.get(days.upper(), days)
    return f"{day_name} | 🕒 {time}"



def format_profile(data: dict) -> str:
    return (
        "<b>Profilińiz</b>\n\n"
        f"Atińiz:      <b>{data.get('full_name', '—')}</b>\n"
        f"GitHub:      <b>@{data.get('github_username', '—')}</b>\n"
        f"Telefon:     <b>{data.get('phone_number', '—')}</b>\n\n"
        "<b>Jiberiw yamasa qayta toltiriw?</b>"
    )