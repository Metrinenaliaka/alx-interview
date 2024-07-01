#!/usr/bin/python3
"""
This is a solution for game theory problem.
"""


def is_prime(num):
    """
    Checks if a number is a prime number.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of the game.
    """
    maria_wins = 0
    ben_wins = 0

    for n in nums[:x]:
        primes = set()
        for i in range(2, n + 1):
            if is_prime(i):
                primes.add(i)

        current_player = 'Maria'
        while primes:
            prime = min(primes)
            primes.remove(prime)
            multiples = set(range(prime, n + 1, prime))
            primes -= multiples

            if current_player == 'Maria':
                current_player = 'Ben'
            else:
                current_player = 'Maria'

        # The player who cannot make a move loses,
        # so we need to count the player who made the last move.
        if current_player == 'Ben':
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return 'Maria'
    elif ben_wins > maria_wins:
        return 'Ben'
    else:
        return None
