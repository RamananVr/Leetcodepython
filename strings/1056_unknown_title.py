"""
LeetCode Problem #1056: Confusing Number

Problem Statement:
A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid. 
We can rotate digits 0, 1, 6, 8, and 9 to become 0, 1, 9, 8, and 6 respectively. 
Digits 2, 3, 4, 5, and 7 become invalid when rotated.

Given an integer n, return true if it is a confusing number, or false otherwise.

Example 1:
Input: n = 6
Output: true
Explanation: We get 9 after rotating 6, which is a different number.

Example 2:
Input: n = 89
Output: true
Explanation: We get 68 after rotating 89, which is a different number.

Example 3:
Input: n = 11
Output: false
Explanation: We get 11 after rotating 11, which is the same number.

Constraints:
- 0 <= n <= 10^9
"""

def confusingNumber(n: int) -> bool:
    # Mapping of digits to their rotated counterparts
    rotation_map = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
    
    # Convert the number to a string
    original = str(n)
    
    # Initialize an empty string for the rotated number
    rotated = ""
    
    # Iterate through the digits of the number in reverse order
    for digit in reversed(original):
        # If the digit is not in the rotation map, it's invalid
        if digit not in rotation_map:
            return False
        # Append the rotated digit to the rotated string
        rotated += rotation_map[digit]
    
    # A number is confusing if the rotated number is different from the original
    return rotated != original

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    print(confusingNumber(n1))  # Output: True

    # Test Case 2
    n2 = 89
    print(confusingNumber(n2))  # Output: True

    # Test Case 3
    n3 = 11
    print(confusingNumber(n3))  # Output: False

    # Test Case 4
    n4 = 25
    print(confusingNumber(n4))  # Output: False

    # Test Case 5
    n5 = 916
    print(confusingNumber(n5))  # Output: True

"""
Time Complexity Analysis:
- Let d be the number of digits in n.
- The algorithm iterates through each digit of n once, performing constant-time operations for each digit.
- Therefore, the time complexity is O(d), where d is the number of digits in n.

Space Complexity Analysis:
- The space complexity is O(d) due to the storage of the rotated string, which can have at most d characters.
- The rotation map is a fixed size (constant space), so it does not contribute to the space complexity.

Topic: Strings
"""