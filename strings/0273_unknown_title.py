"""
LeetCode Problem #273: Integer to English Words

Problem Statement:
Convert a non-negative integer num to its English words representation.

Example 1:
Input: num = 123
Output: "One Hundred Twenty Three"

Example 2:
Input: num = 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:
Input: num = 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:
Input: num = 0
Output: "Zero"

Constraints:
- 0 <= num <= 2^31 - 1
"""

def numberToWords(num: int) -> str:
    if num == 0:
        return "Zero"

    # Define the mappings for numbers to words
    below_20 = [
        "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten",
        "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"
    ]
    tens = [
        "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
    ]
    thousands = ["", "Thousand", "Million", "Billion"]

    def helper(n: int) -> str:
        if n == 0:
            return ""
        elif n < 20:
            return below_20[n - 1] + " "
        elif n < 100:
            return tens[n // 10 - 2] + " " + helper(n % 10)
        else:
            return below_20[n // 100 - 1] + " Hundred " + helper(n % 100)

    res = ""
    for i, unit in enumerate(thousands):
        if num % 1000 != 0:
            res = helper(num % 1000) + unit + " " + res
        num //= 1000

    return res.strip()

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 123
    print(f"Input: {num1}, Output: {numberToWords(num1)}")  # Output: "One Hundred Twenty Three"

    # Test Case 2
    num2 = 12345
    print(f"Input: {num2}, Output: {numberToWords(num2)}")  # Output: "Twelve Thousand Three Hundred Forty Five"

    # Test Case 3
    num3 = 1234567
    print(f"Input: {num3}, Output: {numberToWords(num3)}")  # Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

    # Test Case 4
    num4 = 0
    print(f"Input: {num4}, Output: {numberToWords(num4)}")  # Output: "Zero"

    # Test Case 5
    num5 = 1000000
    print(f"Input: {num5}, Output: {numberToWords(num5)}")  # Output: "One Million"

"""
Time Complexity:
- The function processes each digit of the number at most once, and the helper function operates on chunks of up to 3 digits.
- Therefore, the time complexity is O(N), where N is the number of digits in the input number.

Space Complexity:
- The space complexity is O(1) for the iterative approach since no additional data structures are used.

Topic: Strings
"""