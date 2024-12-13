#!/usr/bin/python3
"""Prime game module.
"""


def isWinner(x, nums):
    """Determines the winner of a prime game session with `x` rounds.
    Args:
        x (int): The number of rounds.
        nums (list): List of integers representing the upper limit
        of numbers for each round.
    Returns:
        str: The name of the player with the most wins ('Maria' or 'Ben').
        If the number of wins is the same, returns None.
    """
    if x < 1 or not nums:
        # If there are no rounds or nums is empty, return None
        return None

    # Initialize win counters for Maria and Ben
    marias_wins, bens_wins = 0, 0
    # Generate primes up to the maximum number in nums
    n = max(nums)
    # Initialize a list to track prime numbers
    primes = [True for _ in range(1, n + 1, 1)]
    primes[0] = False  # 1 is not a prime number

    # Sieve of Eratosthenes to find all prime numbers up to n
    for i, is_prime in enumerate(primes, 1):
        if i == 1 or not is_prime:
            continue
        for j in range(i + i, n + 1, i):
            primes[j - 1] = False  # Mark multiples of i as non-prime

    # Determine the winner for each round
    for _, n in zip(range(x), nums):
        # Count the number of primes less than or equal to n
        primes_count = len(list(filter(lambda x: x, primes[0: n])))

        # Update win counters based on the number of primes
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    # Determine the overall winner
    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
