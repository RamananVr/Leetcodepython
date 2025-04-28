"""
LeetCode Problem #1972: First and Last Day of the Week

Problem Statement:
You are given a list of dates in the format "YYYY-MM-DD". Your task is to determine the first and last day of the week for each date in the list. The week starts on Monday and ends on Sunday. Return a list of tuples where each tuple contains the first and last day of the week for the corresponding date in the input list.

Example:
Input: ["2023-10-04", "2023-10-08"]
Output: [("2023-10-02", "2023-10-08"), ("2023-10-02", "2023-10-08")]

Constraints:
1. The input list will contain at least one date and at most 10^4 dates.
2. Each date will be a valid date in the format "YYYY-MM-DD".
3. The output should be in the same order as the input.
"""

from datetime import datetime, timedelta
from typing import List, Tuple

def first_and_last_day_of_week(dates: List[str]) -> List[Tuple[str, str]]:
    """
    Given a list of dates, return the first and last day of the week for each date.

    Args:
    dates (List[str]): A list of dates in the format "YYYY-MM-DD".

    Returns:
    List[Tuple[str, str]]: A list of tuples where each tuple contains the first and last day of the week.
    """
    result = []
    for date_str in dates:
        # Parse the date string into a datetime object
        date = datetime.strptime(date_str, "%Y-%m-%d")
        
        # Calculate the first day of the week (Monday)
        start_of_week = date - timedelta(days=date.weekday())
        
        # Calculate the last day of the week (Sunday)
        end_of_week = start_of_week + timedelta(days=6)
        
        # Format the dates back to "YYYY-MM-DD" and append to the result
        result.append((start_of_week.strftime("%Y-%m-%d"), end_of_week.strftime("%Y-%m-%d")))
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dates = ["2023-10-04", "2023-10-08"]
    print(first_and_last_day_of_week(dates))  # Expected: [("2023-10-02", "2023-10-08"), ("2023-10-02", "2023-10-08")]

    # Test Case 2
    dates = ["2023-01-01", "2023-12-31"]
    print(first_and_last_day_of_week(dates))  # Expected: [("2022-12-26", "2023-01-01"), ("2023-12-25", "2023-12-31")]

    # Test Case 3
    dates = ["2023-07-15"]
    print(first_and_last_day_of_week(dates))  # Expected: [("2023-07-10", "2023-07-16")]

    # Test Case 4
    dates = ["2023-03-01", "2023-03-07", "2023-03-08"]
    print(first_and_last_day_of_week(dates))  # Expected: [("2023-02-27", "2023-03-05"), ("2023-03-06", "2023-03-12"), ("2023-03-06", "2023-03-12")]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Parsing each date and performing calculations for the first and last day of the week takes O(1) time.
- For a list of n dates, the total time complexity is O(n).

Space Complexity:
- The space used for the result list is proportional to the number of dates, i.e., O(n).
- The function uses a constant amount of additional space for intermediate calculations, so the overall space complexity is O(n).
"""

# Topic: Date and Time Manipulation