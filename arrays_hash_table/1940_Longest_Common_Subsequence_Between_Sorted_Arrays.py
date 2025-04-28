"""
LeetCode Problem #1940: Longest Common Subsequence Between Sorted Arrays

Problem Statement:
Given an array of `k` sorted integer arrays `arrays`, return the longest common subsequence (LCS) that is present in all the arrays.

A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.

Example:
Input: arrays = [[1,3,4], [1,4,7,9]]
Output: [1,4]

Constraints:
1. k == arrays.length
2. 2 <= k <= 100
3. 1 <= arrays[i].length <= 10^5
4. 1 <= arrays[i][j] <= 10^5
5. arrays[i] is sorted in strictly increasing order.
"""

from collections import Counter
from typing import List

def longest_common_subsequence(arrays: List[List[int]]) -> List[int]:
    """
    Finds the longest common subsequence present in all sorted arrays.

    Args:
    arrays (List[List[int]]): A list of k sorted integer arrays.

    Returns:
    List[int]: The longest common subsequence present in all arrays.
    """
    # Use a Counter to track the frequency of each element across all arrays
    element_count = Counter()
    k = len(arrays)  # Number of arrays

    # Increment the count for each element in each array
    for array in arrays:
        # Use a set to avoid counting duplicates within the same array
        element_count.update(set(array))

    # Filter elements that appear in all k arrays
    result = [key for key, count in element_count.items() if count == k]

    # Return the result sorted (since the arrays are sorted, the LCS must also be sorted)
    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arrays1 = [[1, 3, 4], [1, 4, 7, 9]]
    print(longest_common_subsequence(arrays1))  # Output: [1, 4]

    # Test Case 2
    arrays2 = [[2, 3, 5, 7], [3, 5, 7, 11], [1, 3, 5, 7, 13]]
    print(longest_common_subsequence(arrays2))  # Output: [3, 5, 7]

    # Test Case 3
    arrays3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(longest_common_subsequence(arrays3))  # Output: []

    # Test Case 4
    arrays4 = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
    print(longest_common_subsequence(arrays4))  # Output: [3, 4]

    # Test Case 5
    arrays5 = [[10, 20, 30], [10, 20, 30], [10, 20, 30]]
    print(longest_common_subsequence(arrays5))  # Output: [10, 20, 30]

"""
Time Complexity:
- Let n be the average length of the arrays and k be the number of arrays.
- For each array, we convert it to a set (O(n)) and update the Counter (O(n)).
- This results in a total time complexity of O(k * n).
- Sorting the result takes O(m * log(m)), where m is the size of the LCS (typically much smaller than n).

Space Complexity:
- The Counter stores at most O(n * k) elements (in the worst case where all elements are unique across arrays).
- The result list takes O(m) space, where m is the size of the LCS.
- Overall space complexity is O(n * k).

Topic: Arrays, Hash Table
"""