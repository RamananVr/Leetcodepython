"""
LeetCode Question #2947: Problem Statement

You are given a string `s` consisting of lowercase English letters. You can perform the following operation on the string any number of times:

- Choose any character in the string and remove it.

Your goal is to determine the minimum number of operations required to make all the characters in the string distinct.

Constraints:
- 1 <= len(s) <= 10^5
- `s` consists of lowercase English letters.

Example:
Input: s = "aabbcc"
Output: 3
Explanation: You can remove one 'a', one 'b', and one 'c' to make all characters distinct.

Input: s = "abc"
Output: 0
Explanation: All characters are already distinct, so no operations are needed.
"""

# Python Solution
def min_operations_to_make_distinct(s: str) -> int:
    """
    Calculate the minimum number of operations required to make all characters in the string distinct.

    :param s: Input string consisting of lowercase English letters.
    :return: Minimum number of operations required.
    """
    from collections import Counter

    # Count the frequency of each character in the string
    char_count = Counter(s)

    # Initialize the number of operations
    operations = 0

    # Iterate through the character frequencies
    for freq in char_count.values():
        # If a character appears more than once, add the excess to operations
        if freq > 1:
            operations += freq - 1

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All characters are distinct
    s1 = "abc"
    print(min_operations_to_make_distinct(s1))  # Output: 0

    # Test Case 2: Some characters are repeated
    s2 = "aabbcc"
    print(min_operations_to_make_distinct(s2))  # Output: 3

    # Test Case 3: All characters are the same
    s3 = "aaaa"
    print(min_operations_to_make_distinct(s3))  # Output: 3

    # Test Case 4: Large input with mixed characters
    s4 = "aabbccddeeffgghhii"
    print(min_operations_to_make_distinct(s4))  # Output: 9

    # Test Case 5: Single character
    s5 = "z"
    print(min_operations_to_make_distinct(s5))  # Output: 0

"""
Time and Space Complexity Analysis

Time Complexity:
- Counting the frequency of characters using `Counter` takes O(n), where n is the length of the string.
- Iterating through the frequencies takes O(26) since there are at most 26 lowercase English letters.
- Overall time complexity: O(n).

Space Complexity:
- The `Counter` object stores at most 26 key-value pairs (one for each lowercase English letter).
- Space complexity: O(1) (constant space for the frequency map).

Topic: Strings
"""