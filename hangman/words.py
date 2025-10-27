import random
def sort_secret_word(words: list[str]) -> str:
    index_ = random.randint(0,100)
    secret_word = words[index_]
    return secret_word