"""
LeetCode Question #2100: Find Good Days to Rob the Bank

Problem Statement:
You are given an integer array `security` where `security[i]` is the number of guards on duty on the i-th day. 
The days are numbered from 0 to `security.length - 1`. You are also given an integer `time`.

A day is considered "good" if:
1. The number of guards on duty for the previous `time` days is non-increasing.
2. The number of guards on duty for the next `time` days is non-decreasing.

More formally, this means:
- `security[i - time] >= security[i - time + 1] >= ... >= security[i]` for all `i - time >= 0`.
- `security[i] <= security[i + 1] <= ... <= security[i + time]` for all `i + time < security.length`.

Return a list of all good days to rob the bank. You may return the answer in any order.

Example 1:
Input: security = [5, 3, 3, 3, 5, 6, 2], time = 2
Output: [2, 3]

Example 2:
Input: security = [1, 1, 1, 1, 1], time = 0
Output: [0, 1, 2, 3, 4]

Example 3:
Input: security = [1, 2, 3, 4, 5, 6], time = 2
Output: []

Constraints:
- 1 <= security.length <= 10^5
- 0 <= security[i] <= 10^5
- 0 <= time <= 10^5
"""

# Python Solution
def goodDaysToRobBank(security, time):
    n = len(security)
    if time == 0:
        return list(range(n))
    
    # Arrays to store the number of non-increasing and non-decreasing days
    non_increasing = [0] * n
    non_decreasing = [0] * n
    
    # Calculate non-increasing days
    for i in range(1, n):
        if security[i] <= security[i - 1]:
            non_increasing[i] = non_increasing[i - 1] + 1
    
    # Calculate non-decreasing days
    for i in range(n - 2, -1, -1):
        if security[i] <= security[i + 1]:
            non_decreasing[i] = non_decreasing[i + 1] + 1
    
    # Find all good days
    result = []
    for i in range(time, n - time):
        if non_increasing[i] >= time and non_decreasing[i] >= time:
            result.append(i)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    security = [5, 3, 3, 3, 5, 6, 2]
    time = 2
    print(goodDaysToRobBank(security, time))  # Output: [2, 3]

    # Test Case 2
    security = [1, 1, 1, 1, 1]
    time = 0
    print(goodDaysToRobBank(security, time))  # Output: [0, 1, 2, 3, 4]

    # Test Case 3
    security = [1, 2, 3, 4, 5, 6]
    time = 2
    print(goodDaysToRobBank(security, time))  # Output: []

    # Test Case 4
    security = [10, 8, 6, 5, 5, 5, 6, 8, 10]
    time = 2
    print(goodDaysToRobBank(security, time))  # Output: [4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the `non_increasing` array takes O(n) time.
- Calculating the `non_decreasing` array takes O(n) time.
- Iterating through the array to find good days takes O(n) time.
Overall, the time complexity is O(n).

Space Complexity:
- The `non_increasing` and `non_decreasing` arrays each take O(n) space.
- The result list takes O(k) space, where k is the number of good days (k <= n).
Overall, the space complexity is O(n).
"""

# Topic: Arrays