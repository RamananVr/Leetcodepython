"""
LeetCode Problem #345: Reverse Vowels of a String

Problem Statement:
Given a string `s`, reverse only all the vowels in the string and return it.
The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases (e.g., 'A' and 'a').

Example 1:
Input: s = "hello"
Output: "holle"

Example 2:
Input: s = "leetcode"
Output: "leotcede"

Constraints:
- 1 <= s.length <= 3 * 10^5
- s consists of printable ASCII characters.
"""

def reverseVowels(s: str) -> str:
    """
    Reverse only the vowels in the input string `s`.
    
    :param s: Input string
    :return: String with vowels reversed
    """
    # Define a set of vowels for quick lookup
    vowels = set("aeiouAEIOU")
    
    # Convert the string to a list to allow in-place modifications
    s_list = list(s)
    
    # Use two pointers to find and swap vowels
    left, right = 0, len(s_list) - 1
    while left < right:
        # Move the left pointer until a vowel is found
        while left < right and s_list[left] not in vowels:
            left += 1
        # Move the right pointer until a vowel is found
        while left < right and s_list[right] not in vowels:
            right -= 1
        # Swap the vowels
        s_list[left], s_list[right] = s_list[right], s_list[left]
        # Move both pointers inward
        left += 1
        right -= 1
    
    # Convert the list back to a string and return
    return ''.join(s_list)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "hello"
    print(reverseVowels(s1))  # Output: "holle"

    # Test Case 2
    s2 = "leetcode"
    print(reverseVowels(s2))  # Output: "leotcede"

    # Test Case 3
    s3 = "aA"
    print(reverseVowels(s3))  # Output: "Aa"

    # Test Case 4
    s4 = "bcdfg"
    print(reverseVowels(s4))  # Output: "bcdfg" (no vowels to reverse)

    # Test Case 5
    s5 = "aeiou"
    print(reverseVowels(s5))  # Output: "uoiea"

"""
Time and Space Complexity Analysis:

Time Complexity:
- O(n), where n is the length of the string `s`.
  - Each character is visited at most twice (once by the left pointer and once by the right pointer).

Space Complexity:
- O(n), where n is the length of the string `s`.
  - This is due to the conversion of the string to a list for in-place modifications.
  - If the input string is immutable, this additional space is required.

Topic: Two Pointers
"""