"""
LeetCode Problem #1215: Stepping Numbers

Problem Statement:
A "stepping number" is an integer such that all of its adjacent digits have an absolute difference of exactly 1. 
For example, 321 is a stepping number while 421 is not.

Given two integers low and high, return a sorted list of all the stepping numbers in the inclusive range [low, high].

Constraints:
- 0 <= low <= high <= 2 * 10^9
- The total number of stepping numbers in the range will be at most 10^4.

Example:
Input: low = 0, high = 21
Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]
"""

from collections import deque

def countSteppingNumbers(low: int, high: int) -> list[int]:
    """
    Returns a sorted list of all stepping numbers in the range [low, high].
    """
    if low > high:
        return []

    # Result list to store stepping numbers
    result = []

    # BFS queue to generate stepping numbers
    queue = deque(range(10))  # Start with all single-digit numbers (0-9)

    while queue:
        num = queue.popleft()

        # If the number is within the range, add it to the result
        if low <= num <= high:
            result.append(num)

        # If the number exceeds the high limit, skip further processing
        if num == 0 or num > high:
            continue

        # Get the last digit of the current number
        last_digit = num % 10

        # Generate the next possible stepping numbers
        if last_digit > 0:  # Append last_digit - 1
            next_num = num * 10 + (last_digit - 1)
            if next_num <= high:
                queue.append(next_num)
        if last_digit < 9:  # Append last_digit + 1
            next_num = num * 10 + (last_digit + 1)
            if next_num <= high:
                queue.append(next_num)

    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 0
    high = 21
    print(countSteppingNumbers(low, high))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21]

    # Test Case 2
    low = 10
    high = 15
    print(countSteppingNumbers(low, high))  # Output: [10, 12]

    # Test Case 3
    low = 0
    high = 0
    print(countSteppingNumbers(low, high))  # Output: [0]

    # Test Case 4
    low = 100
    high = 200
    print(countSteppingNumbers(low, high))  # Output: [101, 121]

"""
Time Complexity:
- The BFS approach ensures that we generate each stepping number only once.
- Since the total number of stepping numbers in the range is at most 10^4, the time complexity is O(10^4).

Space Complexity:
- The space complexity is determined by the BFS queue and the result list.
- In the worst case, the queue and result list can each hold up to 10^4 numbers.
- Thus, the space complexity is O(10^4).

Topic: Breadth-First Search (BFS)
"""