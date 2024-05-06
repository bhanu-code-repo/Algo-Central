import pytest
from app.algo.iterative_binary_search import binary_search_iterative

def test_binary_search_iterative():
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 5
    expected_index = 4
    assert binary_search_iterative(nums, target) == expected_index

def test_binary_search_iterative_empty_list():
    # Empty list
    nums = []
    target = 5
    assert binary_search_iterative(nums, target) == -1

def test_binary_search_iterative_single_element_list():
    # Single element list
    nums = [1]
    target = 1
    assert binary_search_iterative(nums, target) == 0

def test_binary_search_iterative_list_with_duplicates():
    # List with duplicate elements
    nums = [1, 3, 5, 5, 7, 7, 9, 9]
    target = 5
    expected_index = 2  # First occurrence of target
    # Modify the expected index to consider duplicates
    assert binary_search_iterative(nums, target) == expected_index

def test_binary_search_iterative_list_with_negative_numbers():
    # List with negative numbers
    nums = [-5, -3, -1, 0, 2, 4, 6, 8]
    target = -3
    expected_index = 1
    assert binary_search_iterative(nums, target) == expected_index

def test_binary_search_iterative_large_list():
    # Large list
    nums = list(range(1, 10001))
    target = 5000
    expected_index = 4999
    assert binary_search_iterative(nums, target) == expected_index

def test_binary_search_iterative_target_not_in_list():
    # Target not in the list
    nums = [1, 3, 5, 7, 9]
    target = 4
    assert binary_search_iterative(nums, target) == -1