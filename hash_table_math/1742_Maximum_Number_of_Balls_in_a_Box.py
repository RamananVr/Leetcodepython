"""
LeetCode Problem #1742: Maximum Number of Balls in a Box

Problem Statement:
You are working in a ball factory where you have n balls numbered from lowLimit up to highLimit inclusive (i.e., n == highLimit - lowLimit + 1), and an infinite number of boxes numbered from 1 to infinity.

Your job is to put each ball in a box based on the sum of its digits. For example, the ball number 321 will be put in the box number 3 + 2 + 1 = 6, and the ball number 10 will be put in the box number 1 + 0 = 1.

Given two integers lowLimit and highLimit, return the number of balls in the box with the most balls.

Example:
Input: lowLimit = 1, highLimit = 10
Output: 2
Explanation:
Box 1 contains balls with numbers {1, 10}.
Box 2 contains balls with number {2}.
Box 3 contains balls with number {3}.
...
Box 10 contains balls with number {10}.
The box with the most balls is box 1 with 2 balls.

Constraints:
- 1 <= lowLimit <= highLimit <= 10^5
"""

# Python Solution
from collections import defaultdict

def countBalls(lowLimit: int, highLimit: int) -> int:
    def digit_sum(n: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))
    
    box_counts = defaultdict(int)
    
    for ball in range(lowLimit, highLimit + 1):
        box_number = digit_sum(ball)
        box_counts[box_number] += 1
    
    return max(box_counts.values())

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lowLimit = 1
    highLimit = 10
    print(countBalls(lowLimit, highLimit))  # Output: 2

    # Test Case 2
    lowLimit = 5
    highLimit = 15
    print(countBalls(lowLimit, highLimit))  # Output: 2

    # Test Case 3
    lowLimit = 19
    highLimit = 28
    print(countBalls(lowLimit, highLimit))  # Output: 2

    # Test Case 4
    lowLimit = 1
    highLimit = 100
    print(countBalls(lowLimit, highLimit))  # Output: 9

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the digit sum for a number takes O(log10(n)) time, where n is the number of digits in the number.
- Iterating through all numbers from lowLimit to highLimit takes O(highLimit - lowLimit + 1).
- Therefore, the overall time complexity is O((highLimit - lowLimit + 1) * log10(highLimit)).

Space Complexity:
- We use a defaultdict to store the counts of balls in each box. In the worst case, the number of unique box numbers is proportional to the number of digits in highLimit, which is O(log10(highLimit)).
- Thus, the space complexity is O(log10(highLimit)).
"""

# Topic: Hash Table, Math