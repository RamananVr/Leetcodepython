"""
LeetCode Problem #1694: Reformat Phone Number

Problem Statement:
You are given a phone number as a string `number`. `number` consists of digits, spaces `' '`, and/or dashes `'-'`.

You would like to reformat the phone number in a certain manner. Firstly, remove all spaces and dashes. Then, group the digits from left to right into blocks of length 3 until there are 4 or fewer digits. The final digits are then grouped as follows:

- 2 digits: A single block of length 2.
- 3 digits: A single block of length 3.
- 4 digits: Two blocks of length 2 each.

The blocks are then joined by dashes. Notice that the reformatting process should never produce any blocks of length 1 and produce the minimum number of blocks.

Return the reformatted phone number as a string.

Example 1:
Input: number = "1-23-45 6"
Output: "123-456"

Example 2:
Input: number = "123 4-567"
Output: "123-45-67"

Example 3:
Input: number = "123 4-5678"
Output: "123-456-78"

Constraints:
- `2 <= number.length <= 100`
- `number` consists of digits and the characters `'-'` and `' '`.
- `number` contains at least two digits.
"""

# Clean, Correct Python Solution
def reformatNumber(number: str) -> str:
    # Step 1: Remove all spaces and dashes
    digits = [ch for ch in number if ch.isdigit()]
    
    # Step 2: Initialize result list
    result = []
    i = 0
    n = len(digits)
    
    # Step 3: Process digits in groups of 3
    while n - i > 4:
        result.append("".join(digits[i:i+3]))
        i += 3
    
    # Step 4: Handle the last 2-4 digits
    if n - i == 4:
        result.append("".join(digits[i:i+2]))
        result.append("".join(digits[i+2:i+4]))
    else:
        result.append("".join(digits[i:]))
    
    # Step 5: Join the result with dashes
    return "-".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    number1 = "1-23-45 6"
    print(reformatNumber(number1))  # Output: "123-456"

    # Test Case 2
    number2 = "123 4-567"
    print(reformatNumber(number2))  # Output: "123-45-67"

    # Test Case 3
    number3 = "123 4-5678"
    print(reformatNumber(number3))  # Output: "123-456-78"

    # Test Case 4
    number4 = "12"
    print(reformatNumber(number4))  # Output: "12"

    # Test Case 5
    number5 = "175-229-353-94-75"
    print(reformatNumber(number5))  # Output: "175-229-353-94-75"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Removing spaces and dashes takes O(n), where n is the length of the input string.
- Grouping digits into blocks and processing them takes O(n).
- Joining the result with dashes also takes O(n).
Overall, the time complexity is O(n).

Space Complexity:
- The space required to store the filtered digits is O(n).
- The result list also takes O(n) space.
Overall, the space complexity is O(n).
"""

# Topic: String Manipulation