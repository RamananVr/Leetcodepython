"""
LeetCode Problem #1904: The Number of Full Rounds You Have Played

Problem Statement:
You are participating in an online game, and you have a start time and an end time for your gaming session. Both the start time and end time are given in the format "HH:MM". A round in the game lasts 15 minutes, and the start of every round happens at every quarter-hour mark (00, 15, 30, 45). For example, a round can start at "00:00", "00:15", "00:30", "00:45", and so on.

You want to calculate the number of full rounds you have played during your gaming session. A full round is a round that starts and ends entirely within your gaming session.

Given two strings `startTime` and `finishTime` in the format "HH:MM", return the number of full rounds you have played.

Note:
- If the end time is earlier than the start time, it means the gaming session spans midnight.

Constraints:
- `startTime` and `finishTime` are in the format "HH:MM".
- `00 <= HH <= 23`
- `00 <= MM <= 59`

Example:
Input: startTime = "12:01", finishTime = "12:44"
Output: 1
Explanation: You can only play one full round from 12:15 to 12:30.

Input: startTime = "20:00", finishTime = "06:00"
Output: 40
Explanation: The gaming session spans midnight. You can play 40 full rounds from 20:00 to 06:00.

Input: startTime = "00:00", finishTime = "23:59"
Output: 95
Explanation: You can play 95 full rounds in this gaming session.
"""

def numberOfRounds(startTime: str, finishTime: str) -> int:
    def timeToMinutes(time: str) -> int:
        """Convert time in HH:MM format to total minutes since 00:00."""
        hours, minutes = map(int, time.split(":"))
        return hours * 60 + minutes

    def roundUpToQuarter(minutes: int) -> int:
        """Round up minutes to the next quarter-hour mark."""
        return (minutes + 14) // 15 * 15

    def roundDownToQuarter(minutes: int) -> int:
        """Round down minutes to the previous quarter-hour mark."""
        return minutes // 15 * 15

    startMinutes = timeToMinutes(startTime)
    endMinutes = timeToMinutes(finishTime)

    # Handle the case where the session spans midnight
    if endMinutes < startMinutes:
        endMinutes += 24 * 60  # Add 24 hours in minutes

    # Round start time up to the next quarter-hour and end time down to the previous quarter-hour
    startRounded = roundUpToQuarter(startMinutes)
    endRounded = roundDownToQuarter(endMinutes)

    # Calculate the number of full rounds
    if startRounded >= endRounded:
        return 0
    return (endRounded - startRounded) // 15

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startTime = "12:01"
    finishTime = "12:44"
    print(numberOfRounds(startTime, finishTime))  # Output: 1

    # Test Case 2
    startTime = "20:00"
    finishTime = "06:00"
    print(numberOfRounds(startTime, finishTime))  # Output: 40

    # Test Case 3
    startTime = "00:00"
    finishTime = "23:59"
    print(numberOfRounds(startTime, finishTime))  # Output: 95

    # Test Case 4
    startTime = "18:45"
    finishTime = "18:46"
    print(numberOfRounds(startTime, finishTime))  # Output: 0

    # Test Case 5
    startTime = "23:30"
    finishTime = "00:15"
    print(numberOfRounds(startTime, finishTime))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a constant amount of work regardless of the input size. Converting time to minutes, rounding to the nearest quarter-hour, and performing arithmetic operations are all O(1) operations.
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The function uses a constant amount of extra space for variables and does not use any data structures that grow with input size.
- Therefore, the overall space complexity is O(1).

Topic: Math, Time Manipulation
"""