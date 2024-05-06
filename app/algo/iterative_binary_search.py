

def binary_search_iterative(nums: list[int], target: int) -> int:
    
    # initialize result to -1 to indicate target not found
    result = -1

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
            result = mid
            right = mid - 1
        
        # discard all elements in the right search space,
        # including the middle element
        elif target < nums_sorted[mid]:
            right = mid - 1
            
        # discard all elements in the left search space,
        # including the middle element
        else:
            left = mid + 1
    
    # `target` doesn't exist in the list
    return result