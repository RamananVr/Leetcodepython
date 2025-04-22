"""
LeetCode Question #171: Excel Sheet Column Number

Problem Statement:
Given a string `columnTitle` that represents the column title as appears in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...

Constraints:
- 1 <= columnTitle.length <= 7
- columnTitle consists only of uppercase English letters.
- columnTitle is guaranteed to be a valid Excel column title.

Example:
Input: columnTitle = "AB"
Output: 28

Input: columnTitle = "ZY"
Output: 701

Input: columnTitle = "FXSHRXW"
Output: 2147483647
"""

def titleToNumber(columnTitle: str) -> int:
    """
    Converts an Excel column title to its corresponding column number.

    Args:
    columnTitle (str): The Excel column title.

    Returns:
    int: The corresponding column number.
    """
    result = 0
    for char in columnTitle:
        # Convert the character to its corresponding value (A=1, B=2, ..., Z=26)
        value = ord(char) - ord('A') + 1
        # Update the result using base-26 logic
        result = result * 26 + value
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    columnTitle = "A"
    print(f"Input: {columnTitle}, Output: {titleToNumber(columnTitle)}")  # Expected: 1

    # Test Case 2
    columnTitle = "AB"
    print(f"Input: {columnTitle}, Output: {titleToNumber(columnTitle)}")  # Expected: 28

    # Test Case 3
    columnTitle = "ZY"
    print(f"Input: {columnTitle}, Output: {titleToNumber(columnTitle)}")  # Expected: 701

    # Test Case 4
    columnTitle = "FXSHRXW"
    print(f"Input: {columnTitle}, Output: {titleToNumber(columnTitle)}")  # Expected: 2147483647

"""
Time Complexity:
- The time complexity of the solution is O(n), where n is the length of the input string `columnTitle`.
  This is because we iterate through each character of the string once.

Space Complexity:
- The space complexity is O(1), as we use only a constant amount of extra space.

Topic: Strings, Math
"""