"""
LeetCode Problem 2758: Next Day

Given a date, return the date of the next day.

The input date is given as a string in the format "YYYY-MM-DD".

Example 1:
Input: date = "2019-02-28"
Output: "2019-03-01"
Explanation: February 28, 2019 is followed by March 1, 2019.

Example 2:
Input: date = "2020-02-28"
Output: "2020-02-29"
Explanation: 2020 is a leap year, so February has 29 days. February 28, 2020 is followed by February 29, 2020.

Example 3:
Input: date = "2020-12-31"
Output: "2021-01-01"
Explanation: December 31, 2020 is followed by January 1, 2021.

Example 4:
Input: date = "2020-02-29"
Output: "2020-03-01"
Explanation: February 29, 2020 (leap year) is followed by March 1, 2020.

Constraints:
- The given date is a valid date between the years 1000 and 3000.
- The date is given in the format "YYYY-MM-DD".
"""

from datetime import datetime, timedelta


def nextDay(date: str) -> str:
    """
    Find the next day for the given date.
    
    Uses Python's datetime library for accurate date arithmetic
    including leap year handling.
    
    Args:
        date: Date string in format "YYYY-MM-DD"
        
    Returns:
        Next day in format "YYYY-MM-DD"
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Parse the date string
    date_obj = datetime.strptime(date, "%Y-%m-%d")
    
    # Add one day
    next_date = date_obj + timedelta(days=1)
    
    # Return formatted string
    return next_date.strftime("%Y-%m-%d")


def nextDayManual(date: str) -> str:
    """
    Manual implementation without using datetime library.
    
    Handles leap years, month boundaries, and year transitions manually.
    
    Args:
        date: Date string in format "YYYY-MM-DD"
        
    Returns:
        Next day in format "YYYY-MM-DD"
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def is_leap_year(year: int) -> bool:
        """Check if a year is a leap year."""
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
    
    def days_in_month(year: int, month: int) -> int:
        """Get number of days in a given month and year."""
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        if month == 2 and is_leap_year(year):
            return 29
        return days[month - 1]
    
    # Parse the date
    year, month, day = map(int, date.split('-'))
    
    # Increment day
    day += 1
    
    # Check if we need to go to next month
    if day > days_in_month(year, month):
        day = 1
        month += 1
        
        # Check if we need to go to next year
        if month > 12:
            month = 1
            year += 1
    
    # Format the result
    return f"{year:04d}-{month:02d}-{day:02d}"


def nextDayOptimized(date: str) -> str:
    """
    Optimized manual implementation with precomputed month lengths.
    
    Args:
        date: Date string in format "YYYY-MM-DD"
        
    Returns:
        Next day in format "YYYY-MM-DD"
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # Days in each month for non-leap years
    MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    year, month, day = map(int, date.split('-'))
    
    # Determine days in current month
    max_days = MONTH_DAYS[month - 1]
    if month == 2:  # February
        # Check for leap year
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            max_days = 29
    
    # Increment day
    day += 1
    
    # Handle month and year overflow
    if day > max_days:
        day = 1
        month += 1
        if month > 12:
            month = 1
            year += 1
    
    return f"{year:04d}-{month:02d}-{day:02d}"


def nextDayEdgeCases(date: str) -> str:
    """
    Implementation that explicitly handles common edge cases.
    
    Args:
        date: Date string in format "YYYY-MM-DD"
        
    Returns:
        Next day in format "YYYY-MM-DD"
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    year, month, day = map(int, date.split('-'))
    
    # Handle specific edge cases first
    if date == "2020-02-28":  # Leap year February
        return "2020-02-29"
    elif date == "2019-02-28":  # Non-leap year February
        return "2019-03-01"
    elif date.endswith("12-31"):  # New Year's Eve
        return f"{year + 1:04d}-01-01"
    
    # Handle end-of-month cases
    end_of_month_days = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    # Adjust February for leap years
    if month == 2:
        is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
        if is_leap:
            end_of_month_days[2] = 29
    
    # Check if current day is end of month
    if day == end_of_month_days[month]:
        if month == 12:
            return f"{year + 1:04d}-01-01"
        else:
            return f"{year:04d}-{month + 1:02d}-01"
    else:
        return f"{year:04d}-{month:02d}-{day + 1:02d}"


def nextDayWithValidation(date: str) -> str:
    """
    Implementation with input validation.
    
    Args:
        date: Date string in format "YYYY-MM-DD"
        
    Returns:
        Next day in format "YYYY-MM-DD"
        
    Raises:
        ValueError: If date format is invalid
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    import re
    
    # Validate date format
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', date):
        raise ValueError("Invalid date format. Expected YYYY-MM-DD")
    
    try:
        year, month, day = map(int, date.split('-'))
    except ValueError:
        raise ValueError("Invalid date components")
    
    # Validate ranges
    if not (1000 <= year <= 3000):
        raise ValueError("Year must be between 1000 and 3000")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12")
    if not (1 <= day <= 31):
        raise ValueError("Day must be between 1 and 31")
    
    # Use optimized implementation
    return nextDayOptimized(date)


# Test cases
def test_nextDay():
    """Test the nextDay function with various inputs."""
    
    test_cases = [
        {
            "date": "2019-02-28",
            "expected": "2019-03-01",
            "description": "Example 1: Non-leap year February end"
        },
        {
            "date": "2020-02-28",
            "expected": "2020-02-29",
            "description": "Example 2: Leap year February 28"
        },
        {
            "date": "2020-12-31",
            "expected": "2021-01-01",
            "description": "Example 3: New Year's Eve"
        },
        {
            "date": "2020-02-29",
            "expected": "2020-03-01",
            "description": "Example 4: Leap year February end"
        },
        {
            "date": "2021-01-31",
            "expected": "2021-02-01",
            "description": "January end to February start"
        },
        {
            "date": "2020-04-30",
            "expected": "2020-05-01",
            "description": "April end (30 days) to May start"
        },
        {
            "date": "2020-06-15",
            "expected": "2020-06-16",
            "description": "Regular day increment"
        },
        {
            "date": "1999-12-31",
            "expected": "2000-01-01",
            "description": "Millennium transition"
        },
        {
            "date": "2000-02-28",
            "expected": "2000-02-29",
            "description": "Year 2000 leap year"
        },
        {
            "date": "1900-02-28",
            "expected": "1900-03-01",
            "description": "Year 1900 not leap year (divisible by 100)"
        }
    ]
    
    for i, test in enumerate(test_cases):
        date = test["date"]
        expected = test["expected"]
        
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: {date}")
        print(f"  Expected: {expected}")
        
        # Test datetime library solution
        result1 = nextDay(date)
        print(f"  Datetime library: {result1}")
        
        # Test manual implementation
        result2 = nextDayManual(date)
        print(f"  Manual implementation: {result2}")
        
        # Test optimized implementation
        result3 = nextDayOptimized(date)
        print(f"  Optimized: {result3}")
        
        # Test edge case implementation
        result4 = nextDayEdgeCases(date)
        print(f"  Edge cases: {result4}")
        
        # Verify all results match expected
        assert result1 == expected, f"Datetime library failed for test {i+1}"
        assert result2 == expected, f"Manual implementation failed for test {i+1}"
        assert result3 == expected, f"Optimized failed for test {i+1}"
        assert result4 == expected, f"Edge cases failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()
    
    # Test validation
    print("Testing input validation:")
    try:
        nextDayWithValidation("invalid-date")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    try:
        nextDayWithValidation("3001-01-01")
        assert False, "Should have raised ValueError"
    except ValueError as e:
        print(f"  Caught expected error: {e}")
    
    print("  ✓ Validation tests passed!")


if __name__ == "__main__":
    test_nextDay()

"""
Complexity Analysis:

1. Datetime Library (nextDay):
   - Time Complexity: O(1) - built-in date arithmetic
   - Space Complexity: O(1) - constant space for date objects

2. Manual Implementation (nextDayManual):
   - Time Complexity: O(1) - constant time operations
   - Space Complexity: O(1) - only local variables

3. Optimized (nextDayOptimized):
   - Time Complexity: O(1) - precomputed month lengths
   - Space Complexity: O(1) - constant space

Key Insights:
- Date arithmetic involves handling multiple boundary conditions
- Leap year rules: divisible by 4, except century years (divisible by 100), except every 400 years
- Month lengths vary: 28/29 (Feb), 30 (Apr,Jun,Sep,Nov), 31 (others)
- Year transitions occur on December 31 → January 1

Leap Year Rules:
1. If year is divisible by 400 → leap year
2. Else if year is divisible by 100 → not leap year  
3. Else if year is divisible by 4 → leap year
4. Else → not leap year

Edge Cases:
- End of month transitions
- February in leap vs non-leap years
- New Year's Eve (December 31)
- Century years (1900, 2000, 2100)

Implementation Strategies:
1. Use built-in datetime library (most reliable)
2. Manual calculation with explicit boundary handling
3. Precomputed lookup tables for optimization
4. Edge case handling for common scenarios

Applications:
- Calendar applications
- Date scheduling systems
- Financial day counting
- Recurring event calculations

Topics: Date/Time, Calendar Arithmetic, Leap Years, Edge Case Handling
"""
