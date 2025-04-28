"""
LeetCode Problem #2801: Count Stepping Numbers in Range

Problem Statement:
A "stepping number" is an integer such that all adjacent digits have an absolute difference of exactly 1. 
For example, 123 is a stepping number because |1 - 2| = 1 and |2 - 3| = 1, but 358 is not a stepping number 
because |3 - 5| ≠ 1.

Given two integers low and high, return the count of all stepping numbers in the inclusive range [low, high].

Constraints:
- 0 <= low <= high <= 10^9

Example:
Input: low = 0, high = 21
Output: 13
Explanation: The stepping numbers in the range are [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21].
"""

# Solution
from collections import deque

def countSteppingNumbers(low: int, high: int) -> int:
    """
    Counts the number of stepping numbers in the inclusive range [low, high].
    
    :param low: The lower bound of the range.
    :param high: The upper bound of the range.
    :return: The count of stepping numbers in the range.
    """
    if low > high:
        return 0
    
    # BFS approach to generate stepping numbers
    queue = deque(range(10))  # Start with single-digit numbers (0-9)
    count = 0
    
    while queue:
        num = queue.popleft()
        
        # If the number is within the range, count it
        if low <= num <= high:
            count += 1
        
        # If the number exceeds the upper bound, skip further processing
        if num == 0 or num > high:
            continue
        
        # Get the last digit of the current number
        last_digit = num % 10
        
        # Generate the next stepping numbers
        if last_digit > 0:
            next_num = num * 10 + (last_digit - 1)
            if next_num <= high:
                queue.append(next_num)
        if last_digit < 9:
            next_num = num * 10 + (last_digit + 1)
            if next_num <= high:
                queue.append(next_num)
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 0
    high = 21
    print(countSteppingNumbers(low, high))  # Output: 13

    # Test Case 2
    low = 10
    high = 15
    print(countSteppingNumbers(low, high))  # Output: 2 (10, 12)

    # Test Case 3
    low = 0
    high = 0
    print(countSteppingNumbers(low, high))  # Output: 1 (0)

    # Test Case 4
    low = 100
    high = 200
    print(countSteppingNumbers(low, high))  # Output: 10 (101, 121, 123, 141, 143, 161, 163, 181, 183, 201)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The BFS approach ensures that we only generate valid stepping numbers within the range [low, high].
- The number of stepping numbers is limited by the range and the constraints of the problem.
- In the worst case, we generate all stepping numbers up to 10^9, but this is highly constrained by the range.
- The complexity is approximately O(N), where N is the number of stepping numbers generated.

Space Complexity:
- The space complexity is determined by the size of the queue used in BFS.
- In the worst case, the queue can hold all stepping numbers up to the range [low, high].
- The space complexity is approximately O(N), where N is the number of stepping numbers generated.

Topic: BFS (Breadth-First Search)
"""