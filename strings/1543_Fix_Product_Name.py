"""
LeetCode Problem #1543: Fix Product Name

Problem Statement:
You are given a string `s` that represents a product name. The product name is considered valid if it satisfies the following conditions:
1. It contains only lowercase English letters and spaces.
2. It does not contain two consecutive spaces.
3. It does not start or end with a space.

Your task is to write a function `fixProductName(s: str) -> str` that modifies the input string `s` to make it a valid product name by:
- Removing leading and trailing spaces.
- Replacing multiple consecutive spaces with a single space.

Return the modified string.

Constraints:
- The input string `s` consists of printable ASCII characters.
- The length of `s` is between 1 and 10^5.

Example:
Input: "  hello   world  "
Output: "hello world"
"""

def fixProductName(s: str) -> str:
    """
    Fixes the product name by removing leading/trailing spaces and replacing multiple spaces with a single space.
    
    :param s: The input string representing the product name.
    :return: A valid product name string.
    """
    # Strip leading and trailing spaces
    s = s.strip()
    # Replace multiple spaces with a single space
    s = ' '.join(s.split())
    return s

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "  hello   world  "
    print(fixProductName(s1))  # Expected Output: "hello world"

    # Test Case 2
    s2 = "a   b   c"
    print(fixProductName(s2))  # Expected Output: "a b c"

    # Test Case 3
    s3 = "   singleword   "
    print(fixProductName(s3))  # Expected Output: "singleword"

    # Test Case 4
    s4 = "   "
    print(fixProductName(s4))  # Expected Output: ""

    # Test Case 5
    s5 = "noextra spaces"
    print(fixProductName(s5))  # Expected Output: "noextra spaces"

"""
Time Complexity Analysis:
- The `strip()` function runs in O(n), where n is the length of the string.
- The `split()` function splits the string into words, which also takes O(n).
- The `' '.join()` function concatenates the words with a single space, which takes O(n).
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The `split()` function creates a list of words, which requires O(k) space, where k is the number of words in the string.
- The final result string requires O(n) space.
- Overall, the space complexity is O(n).

Topic: Strings
"""