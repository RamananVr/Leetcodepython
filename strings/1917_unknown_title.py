"""
LeetCode Problem #1917: Leetcodify Strings

Problem Statement:
You are given a string `s` consisting of lowercase English letters. Your task is to transform the string into a "Leetcodified" version by replacing certain characters with their corresponding "leet" equivalents. The mapping is as follows:

- 'a' -> '4'
- 'e' -> '3'
- 'i' -> '1'
- 'o' -> '0'
- 's' -> '5'
- 't' -> '7'

Write a function `leetcodify(s: str) -> str` that takes the input string `s` and returns the transformed "Leetcodified" string.

Example:
Input: s = "leet"
Output: "l337"

Input: s = "hello"
Output: "h3ll0"

Constraints:
- 1 <= len(s) <= 1000
- `s` consists of only lowercase English letters.
"""

def leetcodify(s: str) -> str:
    """
    Transforms the input string into its "Leetcodified" version by replacing
    certain characters with their leet equivalents.

    :param s: Input string consisting of lowercase English letters
    :return: Transformed "Leetcodified" string
    """
    # Define the mapping of characters to their leet equivalents
    leet_map = {
        'a': '4',
        'e': '3',
        'i': '1',
        'o': '0',
        's': '5',
        't': '7'
    }
    
    # Use a list comprehension to replace characters based on the mapping
    return ''.join(leet_map[char] if char in leet_map else char for char in s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "leet"
    print(leetcodify(s1))  # Expected Output: "l337"

    # Test Case 2
    s2 = "hello"
    print(leetcodify(s2))  # Expected Output: "h3ll0"

    # Test Case 3
    s3 = "testcase"
    print(leetcodify(s3))  # Expected Output: "7357c453"

    # Test Case 4
    s4 = "programming"
    print(leetcodify(s4))  # Expected Output: "pr0gr4mm1ng"

    # Test Case 5
    s5 = "abcdefghijklmnopqrstuvwxyz"
    print(leetcodify(s5))  # Expected Output: "4bcd3fgh1jklmn0pqr57uvwxyz"

"""
Time Complexity Analysis:
- The function iterates through each character in the input string `s`, which has a length of `n`.
- For each character, it performs a dictionary lookup in `leet_map`, which is an O(1) operation.
- Therefore, the overall time complexity is O(n), where `n` is the length of the input string.

Space Complexity Analysis:
- The function uses a dictionary `leet_map` with a fixed size of 7 key-value pairs, which is O(1) space.
- The list comprehension creates a new string of length `n`, which requires O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Strings
"""