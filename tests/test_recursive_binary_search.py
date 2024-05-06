import pytest
from app.algo.recursive_binary_search import binary_search_recursive

def test_binary_search_recursive():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    expected_index = 4
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == expected_index

def test_binary_search_recursive_empty_list():
    # Empty list
    nums = []
    target = 5
    assert binary_search_recursive(nums, 0, 0, target) == -1

def test_binary_search_recursive_single_element_list():
    # Single element list
    nums = [1]
    target = 1
    assert binary_search_recursive(nums, 0, 0, target) == 0

def test_binary_search_recursive_list_with_duplicates():
    # List with duplicate elements
    nums = [1, 3, 5, 5, 7, 7, 9, 9]
    target = 5
    expected_index = 2  # First occurrence of target
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == expected_index

def test_binary_search_recursive_list_with_negative_numbers():
    # List with negative numbers
    nums = [-5, -3, -1, 0, 2, 4, 6, 8]
    target = -3
    expected_index = 1
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == expected_index

def test_binary_search_recursive_large_list():
    # Large list
    nums = list(range(1, 10001))
    target = 5000
    expected_index = 4999
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == expected_index

def test_binary_search_recursive_target_not_in_list():
    # Target not in the list
    nums = [1, 3, 5, 7, 9]
    target = 4
    assert binary_search_recursive(nums, 0, len(nums) - 1, target) == -1