
# Merge two sorted sublists `A[low … mid]` and `A[mid+1 … high]`
def merge(A, aux, low, mid, high):
 
    k = low
    i = low
    j = mid + 1
 
    # while there are elements in the left and right runs
    while i <= mid and j <= high:
 
        if A[i] <= A[j]:
            aux[k] = A[i]
            k = k + 1
            i = i + 1
        else:
            aux[k] = A[j]
            k = k + 1
            j = j + 1
 
    # copy remaining elements
    while i <= mid:
        aux[k] = A[i]
        k = k + 1
        i = i + 1
 
    # No need to copy the second half (since the remaining items
    # are already in their correct position in the auxiliary array)
 
    # copy back to the original list to reflect sorted order
    for i in range(low, high + 1):
        A[i] = aux[i]

# Sort list `A[low…high]` using auxiliary list aux
def merge_sort(A, aux, low, high):
 
    # base case
    if high <= low:                     # if run size <= 1
        return
 
    # find midpoint
    mid = (low + ((high - low) >> 1))
 
    # recursively split runs into two halves until run size <= 1,
    # then merge them and return up the call chain
 
    merge_sort(A, aux, low, mid)         # split/merge left half
    merge_sort(A, aux, mid + 1, high)    # split/merge right half
 
    merge(A, aux, low, mid, high)       # merge the two half runs
 
 
# Function to check if `A` is sorted in ascending order or not
def is_sorted(A):
    if not A:  # Check if `A` is empty
        return True

    prev = A[0]
    for i in range(1, len(A)):
        if prev > A[i]:
            print("Merge Sort Fails!!")
            return False

        prev = A[i]

    return True