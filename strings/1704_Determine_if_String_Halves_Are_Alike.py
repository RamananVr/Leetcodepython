"""
LeetCode Problem #1704: Determine if String Halves Are Alike

Problem Statement:
You are given a string s of even length. Split this string into two halves of equal lengths, 
and determine if the two halves are alike. Two halves are alike if they have the same number 
of vowels ('a', 'e', 'i', 'o', 'u', both uppercase and lowercase).

Return true if the two halves are alike; otherwise, return false.

Example 1:
Input: s = "book"
Output: true
Explanation: The two halves "bo" and "ok" have 1 vowel each.

Example 2:
Input: s = "textbook"
Output: false
Explanation: The two halves "text" and "book" have 1 and 2 vowels respectively.

Constraints:
- 2 <= s.length <= 1000
- s.length is even.
- s consists of uppercase and lowercase letters.
"""

# Solution
def halvesAreAlike(s: str) -> bool:
    vowels = set("aeiouAEIOU")
    mid = len(s) // 2
    first_half = s[:mid]
    second_half = s[mid:]
    
    def count_vowels(substring):
        return sum(1 for char in substring if char in vowels)
    
    return count_vowels(first_half) == count_vowels(second_half)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "book"
    print(halvesAreAlike(s1))  # Output: True

    # Test Case 2
    s2 = "textbook"
    print(halvesAreAlike(s2))  # Output: False

    # Test Case 3
    s3 = "AbCdEfGh"
    print(halvesAreAlike(s3))  # Output: True

    # Test Case 4
    s4 = "aeiouAEIOU"
    print(halvesAreAlike(s4))  # Output: True

    # Test Case 5
    s5 = "xyzXYZ"
    print(halvesAreAlike(s5))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through each half of the string to count vowels. 
  This takes O(n) time, where n is the length of the string.
- The string is split into two halves, which is an O(1) operation.
- Overall, the time complexity is O(n).

Space Complexity:
- The set of vowels is stored in memory, which takes O(1) space.
- The function uses a constant amount of additional space for variables.
- Overall, the space complexity is O(1).

Topic: Strings
"""