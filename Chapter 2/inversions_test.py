import pytest
from inversions import count_inversions


@pytest.mark.parametrize('arr,inversions', [
    ([2, 3, 8, 6, 1], 5),
    ([6, 5, 4, 3, 2, 1], 15),
    ([3, 1, 2, 2, 1, 2], 7),
    ([1, 2, 2, 3, 1, 2, 2, 2], 6)
])
def test_inversions(arr, inversions):
    assert count_inversions(arr) == inversions
