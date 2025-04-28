"""
LeetCode Problem #1246: Palindrome Removal

Problem Statement:
Given an integer array `arr`, in one move you can select a subarray of `arr` that is a palindrome and remove it from the array. 
Note that after removing a subarray, the elements on the left and on the right of that subarray move together and form a new array.

Return the minimum number of moves needed to remove all elements from the array.

Constraints:
- 1 <= arr.length <= 100
- 1 <= arr[i] <= 20
"""

def minimumMoves(arr):
    """
    Dynamic Programming solution to find the minimum number of moves to remove all elements from the array.
    """
    n = len(arr)
    dp = [[0] * n for _ in range(n)]

    # Base case: Single element subarrays are palindromes, so they take 1 move to remove.
    for i in range(n):
        dp[i][i] = 1

    # Fill the DP table for subarrays of increasing lengths.
    for length in range(2, n + 1):  # length of the subarray
        for i in range(n - length + 1):
            j = i + length - 1  # end index of the subarray
            # Case 1: Remove the subarray in one move if it's a palindrome.
            if arr[i] == arr[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = float('inf')

            # Case 2: Try splitting the subarray into two parts and minimize the moves.
            for k in range(i, j):
                dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j])

    return dp[0][n - 1]


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2]
    print("Test Case 1:", minimumMoves(arr1))  # Expected Output: 2

    # Test Case 2
    arr2 = [1, 3, 4, 1, 5]
    print("Test Case 2:", minimumMoves(arr2))  # Expected Output: 3

    # Test Case 3
    arr3 = [1, 2, 3, 2, 1]
    print("Test Case 3:", minimumMoves(arr3))  # Expected Output: 1

    # Test Case 4
    arr4 = [1, 2, 2, 1]
    print("Test Case 4:", minimumMoves(arr4))  # Expected Output: 1

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print("Test Case 5:", minimumMoves(arr5))  # Expected Output: 5


"""
Time Complexity Analysis:
- The DP table has dimensions n x n, where n is the length of the array.
- For each subarray (i, j), we iterate over all possible split points k, which takes O(n) time.
- Therefore, the overall time complexity is O(n^3).

Space Complexity Analysis:
- The DP table requires O(n^2) space to store the results for all subarrays.

Topic: Dynamic Programming
"""