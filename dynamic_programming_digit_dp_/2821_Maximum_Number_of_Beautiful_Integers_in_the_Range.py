"""
LeetCode Problem #2821: "Maximum Number of Beautiful Integers in the Range"

Problem Statement:
You are given two integers `low` and `high` representing a range of integers `[low, high]` (inclusive). 
An integer is considered "beautiful" if it satisfies the following conditions:
1. It has an equal number of even and odd digits.
2. The digits of the number are in non-decreasing order.

Return the maximum number of beautiful integers in the range `[low, high]`.

Constraints:
- 1 <= low <= high <= 10^9
- The range `[low, high]` can span up to 10^9 numbers, so an efficient solution is required.
"""

# Solution
def count_beautiful_integers(low: int, high: int) -> int:
    from functools import lru_cache

    def is_beautiful(num: int) -> bool:
        """Check if a number is beautiful."""
        digits = list(map(int, str(num)))
        even_count = sum(1 for d in digits if d % 2 == 0)
        odd_count = len(digits) - even_count
        return even_count == odd_count and digits == sorted(digits)

    @lru_cache(None)
    def count_beautiful_up_to(n: int) -> int:
        """Count beautiful numbers up to n."""
        digits = list(map(int, str(n)))
        length = len(digits)

        def dfs(pos: int, even_count: int, odd_count: int, is_tight: bool, is_leading_zero: bool) -> int:
            if pos == length:
                return 1 if even_count == odd_count and even_count > 0 else 0

            limit = digits[pos] if is_tight else 9
            total = 0

            for digit in range(0, limit + 1):
                new_even_count = even_count + (1 if digit % 2 == 0 else 0)
                new_odd_count = odd_count + (1 if digit % 2 != 0 else 0)
                total += dfs(
                    pos + 1,
                    new_even_count,
                    new_odd_count,
                    is_tight and (digit == limit),
                    is_leading_zero and digit == 0
                )

            return total

        return dfs(0, 0, 0, True, True)

    return count_beautiful_up_to(high) - count_beautiful_up_to(low - 1)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = 10
    high = 100
    print(count_beautiful_integers(low, high))  # Expected output: (depends on the range)

    # Test Case 2
    low = 1
    high = 1000
    print(count_beautiful_integers(low, high))  # Expected output: (depends on the range)

    # Test Case 3
    low = 123
    high = 456
    print(count_beautiful_integers(low, high))  # Expected output: (depends on the range)

"""
Time Complexity:
- The solution uses digit DP, which has a complexity of O(d * even_count * odd_count * 2), where `d` is the number of digits in the number.
- Since the number of digits in the range `[low, high]` is at most 10 (for numbers up to 10^9), the complexity is effectively O(10 * even_count * odd_count * 2), which is constant.

Space Complexity:
- The space complexity is O(d * even_count * odd_count * 2) due to the memoization table used in the digit DP.

Topic: Dynamic Programming (Digit DP)
"""