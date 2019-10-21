from hypothesis import given
from hypothesis.strategies import integers
from common_strategies import sorted_lists

from sum_giving import *

@given(sorted_lists(integers()), integers())
def test_sum_giving_x_indices_must_be_within_bounds_or_none(l, x):
    result = sum_giving(l, x)

    def is_within_bounds(i):
        return 0 <= i < len(l)

    assert result == None or (is_within_bounds(result[0]), is_within_bounds(result[1]))