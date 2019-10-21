from hypothesis import given
from hypothesis.strategies import lists, integers

from merge_sort import *

@given(lists(integers()))
def test_merge_sort(l):
    l1 = l[:]
    assert merge_sort(l1) == sorted(l)

# @given(lists(integers()))
# def test_inplace_merge_sort(l):
#     assert inplace_merge_sort(l) == sorted(l)