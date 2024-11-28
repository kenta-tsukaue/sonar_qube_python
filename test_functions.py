import pytest
from functions import (
    add_numbers, find_max_in_list, true_or_false
)


# テストケース: add_numbers
@pytest.mark.parametrize("a, b, expected", [
    (1, 2, 3),  # 正常系
    (-1, 5, 4),  # 負の値を含むケース
    (0, 0, 0),  # ゼロ
])
def test_add_numbers(a, b, expected):
    assert add_numbers(a, b) == expected


@pytest.mark.parametrize("a, expected", [
    (6, True),
    (7, True),
    (3, False),
])
def test_true_or_false(a, expected):
    assert true_or_false(a) == expected


# テストケース: find_max_in_list
@pytest.mark.parametrize("numbers, expected", [
    ([1, 2, 3], 3),  # 正常系
    ([-1, -2, -3], -1),  # 負の値のみ
    ([0], 0),  # リストが1つの要素を持つ
])
def test_find_max_in_list(numbers, expected):
    assert find_max_in_list(numbers) == expected


def test_find_max_in_list_empty():
    with pytest.raises(ValueError):
        find_max_in_list([])  # 空リストの場合に例外を期待
