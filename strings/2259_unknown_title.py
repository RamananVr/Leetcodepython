"""
LeetCode Problem #2259: Remove Digit From Number to Maximize Result

Problem Statement:
You are given a string `number` representing a positive integer and a character `digit` that occurs in `number`.
Remove exactly one occurrence of `digit` from `number` so that the resulting number is the largest possible.
Return the resulting string after removing one occurrence of `digit`.

It is guaranteed that `digit` occurs at least once in `number`.

Constraints:
- `2 <= number.length <= 100`
- `number` consists of digits from '1' to '9'.
- `digit` is a digit from '1' to '9'.
- `digit` occurs at least once in `number`.

Example 1:
Input: number = "123", digit = "3"
Output: "12"
Explanation: Removing '3' gives "12", which is the largest possible number.

Example 2:
Input: number = "1231", digit = "1"
Output: "231"
Explanation: Removing the first '1' results in "231", which is the largest possible number.

Example 3:
Input: number = "551", digit = "5"
Output: "51"
Explanation: Removing the first '5' results in "51", which is the largest possible number.
"""

def removeDigit(number: str, digit: str) -> str:
    """
    Removes one occurrence of `digit` from `number` to maximize the resulting number.

    Args:
    number (str): The input number as a string.
    digit (str): The digit to remove.

    Returns:
    str: The largest possible number after removing one occurrence of `digit`.
    """
    max_result = ""
    for i in range(len(number)):
        if number[i] == digit:
            # Remove the digit at index i
            candidate = number[:i] + number[i+1:]
            # Update the maximum result if the candidate is larger
            if candidate > max_result:
                max_result = candidate
    return max_result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    number = "123"
    digit = "3"
    print(removeDigit(number, digit))  # Output: "12"

    # Test Case 2
    number = "1231"
    digit = "1"
    print(removeDigit(number, digit))  # Output: "231"

    # Test Case 3
    number = "551"
    digit = "5"
    print(removeDigit(number, digit))  # Output: "51"

    # Additional Test Case 4
    number = "7654321"
    digit = "7"
    print(removeDigit(number, digit))  # Output: "654321"

    # Additional Test Case 5
    number = "11111"
    digit = "1"
    print(removeDigit(number, digit))  # Output: "1111"

"""
Time Complexity:
- The algorithm iterates through the string `number` once, which takes O(n) time, where n is the length of `number`.
- For each occurrence of `digit`, it creates a new string by slicing, which takes O(n) time in the worst case.
- Therefore, the overall time complexity is O(n^2) in the worst case.

Space Complexity:
- The algorithm uses O(n) space for the slicing operation to create candidate strings.
- No additional data structures are used, so the space complexity is O(n).

Topic: Strings
"""