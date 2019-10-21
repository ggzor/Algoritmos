from maximum_subarray import *
import pytest

tests = [
    ([2], (0, 1, 2)),
    ([1, -10, 2, 3, -1, -3], (2, 4, 5)),
    ([-2, -1, 2], (2, 3, 2)),
    ([-2, 10, -3, 6, 5], (1, 5, 18)),
    ([-1, -2, -3, -1, -10], (0, 1, -1)),
    ([-1, -2, 0, -1, -10], (2, 3, 0)),
    ([1, 2, 2, -2, 1], (0, 3, 5)),
    ([1, 2, 3, 4, -2, -3], (0, 4, 10)),
    ([4, -10, 2, 3, -1, -3], (2, 4, 5)),
    ([5, -2, 2, 4, -2, 6], (0, 6, 13)),
    ([4, -2, 1, 3, -2, 6], (0, 6, 10)),
    ([1, -2, 1, 3, -2, 6], (2, 6, 8)),
    ([4, -10, 4, -10, 3, 2], (4, 6, 5)),
    ([4, -10, 3, -1, 3], (2, 5, 5))
]

@pytest.mark.parametrize('a,r', tests)
def test_maximum_subarray(a, r):
    assert maximum_subarray(a, 0, len(a)) == r

@pytest.mark.parametrize('a,r', tests)
def test_naive_maximum_subarray(a, r):
    assert naive_maximum_subarray(a) == r

@pytest.mark.parametrize('a,r', tests)
def test_linear_maximum_subarray(a, r):
    assert linear_maximum_subarray(a) == r

@pytest.mark.parametrize('a,r', tests)
def test_shortest_linear_maximum_subarray(a, r):
    assert shortest_linear_maximum_subarray(a) == r
