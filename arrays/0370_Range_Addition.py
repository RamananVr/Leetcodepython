"""
LeetCode Problem #370: Range Addition

Problem Statement:
You are given an integer length and an array updates where updates[i] = [startIdx, endIdx, inc] 
represents that the subarray A[startIdx...endIdx] (inclusive) should be incremented by inc.

Return the modified array after all updates have been applied to it.

Example:
Input: length = 5, updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
Output: [-2, 0, 3, 5, 3]

Explanation:
Initial state:
[0, 0, 0, 0, 0]

After applying [1, 3, 2]:
[0, 2, 2, 2, 0]

After applying [2, 4, 3]:
[0, 2, 5, 5, 3]

After applying [0, 2, -2]:
[-2, 0, 3, 5, 3]

Constraints:
1. 1 <= length <= 10^5
2. 0 <= updates.length <= 10^4
3. 0 <= startIdx <= endIdx < length
4. -1000 <= inc <= 1000
"""

# Clean and Correct Python Solution
def getModifiedArray(length, updates):
    """
    Apply range updates to an array of zeros and return the final array.

    :param length: int - Length of the array
    :param updates: List[List[int]] - List of updates where each update is [startIdx, endIdx, inc]
    :return: List[int] - The modified array after applying all updates
    """
    # Initialize the array with zeros
    result = [0] * length

    # Apply the range updates using the difference array technique
    for start, end, inc in updates:
        result[start] += inc
        if end + 1 < length:
            result[end + 1] -= inc

    # Compute the prefix sum to finalize the array
    for i in range(1, length):
        result[i] += result[i - 1]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    length = 5
    updates = [[1, 3, 2], [2, 4, 3], [0, 2, -2]]
    print(getModifiedArray(length, updates))  # Output: [-2, 0, 3, 5, 3]

    # Test Case 2
    length = 10
    updates = [[0, 5, 10], [3, 8, 5], [6, 9, -3]]
    print(getModifiedArray(length, updates))  # Output: [10, 10, 10, 15, 15, 15, 12, 12, 2, -3]

    # Test Case 3
    length = 1
    updates = [[0, 0, 5]]
    print(getModifiedArray(length, updates))  # Output: [5]

    # Test Case 4
    length = 6
    updates = []
    print(getModifiedArray(length, updates))  # Output: [0, 0, 0, 0, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Applying updates: O(U), where U is the number of updates (len(updates)).
- Computing the prefix sum: O(N), where N is the length of the array.
- Total: O(U + N).

Space Complexity:
- The result array takes O(N) space.
- Total: O(N).
"""

# Topic: Arrays