"""
LeetCode Problem #2301: Match Substring After Replacement

Problem Statement:
You are given two strings `s` and `sub`, and a 2D character array `mappings` where `mappings[i] = [oldChar_i, newChar_i]` indicates that you can replace any number of `oldChar_i` characters of `sub` with `newChar_i`. Each character in `sub` can only be replaced once.

Return `true` if it is possible to make `sub` a substring of `s` by replacing zero or more characters according to `mappings`. Otherwise, return `false`.

Example:
Input: s = "fool3e7bar", sub = "leet", mappings = [["e", "3"], ["t", "7"], ["t", "8"]]
Output: true
Explanation: Replace the first 'e' in "leet" with '3' and 't' with '7'. "leet" becomes "l3e7", which is a substring of "fool3e7bar".

Constraints:
- `1 <= s.length, sub.length <= 500`
- `0 <= mappings.length <= 10^4`
- `mappings[i].length == 2`
- `oldChar_i`, `newChar_i` are ASCII characters
"""

# Python Solution
def matchReplacement(s: str, sub: str, mappings: list[list[str]]) -> bool:
    # Create a dictionary to store valid replacements
    valid_replacements = {char: set() for char in sub}
    for old, new in mappings:
        if old in valid_replacements:
            valid_replacements[old].add(new)
    
    # Check all substrings of length len(sub) in s
    for i in range(len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j] and sub[j] not in valid_replacements.get(s[i+j], set()):
                match = False
                break
        if match:
            return True
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "fool3e7bar"
    sub1 = "leet"
    mappings1 = [["e", "3"], ["t", "7"], ["t", "8"]]
    print(matchReplacement(s1, sub1, mappings1))  # Output: True

    # Test Case 2
    s2 = "abcde"
    sub2 = "fgh"
    mappings2 = [["f", "a"], ["g", "b"], ["h", "c"]]
    print(matchReplacement(s2, sub2, mappings2))  # Output: True

    # Test Case 3
    s3 = "xyz"
    sub3 = "abc"
    mappings3 = [["a", "x"], ["b", "y"], ["c", "z"]]
    print(matchReplacement(s3, sub3, mappings3))  # Output: True

    # Test Case 4
    s4 = "hello"
    sub4 = "world"
    mappings4 = [["o", "e"], ["r", "l"]]
    print(matchReplacement(s4, sub4, mappings4))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the `valid_replacements` dictionary takes O(m), where m is the length of the `mappings` list.
- Checking all substrings of length `len(sub)` in `s` takes O((n - k) * k), where n is the length of `s` and k is the length of `sub`.
- Overall time complexity: O(m + n * k).

Space Complexity:
- The `valid_replacements` dictionary requires O(m) space in the worst case.
- Overall space complexity: O(m).
"""

# Topic: Strings, Hash Table, Sliding Window