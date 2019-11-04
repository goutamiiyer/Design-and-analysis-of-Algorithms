'''
Given a set of non-negative integers and a value sum, find if there is a subset of the
given set with sum equal to the given sum.

subset[i][j] stores i rows,
    each row [i] corresponds to a size of N, the subset, elements in the subset
    each col [j] corresponds to a value of sum

For Sum = 7 and subset with 3 elements
set = {3, 34, 4}

i stands for the number of elements from the set k that we can take to form the sum
j standas for the sum

row 0 has results of sums using no elements from the set
row 1 has results of sums using only the first element of the set
row 2 has results of sums using the 2 first elements of the set
row 3 has results of sums using the 3 first elements of the set

Our result for this problem is using the 3 elements of the set, row 3 and column 7 which is the sum

       j
       0   1   2   3   4   5   6   7
i  0   T   F   F   F   F   F   F   F    Results with 0 element from set
   1   T   F   F   T   F   F   F   F    Results with the first element from set, 1 to k=1
   2   T   F   F   T   F   F   F   F    Results with two first elements from set, 1 and 2 for k=2
   3   T   F   F   T   T   F   F   T    Results with three first elements from set, 1, 2, 3 for k=3

'''
def is_subsetsum(myset, n, sum):
    subset=([[False for i in range(0,sum+1)]
                     for i in range(n+1)])

    # if j = 0 that means sum is 0
    for i in range(n+1):
        subset[i][0] = True

        # If there are no elements in the set (i = 0) then can't make sum with no elements
        for i in range(1, sum + 1):
            subset[0][i] = False

        # Fill the subset table in botton up manner
        for i in range(1, n + 1):
            for j in range(1, sum + 1):
                if j < myset[i - 1]: # j, the Sum is smaller than ith number in set
                    subset[i][j] = subset[i - 1][j] # we just use what we had in the previous row
                if j >= myset[i - 1]: # This element could fit
                    subset[i][j] = (subset[i - 1][j] or
                                    subset[i - 1][j - myset[i - 1]])
                    #print(subset[i - 1][j] or subset[i - 1][j - myset[i - 1]])
    for i in range(n+1):
        print(subset[i])

    return subset[n][sum]


myset = [3, 34, 4, 12, 5, 2]
#myset = [3, 34, 4]
n = len(myset)
sum = 9

r = is_subsetsum(myset, n, sum)
print("")
print("Amount to sum: " + str(sum))
print("Subset: " + str(myset))
print(r)