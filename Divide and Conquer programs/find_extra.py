"""
    Find index of an extra element
    ◦ Given two sorted arrays. There is only 1 difference between the arrays. First array has one
    element extra added in between. Find the index of the extra element.
    ◦ Can solve it using linear search in O(n)
    ◦ Can solve it using binary search in O(lg n)
"""


def findExtra(A, B, low, high):
    '''
    :param A: First sorted array of integers containing the extra element
    :param B: Second sorted array of integers
    :param low: Index to the low position of the sub-array
    :param high: Index to the high position of the sub-array
    :return: The extra element or a recursive call to findExtra
    '''
    if A[low] != B[low]:
        return A[low] # We found the extra element

    if high >= low: # We keep looking for the extra element
        mid = (low + high) // 2

    if A[mid] == B[mid]: # The extra element is in the right sub_array
        return findExtra(A, B, mid + 1, high)
    else:
        return findExtra(A, B, low, mid) # The extra element is in the left sub_array
    return -1 # There was no extra element

# Defining the two sub_arrays and initializing low and high
A = [1, 5, 7, 8, 9, 10, 11, 12, 13, 15, 18, 20, 21, 22]
B = [1, 5, 7, 8, 9, 10, 11, 12, 15, 18, 20, 21, 22]
low = 0
high = len(A)
# Making a call to findExta and storing the output into the variable "extra"
extra = findExtra(A, B, low, high)
# Printing the result
print("Extra: " + str(extra))