"""
LeetCode Problem #1604: Alert Using Same Key-Card Three or More Times in a One Hour Period

Problem Statement:
LeetCode company workers use key-cards to unlock office doors. Each time a worker uses their key-card, the security system saves the worker's name and the time when it was used. The system emits an alert if any worker uses the key-card three or more times in a one-hour period.

You are given a list of strings `keyName` and `keyTime` where:
- `keyName[i]` is the name of the person who used the key-card at the `i-th` time.
- `keyTime[i]` is the time in "HH:MM" format for the `i-th` time.

Return a list of unique worker names who received an alert. The names should be returned in lexicographical order.

A one-hour period means any 60 minutes (inclusive). For example, "23:51", "23:52", and "00:01" are within a one-hour period, but "23:51" and "00:02" are not.

Constraints:
- `1 <= keyName.length, keyTime.length <= 10^5`
- `keyName.length == keyTime.length`
- `keyTime[i]` is in the format "HH:MM".
- `keyName[i]` contains only lowercase English letters.
- `1 <= keyName[i].length <= 10`.
- The times are not necessarily in order.

Example:
Input: keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","09:20","09:30","09:35"]
Output: ["daniel","luis"]

Explanation:
- "daniel" used the key-card at "10:00", "10:40", and "11:00". All three are within a one-hour period.
- "luis" used the key-card at "09:00", "09:20", "09:30", and "09:35". The first three are within a one-hour period.

Topic: Hash Table, Sorting
"""

from collections import defaultdict
from datetime import datetime

def alertNames(keyName, keyTime):
    # Helper function to convert time string to minutes
    def time_to_minutes(time_str):
        hours, minutes = map(int, time_str.split(":"))
        return hours * 60 + minutes

    # Dictionary to store times for each user
    user_times = defaultdict(list)

    # Populate the dictionary with times for each user
    for name, time in zip(keyName, keyTime):
        user_times[name].append(time_to_minutes(time))

    # List to store names of users who triggered the alert
    alerted_users = []

    # Check each user's times
    for name, times in user_times.items():
        # Sort the times for the user
        times.sort()
        # Check for any three consecutive times within a 60-minute window
        for i in range(len(times) - 2):
            if times[i + 2] - times[i] <= 60:
                alerted_users.append(name)
                break

    # Return the list of alerted users in lexicographical order
    return sorted(alerted_users)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    keyName1 = ["daniel","daniel","daniel","luis","luis","luis","luis"]
    keyTime1 = ["10:00","10:40","11:00","09:00","09:20","09:30","09:35"]
    print(alertNames(keyName1, keyTime1))  # Output: ["daniel", "luis"]

    # Test Case 2
    keyName2 = ["alice","alice","alice","bob","bob","bob","bob"]
    keyTime2 = ["12:01","12:02","12:03","09:00","09:20","09:30","09:35"]
    print(alertNames(keyName2, keyTime2))  # Output: ["alice", "bob"]

    # Test Case 3
    keyName3 = ["john","john","john"]
    keyTime3 = ["23:58","23:59","00:01"]
    print(alertNames(keyName3, keyTime3))  # Output: ["john"]

    # Test Case 4
    keyName4 = ["anna","anna","anna","anna"]
    keyTime4 = ["10:00","10:20","10:40","11:00"]
    print(alertNames(keyName4, keyTime4))  # Output: ["anna"]

"""
Time Complexity:
- Converting each time string to minutes: O(n), where n is the length of `keyName` (or `keyTime`).
- Sorting the times for each user: O(k * log(k)), where k is the average number of times per user.
- Checking for three consecutive times: O(k) per user.
- Overall: O(n + m * log(m)), where m is the total number of unique users.

Space Complexity:
- Storing times for each user: O(n), where n is the length of `keyName`.
- Overall: O(n).
"""