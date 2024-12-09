# 0x0A. Prime Game

## Table of Contents
- [Description](#description)
- [Requirements](#requirements)
- [How It Works](#how-it-works)
- [Usage](#usage)
- [Examples](#examples)
- [Files](#files)
- [Credits](#credits)

---

## Description
The **Prime Game** is a mathematical strategy game played between two players, Maria and Ben. The game involves selecting prime numbers from a set of consecutive integers and removing them along with their multiples. 

Players take turns, starting with Maria. If a player cannot make a move, they lose the game. This project implements the logic to determine the winner of each game, assuming both players play optimally, and returns the overall winner after multiple rounds.

---

## Requirements
This project is designed to run in the following environment:
- **Operating System**: Ubuntu 20.04 LTS
- **Python Version**: Python 3.4.3 or later
- **Style Guide**: PEP 8 (version 1.7.x)

---

## How It Works
1. **Game Rules**:
   - A set of consecutive integers from 1 to `n` is given.
   - Players take turns picking a prime number and removing it along with its multiples from the set.
   - The player who cannot make a move loses the game.

2. **Implementation Details**:
   - A helper function implements the **Sieve of Eratosthenes** to efficiently determine prime numbers up to the largest `n` in the input.
   - A precomputed list stores the cumulative count of prime numbers up to any number.
   - For each round, the count of primes determines the winner:
     - If the count is odd, Maria wins the round.
     - If the count is even, Ben wins the round.
   - The player with the most wins after all rounds is declared the overall winner.

---

## Usage
## Usage
Run the `0-prime_game.py` module to define the winner based on the number of rounds and the numbers for each round.

### Example
```bash
carrie@ubuntu:~/0x0A-primegame$ cat main_0.py
#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))

carrie@ubuntu:~/0x0A-primegame$
carrie@ubuntu:~/0x0A-primegame$ ./main_0.py
Winner: Ben
carrie@ubuntu:~/0x0A-primegame$