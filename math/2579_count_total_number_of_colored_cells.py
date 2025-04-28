"""
LeetCode Question #2579: Count Total Number of Colored Cells

Problem Statement:
You are given an integer `n`. Initially, you have a grid with one colored cell located at the center. 
Each day, you color all the cells adjacent (up, down, left, right) to the colored cells from the previous day. 
Return the total number of colored cells after `n` days.

Constraints:
- 1 <= n <= 10^5
"""

# Solution
def colored_cells(n: int) -> int:
    """
    Calculate the total number of colored cells after n days.

    Args:
    n (int): Number of days.

    Returns:
    int: Total number of colored cells.
    """
    # The total number of colored cells after n days follows the formula:
    # Total cells = n^2 + (n-1)^2
    return n * n + (n - 1) * (n - 1)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 1
    print(colored_cells(n))  # Expected Output: 1

    # Test Case 2
    n = 2
    print(colored_cells(n))  # Expected Output: 5

    # Test Case 3
    n = 3
    print(colored_cells(n))  # Expected Output: 13

    # Test Case 4
    n = 4
    print(colored_cells(n))  # Expected Output: 25

    # Test Case 5
    n = 10
    print(colored_cells(n))  # Expected Output: 181


"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a simple mathematical formula, which takes O(1) time to compute.

Space Complexity:
- The solution uses a constant amount of space, so the space complexity is O(1).

Topic: Math
"""