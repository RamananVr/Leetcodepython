"""
LeetCode Problem #859: Buddy Strings

Problem Statement:
Given two strings `s` and `goal`, return `true` if you can swap two letters in `s` so the result is equal to `goal`, otherwise return `false`.

Swapping letters is defined as taking two indices `i` and `j` (0-indexed) such that `i != j` and swapping the characters at `s[i]` and `s[j]`. For example, swapping at indices `0` and `2` in "abcd" results in "cbad".

Constraints:
- `s` and `goal` are strings of length 1 to 2 * 10^4.
- `s` and `goal` consist of lowercase letters.

"""

def buddyStrings(s: str, goal: str) -> bool:
    # If lengths are different, return False
    if len(s) != len(goal):
        return False
    
    # If strings are identical, check for duplicate characters
    if s == goal:
        seen = set()
        for char in s:
            if char in seen:
                return True
            seen.add(char)
        return False
    
    # Find indices where characters differ
    diff = []
    for i in range(len(s)):
        if s[i] != goal[i]:
            diff.append(i)
    
    # There must be exactly two differences, and swapping them should make the strings equal
    return len(diff) == 2 and s[diff[0]] == goal[diff[1]] and s[diff[1]] == goal[diff[0]]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Swapping 'a' and 'b' makes the strings equal
    s1 = "ab"
    goal1 = "ba"
    print(buddyStrings(s1, goal1))  # Expected: True

    # Test Case 2: Strings are identical but have no duplicate characters
    s2 = "ab"
    goal2 = "ab"
    print(buddyStrings(s2, goal2))  # Expected: False

    # Test Case 3: Strings are identical and have duplicate characters
    s3 = "aa"
    goal3 = "aa"
    print(buddyStrings(s3, goal3))  # Expected: True

    # Test Case 4: Strings differ in more than two places
    s4 = "abcd"
    goal4 = "badc"
    print(buddyStrings(s4, goal4))  # Expected: False

    # Test Case 5: Strings differ in exactly two places, but swapping doesn't make them equal
    s5 = "abcd"
    goal5 = "abdc"
    print(buddyStrings(s5, goal5))  # Expected: True

    # Test Case 6: Strings have different lengths
    s6 = "abc"
    goal6 = "abcd"
    print(buddyStrings(s6, goal6))  # Expected: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the strings once to compare characters, which takes O(n) time, where n is the length of the strings.
- Checking for duplicate characters in the case of identical strings also takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) for the `diff` list, which stores at most two indices.
- In the case of identical strings, the `seen` set may store up to n characters, resulting in O(n) space in the worst case.
- Overall, the space complexity is O(n).

Topic: Strings
"""