import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import pytest
from automaton import run_mp_automaton

TEST_CASES = [
    ("00", "цепочка принадлежит языку"),
    ("a00a", "цепочка принадлежит языку"),
    ("0b0", "цепочка принадлежит языку"),
    ("0bb0", "цепочка принадлежит языку"),
    ("a0b0a", "цепочка принадлежит языку"),
    ("aa0bb0aa", "цепочка принадлежит языку"),
    ("aaa0bbb0aaa", "цепочка принадлежит языку"),
    ("a0bbb0a", "цепочка принадлежит языку"),
    ("aa00aa", "цепочка принадлежит языку"),
    ("a0b0aa", "Ошибка: в позиции 6 неожидаемый символ a"),
    ("aa0b0a", "цепочка не принадлежит языку"),
    ("a0c0a", "Ошибка: в позиции 3 неожидаемый символ c"),
    ("0a0", "Ошибка: в позиции 2 неожидаемый символ a"),
    ("00ba", "Ошибка: в позиции 3 неожидаемый символ b"),
    ("", "цепочка не принадлежит языку"),
]

@pytest.mark.parametrize("input_str, expected", TEST_CASES)
def test_mp_automaton(input_str, expected):
    assert run_mp_automaton(input_str) == expected
