"""
LeetCode Problem #597: Friend Requests I: Overall Acceptance Rate

Problem Statement:
Given two integers `totalFriends` and `totalRequests`, and an integer array `acceptedRequests` where `acceptedRequests[i]` represents the number of friend requests accepted by the i-th user, return the overall acceptance rate as a floating-point number rounded to two decimal places.

The overall acceptance rate is defined as the total number of accepted friend requests divided by the total number of friend requests sent. If no friend requests were sent, return 0.0.

Constraints:
- 1 <= totalFriends <= 10^5
- 0 <= totalRequests <= 10^9
- 0 <= acceptedRequests[i] <= totalRequests
- The length of `acceptedRequests` is equal to `totalFriends`.

Example:
Input: totalFriends = 3, totalRequests = 10, acceptedRequests = [3, 5, 2]
Output: 1.0
Explanation: Total accepted requests = 3 + 5 + 2 = 10. Total requests sent = 10. Acceptance rate = 10 / 10 = 1.0.

Input: totalFriends = 3, totalRequests = 0, acceptedRequests = [0, 0, 0]
Output: 0.0
Explanation: No requests were sent, so the acceptance rate is 0.0.
"""

# Python Solution
def overallAcceptanceRate(totalFriends, totalRequests, acceptedRequests):
    """
    Calculate the overall acceptance rate of friend requests.

    :param totalFriends: int - Number of friends
    :param totalRequests: int - Total number of friend requests sent
    :param acceptedRequests: List[int] - Number of friend requests accepted by each user
    :return: float - Overall acceptance rate rounded to two decimal places
    """
    if totalRequests == 0:
        return 0.0
    
    totalAccepted = sum(acceptedRequests)
    acceptanceRate = totalAccepted / totalRequests
    return round(acceptanceRate, 2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    totalFriends = 3
    totalRequests = 10
    acceptedRequests = [3, 5, 2]
    print(overallAcceptanceRate(totalFriends, totalRequests, acceptedRequests))  # Output: 1.0

    # Test Case 2
    totalFriends = 3
    totalRequests = 0
    acceptedRequests = [0, 0, 0]
    print(overallAcceptanceRate(totalFriends, totalRequests, acceptedRequests))  # Output: 0.0

    # Test Case 3
    totalFriends = 5
    totalRequests = 20
    acceptedRequests = [4, 5, 6, 3, 2]
    print(overallAcceptanceRate(totalFriends, totalRequests, acceptedRequests))  # Output: 1.0

    # Test Case 4
    totalFriends = 2
    totalRequests = 15
    acceptedRequests = [7, 8]
    print(overallAcceptanceRate(totalFriends, totalRequests, acceptedRequests))  # Output: 1.0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of `acceptedRequests` takes O(totalFriends).
- The rest of the operations (division and rounding) are O(1).
- Overall time complexity: O(totalFriends).

Space Complexity:
- The function uses a constant amount of space for variables.
- Overall space complexity: O(1).
"""

# Topic: Arrays