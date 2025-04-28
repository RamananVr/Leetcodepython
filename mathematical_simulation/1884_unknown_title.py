"""
LeetCode Problem #1884: Egg Drop With 2 Eggs and N Floors

Problem Statement:
You are given two identical eggs and you have access to a building with `n` floors labeled from `1` to `n`.

Your goal is to determine the minimum number of moves you need to find the highest floor from which an egg can be dropped without breaking.

Rules:
1. If an egg is dropped and does not break, it can be dropped again from another floor.
2. If an egg is dropped and breaks, it cannot be used again.
3. You can reuse the second egg as many times as needed.

Write a function `twoEggDrop(n)` that returns the minimum number of moves required to find the critical floor.

Constraints:
- 1 <= n <= 1000
"""

def twoEggDrop(n: int) -> int:
    """
    Function to calculate the minimum number of moves required to find the critical floor
    using 2 eggs and n floors.
    """
    # The problem can be solved using a mathematical approach.
    # We need to find the smallest integer `k` such that the sum of the first `k` natural numbers
    # (i.e., k * (k + 1) / 2) is greater than or equal to `n`.
    moves = 0
    while n > 0:
        moves += 1
        n -= moves
    return moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small number of floors
    print(twoEggDrop(2))  # Expected output: 2

    # Test Case 2: Medium number of floors
    print(twoEggDrop(10))  # Expected output: 4

    # Test Case 3: Large number of floors
    print(twoEggDrop(100))  # Expected output: 14

    # Test Case 4: Edge case with 1 floor
    print(twoEggDrop(1))  # Expected output: 1

    # Test Case 5: Edge case with maximum constraint
    print(twoEggDrop(1000))  # Expected output: 45

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a simple loop that iteratively subtracts the current move count from `n`.
- In the worst case, the loop runs until the sum of the first `k` natural numbers exceeds `n`.
- This is approximately O(sqrt(n)) because the sum of the first `k` natural numbers is proportional to k^2.

Space Complexity:
- The solution uses a constant amount of space (O(1)) since no additional data structures are used.

Topic: Mathematical Simulation
"""