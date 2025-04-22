"""
LeetCode Problem #401: Binary Watch

Problem Statement:
A binary watch has 4 LEDs for the hours (0-11) and 6 LEDs for the minutes (0-59). Each LED represents a binary bit, and the number of LEDs that are on indicates the time.

Given a non-negative integer `turnedOn` which represents the number of LEDs that are currently on, return all possible times the watch could represent. You may return the answer in any order.

The hour must be valid (0 <= hour <= 11), and the minute must be valid (0 <= minute <= 59). The order of the output does not matter.

Example 1:
Input: turnedOn = 1
Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

Example 2:
Input: turnedOn = 9
Output: []

Constraints:
- 0 <= turnedOn <= 10
"""

# Solution
from typing import List

def readBinaryWatch(turnedOn: int) -> List[str]:
    def count_bits(n: int) -> int:
        """Helper function to count the number of 1s in the binary representation of n."""
        return bin(n).count('1')
    
    result = []
    for hour in range(12):  # Hours range from 0 to 11
        for minute in range(60):  # Minutes range from 0 to 59
            if count_bits(hour) + count_bits(minute) == turnedOn:
                result.append(f"{hour}:{minute:02d}")
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    turnedOn = 1
    print(readBinaryWatch(turnedOn))  # Expected Output: ["0:01","0:02","0:04","0:08","0:16","0:32","1:00","2:00","4:00","8:00"]

    # Test Case 2
    turnedOn = 9
    print(readBinaryWatch(turnedOn))  # Expected Output: []

    # Test Case 3
    turnedOn = 0
    print(readBinaryWatch(turnedOn))  # Expected Output: ["0:00"]

    # Test Case 4
    turnedOn = 2
    print(readBinaryWatch(turnedOn))  # Expected Output: ["0:03","0:05","0:09","0:17","0:33","1:01","1:02","1:04","1:08","1:16","1:32","2:01","2:02","2:04","2:08","2:16","2:32","3:00","4:01","4:02","4:04","4:08","4:16","4:32","5:00","6:00","8:01","8:02","8:04","8:08","8:16","8:32","9:00","10:00"]

# Time and Space Complexity Analysis
# Time Complexity:
# - The outer loop iterates over 12 possible hours, and the inner loop iterates over 60 possible minutes.
# - For each combination, we calculate the number of 1s in the binary representation of the hour and minute.
# - The complexity of `bin(n).count('1')` is O(k), where k is the number of bits in n. Since n is small (at most 11 for hours and 59 for minutes), this is effectively O(1).
# - Therefore, the total time complexity is O(12 * 60) = O(720), which is constant.

# Space Complexity:
# - The space complexity is O(1) for the helper function and O(m) for the result list, where m is the number of valid times generated.
# - In the worst case, m is small compared to the fixed number of iterations, so the space complexity is effectively O(m).

# Topic: Backtracking / Bit Manipulation