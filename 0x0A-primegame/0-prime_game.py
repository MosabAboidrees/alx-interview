#!/usr/bin/python3
def isWinner(x, nums):
    """Determines the winner of each game of Prime Game"""
    if x < 1 or not nums:
        return None

    # Function to generate prime numbers up to the maximum number in nums
    def sieve_of_eratosthenes(n):
        primes = [True] * (n + 1)
        primes[0] = primes[1] = False
        for i in range(2, int(n**0.5) + 1):
            if primes[i]:
                for j in range(i * i, n + 1, i):
                    primes[j] = False
        return primes

    max_num = max(nums)
    primes = sieve_of_eratosthenes(max_num)
    prime_count = [0] * (max_num + 1)

    # Precompute the count of primes up to each number
    for i in range(1, max_num + 1):
        prime_count[i] = prime_count[i - 1] + (1 if primes[i] else 0)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
