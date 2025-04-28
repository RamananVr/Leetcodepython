"""
LeetCode Problem #1363: Largest Multiple of Three

Problem Statement:
Given an array of digits `digits`, return the largest multiple of three that can be formed by concatenating some of the given digits in any order. If there is no answer, return an empty string.

Since the answer may not fit in an integer, return the answer as a string.

Example 1:
Input: digits = [8, 1, 9]
Output: "981"

Example 2:
Input: digits = [8, 6, 7, 1, 0]
Output: "8760"

Example 3:
Input: digits = [1]
Output: ""

Example 4:
Input: digits = [0, 0, 0, 0]
Output: "0"

Constraints:
- 1 <= digits.length <= 10^4
- 0 <= digits[i] <= 9
"""

from typing import List

def largestMultipleOfThree(digits: List[int]) -> str:
    # Step 1: Count the frequency of each digit and calculate the total sum
    count = [0] * 10
    total_sum = 0
    for digit in digits:
        count[digit] += 1
        total_sum += digit

    # Step 2: Helper function to remove digits
    def remove_digits(remainder, count, num_to_remove):
        for i in range(1, 10):
            if i % 3 == remainder:
                while count[i] > 0 and num_to_remove > 0:
                    count[i] -= 1
                    num_to_remove -= 1
                if num_to_remove == 0:
                    return True
        return False

    # Step 3: Adjust the digits to make the sum divisible by 3
    if total_sum % 3 == 1:
        if not remove_digits(1, count, 1):  # Try removing one digit with remainder 1
            remove_digits(2, count, 2)  # Otherwise, remove two digits with remainder 2
    elif total_sum % 3 == 2:
        if not remove_digits(2, count, 1):  # Try removing one digit with remainder 2
            remove_digits(1, count, 2)  # Otherwise, remove two digits with remainder 1

    # Step 4: Construct the largest number
    result = []
    for i in range(9, -1, -1):
        result.extend([str(i)] * count[i])

    # Step 5: Handle edge case where the result is all zeros
    if result and result[0] == '0':
        return '0'

    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    digits = [8, 1, 9]
    print(largestMultipleOfThree(digits))  # Output: "981"

    # Test Case 2
    digits = [8, 6, 7, 1, 0]
    print(largestMultipleOfThree(digits))  # Output: "8760"

    # Test Case 3
    digits = [1]
    print(largestMultipleOfThree(digits))  # Output: ""

    # Test Case 4
    digits = [0, 0, 0, 0]
    print(largestMultipleOfThree(digits))  # Output: "0"

    # Test Case 5
    digits = [3, 6, 5, 1, 8]
    print(largestMultipleOfThree(digits))  # Output: "8631"

"""
Time Complexity:
- Counting the digits and calculating the total sum takes O(n), where n is the length of the input array.
- Adjusting the digits to make the sum divisible by 3 involves at most O(10) operations (constant time).
- Constructing the result string takes O(n) in the worst case.
Overall, the time complexity is O(n).

Space Complexity:
- The space used for the `count` array is O(10) (constant space).
- The space used for the `result` list is O(n) in the worst case.
Overall, the space complexity is O(n).

Topic: Greedy
"""