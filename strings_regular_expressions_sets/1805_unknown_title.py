"""
LeetCode Problem #1805: Number of Different Integers in a String

Problem Statement:
You are given a string `word` that consists of digits and lowercase English letters.

You will replace every non-digit character with a space. For example, `"a123bc34d8ef34"` will become `" 123  34 8  34"`. 
Notice that you are left with some integers that are separated by at least one space: `"123"`, `"34"`, `"8"`, and `"34"`.

Return the number of different integers after performing the replacement operations on `word`.

Two integers are considered different if their decimal representations, ignoring any leading zeros, are different.

Example 1:
Input: word = "a123bc34d8ef34"
Output: 3
Explanation: The three different integers are "123", "34", and "8". Notice that "34" is only counted once.

Example 2:
Input: word = "leet1234code234"
Output: 2

Example 3:
Input: word = "a1b01c001"
Output: 1
Explanation: The three integers "1", "01", and "001" all represent the same integer because the leading zeros are ignored when comparing their decimal values.

Constraints:
- 1 <= word.length <= 1000
- word consists of digits and lowercase English letters.
"""

# Clean and Correct Python Solution
import re

def numDifferentIntegers(word: str) -> int:
    # Replace all non-digit characters with spaces
    word = re.sub(r'[a-z]', ' ', word)
    # Split the string into parts and remove leading zeros
    integers = set(int(num) for num in word.split() if num.isdigit())
    # Return the count of unique integers
    return len(integers)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "a123bc34d8ef34"
    print(numDifferentIntegers(word1))  # Output: 3

    # Test Case 2
    word2 = "leet1234code234"
    print(numDifferentIntegers(word2))  # Output: 2

    # Test Case 3
    word3 = "a1b01c001"
    print(numDifferentIntegers(word3))  # Output: 1

    # Additional Test Case 4
    word4 = "abc"
    print(numDifferentIntegers(word4))  # Output: 0

    # Additional Test Case 5
    word5 = "0a0b0"
    print(numDifferentIntegers(word5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Replacing non-digit characters with spaces using `re.sub` takes O(n), where n is the length of the string.
- Splitting the string into parts using `split()` takes O(n).
- Converting each valid number to an integer and adding it to a set takes O(k), where k is the number of valid numbers.
- Overall, the time complexity is O(n + k), which simplifies to O(n) since k <= n.

Space Complexity:
- The space complexity is O(k), where k is the number of unique integers stored in the set.
- In the worst case, all characters in the string are digits, and the set will store up to n unique integers.
- Thus, the space complexity is O(n).
"""

# Topic: Strings, Regular Expressions, Sets