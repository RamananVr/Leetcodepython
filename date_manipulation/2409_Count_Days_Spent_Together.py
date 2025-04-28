"""
LeetCode Problem #2409: Count Days Spent Together

Problem Statement:
Alice and Bob are traveling to different cities for their vacations. 
You are given four strings: `arriveAlice`, `leaveAlice`, `arriveBob`, and `leaveBob`. 
- `arriveAlice` and `leaveAlice` are the arrival and departure dates of Alice's vacation.
- `arriveBob` and `leaveBob` are the arrival and departure dates of Bob's vacation.

All dates are given in the format "MM-DD". Alice and Bob only travel within the same year, so the year is not included in the input.

Return the total number of days that Alice and Bob spend together during their vacations.

You can assume that all dates are valid and follow the Gregorian calendar.

Constraints:
- All dates are in the format "MM-DD".
- Alice and Bob's arrival dates are earlier than or equal to their departure dates.

Example:
Input: arriveAlice = "08-15", leaveAlice = "08-18", arriveBob = "08-16", leaveBob = "08-19"
Output: 3
Explanation: Alice will be in the city from 08-15 to 08-18. Bob will be in the city from 08-16 to 08-19. They will spend 08-16, 08-17, and 08-18 together, so the answer is 3.
"""

from datetime import datetime

def countDaysTogether(arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
    """
    Calculate the number of days Alice and Bob spend together during their vacations.

    Args:
    arriveAlice (str): Alice's arrival date in "MM-DD" format.
    leaveAlice (str): Alice's departure date in "MM-DD" format.
    arriveBob (str): Bob's arrival date in "MM-DD" format.
    leaveBob (str): Bob's departure date in "MM-DD" format.

    Returns:
    int: The total number of days Alice and Bob spend together.
    """
    # Convert the dates to datetime objects for easier comparison
    arriveAlice_date = datetime.strptime(arriveAlice, "%m-%d")
    leaveAlice_date = datetime.strptime(leaveAlice, "%m-%d")
    arriveBob_date = datetime.strptime(arriveBob, "%m-%d")
    leaveBob_date = datetime.strptime(leaveBob, "%m-%d")
    
    # Calculate the overlap period
    start_date = max(arriveAlice_date, arriveBob_date)
    end_date = min(leaveAlice_date, leaveBob_date)
    
    # If the overlap period is valid, calculate the number of days
    if start_date <= end_date:
        return (end_date - start_date).days + 1
    else:
        return 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arriveAlice = "08-15"
    leaveAlice = "08-18"
    arriveBob = "08-16"
    leaveBob = "08-19"
    print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))  # Output: 3

    # Test Case 2
    arriveAlice = "10-01"
    leaveAlice = "10-31"
    arriveBob = "11-01"
    leaveBob = "12-31"
    print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))  # Output: 0

    # Test Case 3
    arriveAlice = "01-01"
    leaveAlice = "12-31"
    arriveBob = "01-01"
    leaveBob = "12-31"
    print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))  # Output: 365

    # Test Case 4
    arriveAlice = "06-01"
    leaveAlice = "06-15"
    arriveBob = "06-10"
    leaveBob = "06-20"
    print(countDaysTogether(arriveAlice, leaveAlice, arriveBob, leaveBob))  # Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting the dates to datetime objects takes O(1) for each date, so the total time complexity is O(1).

Space Complexity:
- The space used is constant, as we only store a few datetime objects and variables. Thus, the space complexity is O(1).
"""

# Topic: Date Manipulation