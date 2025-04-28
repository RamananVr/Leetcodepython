"""
LeetCode Problem #2847: Smallest Number With Given Digit Product

Problem Statement:
You are given an integer `n`. Your task is to find the smallest positive integer whose digits' product is equal to `n`. 
If no such number exists, return -1.

Constraints:
- 0 <= n <= 10^9

Example:
Input: n = 36
Output: 49
Explanation: The digits of 49 are 4 and 9, and their product is 36. 49 is the smallest number with this property.

Input: n = 1
Output: 1
Explanation: The smallest number whose digits' product is 1 is 1 itself.

Input: n = 0
Output: 10
Explanation: The smallest number whose digits' product is 0 is 10 (1 * 0 = 0).

Input: n = 13
Output: -1
Explanation: There is no number whose digits' product is 13.
"""

def smallestNumber(n: int) -> int:
    if n == 0:
        return 10  # Special case: smallest number with product 0 is 10 (1 * 0 = 0)
    if n == 1:
        return 1  # Special case: smallest number with product 1 is 1 itself

    # To find the smallest number, we need to break `n` into factors of digits (2-9)
    factors = []
    for digit in range(9, 1, -1):  # Start from 9 and go down to 2
        while n % digit == 0:
            factors.append(digit)
            n //= digit

    # If `n` is not 1 after the loop, it means it has prime factors > 9, so return -1
    if n != 1:
        return -1

    # Sort the factors to form the smallest number
    factors.sort()

    # Combine the factors into a single number
    result = int(''.join(map(str, factors)))
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 36
    print(smallestNumber(n))  # Output: 49

    # Test Case 2
    n = 1
    print(smallestNumber(n))  # Output: 1

    # Test Case 3
    n = 0
    print(smallestNumber(n))  # Output: 10

    # Test Case 4
    n = 13
    print(smallestNumber(n))  # Output: -1

    # Test Case 5
    n = 100
    print(smallestNumber(n))  # Output: 455


"""
Time Complexity Analysis:
- The loop iterates over digits from 9 to 2, and for each digit, it divides `n` repeatedly until `n` is no longer divisible by that digit.
- In the worst case, the number of divisions is proportional to the number of digits in `n` (log(n) base 2).
- Sorting the factors takes O(k log k), where k is the number of factors (at most log(n) base 2).
- Overall time complexity: O(log(n) + k log k), which simplifies to O(log(n)) since k is small.

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of factors stored in the `factors` list.
- Since k is small (at most log(n) base 2), the space complexity is effectively O(log(n)).

Topic: Math, Number Theory
"""