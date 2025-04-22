"""
LeetCode Question #246: Strobogrammatic Number

Problem Statement:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down). 
Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:
Input: num = "69"
Output: true

Example 2:
Input: num = "88"
Output: true

Example 3:
Input: num = "962"
Output: false

Constraints:
- The input num will be a string consisting of digits.
- The input num will not have leading zeros except for the number "0" itself.
"""

def isStrobogrammatic(num: str) -> bool:
    """
    Determines if a number is strobogrammatic.

    Args:
    num (str): The input number as a string.

    Returns:
    bool: True if the number is strobogrammatic, False otherwise.
    """
    # Mapping of digits that are strobogrammatic
    strobogrammatic_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    # Two-pointer approach to check the number
    left, right = 0, len(num) - 1
    while left <= right:
        if num[left] not in strobogrammatic_map or num[right] not in strobogrammatic_map:
            return False
        if strobogrammatic_map[num[left]] != num[right]:
            return False
        left += 1
        right -= 1
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "69"
    print(isStrobogrammatic(num1))  # Output: True

    # Test Case 2
    num2 = "88"
    print(isStrobogrammatic(num2))  # Output: True

    # Test Case 3
    num3 = "962"
    print(isStrobogrammatic(num3))  # Output: False

    # Test Case 4
    num4 = "818"
    print(isStrobogrammatic(num4))  # Output: True

    # Test Case 5
    num5 = "2"
    print(isStrobogrammatic(num5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the input string using a two-pointer approach.
- Each character is checked against the strobogrammatic map, which is an O(1) operation.
- Therefore, the time complexity is O(n), where n is the length of the input string.

Space Complexity:
- The function uses a dictionary to store the strobogrammatic mappings, which is a constant space requirement (O(1)).
- No additional space is used proportional to the input size.
- Therefore, the space complexity is O(1).

Topic: Strings
"""