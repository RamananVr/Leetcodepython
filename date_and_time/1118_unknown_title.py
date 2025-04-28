"""
LeetCode Problem #1118: Number of Days in a Month

Problem Statement:
Given a year `year` and a month `month`, return the number of days in that month.

The input `year` will be in the range [1900, 2100].
The input `month` will be in the range [1, 12].

Note:
- February has 28 days in a common year and 29 days in a leap year.
- Leap years are divisible by 4 but not divisible by 100 unless they are also divisible by 400.

Example:
Input: year = 2000, month = 2
Output: 29

Input: year = 1900, month = 2
Output: 28

Input: year = 2023, month = 7
Output: 31
"""

def number_of_days(year: int, month: int) -> int:
    """
    Returns the number of days in the given month of the given year.
    """
    # Helper function to determine if a year is a leap year
    def is_leap_year(year: int) -> bool:
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    # Days in each month for a common year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # If the month is February, check for leap year
    if month == 2 and is_leap_year(year):
        return 29
    
    # Return the number of days for the given month
    return days_in_month[month - 1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Leap year February
    year = 2000
    month = 2
    print(number_of_days(year, month))  # Output: 29

    # Test Case 2: Non-leap year February
    year = 1900
    month = 2
    print(number_of_days(year, month))  # Output: 28

    # Test Case 3: July in a common year
    year = 2023
    month = 7
    print(number_of_days(year, month))  # Output: 31

    # Test Case 4: November in a common year
    year = 2023
    month = 11
    print(number_of_days(year, month))  # Output: 30

    # Test Case 5: Leap year February
    year = 2024
    month = 2
    print(number_of_days(year, month))  # Output: 29

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function `is_leap_year` performs a constant number of arithmetic operations, so its time complexity is O(1).
- Accessing the `days_in_month` list and checking the leap year condition are both O(1) operations.
- Overall, the time complexity of the solution is O(1).

Space Complexity:
- The function uses a fixed-size list `days_in_month` with 12 elements, which is a constant space requirement.
- No additional space is used apart from a few variables.
- Overall, the space complexity of the solution is O(1).

Topic: Date and Time
"""