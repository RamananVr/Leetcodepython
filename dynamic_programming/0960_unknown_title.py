"""
LeetCode Problem #960: Delete Columns to Make Sorted III

Problem Statement:
You are given an array of `n` strings `strs`, all of the same length. We may choose any set of deletion indices, and for each string, delete all the characters in those indices.

For example, if we have `strs = ["abcdef", "uvwxyz"]` and deletion indices `{0, 2, 3}`, then the final array after deletions will be `["bef", "vyz"]`.

Suppose we chose a set of deletion indices such that after deletions, the final array has its rows in lexicographic order (i.e., `strs[0] <= strs[1] <= strs[2] <= ... <= strs[n-1]`).

Return the minimum number of deletion indices needed to ensure that the rows are in lexicographic order.

Constraints:
- `1 <= strs.length <= 100`
- `1 <= strs[i].length <= 100`

"""

# Solution
def minDeletionSize(strs):
    """
    Finds the minimum number of columns to delete to make the rows lexicographically sorted.

    :param strs: List[str] - List of strings of equal length
    :return: int - Minimum number of columns to delete
    """
    n = len(strs)
    m = len(strs[0])
    
    # dp[i] represents the maximum number of columns that can be kept
    # if we consider up to column i.
    dp = [1] * m
    
    for i in range(m):
        for j in range(i):
            # Check if column i can follow column j
            if all(row[j] <= row[i] for row in strs):
                dp[i] = max(dp[i], dp[j] + 1)
    
    # The minimum number of deletions is the total columns minus the maximum kept columns
    return m - max(dp)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["babca", "bbazb"]
    print(minDeletionSize(strs1))  # Expected Output: 3

    # Test Case 2
    strs2 = ["edcba"]
    print(minDeletionSize(strs2))  # Expected Output: 4

    # Test Case 3
    strs3 = ["ghi", "def", "abc"]
    print(minDeletionSize(strs3))  # Expected Output: 0

    # Test Case 4
    strs4 = ["a", "b", "c"]
    print(minDeletionSize(strs4))  # Expected Output: 0

    # Test Case 5
    strs5 = ["zyx", "wvu", "tsr"]
    print(minDeletionSize(strs5))  # Expected Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all columns (m), and the inner loop iterates over all previous columns (m).
- For each pair of columns (i, j), we check all rows (n) to ensure lexicographic order.
- Thus, the time complexity is O(m^2 * n), where m is the number of columns and n is the number of rows.

Space Complexity:
- We use a DP array of size m to store the maximum number of columns that can be kept.
- Thus, the space complexity is O(m).

Topic: Dynamic Programming
"""