import pytest
from app.algo.recursive_binary_search import binary_search_recursive

def test_binary_search_recursive():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    expected_index = 4
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == expected_index

    target = 10
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == -1