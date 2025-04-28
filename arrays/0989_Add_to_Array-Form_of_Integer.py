"""
LeetCode Problem #989: Add to Array-Form of Integer

Problem Statement:
The array-form of an integer num is an array representing its digits in left-to-right order. 
For example, for num = 123, the array form is [1,2,3]. Given num, the array-form of an integer, 
and an integer k, return the array-form of the integer num + k.

Example 1:
Input: num = [1,2,0,0], k = 34
Output: [1,2,3,4]
Explanation: 1200 + 34 = 1234

Example 2:
Input: num = [2,7,4], k = 181
Output: [4,5,5]
Explanation: 274 + 181 = 455

Example 3:
Input: num = [2,1,5], k = 806
Output: [1,0,2,1]
Explanation: 215 + 806 = 1021

Constraints:
- 1 <= num.length <= 10^4
- 0 <= num[i] <= 9
- num does not contain any leading zeros except for the number 0 itself.
- 0 <= k <= 10^4
"""

# Solution
def addToArrayForm(num, k):
    """
    Add an integer k to the array-form of an integer num.

    Args:
    num (List[int]): The array-form of an integer.
    k (int): The integer to add.

    Returns:
    List[int]: The array-form of the result.
    """
    # Convert the array-form of num to an integer
    num_as_int = int("".join(map(str, num)))
    
    # Add k to the integer representation
    result = num_as_int + k
    
    # Convert the result back to array-form
    return [int(digit) for digit in str(result)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = [1, 2, 0, 0]
    k1 = 34
    print(addToArrayForm(num1, k1))  # Output: [1, 2, 3, 4]

    # Test Case 2
    num2 = [2, 7, 4]
    k2 = 181
    print(addToArrayForm(num2, k2))  # Output: [4, 5, 5]

    # Test Case 3
    num3 = [2, 1, 5]
    k3 = 806
    print(addToArrayForm(num3, k3))  # Output: [1, 0, 2, 1]

    # Test Case 4
    num4 = [0]
    k4 = 10000
    print(addToArrayForm(num4, k4))  # Output: [1, 0, 0, 0, 0]

    # Test Case 5
    num5 = [9, 9, 9, 9]
    k5 = 1
    print(addToArrayForm(num5, k5))  # Output: [1, 0, 0, 0, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Converting the array-form `num` to an integer takes O(n), where n is the length of the array.
- Adding k to the integer takes O(1).
- Converting the result back to array-form takes O(m), where m is the number of digits in the result.
- In the worst case, m = O(n + log(k)), so the overall time complexity is O(n + log(k)).

Space Complexity:
- The space required for the result array is O(m), where m is the number of digits in the result.
- The space complexity is O(n + log(k)) in the worst case.
"""

# Topic: Arrays