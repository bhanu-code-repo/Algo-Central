

def binary_search_recursive(
    nums: list[int], 
    left: int, 
    right: int, 
    target: int
) -> int:
    # base condition (search space is exhausted)
    if left > right or left < 0 or right >= len(nums):
        return -1
    
    # find the mid-value in the search space and
    # compares it with the target
    mid = (left + right) // 2
    
    # base condition (a target is found)
    if target == nums[mid]:
        # check if this is the leftmost occurrence
        while mid > left and nums[mid - 1] == target:
            mid -= 1
        return mid
    
    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binary_search_recursive(nums, left, mid - 1, target)
 
    # discard all elements in the left search space,
    # including the middle element
    else:
        return binary_search_recursive(nums, mid + 1, right, target)