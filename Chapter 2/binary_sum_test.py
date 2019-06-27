from binary_sum import *

from hypothesis import given
from hypothesis.strategies import integers

def naturals(max_value=None): return integers(min_value=0, max_value=max_value)

@given(naturals())
def test_to_binary_list_from_binary_list_are_inverses(value):
    assert from_binary_list(to_binary_list(value)) == value

@given(naturals(), naturals(max_value=20))
def test_to_binary_list_with_greater_length_doesnt_alter_value(value, extra_length):
    base_length = binary_length(value)
    assert from_binary_list(to_binary_list(value, base_length + extra_length)) == value

@given(naturals())
def test_binary_sum_has_0_as_neutral(value):
    zero = to_binary_list(0, binary_length(value))
    number_list = to_binary_list(value)
    assert from_binary_list(binary_sum(number_list, zero)) == from_binary_list(binary_sum(zero, number_list)) == value

@given(naturals(), naturals())
def test_binary_sum_commutes(value1, value2):
    max_length = max(binary_length(value1), binary_length(value2))
    number1 = to_binary_list(value1, max_length)
    number2 = to_binary_list(value2, max_length)

    assert binary_sum(number1, number2) == binary_sum(number2, number1)

@given(naturals(), naturals())
def test_binary_sum_coincides_with_naturals_sum(value1, value2):
    max_length = max(binary_length(value1), binary_length(value2))
    number1 = to_binary_list(value1, max_length)
    number2 = to_binary_list(value2, max_length)

    assert from_binary_list(binary_sum(number1, number2)) == value1 + value2
