"""
LeetCode Problem #2729: Check if The Number is Fascinating

Problem Statement:
You are given an integer `n` that consists of exactly 3 digits.

We call a number fascinating if, after concatenating it with its multiplication by 2 and 3 respectively, 
the resulting number contains all the digits from 1 to 9 exactly once and does not contain any 0s.

Return `true` if `n` is fascinating, or `false` otherwise.

Example 1:
Input: n = 192
Output: true
Explanation: After concatenating 192, 192 * 2 = 384, and 192 * 3 = 576, we get "192384576".
This number contains all digits from 1 to 9 exactly once.

Example 2:
Input: n = 100
Output: false
Explanation: After concatenating 100, 100 * 2 = 200, and 100 * 3 = 300, we get "100200300".
This number does not contain all digits from 1 to 9.

Constraints:
- 100 <= n <= 999
"""

def isFascinating(n: int) -> bool:
    # Concatenate n, n*2, and n*3 as strings
    concatenated = str(n) + str(n * 2) + str(n * 3)
    
    # Check if the concatenated string contains all digits from 1 to 9 exactly once
    return len(concatenated) == 9 and set(concatenated) == set("123456789")


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Fascinating number
    n1 = 192
    print(isFascinating(n1))  # Expected output: True

    # Test Case 2: Not a fascinating number
    n2 = 100
    print(isFascinating(n2))  # Expected output: False

    # Test Case 3: Another fascinating number
    n3 = 273
    print(isFascinating(n3))  # Expected output: True

    # Test Case 4: Not a fascinating number
    n4 = 111
    print(isFascinating(n4))  # Expected output: False

    # Test Case 5: Edge case with smallest 3-digit number
    n5 = 123
    print(isFascinating(n5))  # Expected output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The operations performed are string concatenation and set comparison.
- String concatenation takes O(1) since the input size is fixed (3 digits).
- Creating a set from the concatenated string and comparing it with the set "123456789" also takes O(1) 
  because the length of the concatenated string is always 9.
- Therefore, the overall time complexity is O(1).

Space Complexity:
- The space used is for the concatenated string and the set comparison.
- Since the concatenated string has a fixed length of 9 and the set comparison involves a fixed set of size 9, 
  the space complexity is O(1).

Topic: Strings
"""