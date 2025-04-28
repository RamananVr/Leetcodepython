"""
LeetCode Question #1423: Maximum Points You Can Obtain from Cards

Problem Statement:
There are several cards arranged in a row, and each card has an associated number of points. The points are given in the integer array `cardPoints`.

In one step, you can take one card from the beginning or from the end of the row. You have to take exactly `k` cards.

Your goal is to maximize the total points you can obtain by taking exactly `k` cards.

Given the integer array `cardPoints` and the integer `k`, return the maximum score you can obtain.

Constraints:
- 1 <= cardPoints.length <= 10^5
- 1 <= cardPoints[i] <= 10^4
- 1 <= k <= cardPoints.length
"""

# Solution
def maxScore(cardPoints, k):
    """
    This function calculates the maximum score you can obtain by taking exactly k cards
    from the given cardPoints array.
    """
    n = len(cardPoints)
    total_points = sum(cardPoints)
    
    # If we take all cards, return the total sum
    if k == n:
        return total_points
    
    # Find the minimum sum of the subarray of size (n - k)
    window_size = n - k
    current_window_sum = sum(cardPoints[:window_size])
    min_window_sum = current_window_sum
    
    for i in range(window_size, n):
        current_window_sum += cardPoints[i] - cardPoints[i - window_size]
        min_window_sum = min(min_window_sum, current_window_sum)
    
    # Maximum score is the total points minus the minimum subarray sum
    return total_points - min_window_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cardPoints = [1, 2, 3, 4, 5, 6, 1]
    k = 3
    print(maxScore(cardPoints, k))  # Expected Output: 12

    # Test Case 2
    cardPoints = [2, 2, 2]
    k = 2
    print(maxScore(cardPoints, k))  # Expected Output: 4

    # Test Case 3
    cardPoints = [9, 7, 7, 9, 7, 7, 9]
    k = 7
    print(maxScore(cardPoints, k))  # Expected Output: 55

    # Test Case 4
    cardPoints = [1, 1000, 1]
    k = 1
    print(maxScore(cardPoints, k))  # Expected Output: 1000

    # Test Case 5
    cardPoints = [1, 79, 80, 1, 1, 1, 200, 1]
    k = 3
    print(maxScore(cardPoints, k))  # Expected Output: 202

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the total sum of the array takes O(n).
- Sliding window traversal takes O(n - k), which is O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- We use a constant amount of extra space for variables.
- Overall space complexity: O(1).

Topic: Arrays, Sliding Window
"""