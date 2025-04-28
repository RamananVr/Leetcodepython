"""
LeetCode Problem #2141: Maximum Running Time of N Computers

Problem Statement:
You have n computers and m batteries. The power of the i-th battery is batteries[i]. 
You can insert at most one battery into each computer. You need to distribute the batteries 
among the computers in such a way that all the computers can run simultaneously for the 
maximum amount of time.

Return the maximum number of hours you can run all n computers simultaneously.

Constraints:
- n == number of computers
- m == len(batteries)
- 1 <= n <= m <= 10^5
- 1 <= batteries[i] <= 10^9
"""

from typing import List

def maxRunTime(n: int, batteries: List[int]) -> int:
    """
    Function to calculate the maximum running time of n computers using the given batteries.
    """
    # Total power available
    total_power = sum(batteries)
    
    # Binary search for the maximum possible running time
    left, right = 0, total_power // n
    while left < right:
        mid = (left + right + 1) // 2
        # Check if we can run all computers for `mid` hours
        required_power = n * mid
        available_power = sum(min(battery, mid) for battery in batteries)
        if available_power >= required_power:
            left = mid  # Try for a longer time
        else:
            right = mid - 1  # Try for a shorter time
    
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 2
    batteries1 = [3, 3, 3]
    print(maxRunTime(n1, batteries1))  # Expected Output: 4

    # Test Case 2
    n2 = 2
    batteries2 = [1, 1, 1, 1]
    print(maxRunTime(n2, batteries2))  # Expected Output: 2

    # Test Case 3
    n3 = 3
    batteries3 = [10, 10, 3, 5]
    print(maxRunTime(n3, batteries3))  # Expected Output: 8

    # Test Case 4
    n4 = 1
    batteries4 = [5, 5, 5]
    print(maxRunTime(n4, batteries4))  # Expected Output: 15

"""
Time Complexity Analysis:
- Sorting the batteries is O(m log m), where m is the number of batteries.
- The binary search runs in O(log(total_power // n)) iterations.
- For each iteration, we calculate the available power, which takes O(m).
- Overall complexity: O(m log m + m log(total_power // n)).

Space Complexity Analysis:
- The algorithm uses O(1) additional space apart from the input.

Topic: Binary Search
"""