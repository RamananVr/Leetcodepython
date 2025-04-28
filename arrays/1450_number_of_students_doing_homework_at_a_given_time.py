"""
LeetCode Question #1450: Number of Students Doing Homework at a Given Time

Problem Statement:
Given two integer arrays `startTime` and `endTime` and an integer `queryTime`, 
where `startTime[i]` and `endTime[i]` represent the start and end times of the 
homework session of the ith student, return the number of students doing their 
homework at `queryTime`. More formally, return the number of students where 
`queryTime` lies in the interval `[startTime[i], endTime[i]]` inclusive.

Example 1:
Input: startTime = [1,2,3], endTime = [3,2,7], queryTime = 4
Output: 1

Example 2:
Input: startTime = [4], endTime = [4], queryTime = 4
Output: 1

Example 3:
Input: startTime = [1,1,1,1], endTime = [1,3,2,4], queryTime = 7
Output: 0

Constraints:
- `startTime.length == endTime.length`
- `1 <= startTime.length <= 100`
- `1 <= startTime[i] <= endTime[i] <= 1000`
- `1 <= queryTime <= 1000`
"""

# Python Solution
def busyStudent(startTime, endTime, queryTime):
    """
    Function to count the number of students doing homework at a given queryTime.

    :param startTime: List[int] - Start times of homework sessions
    :param endTime: List[int] - End times of homework sessions
    :param queryTime: int - The time to check
    :return: int - Number of students doing homework at queryTime
    """
    return sum(start <= queryTime <= end for start, end in zip(startTime, endTime))

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
    startTime = [1, 1, 1, 1]
    endTime = [1, 3, 2, 4]
    queryTime = 7
    print(busyStudent(startTime, endTime, queryTime))  # Output: 0

    # Test Case 4
    startTime = [1, 2, 3, 4, 5]
    endTime = [5, 5, 5, 5, 5]
    queryTime = 5
    print(busyStudent(startTime, endTime, queryTime))  # Output: 5

    # Test Case 5
    startTime = [1, 2, 3]
    endTime = [3, 2, 7]
    queryTime = 2
    print(busyStudent(startTime, endTime, queryTime))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `startTime` and `endTime` arrays using `zip`, 
  which has a time complexity of O(n), where n is the length of the arrays.

Space Complexity:
- The function uses a generator expression to calculate the sum, which does not 
  require additional space proportional to the input size. Thus, the space complexity is O(1).
"""

# Topic: Arrays