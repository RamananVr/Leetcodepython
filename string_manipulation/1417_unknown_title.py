"""
LeetCode Problem #1417: Reformat The String

Problem Statement:
Given alphanumeric string `s`, return the string after reformatting so that no two adjacent characters are of the same type. 
That is, no two adjacent characters have the same type (letter or digit). If it is impossible to reformat the string, return an empty string.

Example 1:
Input: s = "a0b1c2"
Output: "0a1b2c"
Explanation: No two adjacent characters are of the same type in "0a1b2c".

Example 2:
Input: s = "leetcode"
Output: ""
Explanation: "leetcode" has only letters, so it is impossible to reformat.

Example 3:
Input: s = "1229857369"
Output: ""
Explanation: "1229857369" has only digits, so it is impossible to reformat.

Example 4:
Input: s = "covid2019"
Output: "c2o0v1i9d"

Constraints:
- 1 <= s.length <= 500
- `s` consists of only lowercase English letters and/or digits.
"""

# Solution
def reformat(s: str) -> str:
    # Separate letters and digits
    letters = [ch for ch in s if ch.isalpha()]
    digits = [ch for ch in s if ch.isdigit()]
    
    # If the difference in counts is greater than 1, reformatting is impossible
    if abs(len(letters) - len(digits)) > 1:
        return ""
    
    # Ensure the longer list is first
    if len(letters) < len(digits):
        letters, digits = digits, letters
    
    # Interleave letters and digits
    result = []
    for i in range(len(s)):
        if i % 2 == 0:
            result.append(letters.pop())
        else:
            result.append(digits.pop())
    
    return "".join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "a0b1c2"
    print(reformat(s1))  # Output: "0a1b2c" or similar valid output
    
    # Test Case 2
    s2 = "leetcode"
    print(reformat(s2))  # Output: ""
    
    # Test Case 3
    s3 = "1229857369"
    print(reformat(s3))  # Output: ""
    
    # Test Case 4
    s4 = "covid2019"
    print(reformat(s4))  # Output: "c2o0v1i9d" or similar valid output
    
    # Test Case 5
    s5 = "ab123"
    print(reformat(s5))  # Output: "1a2b3" or similar valid output

# Time and Space Complexity Analysis
"""
Time Complexity:
- Separating letters and digits takes O(n), where n is the length of the string `s`.
- Interleaving the characters takes O(n) as well.
- Overall, the time complexity is O(n).

Space Complexity:
- The space used for the `letters` and `digits` lists is O(n).
- The result list also takes O(n) space.
- Overall, the space complexity is O(n).
"""

# Topic: String Manipulation