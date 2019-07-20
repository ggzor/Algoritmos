from hypothesis import given
from hypothesis.strategies import integers, lists
from binary_search import *

def sorted_list(min_size=0):
    return lists(integers(), min_size=min_size, unique=True).map(sorted)

@given(sorted_list(), integers())
def test_binary_search_result_is_within_bounds_or_minus_one(l, e):
    result = binary_search(l, e)
    assert 0 <= result < len(l) or result == -1

@given(sorted_list())
def test_binary_search_result_is_minus_one_if_element_is_not_in_list_or_is_empty(l):
    element_not_in_list = 1 if len(l) == 0 else max(l) + 1
    assert binary_search(l, element_not_in_list) == -1

@given(sorted_list(min_size=1), integers(min_value=0))
def test_binary_search_return_index_of_element(l, idx):
    idx %= len(l)
    assert idx == binary_search(l, l[idx])