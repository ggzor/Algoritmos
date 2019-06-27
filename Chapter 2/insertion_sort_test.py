from hypothesis import given
from hypothesis.strategies import lists, integers

from insertion_sort import *

@given(lists(integers()))
def test_insertion_sort(l):
    assert insertion_sort_pythonic(l) == sorted(l)

@given(lists(integers()))
def test_insertion_sort_classic(l):
    assert insertion_sort_classic(l) == sorted(l)

@given(lists(integers()))
def test_reverse_insertion_sort_classic(l):
    assert reverse_insertion_sort_classic(l) == list(reversed(sorted(l)))