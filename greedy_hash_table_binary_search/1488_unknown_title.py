"""
LeetCode Problem #1488: Avoid Flood in The City

Problem Statement:
Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the lake, it becomes full of water. If it rains over a lake that is already full, it will flood. However, you can avoid flooding by using a dry day to dry one lake.

You are given an integer array `rains` where:
- `rains[i] > 0` means it rains over the lake `rains[i]`.
- `rains[i] == 0` means it is a dry day, and you can choose one lake to dry.

Return an array `result` where:
- `result[i] == -1` if `rains[i] > 0`.
- `result[i] == x` (where `x > 0`) if `rains[i] == 0` and you choose to dry lake `x`.

If it is impossible to avoid flooding, return an empty array.

Constraints:
- `1 <= rains.length <= 10^5`
- `0 <= rains[i] <= 10^9`

Example 1:
Input: rains = [1, 2, 3, 4]
Output: [-1, -1, -1, -1]
Explanation: After each rain, the lakes 1, 2, 3, and 4 are full, but no lake floods.

Example 2:
Input: rains = [1, 2, 0, 0, 2, 1]
Output: [-1, -1, 2, 1, -1, -1]
Explanation: After rains 1 and 2, lakes 1 and 2 are full. On the third day, it is dry, so you dry lake 2. On the fourth day, it is dry, so you dry lake 1. After that, when it rains over lake 2 and lake 1 again, there is no flood.

Example 3:
Input: rains = [1, 2, 0, 1, 2]
Output: []
Explanation: After rains 1 and 2, lakes 1 and 2 are full. On the third day, it is dry, but drying one lake will not prevent flooding when it rains over lake 1 and lake 2 again.

---

Python Solution:
"""

from collections import defaultdict
import bisect

def avoidFlood(rains):
    # Dictionary to track the last day a lake was filled
    lake_last_rain = {}
    # List to store dry days
    dry_days = []
    # Result array
    result = [-1] * len(rains)
    
    for i, lake in enumerate(rains):
        if lake > 0:  # It's raining over a lake
            if lake in lake_last_rain:
                # Check if we can dry the lake before it floods
                idx = bisect.bisect_left(dry_days, lake_last_rain[lake])
                if idx == len(dry_days):
                    return []  # No dry day available to prevent flooding
                # Use the dry day to dry the lake
                result[dry_days[idx]] = lake
                dry_days.pop(idx)
            # Update the last day this lake was filled
            lake_last_rain[lake] = i
        else:  # It's a dry day
            dry_days.append(i)
            result[i] = 1  # Placeholder, will be updated later
    
    return result

"""
Example Test Cases:
"""

# Test Case 1
rains1 = [1, 2, 3, 4]
print(avoidFlood(rains1))  # Output: [-1, -1, -1, -1]

# Test Case 2
rains2 = [1, 2, 0, 0, 2, 1]
print(avoidFlood(rains2))  # Output: [-1, -1, 2, 1, -1, -1]

# Test Case 3
rains3 = [1, 2, 0, 1, 2]
print(avoidFlood(rains3))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `rains` array once, which is O(n).
- For each lake that needs to be dried, we use binary search to find the appropriate dry day, which is O(log m), where m is the number of dry days.
- In the worst case, m can be equal to n, so the overall complexity is O(n log n).

Space Complexity:
- We use a dictionary `lake_last_rain` to store the last rain day for each lake, which is O(k), where k is the number of unique lakes.
- We use a list `dry_days` to store the indices of dry days, which is O(n) in the worst case.
- The result array is also O(n).
- Overall space complexity is O(n).

Topic: Greedy, Hash Table, Binary Search
"""