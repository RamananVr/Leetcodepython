"""
LeetCode Problem #1154: Day of the Year

Problem Statement:
Given a string `date` representing a Gregorian calendar date formatted as "YYYY-MM-DD", 
return the day number of the year.

The day number is the number of days from January 1st to the given date, inclusive. 
The input string is guaranteed to be a valid date in the format "YYYY-MM-DD".

Constraints:
- `date.length == 10`
- `date[4] == '-' and date[7] == '-'`
- 1 <= year <= 9999
- 1 <= month <= 12
- 1 <= day <= 31
- The given date is valid in the Gregorian calendar.

Example:
Input: date = "2019-01-09"
Output: 9
Explanation: Given date is the 9th day of the year in 2019.

Input: date = "2019-02-10"
Output: 41
Explanation: February 10th is the 41st day of the year in 2019.

Input: date = "2003-03-01"
Output: 60

Input: date = "2004-03-01"
Output: 61 (2004 is a leap year)
"""

def dayOfYear(date: str) -> int:
    """
    Calculate the day of the year for a given date in the format "YYYY-MM-DD".
    """
    # Parse the input date
    year, month, day = map(int, date.split('-'))
    
    # Days in each month for a non-leap year
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # Check if the year is a leap year
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[1] = 29  # February has 29 days in a leap year
    
    # Calculate the day of the year
    return sum(days_in_month[:month - 1]) + day

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    date1 = "2019-01-09"
    print(dayOfYear(date1))  # Output: 9

    # Test Case 2
    date2 = "2019-02-10"
    print(dayOfYear(date2))  # Output: 41

    # Test Case 3
    date3 = "2003-03-01"
    print(dayOfYear(date3))  # Output: 60

    # Test Case 4
    date4 = "2004-03-01"
    print(dayOfYear(date4))  # Output: 61

"""
Time Complexity:
- Parsing the date and splitting it into year, month, and day takes O(1).
- Summing up the days in the months up to the given month takes O(1) since the number of months is fixed (12).
- Overall, the time complexity is O(1).

Space Complexity:
- The space complexity is O(1) since we use a fixed amount of extra space for the `days_in_month` list and a few variables.

Topic: Date and Time
"""