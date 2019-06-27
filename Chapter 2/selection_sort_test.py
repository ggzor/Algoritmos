from hypothesis import given
from hypothesis.strategies import lists, integers

from selection_sort import *

@given(lists(integers()))
def test_selection_sort(l):
    assert selection_sort(l) == sorted(l)