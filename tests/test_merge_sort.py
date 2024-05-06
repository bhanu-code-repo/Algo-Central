import pytest
from app.algo.merge_sort import merge_sort, is_sorted

def test_merge_sort():
    arr = [12, 11, 13, 5, 6, 7]
    aux = arr.copy()
    merge_sort(arr, aux, 0, len(arr) - 1)
    assert arr == [5, 6, 7, 11, 12, 13]

    arr = [38, 27, 43, 3, 9, 82, 10]
    aux = arr.copy()
    merge_sort(arr, aux, 0, len(arr) - 1)
    assert arr == [3, 9, 10, 27, 38, 43, 82]

def test_merge_sort_empty_list():
    # Empty list
    A = []
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_single_element_list():
    # Single element list
    A = [1]
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_list_with_duplicates():
    # List with duplicate elements
    A = [5, 3, 7, 5, 2, 8, 6, 4]
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_list_with_negative_numbers():
    # List with negative numbers
    A = [-5, -3, -7, -2, -8, -6, -4]
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_large_list():
    # Large list
    A = list(range(10000, 0, -1))
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_already_sorted_list():
    # Already sorted list
    A = list(range(1, 11))
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_list_sorted_in_descending_order():
    # Sorted in descending order
    A = list(range(10, 0, -1))
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)

def test_merge_sort_list_with_floating_point_numbers():
    # Sorted with floating-point numbers
    A = [1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5]
    aux = A.copy()
    merge_sort(A, aux, 0, len(A) - 1)
    assert is_sorted(A)