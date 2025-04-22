"""
LeetCode Problem #828: Count Unique Characters of All Substrings of a Given String

Problem Statement:
Let's define a function `countUniqueChars(s)` that returns the number of unique characters in string `s`.

For example:
- `countUniqueChars("LEETCODE") = 7`. 
  The unique characters are "L", "E", "T", "C", "O", "D".

Given a string `s`, return the sum of `countUniqueChars(t)` where `t` is a substring of `s`.
Notice that some substrings can be repeated in `s`, but if they are unique, their counts should be added.

Example:
Input: s = "ABC"
Output: 10
Explanation: All possible substrings are: "A", "B", "C", "AB", "BC", "ABC".
- "A" has 1 unique character.
- "B" has 1 unique character.
- "C" has 1 unique character.
- "AB" has 2 unique characters.
- "BC" has 2 unique characters.
- "ABC" has 3 unique characters.
Sum of counts = 1 + 1 + 1 + 2 + 2 + 3 = 10.

Constraints:
- 1 <= s.length <= 10^5
- s consists of uppercase English letters only.
"""

# Solution
def uniqueLetterString(s: str) -> int:
    """
    Calculate the sum of countUniqueChars(t) for all substrings t of the given string s.
    """
    # Dictionary to store the last two occurrences of each character
    index = {}
    result = 0
    n = len(s)
    
    for i, char in enumerate(s):
        if char not in index:
            index[char] = [-1, -1]
        
        # Update the result using the formula:
        # Contribution of char = (i - index[char][1]) * (index[char][1] - index[char][0])
        result += (i - index[char][1]) * (index[char][1] - index[char][0])
        
        # Update the last two occurrences of char
        index[char][0], index[char][1] = index[char][1], i
    
    # Handle the remaining contributions after the loop
    for char in index:
        result += (n - index[char][1]) * (index[char][1] - index[char][0])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "ABC"
    print(uniqueLetterString(s1))  # Expected Output: 10

    # Test Case 2
    s2 = "LEETCODE"
    print(uniqueLetterString(s2))  # Expected Output: 92

    # Test Case 3
    s3 = "A"
    print(uniqueLetterString(s3))  # Expected Output: 1

    # Test Case 4
    s4 = "AA"
    print(uniqueLetterString(s4))  # Expected Output: 2

    # Test Case 5
    s5 = "ABAB"
    print(uniqueLetterString(s5))  # Expected Output: 16

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string `s` once, performing constant-time operations for each character.
- Additionally, it iterates through the keys of the `index` dictionary at the end, which is bounded by the number of unique characters (at most 26 for uppercase English letters).
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The `index` dictionary stores at most 26 keys (one for each uppercase English letter), with each key storing a list of two integers.
- Thus, the space complexity is O(1), as the dictionary size is bounded by a constant.

Topic: String Manipulation
"""