"""
LeetCode Problem #2719: Count of Integers

Problem Statement:
You are given two integers `low` and `high`, and an integer `k`. A number is considered valid if:
1. It is between `low` and `high` (inclusive).
2. The sum of its digits is divisible by `k`.

Return the count of all valid numbers.

Constraints:
- 1 <= low <= high <= 10^9
- 1 <= k <= 50
"""

# Solution
def count_valid_numbers(low: int, high: int, k: int) -> int:
    def digit_sum(n: int) -> int:
        """Helper function to calculate the sum of digits of a number."""
        return sum(int(digit) for digit in str(n))
    
    def is_valid(n: int) -> bool:
        """Check if a number is valid based on the problem's conditions."""
        return digit_sum(n) % k == 0
    
    count = 0
    for num in range(low, high + 1):
        if is_valid(num):
            count += 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 10
    high = 20
    k = 5
    print(count_valid_numbers(low, high, k))  # Expected Output: 2 (10 and 15 are valid)

    # Test Case 2
    low = 1
    high = 10
    k = 3
    print(count_valid_numbers(low, high, k))  # Expected Output: 3 (3, 6, and 9 are valid)

    # Test Case 3
    low = 100
    high = 200
    k = 7
    print(count_valid_numbers(low, high, k))  # Expected Output: Depends on the range and k

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the sum of digits for a number takes O(d), where d is the number of digits in the number.
- Iterating through all numbers between `low` and `high` takes O(high - low + 1).
- Therefore, the overall time complexity is O((high - low + 1) * d), where d is the average number of digits in the range.

Space Complexity:
- The space complexity is O(1) since we are only using a few variables and not storing intermediate results.

Topic: Brute Force, Math
"""