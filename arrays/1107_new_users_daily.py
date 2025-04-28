"""
LeetCode Question #1107: New Users Daily

Problem Statement:
You are given a list of integers `users` where `users[i]` represents the number of new users that signed up on the i-th day. 
Your task is to return the day (0-indexed) with the maximum number of new users. If there are multiple days with the same 
maximum number of new users, return the earliest day.

Constraints:
- 1 <= len(users) <= 10^4
- 0 <= users[i] <= 10^5
"""

def max_users_day(users):
    """
    Finds the day with the maximum number of new users. If there are multiple days with the same maximum,
    returns the earliest day.

    :param users: List[int] - List of integers representing new users per day.
    :return: int - The 0-indexed day with the maximum number of new users.
    """
    max_users = max(users)  # Find the maximum number of users
    return users.index(max_users)  # Return the index of the first occurrence of the maximum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Single day
    users = [10]
    print(max_users_day(users))  # Expected output: 0

    # Test Case 2: Multiple days with distinct maximum
    users = [5, 10, 15, 20, 25]
    print(max_users_day(users))  # Expected output: 4

    # Test Case 3: Multiple days with the same maximum
    users = [10, 20, 20, 15, 10]
    print(max_users_day(users))  # Expected output: 1

    # Test Case 4: Large input
    users = [1] * 10000
    users[5000] = 100
    print(max_users_day(users))  # Expected output: 5000

    # Test Case 5: Edge case with all zeros
    users = [0, 0, 0, 0]
    print(max_users_day(users))  # Expected output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the maximum value in the list takes O(n), where n is the length of the list.
- Finding the index of the maximum value also takes O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""