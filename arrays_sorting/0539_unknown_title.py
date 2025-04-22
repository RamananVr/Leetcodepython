"""
LeetCode Problem #539: Minimum Time Difference

Problem Statement:
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time points in the list.

Constraints:
1. 2 <= timePoints.length <= 2 * 10^4
2. timePoints[i] is in the format "HH:MM".

Example:
Input: timePoints = ["23:59","00:00"]
Output: 1

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0

Note:
- The time difference is calculated in minutes.
- The time points are circular, meaning the difference between "23:59" and "00:00" is 1 minute.
"""

# Solution
from typing import List

def findMinDifference(timePoints: List[str]) -> int:
    # Convert time points to minutes
    def time_to_minutes(time: str) -> int:
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    # Convert all time points to minutes
    minutes = sorted(time_to_minutes(time) for time in timePoints)

    # Add the circular difference (24 hours = 1440 minutes)
    minutes.append(minutes[0] + 1440)

    # Find the minimum difference
    min_diff = float('inf')
    for i in range(1, len(minutes)):
        min_diff = min(min_diff, minutes[i] - minutes[i - 1])

    return min_diff

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    timePoints1 = ["23:59", "00:00"]
    print(findMinDifference(timePoints1))  # Output: 1

    # Test Case 2
    timePoints2 = ["00:00", "23:59", "00:00"]
    print(findMinDifference(timePoints2))  # Output: 0

    # Test Case 3
    timePoints3 = ["01:01", "02:01", "03:00"]
    print(findMinDifference(timePoints3))  # Output: 59

    # Test Case 4
    timePoints4 = ["05:31", "22:08", "00:35"]
    print(findMinDifference(timePoints4))  # Output: 147

    # Test Case 5
    timePoints5 = ["12:00", "00:00", "06:00"]
    print(findMinDifference(timePoints5))  # Output: 360

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting each time point to minutes takes O(n), where n is the number of time points.
- Sorting the list of minutes takes O(n log n).
- Calculating the minimum difference takes O(n).
Overall time complexity: O(n log n).

Space Complexity:
- The space required to store the converted time points in minutes is O(n).
Overall space complexity: O(n).

Topic: Arrays, Sorting
"""