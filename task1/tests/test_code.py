import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from automaton import find_chains, check_errors
import pytest

TEST_CASES = [
    ("-11-", "chains", ["0: -11-"]),
    ("-121-", "chains", ["0: -121-"]),
    ("-1221221-", "chains", ["0: -1221221-"]),
    ("-111211223321-", "chains", ["0: -111211223321-"]),
    ("-1231-", "chains", ["0: -1231-"]),
    ("-131-", "chains", ["0: -131-"]),
    ("-1231-1231-", "chains", ["0: -1231-"]),
    ("-1-", "none", []),
    ("123123", "none", []),
    ("-1a1-", "error", "Символ 'a' на позиции 2 не принадлежит алфавиту {1, 2, 3, -}"),
    ("abc", "error", "Символ 'a' на позиции 0 не принадлежит алфавиту {1, 2, 3, -}"),
    ("-2-1321-", "error", "После '-' на позиции 0 следует '2', а не '1'"),
    ("----", "error", "После '-' на позиции 0 следует '-', а не '1'"),
    ("-12-131-", "error", "Перед '-' на позиции 3 стоит '2', а не '1'"),
    ("-123-", "error", "Перед '-' на позиции 4 стоит '3', а не '1'"),
    ("-11--11-", "chains", ["0: -11-", "4: -11-"]),
]

@pytest.mark.parametrize("input_str, expected_type, expected_value", TEST_CASES)
def test_automaton(input_str, expected_type, expected_value):
    chains = find_chains(input_str)
    error = check_errors(input_str, chains)

    if expected_type == "error":
        assert error == expected_value, f"Ожидалась ошибка: {expected_value}, получено: {error}"
    elif expected_type == "chains":
        assert error is None, f"Неожиданная ошибка: {error}"
        result = [f"{start}: {input_str[start:end+1]}" for start, end in chains]
        assert result == expected_value, f"Ожидалось: {expected_value}, получено: {result}"
    elif expected_type == "none":
        assert error is None, f"Неожиданная ошибка: {error}"
        assert len(chains) == 0, f"Ожидалось отсутствие цепочек, найдено: {chains}"
