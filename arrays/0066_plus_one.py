"""
LeetCode Question #66: Plus One

Problem Statement:
You are given a large integer represented as an integer array `digits`, where each `digits[i]` is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. 
The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

Example 1:
Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123. Incrementing by one gives 123 + 1 = 124.

Example 2:
Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321. Incrementing by one gives 4321 + 1 = 4322.

Example 3:
Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9. Incrementing by one gives 9 + 1 = 10.

Constraints:
- 1 <= digits.length <= 100
- 0 <= digits[i] <= 9
- digits does not contain any leading 0's.
"""

# Clean, Correct Python Solution
def plusOne(digits):
    """
    Increment the large integer represented by the digits array by one.

    :param digits: List[int] - The array of digits representing the integer.
    :return: List[int] - The resulting array of digits after incrementing by one.
    """
    n = len(digits)
    for i in range(n - 1, -1, -1):
        if digits[i] < 9:
            digits[i] += 1
            return digits
        digits[i] = 0
    
    # If all digits are 9, we need to add a new leading 1
    return [1] + digits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    digits1 = [1, 2, 3]
    print(plusOne(digits1))  # Output: [1, 2, 4]

    # Test Case 2
    digits2 = [4, 3, 2, 1]
    print(plusOne(digits2))  # Output: [4, 3, 2, 2]

    # Test Case 3
    digits3 = [9]
    print(plusOne(digits3))  # Output: [1, 0]

    # Test Case 4
    digits4 = [9, 9, 9]
    print(plusOne(digits4))  # Output: [1, 0, 0, 0]

    # Test Case 5
    digits5 = [0]
    print(plusOne(digits5))  # Output: [1]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the digits array from the least significant digit to the most significant digit.
- In the worst case, we traverse the entire array once, which takes O(n) time, where n is the length of the digits array.

Space Complexity:
- The algorithm modifies the input array in place and uses O(1) additional space.
- In the case where all digits are 9, we create a new array of size n + 1, which takes O(n) space.
- Therefore, the space complexity is O(n) in the worst case.

Overall:
- Time Complexity: O(n)
- Space Complexity: O(n)
"""

# Topic: Arrays