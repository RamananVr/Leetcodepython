"""
LeetCode Problem #791: Custom Sort String

Problem Statement:
You are given two strings order and s. All the characters of order are unique, and were sorted in some custom order previously. 
Permute the characters of s so that they match the order that order was sorted. More specifically, if a character x occurs 
before a character y in order, then x should occur before y in the returned string.

Return any permutation of s that satisfies this property.

Example:
Input: order = "cba", s = "abcd"
Output: "cbad"
Explanation: "c", "b", and "a" are sorted according to order, so they come first in "s". "d" does not appear in "order", so it can be placed anywhere in the returned string. 

Constraints:
1. 1 <= order.length <= 26
2. 1 <= s.length <= 200
3. order and s consist of lowercase English letters.
4. All the characters of order are unique.
"""

# Solution
def customSortString(order: str, s: str) -> str:
    # Create a frequency map for characters in s
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1
    
    # Build the result string based on the order
    result = []
    for char in order:
        if char in freq:
            result.append(char * freq[char])  # Append the character freq[char] times
            del freq[char]  # Remove the character from the frequency map
    
    # Append remaining characters that are not in order
    for char, count in freq.items():
        result.append(char * count)
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    order = "cba"
    s = "abcd"
    print(customSortString(order, s))  # Output: "cbad"

    # Test Case 2
    order = "xyz"
    s = "zyxxyz"
    print(customSortString(order, s))  # Output: "xyzxyz"

    # Test Case 3
    order = "kqep"
    s = "pekeq"
    print(customSortString(order, s))  # Output: "kqeppe"

    # Test Case 4
    order = "abc"
    s = "aaaabbbbcccc"
    print(customSortString(order, s))  # Output: "aaaabbbbcccc"

    # Test Case 5
    order = "hgfedcba"
    s = "abcdefgh"
    print(customSortString(order, s))  # Output: "hgfedcba"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the frequency map takes O(n), where n is the length of s.
- Iterating through the order string and appending characters takes O(m), where m is the length of order.
- Appending remaining characters from the frequency map takes O(n - m) in the worst case.
- Overall, the time complexity is O(n + m), which simplifies to O(n) since m <= 26 (constant).

Space Complexity:
- The frequency map uses O(n) space in the worst case, where n is the length of s.
- The result list uses O(n) space.
- Overall, the space complexity is O(n).
"""

# Topic: Strings