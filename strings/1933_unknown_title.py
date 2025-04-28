"""
LeetCode Problem #1933: Check if String Is Decomposable Into Value-Equal Substrings

Problem Statement:
A string s is called decomposable if it can be formed by concatenating one or more value-equal substrings, 
where a value-equal substring is a substring consisting of only one unique character. 
For example, "111" and "33" are value-equal substrings, but "123" and "112" are not.

Return true if the string s is decomposable into value-equal substrings with exactly one substring of length 2 
and the remaining substrings of length 3. Otherwise, return false.

Example 1:
Input: s = "00011111222"
Output: true
Explanation: s can be decomposed into "000", "111", "111", and "22". Exactly one substring has a length of 2.

Example 2:
Input: s = "011100022233"
Output: false
Explanation: s cannot be decomposed into value-equal substrings with exactly one substring of length 2.

Example 3:
Input: s = "000111000"
Output: false
Explanation: s cannot be decomposed into value-equal substrings with exactly one substring of length 2.

Constraints:
- 1 <= s.length <= 1000
- s consists of only digits.
"""

def isDecomposable(s: str) -> bool:
    count = 0
    i = 0
    n = len(s)
    has_two = False

    while i < n:
        # Count the length of the current value-equal substring
        j = i
        while j < n and s[j] == s[i]:
            j += 1
        length = j - i

        # Check if the length is valid
        if length % 3 == 1:  # Invalid length
            return False
        elif length % 3 == 2:  # Length 2 substring
            if has_two:  # Already found a length 2 substring
                return False
            has_two = True

        # Move to the next group
        i = j

    # Ensure exactly one length 2 substring exists
    return has_two


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "00011111222"
    print(isDecomposable(s1))  # Output: True

    # Test Case 2
    s2 = "011100022233"
    print(isDecomposable(s2))  # Output: False

    # Test Case 3
    s3 = "000111000"
    print(isDecomposable(s3))  # Output: False

    # Test Case 4
    s4 = "22233344455"
    print(isDecomposable(s4))  # Output: True

    # Test Case 5
    s5 = "111222333"
    print(isDecomposable(s5))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the string once, counting the length of each value-equal substring.
- This results in a time complexity of O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `count`, `i`, and `has_two`.
- Therefore, the space complexity is O(1).

Topic: Strings
"""