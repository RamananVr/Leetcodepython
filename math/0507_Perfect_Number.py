"""
LeetCode Problem #507: Perfect Number

Problem Statement:
A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding itself. 
For instance, 28 is a perfect number because its divisors are 1, 2, 4, 7, and 14, and 1 + 2 + 4 + 7 + 14 = 28.

Given an integer `num`, return `True` if `num` is a perfect number, otherwise return `False`.

Constraints:
- 1 <= num <= 10^8
"""

def checkPerfectNumber(num: int) -> bool:
    if num <= 1:
        return False  # Perfect numbers must be greater than 1
    
    divisors_sum = 1  # Start with 1 as it is a divisor of all numbers
    sqrt_num = int(num**0.5)
    
    for i in range(2, sqrt_num + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:  # Avoid adding the square root twice for perfect squares
                divisors_sum += num // i
    
    return divisors_sum == num

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Perfect number
    print(checkPerfectNumber(28))  # Expected output: True

    # Test Case 2: Not a perfect number
    print(checkPerfectNumber(6))  # Expected output: True

    # Test Case 3: Not a perfect number
    print(checkPerfectNumber(12))  # Expected output: False

    # Test Case 4: Edge case (smallest number)
    print(checkPerfectNumber(1))  # Expected output: False

    # Test Case 5: Large perfect number
    print(checkPerfectNumber(8128))  # Expected output: True

"""
Time Complexity:
- The loop runs up to the square root of `num`, so the time complexity is O(sqrt(num)).
- For each divisor found, we perform constant-time operations (adding to the sum).

Space Complexity:
- The space complexity is O(1) since we use a constant amount of extra space.

Topic: Math
"""