"""
LeetCode Problem #1454: Number of Students Doing Homework at a Given Time

Problem Statement:
Given two integer arrays `startTime` and `endTime` and an integer `queryTime`.

The `i-th` student started doing their homework at the time `startTime[i]` and finished it at time `endTime[i]`.

Return the number of students doing their homework at time `queryTime`. More formally, return the number of students where `queryTime` lies in the interval `[startTime[i], endTime[i]]` inclusive.

Constraints:
- `startTime.length == endTime.length`
- `1 <= startTime.length <= 100`
- `1 <= startTime[i] <= endTime[i] <= 1000`
- `1 <= queryTime <= 1000`
"""

def busyStudent(startTime, endTime, queryTime):
    """
    Function to count the number of students doing homework at a given queryTime.

    :param startTime: List[int] - List of start times for each student
    :param endTime: List[int] - List of end times for each student
    :param queryTime: int - The specific time to check
    :return: int - Number of students doing homework at queryTime
    """
    return sum(1 for start, end in zip(startTime, endTime) if start <= queryTime <= end)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 4
    print(busyStudent(startTime, endTime, queryTime))  # Output: 1

    # Test Case 2
    startTime = [4]
    endTime = [4]
    queryTime = 4
    print(busyStudent(startTime, endTime, queryTime))  # Output: 1

    # Test Case 3
    startTime = [4]
    endTime = [4]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))  # Output: 0

    # Test Case 4
    startTime = [1, 1, 1, 1]
    endTime = [1, 3, 2, 4]
    queryTime = 2
    print(busyStudent(startTime, endTime, queryTime))  # Output: 3

    # Test Case 5
    startTime = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    endTime = [10, 10, 10, 10, 10, 10, 10, 10, 10]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))  # Output: 5

"""
Time Complexity:
- The function iterates through the `startTime` and `endTime` arrays once using the `zip` function.
- For each pair, it performs a constant-time comparison to check if `queryTime` lies within the interval.
- Therefore, the time complexity is O(n), where n is the length of the `startTime` (or `endTime`) array.

Space Complexity:
- The function uses a generator expression to calculate the sum, which does not require additional space proportional to the input size.
- Thus, the space complexity is O(1).

Topic: Arrays
"""