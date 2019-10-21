from hypothesis import given
from hypothesis.strategies import integers
from common_strategies import sorted_lists

from binary_search import *

@given(sorted_lists(integers()), integers())
def test_binary_search_result_is_within_bounds_or_minus_one(l, e):
    result = binary_search(l, e)
    assert 0 <= result < len(l) or result == -1

@given(sorted_lists(integers()))
def test_binary_search_result_is_minus_one_if_element_is_not_in_list_or_is_empty(l):
    element_not_in_list = 1 if len(l) == 0 else max(l) + 1
    assert binary_search(l, element_not_in_list) == -1

@given(sorted_lists(integers(), min_size=1, unique=True), integers(min_value=0))
def test_binary_search_return_index_of_element(l, idx):
    idx %= len(l)
    assert idx == binary_search(l, l[idx])