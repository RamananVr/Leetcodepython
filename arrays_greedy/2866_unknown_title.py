"""
LeetCode Problem #2866: Beautiful Towers II

Problem Statement:
You are given an array `maxHeights` of positive integers where `maxHeights[i]` represents the maximum height of a tower that can be built at position `i`. A tower is a sequence of blocks stacked vertically.

You are tasked with building towers such that:
1. The height of the tower at position `i` is at most `maxHeights[i]`.
2. The height difference between any two adjacent towers is at most 1.

Your goal is to maximize the sum of the heights of all towers.

Return the maximum sum of the heights of the towers that can be achieved under these constraints.

Constraints:
- `1 <= maxHeights.length <= 10^5`
- `1 <= maxHeights[i] <= 10^5`
"""

def maximumSumOfHeights(maxHeights):
    """
    Function to calculate the maximum sum of tower heights under the given constraints.

    :param maxHeights: List[int] - The maximum heights of the towers.
    :return: int - The maximum sum of the heights of the towers.
    """
    n = len(maxHeights)
    
    # Initialize the result
    max_sum = 0

    # Iterate over each position as the peak
    for peak in range(n):
        # Calculate the heights to the left of the peak
        left_heights = [0] * n
        left_heights[peak] = maxHeights[peak]
        for i in range(peak - 1, -1, -1):
            left_heights[i] = min(maxHeights[i], left_heights[i + 1] + 1)
        
        # Calculate the heights to the right of the peak
        right_heights = [0] * n
        right_heights[peak] = maxHeights[peak]
        for i in range(peak + 1, n):
            right_heights[i] = min(maxHeights[i], right_heights[i - 1] + 1)
        
        # Combine the left and right heights
        total_heights = [min(left_heights[i], right_heights[i]) for i in range(n)]
        
        # Calculate the sum of the heights
        max_sum = max(max_sum, sum(total_heights))
    
    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    maxHeights = [2, 1, 4, 3]
    print(maximumSumOfHeights(maxHeights))  # Expected Output: 8

    # Test Case 2
    maxHeights = [5, 3, 2, 1]
    print(maximumSumOfHeights(maxHeights))  # Expected Output: 9

    # Test Case 3
    maxHeights = [1, 2, 3, 4, 5]
    print(maximumSumOfHeights(maxHeights))  # Expected Output: 9

    # Test Case 4
    maxHeights = [1]
    print(maximumSumOfHeights(maxHeights))  # Expected Output: 1

"""
Time Complexity Analysis:
- Let `n` be the length of the `maxHeights` array.
- For each position `peak` (O(n)), we calculate the left and right heights (O(n) each).
- This results in an overall time complexity of O(n^2).

Space Complexity Analysis:
- We use two auxiliary arrays `left_heights` and `right_heights`, each of size `n`.
- This results in a space complexity of O(n).

Note: The current solution is not optimal for large inputs due to its O(n^2) time complexity. A more efficient solution using a monotonic stack or other techniques may be required for competitive programming scenarios.

Topic: Arrays, Greedy
"""