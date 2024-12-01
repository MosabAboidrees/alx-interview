#!/usr/bin/python3
"""
Module to determine the fewest number of coins needed
to meet a given amount total.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the given total.
    Args:
        coins (list): A list of integers representing the coin denominations.
        total (int): The target total amount.
    Returns:
        int: Fewest number of coins needed to meet the total,
        or -1 if it can't be met.
    """
    if total <= 0:
        return 0

    # Sort coins in descending order to start with the largest denominations
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total <= 0:
            break
        # Use as many coins of this denomination as possible
        count += total // coin
        total %= coin

    # If the total isn't zero, it means we can't meet the target amount
    return count if total == 0 else -1
