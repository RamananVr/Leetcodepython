"""
LeetCode Problem #1360: Number of Days Between Two Dates

Problem Statement:
Write a function that takes two strings `date1` and `date2`, each representing a date in the format "YYYY-MM-DD". 
The function should return the number of days between the two dates.

The difference between the two dates is defined as:
- The absolute difference in days between the two dates.

Constraints:
- The given dates are valid dates between the years 1971 and 2100.
- Dates are given in the format "YYYY-MM-DD".

Example:
Input: date1 = "2020-01-15", date2 = "2019-12-31"
Output: 15
"""

from datetime import datetime

def days_between_dates(date1: str, date2: str) -> int:
    """
    Calculate the number of days between two dates.

    Args:
    date1 (str): The first date in "YYYY-MM-DD" format.
    date2 (str): The second date in "YYYY-MM-DD" format.

    Returns:
    int: The absolute number of days between the two dates.
    """
    # Convert the date strings to datetime objects
    d1 = datetime.strptime(date1, "%Y-%m-%d")
    d2 = datetime.strptime(date2, "%Y-%m-%d")
    
    # Calculate the absolute difference in days
    return abs((d1 - d2).days)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    date1 = "2020-01-15"
    date2 = "2019-12-31"
    print(days_between_dates(date1, date2))  # Output: 15

    # Test Case 2
    date1 = "2021-03-01"
    date2 = "2021-03-01"
    print(days_between_dates(date1, date2))  # Output: 0

    # Test Case 3
    date1 = "1971-01-01"
    date2 = "2100-12-31"
    print(days_between_dates(date1, date2))  # Output: 47481

    # Test Case 4
    date1 = "2022-12-31"
    date2 = "2023-01-01"
    print(days_between_dates(date1, date2))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting each date string to a datetime object using `datetime.strptime` takes O(1) time since the input format is fixed.
- Calculating the difference in days is also O(1).
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The function uses a constant amount of space to store the datetime objects and perform calculations.
- Therefore, the space complexity is O(1).

Topic: Date Manipulation
"""