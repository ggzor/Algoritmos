from hypothesis import given
from hypothesis.strategies import lists, integers

from merge_sort import *

@given(lists(integers()))
def test_merge_sort(l):
    assert merge_sort(l) == sorted(l)