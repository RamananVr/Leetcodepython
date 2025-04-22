"""
LeetCode Problem #483: Smallest Good Base

Problem Statement:
------------------
Given an integer `n` represented as a string, return the smallest good base of `n`.

A "good base" `k` satisfies the following condition:
For an integer `n`, there exists an integer `m` such that:
    n = k^m + k^(m-1) + ... + k^1 + k^0
In other words, `n` can be expressed as the sum of a geometric series with base `k` and length `m+1`.

Return the smallest good base as a string.

Constraints:
- `n` is a string representation of an integer in the range [3, 10^18].

Example 1:
Input: n = "13"
Output: "3"
Explanation: 13 can be written as 3^2 + 3^1 + 3^0 (a geometric series with base 3).

Example 2:
Input: n = "4681"
Output: "8"
Explanation: 4681 can be written as 8^4 + 8^3 + 8^2 + 8^1 + 8^0 (a geometric series with base 8).

Example 3:
Input: n = "1000000000000000000"
Output: "999999999999999999"
Explanation: 1000000000000000000 can be written as 999999999999999999^1 + 999999999999999999^0.

Note:
- The answer is guaranteed to be unique.
"""

# Python Solution
import math

def smallestGoodBase(n: str) -> str:
    num = int(n)
    
    # The maximum possible value for m (length of the series - 1)
    max_m = int(math.log2(num))  # log2(num) gives the maximum possible m
    
    for m in range(max_m, 1, -1):  # Try decreasing values of m
        # Binary search for the base k
        left, right = 2, int(num ** (1 / m)) + 1
        while left < right:
            mid = (left + right) // 2
            # Calculate the sum of the geometric series
            total = (mid ** (m + 1) - 1) // (mid - 1)
            if total == num:
                return str(mid)
            elif total < num:
                left = mid + 1
            else:
                right = mid
    
    # If no base is found, the smallest good base is num - 1
    return str(num - 1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = "13"
    print(smallestGoodBase(n1))  # Output: "3"

    # Test Case 2
    n2 = "4681"
    print(smallestGoodBase(n2))  # Output: "8"

    # Test Case 3
    n3 = "1000000000000000000"
    print(smallestGoodBase(n3))  # Output: "999999999999999999"

"""
Time and Space Complexity Analysis:
-----------------------------------
Time Complexity:
- The outer loop iterates over possible values of m, up to log2(num). This is O(log(num)).
- For each m, we perform a binary search over possible values of k, which is O(log(num)).
- Calculating the sum of the geometric series is O(1) for each iteration.
- Overall complexity: O(log(num) * log(num)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Math, Binary Search
"""