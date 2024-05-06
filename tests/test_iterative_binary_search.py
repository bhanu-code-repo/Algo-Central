import pytest
from app.algo.iterative_binary_search import binary_search_iterative

def test_binary_search_iterative():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    expected_index = 4
    assert binary_search_iterative(nums, target) == expected_index

    target = 10
    assert binary_search_iterative(nums, target) == -1