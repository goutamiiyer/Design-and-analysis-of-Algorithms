"""
Given an array of n distinct integers sorted in ascending order, write a function that returns a
Fixed Point in the array, if there is any Fixed Point present in array, else returns -1. Fixed
Point in an array is an index i such that arr[i] is equal to i. Note that integers in array can be
negative.

◦ Can solve it using linear search in O(n)
◦ Can solve it using binary search in O(lg n)
"""


def find_fixed(A, low, high):
    if high >= low: # We divide the array to look for a fixed point
        mid = (low + high) // 2
    if mid == A[mid]: # We check if we have a fixed point in position mid, if we do, we return it
        return mid
    if mid > A[mid]: # If mid > A[mid] then the fix point should be in the right side
        return find_fixed(A, (mid + 1), high)
    else: # If mid < A[mid] then the fix point should be in the left side
        return find_fixed(A, low, (mid - 1))
    return -1


# Defining the array A and low and high
A = [-5, -2, 0, 3, 4, 8, 15, 20]
n = len(A)

# Calling find_fixed
fixed = find_fixed(A, 0, n-1)
# Pringint the result
print("Fixex point: " + str(fixed))

