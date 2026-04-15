from calculator import multiply


def test_multiply_positive():
    assert multiply(2, 3) == 6


def test_multiply_negative():
    assert multiply(-1, -2) == 2


def test_multiply_by_zero():
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0


def test_multiply_mixed_signs():
    assert multiply(2, -3) == -6
