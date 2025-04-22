"""
LeetCode Problem #668: Kth Smallest Number in Multiplication Table

Problem Statement:
Nearly every one of us has used the Multiplication Table. But could you find out the k-th smallest number 
quickly from the multiplication table?

Given the integers m, n, and k, return the k-th smallest number in the m x n multiplication table.

Example 1:
Input: m = 3, n = 3, k = 5
Output: 3
Explanation: The multiplication table is:
1   2   3
2   4   6
3   6   9
The 5th smallest number is 3.

Example 2:
Input: m = 2, n = 3, k = 6
Output: 6
Explanation: The multiplication table is:
1   2   3
2   4   6
The 6th smallest number is 6.

Constraints:
- 1 <= m, n <= 300
- 1 <= k <= m * n
"""

# Solution
def findKthNumber(m: int, n: int, k: int) -> int:
    def count_less_equal(x):
        """Helper function to count numbers <= x in the multiplication table."""
        count = 0
        for i in range(1, m + 1):
            count += min(x // i, n)
        return count

    # Binary search to find the k-th smallest number
    left, right = 1, m * n
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    m1, n1, k1 = 3, 3, 5
    print(findKthNumber(m1, n1, k1))  # Output: 3

    # Test Case 2
    m2, n2, k2 = 2, 3, 6
    print(findKthNumber(m2, n2, k2))  # Output: 6

    # Test Case 3
    m3, n3, k3 = 3, 3, 1
    print(findKthNumber(m3, n3, k3))  # Output: 1

    # Test Case 4
    m4, n4, k4 = 300, 300, 90000
    print(findKthNumber(m4, n4, k4))  # Output: 300

"""
Time Complexity:
- The binary search runs in O(log(m * n)) iterations.
- For each iteration, the `count_less_equal` function runs in O(m) time.
- Therefore, the overall time complexity is O(m * log(m * n)).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""