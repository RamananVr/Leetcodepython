"""
LeetCode Question #252: Meeting Rooms

Problem Statement:
Given an array of meeting time intervals where `intervals[i] = [start_i, end_i]`, determine if a person could attend all meetings.
An individual can attend all meetings if no two meetings overlap.

Example 1:
Input: intervals = [[0,30],[5,10],[15,20]]
Output: False

Example 2:
Input: intervals = [[7,10],[2,4]]
Output: True

Constraints:
- 0 <= intervals.length <= 10^4
- intervals[i].length == 2
- 0 <= start_i < end_i <= 10^6
"""

def canAttendMeetings(intervals):
    """
    Determines if a person can attend all meetings without any overlap.

    :param intervals: List[List[int]] - A list of meeting time intervals
    :return: bool - True if a person can attend all meetings, False otherwise
    """
    # Sort intervals by their start times
    intervals.sort(key=lambda x: x[0])
    
    # Check for overlapping intervals
    for i in range(1, len(intervals)):
        # If the start of the current meeting is less than the end of the previous meeting, there's an overlap
        if intervals[i][0] < intervals[i - 1][1]:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Overlapping meetings
    intervals1 = [[0, 30], [5, 10], [15, 20]]
    print(canAttendMeetings(intervals1))  # Output: False

    # Test Case 2: Non-overlapping meetings
    intervals2 = [[7, 10], [2, 4]]
    print(canAttendMeetings(intervals2))  # Output: True

    # Test Case 3: Empty intervals
    intervals3 = []
    print(canAttendMeetings(intervals3))  # Output: True

    # Test Case 4: Single meeting
    intervals4 = [[1, 5]]
    print(canAttendMeetings(intervals4))  # Output: True

    # Test Case 5: Meetings with no overlap but sorted in reverse order
    intervals5 = [[5, 10], [0, 4]]
    print(canAttendMeetings(intervals5))  # Output: True

"""
Time Complexity Analysis:
- Sorting the intervals takes O(n log n), where n is the number of intervals.
- The subsequent loop to check for overlaps runs in O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the space used by the sorting algorithm).
- Overall space complexity: O(1).

Topic: Arrays, Sorting
"""