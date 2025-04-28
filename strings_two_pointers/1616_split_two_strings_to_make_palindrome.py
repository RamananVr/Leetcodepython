"""
LeetCode Question #1616: Split Two Strings to Make Palindrome

Problem Statement:
You are given two strings `a` and `b` of the same length. 
Choose an index and split both strings at the same index, splitting `a` into two strings: `a_left` and `a_right`, 
and splitting `b` into two strings: `b_left` and `b_right`. Check if there exists an index where 
`a_left + b_right` or `b_left + a_right` forms a palindrome.

Return `true` if it is possible to form a palindrome string, otherwise return `false`.

A string is a palindrome if it reads the same backward as forward.

Constraints:
- `1 <= a.length, b.length <= 10^5`
- `a.length == b.length`
- `a` and `b` consist of lowercase English letters.
"""

def is_palindrome(s: str) -> bool:
    """
    Helper function to check if a string is a palindrome.
    """
    return s == s[::-1]

def check_palindrome_formation(a: str, b: str) -> bool:
    """
    Main function to check if a palindrome can be formed by splitting strings `a` and `b`.
    """
    def can_form_palindrome(x: str, y: str) -> bool:
        """
        Check if x_left + y_right or y_left + x_right can form a palindrome.
        """
        i, j = 0, len(x) - 1
        while i < j and x[i] == y[j]:
            i += 1
            j -= 1
        # Check the remaining substring
        return is_palindrome(x[i:j+1]) or is_palindrome(y[i:j+1])
    
    # Check both combinations: a_left + b_right and b_left + a_right
    return can_form_palindrome(a, b) or can_form_palindrome(b, a)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a = "x"
    b = "y"
    print(check_palindrome_formation(a, b))  # Output: True

    # Test Case 2
    a = "abdef"
    b = "fecab"
    print(check_palindrome_formation(a, b))  # Output: True

    # Test Case 3
    a = "ulacfd"
    b = "jizalu"
    print(check_palindrome_formation(a, b))  # Output: True

    # Test Case 4
    a = "abcd"
    b = "efgh"
    print(check_palindrome_formation(a, b))  # Output: False

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The helper function `is_palindrome` runs in O(n) time for a substring of length n.
   - The `can_form_palindrome` function iterates through the strings with two pointers, which takes O(n) time.
   - In the worst case, we check two combinations (`a_left + b_right` and `b_left + a_right`), so the total time complexity is O(n).

2. Space Complexity:
   - The algorithm uses O(1) additional space since it only uses pointers and does not allocate extra space for substrings.

Overall:
Time Complexity: O(n)
Space Complexity: O(1)

Topic: Strings, Two Pointers
"""