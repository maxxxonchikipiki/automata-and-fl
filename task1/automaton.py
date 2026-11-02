TRANSITIONS = {
    0: {'-': 1, '1': 6, '2': 6, '3': 6},
    1: {'-': 6, '1': 2, '2': 6, '3': 6},
    2: {'-': 6, '1': 4, '2': 3, '3': 3},
    3: {'-': 6, '1': 4, '2': 3, '3': 3},
    4: {'-': 5, '1': 2, '2': 3, '3': 3},
    5: {'-': 6, '1': 6, '2': 6, '3': 6},
    6: {'-': 6, '1': 6, '2': 6, '3': 6},
}

ALPHABET = {'1', '2', '3', '-'}
FINAL_STATE = 5
DEAD_STATE = 6


def is_valid_chain(s: str) -> bool:
    state = 0
    for char in s:
        if char not in ALPHABET:
            return False
        state = TRANSITIONS[state][char]
        if state == DEAD_STATE:
            return False
    return state == FINAL_STATE


def check_alphabet(s: str):
    for i, char in enumerate(s):
        if char not in ALPHABET:
            return f"Ошибка: символ '{char}' не принадлежит алфавиту {{1, 2, 3, -}}"
    return None


def run(s: str) -> str:
    if not s:
        return "цепочек не найдено"
    error = check_alphabet(s)
    if error:
        return error
    if is_valid_chain(s):
        return f"0: {s}"
    return "цепочек не найдено"


if __name__ == "__main__":
    print(run(input().strip()))
