"""
LeetCode Question #1891: Cutting Ribbons

Problem Statement:
You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon, and an integer k. 
You may cut any of the ribbons into any number of segments of positive integer lengths, or leave them as they are. 
Your goal is to obtain k ribbons of the same length. What is the maximum possible length of each ribbon you can obtain 
while still having k ribbons in total? If you cannot obtain k ribbons, return 0.

Example 1:
Input: ribbons = [9, 7, 5], k = 3
Output: 5
Explanation: Cut the ribbons as follows:
- Cut the first ribbon into two segments of length 5 and 4.
- Cut the second ribbon into one segment of length 5 and two segments of length 2.
- Leave the third ribbon as it is.
Now you have 3 ribbons of length 5.

Example 2:
Input: ribbons = [7, 5, 9], k = 4
Output: 4
Explanation: Cut the ribbons as follows:
- Cut the first ribbon into one segment of length 4 and one segment of length 3.
- Cut the second ribbon into one segment of length 4 and one segment of length 1.
- Cut the third ribbon into two segments of length 4 and one segment of length 1.
Now you have 4 ribbons of length 4.

Example 3:
Input: ribbons = [5, 5, 5], k = 4
Output: 0
Explanation: It is impossible to obtain 4 ribbons of the same length.

Constraints:
- 1 <= ribbons.length <= 10^5
- 1 <= ribbons[i] <= 10^5
- 1 <= k <= 10^9
"""

# Solution
def maxLength(ribbons, k):
    def can_cut(length):
        # Check if we can cut at least k ribbons of the given length
        return sum(ribbon // length for ribbon in ribbons) >= k

    # Binary search for the maximum possible length
    left, right = 1, max(ribbons)
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if can_cut(mid):
            result = mid  # Update result if we can cut k ribbons
            left = mid + 1  # Try for a larger length
        else:
            right = mid - 1  # Try for a smaller length

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ribbons = [9, 7, 5]
    k = 3
    print(maxLength(ribbons, k))  # Output: 5

    # Test Case 2
    ribbons = [7, 5, 9]
    k = 4
    print(maxLength(ribbons, k))  # Output: 4

    # Test Case 3
    ribbons = [5, 5, 5]
    k = 4
    print(maxLength(ribbons, k))  # Output: 0

    # Test Case 4
    ribbons = [1, 2, 3, 4, 9]
    k = 5
    print(maxLength(ribbons, k))  # Output: 2

    # Test Case 5
    ribbons = [100000, 100000, 100000]
    k = 10
    print(maxLength(ribbons, k))  # Output: 30000

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search runs in O(log(max(ribbons))) iterations, where max(ribbons) is the maximum ribbon length.
- For each iteration, we calculate the number of ribbons that can be cut, which takes O(n) time, where n is the length of the ribbons array.
- Therefore, the overall time complexity is O(n * log(max(ribbons))).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables for the binary search and calculations.

Topic: Binary Search
"""