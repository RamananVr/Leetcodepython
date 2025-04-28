"""
LeetCode Problem #1809: Ad-Free Sessions

Problem Statement:
You are given a list of integers `sessions` where `sessions[i]` represents the duration of the i-th session in minutes. 
An ad-free session is defined as a session whose duration is strictly greater than 5 minutes. 
Return the number of ad-free sessions in the list.

Example:
Input: sessions = [3, 10, 7, 2, 6]
Output: 3
Explanation: The ad-free sessions are [10, 7, 6], so the count is 3.

Constraints:
- 1 <= len(sessions) <= 10^4
- 1 <= sessions[i] <= 10^4
"""

# Solution
def count_ad_free_sessions(sessions):
    """
    Counts the number of ad-free sessions in the given list.

    :param sessions: List[int] - A list of session durations in minutes.
    :return: int - The number of ad-free sessions.
    """
    return sum(1 for session in sessions if session > 5)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sessions = [3, 10, 7, 2, 6]
    print(count_ad_free_sessions(sessions))  # Output: 3

    # Test Case 2
    sessions = [1, 2, 3, 4, 5]
    print(count_ad_free_sessions(sessions))  # Output: 0

    # Test Case 3
    sessions = [6, 7, 8, 9, 10]
    print(count_ad_free_sessions(sessions))  # Output: 5

    # Test Case 4
    sessions = [5, 5, 5, 5, 5]
    print(count_ad_free_sessions(sessions))  # Output: 0

    # Test Case 5
    sessions = [100, 200, 300, 400, 500]
    print(count_ad_free_sessions(sessions))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list of sessions once, checking if each session duration is greater than 5.
- This results in a time complexity of O(n), where n is the length of the `sessions` list.

Space Complexity:
- The function uses a generator expression to count the ad-free sessions, which does not require additional space proportional to the input size.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""