"""
LeetCode Problem #441: Arranging Coins

Problem Statement:
You have `n` coins and you want to build a staircase with these coins. The staircase consists of k rows, 
where the ith row has exactly i coins. The last row of the staircase may be incomplete.

Given the integer `n`, return the total number of full rows of the staircase you will build.

Example 1:
Input: n = 5
Output: 2
Explanation: Because the 3rd row is incomplete, we return 2.

Example 2:
Input: n = 8
Output: 3
Explanation: Because the 4th row is incomplete, we return 3.

Constraints:
- 1 <= n <= 2^31 - 1
"""

# Solution
def arrangeCoins(n: int) -> int:
    """
    This function calculates the number of complete rows in a staircase
    that can be formed using n coins.
    """
    left, right = 0, n
    while left <= right:
        mid = (left + right) // 2
        total_coins = mid * (mid + 1) // 2  # Sum of first `mid` natural numbers
        if total_coins == n:
            return mid
        elif total_coins < n:
            left = mid + 1
        else:
            right = mid - 1
    return right

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    print(f"Input: {n1}, Output: {arrangeCoins(n1)}")  # Expected Output: 2

    # Test Case 2
    n2 = 8
    print(f"Input: {n2}, Output: {arrangeCoins(n2)}")  # Expected Output: 3

    # Test Case 3
    n3 = 1
    print(f"Input: {n3}, Output: {arrangeCoins(n3)}")  # Expected Output: 1

    # Test Case 4
    n4 = 10
    print(f"Input: {n4}, Output: {arrangeCoins(n4)}")  # Expected Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution uses binary search to find the number of complete rows. The range of search is from 0 to n, 
and the binary search reduces the search space by half in each iteration. Therefore, the time complexity is O(log n).

Space Complexity:
The solution uses a constant amount of space, as no additional data structures are used. 
Thus, the space complexity is O(1).
"""

# Topic: Binary Search