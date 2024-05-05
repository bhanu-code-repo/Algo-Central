
def binary_search_iterative(nums: list[int], target: int) -> int:
    
    # check if the list is sorted and sort it if it's not
    nums_sorted = sorted(nums) if nums != sorted(nums) else nums
    
    # search space is nums[left…right]
    (left, right) = (0, len(nums_sorted) - 1)
    
    # loop till the search space is exhausted
    while left <= right:
        
        # find the mid-value in the search space and
        # compares it with the target
        mid = (left + right) // 2
        
        # target is found
        if target == nums_sorted[mid]:
            return mid
        
        # discard all elements in the right search space,
        # including the middle element
        elif target < nums_sorted[mid]:
            right = mid - 1
            
        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1
    
    # `target` doesn't exist in the list
    return -1

def binary_search_recursive(
    nums: list[int], 
    left: int, 
    right: int, 
    target: int
) -> int:
    # base condition (search space is exhausted)
    if left > right:
        return -1
    
    # find the mid-value in the search space and
    # compares it with the target
    mid = (left + right) // 2
    
    # base condition (a target is found)
    if target == nums[mid]:
        return mid
    
    # discard all elements in the right search space,
    # including the middle element
    elif target < nums[mid]:
        return binary_search_recursive(nums, left, mid - 1, target)
 
    # discard all elements in the left search space,
    # including the middle element
    else:
        return binary_search_recursive(nums, mid + 1, right, target)