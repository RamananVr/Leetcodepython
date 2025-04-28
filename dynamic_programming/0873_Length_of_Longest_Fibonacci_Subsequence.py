"""
LeetCode Problem #873: Length of Longest Fibonacci Subsequence

Problem Statement:
A sequence x1, x2, ..., xn is Fibonacci-like if:
- n >= 3
- xi + xi+1 = xi+2 for all i + 2 <= n

Given a strictly increasing array arr of positive integers forming a sequence, return the length of the longest Fibonacci-like subsequence of arr. If one does not exist, return 0.

A subsequence is derived from another sequence arr by deleting some or no elements without changing the order of the remaining elements. For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].

Constraints:
- 3 <= len(arr) <= 1000
- 1 <= arr[i] < arr[i + 1] <= 10^9
"""

def lenLongestFibSubseq(arr):
    """
    Function to find the length of the longest Fibonacci-like subsequence in the array.

    :param arr: List[int] - A strictly increasing array of positive integers
    :return: int - Length of the longest Fibonacci-like subsequence
    """
    index_map = {x: i for i, x in enumerate(arr)}
    dp = {}
    max_len = 0

    for k in range(len(arr)):
        for j in range(k):
            # Check if arr[k] - arr[j] exists in the array and is valid
            i = index_map.get(arr[k] - arr[j])
            if i is not None and i < j:
                # Update dp state
                dp[j, k] = dp.get((i, j), 2) + 1
                max_len = max(max_len, dp[j, k])

    return max_len if max_len >= 3 else 0


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5, 6, 7, 8]
    print(lenLongestFibSubseq(arr1))  # Expected Output: 5 (The sequence is [1, 2, 3, 5, 8])

    # Test Case 2
    arr2 = [1, 3, 7, 11, 12, 14, 18]
    print(lenLongestFibSubseq(arr2))  # Expected Output: 3 (The sequence is [1, 11, 12])

    # Test Case 3
    arr3 = [1, 2, 3, 5, 8, 13, 21]
    print(lenLongestFibSubseq(arr3))  # Expected Output: 7 (The sequence is [1, 2, 3, 5, 8, 13, 21])

    # Test Case 4
    arr4 = [1, 3, 5, 9, 10, 11, 12]
    print(lenLongestFibSubseq(arr4))  # Expected Output: 0 (No Fibonacci-like subsequence exists)

    # Test Case 5
    arr5 = [1, 2, 3]
    print(lenLongestFibSubseq(arr5))  # Expected Output: 3 (The sequence is [1, 2, 3])


"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over k (O(n)), and the inner loop iterates over j (O(n)).
- For each pair (j, k), we perform a dictionary lookup (O(1)).
- Thus, the overall time complexity is O(n^2).

Space Complexity:
- We use a dictionary `dp` to store pairs of indices and their Fibonacci subsequence lengths.
- In the worst case, the dictionary can store O(n^2) entries.
- The space complexity is O(n^2).

Topic: Dynamic Programming
"""