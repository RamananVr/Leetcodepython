"""
LeetCode Problem #944: Delete Columns to Make Sorted

Problem Statement:
You are given an array of `n` strings `strs`, all of the same length.

The strings can be arranged such that there is one string per row, making a grid. For example, `strs = ["abc", "bce", "cae"]` can be arranged as:
    a b c
    b c e
    c a e

You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted, but column 1 ('b', 'c', 'a') is not, so you would delete column 1.

Return the number of columns that you will delete.

Example 1:
Input: strs = ["cba", "daf", "ghi"]
Output: 1
Explanation: The grid looks as follows:
    c b a
    d a f
    g h i
Columns 0 and 2 are sorted, but column 1 is not, so you only need to delete 1 column.

Example 2:
Input: strs = ["a", "b"]
Output: 0
Explanation: The grid looks as follows:
    a
    b
All columns are sorted, so you do not need to delete any columns.

Example 3:
Input: strs = ["zyx", "wvu", "tsr"]
Output: 3
Explanation: The grid looks as follows:
    z y x
    w v u
    t s r
All columns are unsorted, so you will need to delete all 3 columns.

Constraints:
- `n == strs.length`
- `1 <= n <= 100`
- `1 <= strs[i].length <= 1000`
- `strs[i]` consists of lowercase English letters.
"""

# Python Solution
def minDeletionSize(strs):
    """
    Function to calculate the number of columns to delete to make the grid sorted.
    
    :param strs: List[str] - List of strings of equal length
    :return: int - Number of columns to delete
    """
    # Initialize a counter for unsorted columns
    unsorted_count = 0
    
    # Iterate over each column index
    for col in range(len(strs[0])):
        # Check if the column is sorted
        for row in range(1, len(strs)):
            if strs[row][col] < strs[row - 1][col]:
                # If not sorted, increment the counter and break
                unsorted_count += 1
                break
    
    return unsorted_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["cba", "daf", "ghi"]
    print(minDeletionSize(strs1))  # Output: 1

    # Test Case 2
    strs2 = ["a", "b"]
    print(minDeletionSize(strs2))  # Output: 0

    # Test Case 3
    strs3 = ["zyx", "wvu", "tsr"]
    print(minDeletionSize(strs3))  # Output: 3

    # Test Case 4
    strs4 = ["abc", "bce", "cae"]
    print(minDeletionSize(strs4))  # Output: 1

    # Test Case 5
    strs5 = ["aaa", "aaa", "aaa"]
    print(minDeletionSize(strs5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the number of strings and `m` be the length of each string.
- We iterate over each column (m iterations) and for each column, we iterate over the rows (n iterations).
- Thus, the time complexity is O(n * m).

Space Complexity:
- We use a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays