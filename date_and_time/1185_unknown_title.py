"""
LeetCode Problem #1185: Day of the Week

Problem Statement:
Given a date, return the corresponding day of the week for that date.

The input is given as three integers representing the year, month, and day of the month respectively.
Return the answer as one of the following strings: 
["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"].

Constraints:
- The given dates are valid dates between the years 1971 and 2100.

Example:
Input: year = 2021, month = 9, day = 8
Output: "Wednesday"
"""

from datetime import datetime

def dayOfTheWeek(day: int, month: int, year: int) -> str:
    """
    Given a date (day, month, year), return the day of the week as a string.
    """
    # List of days of the week starting from Sunday
    days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    
    # Use Python's datetime module to calculate the day of the week
    date = datetime(year, month, day)
    day_index = date.weekday()  # weekday() returns 0 for Monday, 6 for Sunday
    
    # Adjust the index to match the required format (Sunday = 0, Monday = 1, ..., Saturday = 6)
    return days_of_week[(day_index + 1) % 7]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    year, month, day = 2021, 9, 8
    print(dayOfTheWeek(day, month, year))  # Output: "Wednesday"

    # Test Case 2
    year, month, day = 1971, 1, 1
    print(dayOfTheWeek(day, month, year))  # Output: "Friday"

    # Test Case 3
    year, month, day = 2100, 12, 31
    print(dayOfTheWeek(day, month, year))  # Output: "Friday"

    # Test Case 4
    year, month, day = 2000, 2, 29
    print(dayOfTheWeek(day, month, year))  # Output: "Tuesday"

    # Test Case 5
    year, month, day = 2023, 10, 1
    print(dayOfTheWeek(day, month, year))  # Output: "Sunday"

"""
Time Complexity Analysis:
- The datetime module's `datetime` constructor and `weekday()` method both run in O(1) time.
- Therefore, the overall time complexity of the function is O(1).

Space Complexity Analysis:
- The function uses a fixed-size list `days_of_week` and a single `datetime` object, both of which require O(1) space.
- Therefore, the overall space complexity of the function is O(1).

Topic: Date and Time
"""