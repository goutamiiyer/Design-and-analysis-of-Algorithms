'''
Given a set of non-negative integers and a value sum, find if there is a subset of the
given set with sum equal to the given sum.
'''

def fibonacci(n):
    """
        Non recursive fibonacci function
    """
    r = [0] * (n+1)
    r[0] = 1
    r[1] = 1
    for i in range(2, n+1):
        r[i] = r[i-1] + r[i-2]
    return
n = 10
r = fibonacci(n)
print(r)
print(r[n])