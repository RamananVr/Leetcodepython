"""
LeetCode Question #168: Excel Sheet Column Title

Problem Statement:
Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.

For example:
    1 -> "A"
    2 -> "B"
    3 -> "C"
    ...
    26 -> "Z"
    27 -> "AA"
    28 -> "AB"
    ...

Constraints:
- 1 <= columnNumber <= 2^31 - 1

The problem is essentially converting a number to a base-26 representation where the digits are mapped to letters 'A' to 'Z'.
"""

# Solution
def convertToTitle(columnNumber: int) -> str:
    result = []
    while columnNumber > 0:
        columnNumber -= 1  # Adjust for 1-based indexing
        remainder = columnNumber % 26
        result.append(chr(remainder + ord('A')))  # Map remainder to corresponding letter
        columnNumber //= 26
    return ''.join(result[::-1])  # Reverse the result to get the correct column title

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Single letter
    print(convertToTitle(1))  # Expected Output: "A"
    
    # Test Case 2: End of single letter range
    print(convertToTitle(26))  # Expected Output: "Z"
    
    # Test Case 3: Start of double letter range
    print(convertToTitle(27))  # Expected Output: "AA"
    
    # Test Case 4: Arbitrary double letter
    print(convertToTitle(28))  # Expected Output: "AB"
    
    # Test Case 5: Large number
    print(convertToTitle(701))  # Expected Output: "ZY"
    
    # Test Case 6: Very large number
    print(convertToTitle(2147483647))  # Expected Output: "FXSHRXW"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs a division operation repeatedly until columnNumber becomes 0.
- The number of iterations is proportional to the number of digits in the base-26 representation of columnNumber.
- Since columnNumber can be at most 2^31 - 1, the number of iterations is O(log(columnNumber)) in base 26.
- Therefore, the time complexity is O(log(columnNumber)).

Space Complexity:
- The space complexity is O(log(columnNumber)) due to the storage of the result list, which holds the characters of the column title.
- The final string is constructed by reversing the list, which also takes O(log(columnNumber)) space.

Topic: Math / String Manipulation
"""