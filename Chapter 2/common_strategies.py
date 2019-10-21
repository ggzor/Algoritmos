from hypothesis.strategies import lists

def sorted_lists(inner_strategy, **kwargs):
    return lists(inner_strategy, **kwargs).map(sorted)