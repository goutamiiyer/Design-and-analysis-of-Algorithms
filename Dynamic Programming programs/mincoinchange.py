
# Minimum number of coins to make change

'''
Table r[i] contains the minimum number of coins needed to make change for each value of i
i.e. r[4] contains the minimum number of coins to make change for 4

For each value we try adding all the possible coins, for example, for r[4] we can try adding coins of
    1
    2
    3
In order to try a new coin, if we already have a result with another configuration, we substract the
value of the current coin[k] from the current value of i (for the coin with value 3 and computing
the value for 4, we take the optimal solution for 1 and add the new coin to get the current solution
for 4.

Given coins = {1, 2, 3}
     0   1   2   3   4   5   6   7   8   9   10
r    0   1   1   1   2   2   2   3   3   3   4

'''

MAX_VAL = 99999

def minCoinChange(coins, num_coins, N):
    r = [MAX_VAL] * (N+1)

    # Base case, no change to do
    r[0] = 0

    # For each size of N from 1 up to N
    for i in range(1, N+1):
        # For all choices of coins that we can add
        for k in range(0, num_coins):
            # Only if the new coin is smaller than what we want to make change of...
            if coins[k] <= i:
                previous = r[i - coins[k]] # The result without the amount of the new coin

                # if previous has a valid solution and previous plus this coins is better thatn r[i]
                if previous != MAX_VAL and previous + 1 < r[i]:
                    r[i] = previous + 1 # Save the number of coins for this better solution
    print(r)
    return r[N]

N = 10
mycoins = [1, 2, 3]
r = minCoinChange(mycoins, len(mycoins), N)
print(r)
