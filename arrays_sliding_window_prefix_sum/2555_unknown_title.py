"""
LeetCode Problem #2555: Maximize Win From Two Segments

Problem Statement:
You are given an integer array `prizes` where `prizes[i]` represents the prize value of the i-th house in a row. 
You are also given an integer `k`. You want to maximize the total prize value you can collect by choosing two 
non-overlapping segments of houses. Each segment must have a length of at most `k`.

Return the maximum total prize value you can collect.

Constraints:
- 1 <= prizes.length <= 10^5
- 1 <= prizes[i] <= 10^4
- 1 <= k <= prizes.length
"""

# Solution
def maximizeWin(prizes, k):
    n = len(prizes)
    prefix_sum = [0] * (n + 1)
    
    # Calculate prefix sums for efficient range sum queries
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + prizes[i]
    
    # Sliding window to calculate the maximum sum of a segment of length <= k
    max_segment = [0] * (n + 1)
    max_sum = 0
    
    for i in range(1, n + 1):
        if i >= k:
            max_sum = max(max_sum, prefix_sum[i] - prefix_sum[i - k])
        max_segment[i] = max_sum
    
    # Calculate the maximum sum of two non-overlapping segments
    result = 0
    for i in range(1, n + 1):
        if i >= k:
            result = max(result, (prefix_sum[i] - prefix_sum[i - k]) + max_segment[i - k])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prizes = [1, 2, 3, 4, 5]
    k = 2
    print(maximizeWin(prizes, k))  # Expected Output: 9 (segments [4, 5] and [1, 2])

    # Test Case 2
    prizes = [5, 1, 2, 3, 4, 5]
    k = 3
    print(maximizeWin(prizes, k))  # Expected Output: 15 (segments [5, 1, 2] and [3, 4, 5])

    # Test Case 3
    prizes = [10, 20, 30, 40, 50]
    k = 1
    print(maximizeWin(prizes, k))  # Expected Output: 90 (segments [50] and [40])

    # Test Case 4
    prizes = [1, 1, 1, 1, 1]
    k = 2
    print(maximizeWin(prizes, k))  # Expected Output: 4 (segments [1, 1] and [1, 1])

    # Test Case 5
    prizes = [10, 9, 8, 7, 6, 5]
    k = 2
    print(maximizeWin(prizes, k))  # Expected Output: 34 (segments [10, 9] and [8, 7])

"""
Time Complexity:
- Calculating the prefix sum takes O(n).
- The sliding window to calculate the maximum segment sum takes O(n).
- The final loop to calculate the result also takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The prefix_sum array takes O(n) space.
- The max_segment array takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Sliding Window, Prefix Sum
"""