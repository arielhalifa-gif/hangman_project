def visual_secret_word(secret_word: str) -> list[str]:
    list_word = []
    for ch in secret_word:
        list_word.append("_")
    return list_word


def init_state(secret: str, max_tries: int) -> dict:
    display = visual_secret_word(secret)
    return {"secret": secret, "display": display, "guessed": [], "wrong_guesses": [], "max_tries": max_tries}

def validate_guess(ch: str, guessed: set[str]) -> tuple[bool, str]:
    if isinstance(ch, str):
        if ch in guessed:
            return (False, "you already choose that letter")
        return (True, "this is a valid letter")
    return (False, "this is not a valid letter")


def apply_guess(state: dict, ch: str) -> bool:
    secret_w = state["secret"]
    if ch in secret_w:
        return True
    return False


def is_won(state: dict) -> bool:
    if ("_" in state["display"]):
        return False
    return True

def is_lost(state: dict) -> bool:
    wrong = state["wrong_guesses"]
    max_tries = state["max_tries"]
    if len(wrong) > max_tries:
        return True
    return False

def render_display(state: dict) -> str:
    temp_str = ""
    for ch in state["display"]:
        temp_str += ch
    return temp_str


def render_summary(state: dict) -> str:
    