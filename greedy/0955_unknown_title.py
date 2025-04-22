"""
LeetCode Problem #955: Delete Columns to Make Sorted II

Problem Statement:
You are given an array of strings `strs`, where each string is of the same length. You may choose any number of deletion indices, and for each string, delete all the characters in those indices.

For example, if `strs = ["abcdef", "uvwxyz"]` and you delete indices `0`, `2`, and `3`, the final array will be `["bef", "vyz"]`.

Suppose we chose a set of deletion indices such that after deletions, the final array is in lexicographic order (i.e., `strs[i] <= strs[i+1]` for all `i`). Return the minimum number of indices you must delete to ensure that `strs` is sorted in lexicographic order.

Constraints:
- `1 <= strs.length <= 100`
- `1 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

"""

# Python Solution
def minDeletionSize(strs):
    """
    Function to find the minimum number of columns to delete to make the array lexicographically sorted.

    :param strs: List[str] - List of strings of equal length
    :return: int - Minimum number of columns to delete
    """
    num_rows = len(strs)
    num_cols = len(strs[0])
    deleted_columns = 0
    sorted_rows = [False] * (num_rows - 1)  # Tracks if rows are already sorted

    for col in range(num_cols):
        # Check if deleting this column keeps the rows sorted
        if all(sorted_rows[i] or strs[i][col] <= strs[i + 1][col] for i in range(num_rows - 1)):
            # Update sorted_rows based on the current column
            for i in range(num_rows - 1):
                if strs[i][col] < strs[i + 1][col]:
                    sorted_rows[i] = True
        else:
            # If deleting this column is necessary, increment the count
            deleted_columns += 1

    return deleted_columns

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["ca", "bb", "ac"]
    print(minDeletionSize(strs1))  # Output: 1

    # Test Case 2
    strs2 = ["xc", "yb", "za"]
    print(minDeletionSize(strs2))  # Output: 0

    # Test Case 3
    strs3 = ["zyx", "wvu", "tsr"]
    print(minDeletionSize(strs3))  # Output: 3

    # Test Case 4
    strs4 = ["a", "b", "c"]
    print(minDeletionSize(strs4))  # Output: 0

    # Test Case 5
    strs5 = ["abcdef", "uvwxyz"]
    print(minDeletionSize(strs5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through each column (O(num_cols)) and checks the rows for lexicographic order (O(num_rows)).
- Therefore, the time complexity is O(num_cols * num_rows), where num_cols is the number of columns and num_rows is the number of rows.

Space Complexity:
- The algorithm uses an auxiliary list `sorted_rows` of size num_rows - 1 to track sorted rows.
- Therefore, the space complexity is O(num_rows).

Topic: Greedy
"""