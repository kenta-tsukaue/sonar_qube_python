def add_numbers(a, b):
    """2つの数値を加算する"""
    return a + b


def find_max_in_list(numbers):
    """リスト内の最大値を返す"""
    if not numbers:
        raise ValueError("空のリストは処理できません")
    return max(numbers)


def true_or_false(number):
    if number > 5:
        return True
    else:
        return False
