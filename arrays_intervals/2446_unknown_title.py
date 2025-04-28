"""
LeetCode Problem #2446: Determine if Two Events Have Conflict

Problem Statement:
You are given two arrays of strings `event1` and `event2`, where:
- `event1 = [startTime1, endTime1]` and `event2 = [startTime2, endTime2]`.

Event times are given in the format "HH:MM". A conflict happens when two events overlap, i.e., one event starts before or when the other event ends, and the other event starts before or when the first event ends.

Return `True` if there is a conflict between the two events. Otherwise, return `False`.

Constraints:
- `event1.length == event2.length == 2`
- `event1[i].length == event2[i].length == 5`
- `startTime1 <= endTime1`
- `startTime2 <= endTime2`
- All the event times are valid 24-hour times.
"""

def haveConflict(event1: list[str], event2: list[str]) -> bool:
    """
    Determines if two events have a conflict based on their start and end times.

    Args:
    event1 (list[str]): A list containing the start and end times of the first event.
    event2 (list[str]): A list containing the start and end times of the second event.

    Returns:
    bool: True if the events have a conflict, False otherwise.
    """
    # Extract start and end times for both events
    start1, end1 = event1
    start2, end2 = event2

    # Check if the two events overlap
    return not (end1 < start2 or end2 < start1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Overlapping events
    event1 = ["01:15", "02:00"]
    event2 = ["02:00", "03:00"]
    print(haveConflict(event1, event2))  # Expected: True

    # Test Case 2: Non-overlapping events
    event1 = ["01:00", "02:00"]
    event2 = ["02:01", "03:00"]
    print(haveConflict(event1, event2))  # Expected: False

    # Test Case 3: Fully overlapping events
    event1 = ["01:00", "03:00"]
    event2 = ["02:00", "02:30"]
    print(haveConflict(event1, event2))  # Expected: True

    # Test Case 4: Identical events
    event1 = ["01:00", "02:00"]
    event2 = ["01:00", "02:00"]
    print(haveConflict(event1, event2))  # Expected: True

    # Test Case 5: Edge case with no overlap
    event1 = ["01:00", "01:30"]
    event2 = ["01:31", "02:00"]
    print(haveConflict(event1, event2))  # Expected: False

"""
Time Complexity Analysis:
- Extracting the start and end times for both events is O(1).
- The comparison operations to check for overlap are O(1).
- Overall, the time complexity is O(1).

Space Complexity Analysis:
- The function uses a constant amount of space for variables, so the space complexity is O(1).

Topic: Arrays, Intervals
"""