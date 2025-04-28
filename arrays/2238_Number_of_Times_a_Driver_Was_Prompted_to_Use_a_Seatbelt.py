"""
LeetCode Problem #2238: Number of Times a Driver Was Prompted to Use a Seatbelt

Problem Statement:
A car has a seatbelt reminder system that prompts the driver to use a seatbelt. 
The system records the number of times the driver was prompted to use the seatbelt 
during a trip. You are given an array `seatbeltPrompts` where `seatbeltPrompts[i]` 
represents the number of times the driver was prompted during the i-th trip. 
Return the total number of times the driver was prompted across all trips.

Example:
Input: seatbeltPrompts = [3, 1, 2, 4]
Output: 10
Explanation: The driver was prompted 3 times during the first trip, 1 time during the second trip, 
2 times during the third trip, and 4 times during the fourth trip. The total is 3 + 1 + 2 + 4 = 10.

Constraints:
- 1 <= seatbeltPrompts.length <= 10^4
- 0 <= seatbeltPrompts[i] <= 10^3
"""

# Python Solution
def totalSeatbeltPrompts(seatbeltPrompts):
    """
    Calculate the total number of seatbelt prompts across all trips.

    :param seatbeltPrompts: List[int] - List of seatbelt prompts for each trip.
    :return: int - Total number of seatbelt prompts.
    """
    return sum(seatbeltPrompts)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    seatbeltPrompts = [3, 1, 2, 4]
    print(totalSeatbeltPrompts(seatbeltPrompts))  # Output: 10

    # Test Case 2
    seatbeltPrompts = [0, 0, 0, 0]
    print(totalSeatbeltPrompts(seatbeltPrompts))  # Output: 0

    # Test Case 3
    seatbeltPrompts = [5, 10, 15]
    print(totalSeatbeltPrompts(seatbeltPrompts))  # Output: 30

    # Test Case 4
    seatbeltPrompts = [1000, 1000, 1000, 1000]
    print(totalSeatbeltPrompts(seatbeltPrompts))  # Output: 4000

    # Test Case 5
    seatbeltPrompts = [1]
    print(totalSeatbeltPrompts(seatbeltPrompts))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
The function uses the built-in `sum()` function to calculate the total of the elements in the list.
This operation has a time complexity of O(n), where n is the length of the `seatbeltPrompts` list.

Space Complexity:
The function does not use any additional data structures, and the space complexity is O(1).
"""

# Topic: Arrays