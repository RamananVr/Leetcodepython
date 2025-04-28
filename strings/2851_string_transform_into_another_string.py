"""
LeetCode Question #2851: String Transform Into Another String

Problem Statement:
You are given two strings s1 and s2 of the same length consisting of lowercase English letters. 
You want to transform s1 into s2 using the following operation any number of times:

- Choose any character c from s1 and change it to any other lowercase English letter.

Return true if you can transform s1 into s2. Otherwise, return false.

The transformation is possible if and only if:
1. Each character in s1 can be mapped to a character in s2.
2. There is no circular dependency in the mapping.
3. There is at least one unused character in the alphabet to break cycles.

Constraints:
- 1 <= s1.length == s2.length <= 10^4
- s1 and s2 consist of lowercase English letters.
"""

# Solution
def canConvert(s1: str, s2: str) -> bool:
    # If the strings are already equal, no transformation is needed
    if s1 == s2:
        return True
    
    # Create a mapping from characters in s1 to characters in s2
    mapping = {}
    for c1, c2 in zip(s1, s2):
        if c1 in mapping:
            # If the mapping is inconsistent, return False
            if mapping[c1] != c2:
                return False
        else:
            mapping[c1] = c2
    
    # Check for circular dependencies
    # If the number of unique characters in s2 is less than 26, we can break cycles
    return len(set(s2)) < 26

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple transformation
    s1 = "aabcc"
    s2 = "ccdee"
    print(canConvert(s1, s2))  # Expected output: True

    # Test Case 2: Impossible transformation due to circular dependency
    s1 = "abcdefghijklmnopqrstuvwxyz"
    s2 = "bcdefghijklmnopqrstuvwxyza"
    print(canConvert(s1, s2))  # Expected output: False

    # Test Case 3: Already equal strings
    s1 = "abc"
    s2 = "abc"
    print(canConvert(s1, s2))  # Expected output: True

    # Test Case 4: Transformation with unused characters
    s1 = "leetcode"
    s2 = "codeleet"
    print(canConvert(s1, s2))  # Expected output: True

    # Test Case 5: Edge case with single character strings
    s1 = "a"
    s2 = "b"
    print(canConvert(s1, s2))  # Expected output: True

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the strings s1 and s2 once to create the mapping, which takes O(n) time, 
  where n is the length of the strings.
- Checking the number of unique characters in s2 takes O(n) in the worst case.

Overall time complexity: O(n)

Space Complexity:
- The mapping dictionary stores at most 26 key-value pairs (one for each lowercase English letter), 
  which is O(1) space.
- The set operation to count unique characters in s2 also takes O(1) space since there are at most 26 unique characters.

Overall space complexity: O(1)
"""

# Topic: Strings