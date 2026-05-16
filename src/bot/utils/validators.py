import re


def is_valid_full_name(text: str) -> bool:
    if not re.match(r"^[A-Za-z\s'‘“áóǵńíúÁÓǴŃÍÚ]+$", text):
        return False

    words = text.strip().split()

    if len(words) != 2:
        return False
    
    for word in words:
        clean_word = word.replace("'", "")
        if len(clean_word) < 4:
            return False

    return True


def validate_github_username(username: str) -> bool:
    pattern = r'^[a-zA-Z0-9](?:[a-zA-Z0-9]|-(?=[a-zA-Z0-9])){0,38}$'
    return bool(re.match(pattern, username))