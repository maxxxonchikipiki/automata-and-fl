Q0, Q1, Q2, Q3, Q4, Q5 = 0, 1, 2, 3, 4, 5

Z0 = 'Z'
A = 'a'

TRANSITIONS = {
    (Q0, ('a', Z0)): (Q0, A + Z0),
    (Q0, ('a', A)):  (Q0, A + A),
    (Q0, ('0', Z0)): (Q1, Z0),
    (Q0, ('0', A)):  (Q1, A),

    (Q1, ('b', Z0)): (Q2, Z0),
    (Q1, ('b', A)):  (Q2, A),
    (Q1, ('0', Z0)): (Q3, Z0),
    (Q1, ('0', A)):  (Q3, A),

    (Q2, ('b', Z0)): (Q2, Z0),
    (Q2, ('b', A)):  (Q2, A),
    (Q2, ('0', Z0)): (Q3, Z0),
    (Q2, ('0', A)):  (Q3, A),

    (Q3, ('a', A)):  (Q4, ''),
    (Q3, ('', Z0)):  (Q5, Z0),

    (Q4, ('a', A)):  (Q4, ''),
    (Q4, ('', Z0)):  (Q5, Z0),
}

ALPHABET = {'0', 'a', 'b'}


def run_mp_automaton(s: str) -> str:
    for i, char in enumerate(s):
        if char not in ALPHABET:
            return f"Ошибка: в позиции {i + 1} неожидаемый символ {char}"

    state = Q0
    stack = [Z0]
    pos = 0

    while True:
        char = s[pos] if pos < len(s) else ''

        if not stack:
            return f"Ошибка: в позиции {pos + 1} неожидаемый символ {char if char else 'конец строки'}"
        top = stack[-1]

        key = (state, (char, top))
        if key not in TRANSITIONS:
            if char:
                return f"Ошибка: в позиции {pos + 1} неожидаемый символ {char}"
            else:
                return "цепочка не принадлежит языку"

        new_state, replacement = TRANSITIONS[key]

        stack.pop()
        for sym in reversed(replacement):
            stack.append(sym)

        state = new_state

        if char:
            pos += 1

        if state == Q5:
            if pos == len(s):
                return "цепочка принадлежит языку"
            else:
                return f"Ошибка: в позиции {pos + 1} неожидаемый символ {s[pos]}"


if __name__ == "__main__":
    input_string = input().strip()
    print(run_mp_automaton(input_string))
