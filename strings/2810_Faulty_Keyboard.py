"""
LeetCode Problem #2810: Faulty Keyboard

Problem Statement:
Your laptop keyboard is faulty, and whenever you type a character 'i', it reverses the string that you have written so far. 
You are given a 0-indexed string s, and you type each character of s using your faulty keyboard.

Return the final string that will be present on your laptop screen.

Example 1:
Input: s = "string"
Output: "rtsng"
Explanation: 
After typing first character, the text on the screen is "s".
After the second character, the text is "st".
After the third character, the text is "str".
Since the fourth character is an 'i', the text gets reversed and becomes "rts".
After the fifth character, the text is "rtsn".
After the sixth character, the text is "rtsng". 

Example 2:
Input: s = "poiinter"
Output: "ponter"
Explanation: 
After typing first character, the text on the screen is "p".
After the second character, the text is "po".
After the third character, the text is "poi".
Since the fourth character is an 'i', the text gets reversed and becomes "iop".
Since the fifth character is an 'i', the text gets reversed again and becomes "poi".
After the sixth character, the text is "poin".
After the seventh character, the text is "point".
After the eighth character, the text is "ponter".

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters.
"""

# Python Solution
def finalString(s: str) -> str:
    result = []
    for char in s:
        if char == 'i':
            result.reverse()
        else:
            result.append(char)
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "string"
    print(finalString(s1))  # Output: "rtsng"

    # Test Case 2
    s2 = "poiinter"
    print(finalString(s2))  # Output: "ponter"

    # Additional Test Case 3
    s3 = "iiabc"
    print(finalString(s3))  # Output: "cba"

    # Additional Test Case 4
    s4 = "abc"
    print(finalString(s4))  # Output: "abc"

    # Additional Test Case 5
    s5 = "iiii"
    print(finalString(s5))  # Output: ""

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once, so the time complexity is O(n), where n is the length of the string.
- The `result.reverse()` operation takes O(k) time, where k is the current length of the `result` list. In the worst case, this could happen multiple times, but since the total number of operations is proportional to the length of the string, the overall time complexity remains O(n).

Space Complexity:
- The space complexity is O(n) because we use a list `result` to store the characters of the final string.
"""

# Topic: Strings