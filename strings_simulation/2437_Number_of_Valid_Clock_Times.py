"""
LeetCode Problem #2437: Number of Valid Clock Times

Problem Statement:
You are given a string `time` in the format "hh:mm", where some of the digits in the string are hidden (represented by `?`).
The valid times range from "00:00" to "23:59" (inclusive). Return the total number of valid clock times that can be represented
by the string.

Example:
- For time = "?5:00", the valid times are "05:00", "15:00", so the answer is 2.
- For time = "0?:0?", the valid times are "00:00", "01:01", ..., "09:09", so the answer is 100.

Constraints:
- `time` is a string in the format "hh:mm".
- `time` consists of digits and the character '?'.

"""

def countTime(time: str) -> int:
    """
    Function to calculate the number of valid clock times that can be represented by the given string `time`.
    """
    # Split the time into hours and minutes
    hours, minutes = time.split(":")
    
    # Calculate the number of valid hour combinations
    if hours == "??":
        hour_count = 24  # All 24 hours are valid
    elif hours[0] == "?":
        if hours[1] == "?":
            hour_count = 24  # All 24 hours are valid
        else:
            hour_count = 3 if int(hours[1]) <= 3 else 2  # First digit can be 0, 1, or 2
    elif hours[1] == "?":
        hour_count = 10 if hours[0] != "2" else 4  # Second digit depends on the first digit
    else:
        hour_count = 1  # Fixed hour
    
    # Calculate the number of valid minute combinations
    if minutes == "??":
        minute_count = 60  # All 60 minutes are valid
    elif minutes[0] == "?":
        minute_count = 6  # First digit can be 0-5
    elif minutes[1] == "?":
        minute_count = 10  # Second digit can be 0-9
    else:
        minute_count = 1  # Fixed minute
    
    # Total valid times is the product of valid hour and minute combinations
    return hour_count * minute_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    time1 = "?5:00"
    print(countTime(time1))  # Output: 2

    # Test Case 2
    time2 = "0?:0?"
    print(countTime(time2))  # Output: 100

    # Test Case 3
    time3 = "??:??"
    print(countTime(time3))  # Output: 1440

    # Test Case 4
    time4 = "1?:22"
    print(countTime(time4))  # Output: 10

    # Test Case 5
    time5 = "2?:4?"
    print(countTime(time5))  # Output: 40


"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs constant-time operations to calculate the number of valid hour and minute combinations.
- Therefore, the time complexity is O(1).

Space Complexity:
- The function uses a constant amount of extra space for variables and does not use any data structures that grow with input size.
- Therefore, the space complexity is O(1).

Topic: Strings, Simulation
"""