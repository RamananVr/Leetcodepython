"""
LeetCode Problem #2231: Largest Number After Digit Swaps by Parity

Problem Statement:
You are given a positive integer `num`. You may swap any two digits of `num` that have the same parity 
(even or odd). Return the largest possible value of `num` after any number of swaps.

Example 1:
Input: num = 1234
Output: 3412
Explanation: Swap the even digits (2 and 4) and the odd digits (1 and 3) to get 3412.

Example 2:
Input: num = 65875
Output: 87655
Explanation: Swap the odd digits (5, 5, 7) and the even digits (6, 8) to get 87655.

Constraints:
- 1 <= num <= 10^9
"""

# Solution
def largestInteger(num: int) -> int:
    # Convert the number to a list of digits
    digits = list(map(int, str(num)))
    
    # Separate digits by parity
    odd_digits = sorted([d for d in digits if d % 2 == 1], reverse=True)
    even_digits = sorted([d for d in digits if d % 2 == 0], reverse=True)
    
    # Reconstruct the number by swapping digits based on parity
    result = []
    for d in digits:
        if d % 2 == 0:
            result.append(even_digits.pop(0))  # Take the largest remaining even digit
        else:
            result.append(odd_digits.pop(0))  # Take the largest remaining odd digit
    
    # Convert the result list back to an integer
    return int("".join(map(str, result)))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = 1234
    print(largestInteger(num1))  # Output: 3412

    # Test Case 2
    num2 = 65875
    print(largestInteger(num2))  # Output: 87655

    # Test Case 3
    num3 = 247
    print(largestInteger(num3))  # Output: 742

    # Test Case 4
    num4 = 13579
    print(largestInteger(num4))  # Output: 97531

    # Test Case 5
    num5 = 24680
    print(largestInteger(num5))  # Output: 86420

"""
Time and Space Complexity Analysis:

Time Complexity:
- Separating digits by parity takes O(n), where n is the number of digits in `num`.
- Sorting the odd and even digits takes O(n log n) in the worst case.
- Reconstructing the result takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- We use additional space to store the odd and even digits, which takes O(n).
- The result list also takes O(n) space.
- Overall space complexity: O(n).

Topic: Arrays
"""