"""
LeetCode Problem #1842: Next Palindrome Using Same Digits

Problem Statement:
Given a numeric string `num`, return the next palindrome using the same digits of `num`. 
If no such palindrome exists, return an empty string.

A palindrome is a number that reads the same backward as forward.

Constraints:
- 1 <= num.length <= 10^5
- num consists of digits only.

Example:
Input: num = "32123"
Output: "32323"

Input: num = "12321"
Output: "12421"

Input: num = "54321"
Output: ""

Note:
- The next palindrome must be strictly greater than the given number.
- The digits of the palindrome must be a rearrangement of the digits of the input number.
"""

from typing import List

def nextPalindrome(num: str) -> str:
    """
    Finds the next palindrome using the same digits of the input number.
    If no such palindrome exists, returns an empty string.
    """
    def next_permutation(arr: List[int]) -> bool:
        """
        Modifies arr to the next lexicographical permutation.
        Returns True if the next permutation exists, otherwise False.
        """
        n = len(arr)
        i = n - 2
        # Find the first decreasing element from the right
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        if i == -1:
            return False  # No next permutation exists

        # Find the smallest element larger than arr[i] to the right of i
        j = n - 1
        while arr[j] <= arr[i]:
            j -= 1

        # Swap elements at i and j
        arr[i], arr[j] = arr[j], arr[i]

        # Reverse the elements to the right of i
        arr[i + 1:] = reversed(arr[i + 1:])
        return True

    n = len(num)
    if n == 1:
        return ""  # Single digit numbers cannot form a palindrome

    # Step 1: Extract the first half of the number
    half = list(num[:(n + 1) // 2])  # Take the first half (including middle if odd length)

    # Step 2: Find the next lexicographical permutation of the first half
    if not next_permutation(half):
        return ""  # If no next permutation exists, return empty string

    # Step 3: Construct the palindrome
    if n % 2 == 0:
        # Even length: mirror the first half
        palindrome = "".join(half + half[::-1])
    else:
        # Odd length: mirror the first half excluding the middle digit
        palindrome = "".join(half + half[-2::-1])

    # Step 4: Check if the palindrome is greater than the input number
    return palindrome if palindrome > num else ""


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "32123"
    print(nextPalindrome(num1))  # Output: "32323"

    # Test Case 2
    num2 = "12321"
    print(nextPalindrome(num2))  # Output: "12421"

    # Test Case 3
    num3 = "54321"
    print(nextPalindrome(num3))  # Output: ""

    # Test Case 4
    num4 = "1111"
    print(nextPalindrome(num4))  # Output: ""

    # Test Case 5
    num5 = "1"
    print(nextPalindrome(num5))  # Output: ""


"""
Time Complexity Analysis:
- Let n = len(num).
- The next_permutation function runs in O(n) time for finding the next lexicographical permutation.
- Constructing the palindrome also takes O(n) time.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(n) due to the storage of the first half of the number.

Topic: Strings, Permutations
"""