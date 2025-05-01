"""
LeetCode Problem #1576: Replace All ?'s to Avoid Consecutive Repeating Characters

Problem Statement:
Given a string `s` containing only lowercase English letters and the '?' character, 
replace all the '?' characters in the string such that the final string does not contain 
any consecutive repeating characters. You can replace '?' with any lowercase English letter.

It is guaranteed that it is always possible to replace every '?' character with a letter 
to achieve a final string without consecutive repeating characters.

Return the final string after all the replacements are done.

Example 1:
Input: s = "?zs"
Output: "azs"
Explanation: Replace the first '?' with 'a' to make "azs". There are no consecutive repeating characters.

Example 2:
Input: s = "ubv?w"
Output: "ubvaw"
Explanation: Replace the '?' with 'a' to make "ubvaw". There are no consecutive repeating characters.

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters and '?'.
"""

# Solution
def modifyString(s: str) -> str:
    """
    Replace all '?' in the string such that there are no consecutive repeating characters.
    
    Args:
    s (str): Input string containing lowercase letters and '?'.
    
    Returns:
    str: Modified string with no consecutive repeating characters.
    """
    s = list(s)  # Convert string to list for mutability
    n = len(s)
    
    for i in range(n):
        if s[i] == '?':
            for replacement in 'abc':  # Try replacing '?' with 'a', 'b', or 'c'
                # Check if the replacement does not create consecutive duplicates
                if (i > 0 and s[i - 1] == replacement) or (i < n - 1 and s[i + 1] == replacement):
                    continue
                s[i] = replacement
                break
    
    return ''.join(s)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "?zs"
    print(modifyString(s1))  # Expected Output: "azs"

    # Test Case 2
    s2 = "ubv?w"
    print(modifyString(s2))  # Expected Output: "ubvaw"

    # Test Case 3
    s3 = "j?qg??b"
    print(modifyString(s3))  # Expected Output: "jaqgacb"

    # Test Case 4
    s4 = "??"
    print(modifyString(s4))  # Expected Output: "ab" (or any valid string like "ba")

    # Test Case 5
    s5 = "a?b?c?"
    print(modifyString(s5))  # Expected Output: "acbacb"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once (O(n)).
- For each '?', it tries up to 3 replacements ('a', 'b', 'c'), which is constant time (O(1)).
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a list to store the mutable version of the string, which takes O(n) space.
- No additional data structures are used.
- Overall space complexity: O(n).

Topic: String Manipulation
"""