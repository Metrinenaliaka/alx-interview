#!/usr/bin/python3
"""
I decided to use dynamicprogramming
using tables
"""


def makeChange(coins, total):
    """
    minimum number of coins to make change for total
    """
    # Create a table to store the minimum number
    # of coins needed for each value from 0 to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Calculate the minimum number of coins needed
    # for each value from 1 to total
    for i in range(1, total + 1):
        for coin in coins:
            if coin <= i:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
