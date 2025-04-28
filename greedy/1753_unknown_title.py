"""
LeetCode Problem #1753: Maximum Score From Removing Stones

Problem Statement:
You are playing a solitaire game with three piles of stones of sizes `a`, `b`, and `c` respectively. 
Each turn, you choose two different non-empty piles, take one stone from each, and add 1 point to your score. 
The game stops when there are fewer than two non-empty piles.

Given three integers `a`, `b`, and `c`, return the maximum score you can achieve.

Constraints:
- 1 <= a, b, c <= 10^5
"""

def maximumScore(a: int, b: int, c: int) -> int:
    """
    Calculate the maximum score by removing stones from the three piles.

    Args:
    a (int): Number of stones in the first pile.
    b (int): Number of stones in the second pile.
    c (int): Number of stones in the third pile.

    Returns:
    int: The maximum score achievable.
    """
    # Sort the piles to ensure a <= b <= c
    piles = sorted([a, b, c])
    a, b, c = piles[0], piles[1], piles[2]

    # If the sum of the two smaller piles is less than or equal to the largest pile,
    # the maximum score is simply the sum of the two smaller piles.
    if a + b <= c:
        return a + b

    # Otherwise, distribute stones evenly between the piles
    return (a + b + c) // 2


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b, c = 2, 4, 6
    print(maximumScore(a, b, c))  # Expected Output: 6

    # Test Case 2
    a, b, c = 4, 4, 6
    print(maximumScore(a, b, c))  # Expected Output: 7

    # Test Case 3
    a, b, c = 1, 8, 8
    print(maximumScore(a, b, c))  # Expected Output: 8

    # Test Case 4
    a, b, c = 1, 1, 1
    print(maximumScore(a, b, c))  # Expected Output: 1

    # Test Case 5
    a, b, c = 10, 10, 10
    print(maximumScore(a, b, c))  # Expected Output: 15


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the three piles takes O(1) since there are only three elements.
- The rest of the operations (comparison and arithmetic) are O(1).
- Overall time complexity: O(1).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables.
- Overall space complexity: O(1).

Topic: Greedy
"""