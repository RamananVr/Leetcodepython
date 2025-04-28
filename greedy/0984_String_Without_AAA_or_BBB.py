"""
LeetCode Problem #984: String Without AAA or BBB

Problem Statement:
Given two integers `a` and `b`, return any string `s` such that:
- `s` has length `a + b` and contains exactly `a` 'a' letters, and exactly `b` 'b' letters.
- The substring "aaa" does not occur in `s`.
- The substring "bbb" does not occur in `s`.

It is guaranteed that there is at least one valid solution for the given input.

Constraints:
- 0 <= a, b <= 100
- It is guaranteed that at least one valid solution exists.
"""

def strWithout3a3b(a: int, b: int) -> str:
    """
    Generate a string with exactly `a` 'a' letters and `b` 'b' letters,
    ensuring that neither "aaa" nor "bbb" appears as a substring.
    """
    result = []
    while a > 0 or b > 0:
        if a > b:
            if a > 1:
                result.append('aa')
                a -= 2
            else:
                result.append('a')
                a -= 1
            if b > 0:
                result.append('b')
                b -= 1
        elif b > a:
            if b > 1:
                result.append('bb')
                b -= 2
            else:
                result.append('b')
                b -= 1
            if a > 0:
                result.append('a')
                a -= 1
        else:  # a == b
            result.append('a')
            a -= 1
            result.append('b')
            b -= 1
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Equal number of 'a' and 'b'
    print(strWithout3a3b(3, 3))  # Output: "ababab" or similar valid string

    # Test Case 2: More 'a' than 'b'
    print(strWithout3a3b(5, 2))  # Output: "aabaa" or similar valid string

    # Test Case 3: More 'b' than 'a'
    print(strWithout3a3b(2, 5))  # Output: "bbabb" or similar valid string

    # Test Case 4: Edge case with no 'a'
    print(strWithout3a3b(0, 3))  # Output: "bbb"

    # Test Case 5: Edge case with no 'b'
    print(strWithout3a3b(4, 0))  # Output: "aaaa"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the total number of characters `a + b` to construct the result string.
- Each iteration appends one or two characters to the result list.
- Therefore, the time complexity is O(a + b).

Space Complexity:
- The space complexity is O(a + b) due to the result list storing the final string.

Topic: Greedy
"""