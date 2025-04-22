"""
LeetCode Problem #949: Largest Time for Given Digits

Problem Statement:
Given an array `arr` of 4 digits, find the largest 24-hour time that can be made.
The smallest 24-hour time is 00:00, and the largest is 23:59. Starting from 00:00, 
a time is larger if it is closer to 23:59 on a 24-hour clock.

Return the largest time in "HH:MM" format. If no valid time can be made, return an empty string.

Example 1:
Input: arr = [1,2,3,4]
Output: "23:41"

Example 2:
Input: arr = [5,5,5,5]
Output: ""

Constraints:
- arr.length == 4
- 0 <= arr[i] <= 9
"""

from itertools import permutations

def largestTimeFromDigits(arr):
    """
    Finds the largest 24-hour time that can be made from the given 4 digits.

    :param arr: List[int] - A list of 4 integers representing digits.
    :return: str - The largest valid time in "HH:MM" format, or an empty string if no valid time exists.
    """
    max_time = -1
    # Generate all permutations of the 4 digits
    for perm in permutations(arr):
        # Extract hours and minutes from the permutation
        hours = perm[0] * 10 + perm[1]
        minutes = perm[2] * 10 + perm[3]
        # Check if the time is valid
        if 0 <= hours < 24 and 0 <= minutes < 60:
            # Convert the time to minutes since 00:00 and update max_time
            total_minutes = hours * 60 + minutes
            max_time = max(max_time, total_minutes)
    
    # If no valid time was found, return an empty string
    if max_time == -1:
        return ""
    
    # Convert max_time back to "HH:MM" format
    max_hours = max_time // 60
    max_minutes = max_time % 60
    return f"{max_hours:02}:{max_minutes:02}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4]
    print(largestTimeFromDigits(arr1))  # Output: "23:41"

    # Test Case 2
    arr2 = [5, 5, 5, 5]
    print(largestTimeFromDigits(arr2))  # Output: ""

    # Test Case 3
    arr3 = [0, 0, 1, 0]
    print(largestTimeFromDigits(arr3))  # Output: "10:00"

    # Test Case 4
    arr4 = [2, 0, 6, 6]
    print(largestTimeFromDigits(arr4))  # Output: "20:06"

    # Test Case 5
    arr5 = [0, 4, 0, 0]
    print(largestTimeFromDigits(arr5))  # Output: "04:00"

"""
Time Complexity:
- Generating all permutations of the 4 digits takes O(4!) = O(24).
- For each permutation, we perform constant-time operations to check validity and update the maximum time.
- Thus, the overall time complexity is O(24) = O(1) (constant time).

Space Complexity:
- The space complexity is O(1) for storing variables like `max_time` and intermediate calculations.
- The permutations function uses O(4!) = O(24) space for generating permutations, but this is also constant.

Overall, both time and space complexity are O(1) due to the fixed size of the input.

Topic: Arrays
"""