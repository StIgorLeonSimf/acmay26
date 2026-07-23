from fractions_calk import add, sub, mult, div
import unittest
import pytest

"""
assert a == b  - проверка равенства
assert a != b  - проверка неравенства
assert a in b  - проверка вхождения 
assert isinstance(a, type) - проверка типа данных
assert a is True / a is False - проверка булевых значений
"""


# @pytest.fixture
# def data():
#     numbs = [1, 2, 3, 4]
#     return numbs
#
# def test_data(data):
#     assert sum(data) == 10
#     assert min(data) == 1
#     assert max(data) == 4


# def divide(a, b):
#     return a / b
#
# def test_divide():
#     result = divide(10, 2)
#     assert result == 5


# class TestMath(unittest.TestCase):
#     def test_add(self):
#         self.assertEqual(add(1, 2, 1, 2), (4, 4))

# def test_add():#
#     assert add(1, 2, 1, 2) == (4, 4)
#     assert add(2, 2, 2, 2) == (8, 4)
@pytest.mark.parametrize("n1, d1, n2, d2, res",
                         [(1, 2, 1, 2, (4, 4)),
                          (2, 2, 2, 2, (8, 4))
                          ])
def test_add(n1, d1, n2, d2, res):
    assert add(n1, d1, n2, d2) == res




# def test_zero():
#     with pytest.raises(ZeroDivisionError):
#         divide(10, 0)


if __name__ == '__main__':
    # unittest.main()
    pass
