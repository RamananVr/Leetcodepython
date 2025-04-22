"""
LeetCode Problem #681: Next Closest Time

Problem Statement:
Given a time represented in the format "HH:MM", form the next closest time by reusing the current digits. 
There is no limit on how many times a digit can be reused. You may assume the given input time is valid 
and follows the 24-hour clock format.

Example 1:
Input: time = "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4 is 19:39, which occurs 5 minutes later. 
It is not 19:33 because this uses digits not in the original time.

Example 2:
Input: time = "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9 is 22:22. It is the next day.

Constraints:
- time is in the format "HH:MM".
- It is guaranteed that the given input is valid and follows the 24-hour clock format.
"""

def nextClosestTime(time: str) -> str:
    # Extract the digits from the input time
    digits = set(time.replace(":", ""))
    current_minutes = int(time[:2]) * 60 + int(time[3:])  # Convert time to total minutes

    while True:
        # Increment the time by 1 minute
        current_minutes = (current_minutes + 1) % (24 * 60)  # Wrap around after 24 hours
        # Convert back to hours and minutes
        hours, minutes = divmod(current_minutes, 60)
        # Format the time as "HH:MM"
        next_time = f"{hours:02}:{minutes:02}"
        # Check if all digits in the new time are valid
        if all(digit in digits for digit in next_time.replace(":", "")):
            return next_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    time1 = "19:34"
    print(nextClosestTime(time1))  # Output: "19:39"

    # Test Case 2
    time2 = "23:59"
    print(nextClosestTime(time2))  # Output: "22:22"

    # Test Case 3
    time3 = "01:32"
    print(nextClosestTime(time3))  # Output: "01:33"

    # Test Case 4
    time4 = "11:11"
    print(nextClosestTime(time4))  # Output: "11:11" (same time since it's already the closest)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The worst-case scenario involves iterating through all possible times in a 24-hour period (1440 minutes).
- For each minute, we check if the digits are valid, which takes O(1) since the time string is always of fixed length.
- Thus, the time complexity is O(1440) = O(1) (constant time in practice due to the fixed size of the input).

Space Complexity:
- The space complexity is O(1) since we only use a fixed amount of extra space for variables and the set of digits.

Topic: Strings, Simulation
"""