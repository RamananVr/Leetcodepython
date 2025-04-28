"""
LeetCode Problem #1817: Finding the Users Active Minutes (UAM)

Problem Statement:
You are given the logs of user activity on LeetCode, and an integer k. The logs are represented by a 2D integer array `logs` where each `logs[i] = [IDi, timei]` indicates that the user with ID `IDi` performed an activity at the minute `timei`.

The "user active minutes" (UAM) for a given user is defined as the number of unique minutes in which the user performed an activity on LeetCode. A user’s UAM is considered `x` if the user performed activities in `x` unique minutes.

You are to calculate a 1-indexed array `answer` of size `k` such that, for each `j` (1 <= j <= k), `answer[j - 1]` is the number of users whose UAM equals `j`.

Return the array `answer` as described above.

Constraints:
- `1 <= logs.length <= 10^4`
- `0 <= IDi <= 10^9`
- `1 <= timei <= 10^5`
- `1 <= k <= 10^5`
"""

from collections import defaultdict

def findingUsersActiveMinutes(logs, k):
    """
    Function to calculate the number of users with a specific number of unique active minutes (UAM).
    
    Args:
    logs (List[List[int]]): A list of logs where each log is [user_id, time].
    k (int): The maximum UAM value to consider.
    
    Returns:
    List[int]: A list where the i-th element represents the number of users with UAM equal to i+1.
    """
    # Step 1: Use a dictionary to store unique active minutes for each user
    user_minutes = defaultdict(set)
    for user_id, time in logs:
        user_minutes[user_id].add(time)
    
    # Step 2: Count the UAM for each user
    uam_count = defaultdict(int)
    for user_id, minutes in user_minutes.items():
        uam_count[len(minutes)] += 1
    
    # Step 3: Build the result array
    result = [0] * k
    for uam, count in uam_count.items():
        if uam <= k:
            result[uam - 1] = count
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs = [[0, 5], [1, 2], [0, 2], [0, 5], [1, 3]]
    k = 5
    print(findingUsersActiveMinutes(logs, k))  # Output: [0, 2, 0, 0, 0]

    # Test Case 2
    logs = [[1, 1], [2, 2], [2, 3]]
    k = 4
    print(findingUsersActiveMinutes(logs, k))  # Output: [1, 1, 0, 0]

    # Test Case 3
    logs = [[1, 1], [1, 1], [1, 1]]
    k = 1
    print(findingUsersActiveMinutes(logs, k))  # Output: [1]

"""
Time Complexity Analysis:
- Step 1: Iterating through `logs` takes O(n), where n is the length of the logs array.
- Step 2: Iterating through `user_minutes` takes O(u), where u is the number of unique users. For each user, adding to the set takes O(1) on average.
- Step 3: Iterating through `uam_count` takes O(k) in the worst case.
Overall time complexity: O(n + u + k).

Space Complexity Analysis:
- The `user_minutes` dictionary stores up to O(u * m) unique entries, where u is the number of unique users and m is the average number of unique minutes per user.
- The `uam_count` dictionary stores up to O(k) entries.
Overall space complexity: O(u * m + k).

Topic: Hash Table
"""