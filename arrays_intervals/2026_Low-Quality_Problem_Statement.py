"""
LeetCode Problem #2026: Low-Quality Problem Statement
Title: Determine if Two Events Have Conflict

Problem Statement:
You are given two events represented as a list of strings `event1` and `event2`, where:
- `event1 = [start1, end1]` and `event2 = [start2, end2]`.
- `start1` and `end1` represent the start and end times of the first event, respectively.
- `start2` and `end2` represent the start and end times of the second event, respectively.

Each time is in the format "HH:MM", where `00 <= HH <= 23` and `00 <= MM <= 59`.

Your task is to determine if the two events conflict. Two events conflict if they overlap at any point in time.

Return `True` if the two events conflict, and `False` otherwise.

Constraints:
1. `event1.length == event2.length == 2`
2. `event1[0] <= event1[1]`
3. `event2[0] <= event2[1]`
4. All event times are valid 24-hour times.

Example:
Input: event1 = ["01:15", "02:00"], event2 = ["02:00", "03:00"]
Output: True

Input: event1 = ["01:00", "02:00"], event2 = ["01:20", "03:00"]
Output: True

Input: event1 = ["10:00", "11:00"], event2 = ["14:00", "15:00"]
Output: False
"""

# Solution
def haveConflict(event1, event2):
    """
    Determines if two events conflict based on their start and end times.

    Args:
    event1 (List[str]): A list containing the start and end times of the first event.
    event2 (List[str]): A list containing the start and end times of the second event.

    Returns:
    bool: True if the events conflict, False otherwise.
    """
    # Extract start and end times for both events
    start1, end1 = event1
    start2, end2 = event2

    # Two events conflict if their time intervals overlap
    return not (end1 < start2 or end2 < start1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Overlapping at the boundary
    event1 = ["01:15", "02:00"]
    event2 = ["02:00", "03:00"]
    print(haveConflict(event1, event2))  # Output: True

    # Test Case 2: Fully overlapping
    event1 = ["01:00", "02:00"]
    event2 = ["01:20", "03:00"]
    print(haveConflict(event1, event2))  # Output: True

    # Test Case 3: No overlap
    event1 = ["10:00", "11:00"]
    event2 = ["14:00", "15:00"]
    print(haveConflict(event1, event2))  # Output: False

    # Test Case 4: Exact same time intervals
    event1 = ["09:00", "10:00"]
    event2 = ["09:00", "10:00"]
    print(haveConflict(event1, event2))  # Output: True

    # Test Case 5: One event completely within another
    event1 = ["08:00", "12:00"]
    event2 = ["09:00", "10:00"]
    print(haveConflict(event1, event2))  # Output: True

# Time Complexity Analysis:
# The solution involves a constant number of comparisons (4 comparisons in total).
# Therefore, the time complexity is O(1).

# Space Complexity Analysis:
# The solution does not use any additional data structures or memory.
# Therefore, the space complexity is O(1).

# Topic: Arrays, Intervals