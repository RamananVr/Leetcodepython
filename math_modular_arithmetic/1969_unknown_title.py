"""
LeetCode Problem #1969: Minimum Non-Zero Product of the Array Elements

Problem Statement:
You are given a positive integer `p`. Consider an array `nums` that contains the integers in the range `[1, 2^p - 1]`.

You are allowed to perform the following operation any number of times:
- Choose two elements `x` and `y` from the array.
- Remove `x` and `y` from the array.
- Add the product `x * y` to the array.

Your goal is to minimize the value of the only remaining element in the array after performing the above operation any number of times.

Return the minimum non-zero product of the array elements modulo `10^9 + 7`.

Constraints:
- `1 <= p <= 60`

"""

# Solution
def minNonZeroProduct(p: int) -> int:
    MOD = 10**9 + 7
    
    # The largest number in the range [1, 2^p - 1]
    max_num = (1 << p) - 1
    
    # The second largest number in the range
    second_max_num = max_num - 1
    
    # The count of the second largest number in the product
    count = (max_num // 2)
    
    # Compute the result using modular exponentiation
    result = (max_num * pow(second_max_num, count, MOD)) % MOD
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    p = 1
    print(minNonZeroProduct(p))  # Expected Output: 1

    # Test Case 2
    p = 2
    print(minNonZeroProduct(p))  # Expected Output: 6

    # Test Case 3
    p = 3
    print(minNonZeroProduct(p))  # Expected Output: 1512

    # Test Case 4
    p = 4
    print(minNonZeroProduct(p))  # Expected Output: 581202553

    # Test Case 5
    p = 60
    print(minNonZeroProduct(p))  # Expected Output: A large number modulo 10^9 + 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- Computing `max_num` and `second_max_num` takes O(1).
- Modular exponentiation using `pow(base, exp, mod)` is O(log(exp)), where `exp` is `max_num // 2`.
- Overall time complexity: O(log(2^(p-1))) = O(p).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of space.

Topic: Math, Modular Arithmetic
"""