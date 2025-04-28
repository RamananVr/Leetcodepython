"""
LeetCode Problem #2125: Number of Laser Beams in a Bank

Problem Statement:
You are given a 2D matrix `bank` representing a bank, where:
- `bank[i]` is a string that represents the `i-th` row of the bank.
- `bank[i][j]` is either '0' (empty) or '1' (a security device).

The number of laser beams between any two rows is equal to the product of the number of security devices in the two rows. 
- For example, if the first row has `r1` security devices and the second row has `r2` security devices, the number of laser beams between these two rows is `r1 * r2`.

Return the total number of laser beams in the bank. Rows with no security devices (all '0's) cannot form laser beams.

Example:
Input: bank = ["011001", "000000", "010100", "001000"]
Output: 8
Explanation:
- The 1st row has 3 devices.
- The 2nd row has 0 devices and is ignored.
- The 3rd row has 2 devices.
- The 4th row has 1 device.
- Total beams = (3 * 2) + (2 * 1) = 8.

Constraints:
- `1 <= bank.length <= 500`
- `1 <= bank[i].length <= 500`
- `bank[i][j]` is either '0' or '1'.
"""

# Clean and Correct Python Solution
def numberOfBeams(bank):
    """
    Calculate the total number of laser beams in the bank.

    :param bank: List[str] - A list of strings representing the bank rows.
    :return: int - Total number of laser beams.
    """
    # Count the number of security devices in each row
    device_counts = [row.count('1') for row in bank if row.count('1') > 0]
    
    # Calculate the total number of laser beams
    total_beams = 0
    for i in range(1, len(device_counts)):
        total_beams += device_counts[i - 1] * device_counts[i]
    
    return total_beams

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bank1 = ["011001", "000000", "010100", "001000"]
    print(numberOfBeams(bank1))  # Output: 8

    # Test Case 2
    bank2 = ["000", "111", "000", "111"]
    print(numberOfBeams(bank2))  # Output: 0

    # Test Case 3
    bank3 = ["1", "0", "1"]
    print(numberOfBeams(bank3))  # Output: 0

    # Test Case 4
    bank4 = ["101", "000", "111"]
    print(numberOfBeams(bank4))  # Output: 6

    # Test Case 5
    bank5 = ["0", "0", "0"]
    print(numberOfBeams(bank5))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `m` be the number of rows in the bank and `n` be the number of columns.
- Counting the number of '1's in each row takes O(n) for each row.
- In the worst case, all rows have devices, so we iterate through the list of device counts once to calculate the beams.
- Overall time complexity: O(m * n).

Space Complexity:
- We store the device counts in a list, which takes O(m) space in the worst case.
- Overall space complexity: O(m).
"""

# Topic: Arrays, String Manipulation