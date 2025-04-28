"""
LeetCode Problem #1736: Latest Time by Replacing Hidden Digits

Problem Statement:
You are given a string `time` in the form of "hh:mm", where some of the digits in the string are hidden (represented by `?`).
The valid times are between "00:00" and "23:59" (inclusive). Replace every `?` with a digit (0-9) such that the resulting time
is the latest valid time possible.

Return the latest valid time in the format "hh:mm".

Constraints:
- `time` is a valid string of length 5 in the format "hh:mm".
- `time[2]` is always ':'.
- `time` contains exactly 4 digits or '?' characters.

Example:
Input: time = "2?:?0"
Output: "23:50"

Input: time = "0?:3?"
Output: "09:39"

Input: time = "1?:22"
Output: "19:22"
"""

# Python Solution
def maximumTime(time: str) -> str:
    # Convert the string to a list for easier manipulation
    time = list(time)
    
    # Handle the hour part
    if time[0] == '?':
        time[0] = '2' if time[1] == '?' or time[1] <= '3' else '1'
    if time[1] == '?':
        time[1] = '3' if time[0] == '2' else '9'
    
    # Handle the minute part
    if time[3] == '?':
        time[3] = '5'
    if time[4] == '?':
        time[4] = '9'
    
    # Join the list back into a string and return
    return ''.join(time)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    time1 = "2?:?0"
    print(maximumTime(time1))  # Output: "23:50"

    # Test Case 2
    time2 = "0?:3?"
    print(maximumTime(time2))  # Output: "09:39"

    # Test Case 3
    time3 = "1?:22"
    print(maximumTime(time3))  # Output: "19:22"

    # Test Case 4
    time4 = "??:??"
    print(maximumTime(time4))  # Output: "23:59"

    # Test Case 5
    time5 = "?4:5?"
    print(maximumTime(time5))  # Output: "14:59"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution processes each character of the input string exactly once, so the time complexity is O(1) since the input size is fixed at 5 characters.

Space Complexity:
- The solution uses a constant amount of extra space for the list conversion and manipulation, so the space complexity is O(1).

Topic: Strings
"""