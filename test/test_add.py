from src.add import add


def test_add():
    a = 1
    b = 2
    expected_result = 3
    assert add(a, b) == expected_result