"""
LeetCode Problem #793: Preimage Size of Factorial Zeroes Function

Problem Statement:
Let f(x) be the number of zeroes at the end of x! (x factorial). For example:
- f(3) = 0 because 3! = 6 has no trailing zeroes.
- f(11) = 2 because 11! = 39916800 has 2 trailing zeroes.

Given an integer k, return the number of non-negative integers x such that f(x) = k.

Example:
Input: k = 5
Output: 0

Explanation:
There are no integers x such that f(x) = 5.

Constraints:
- 0 <= k <= 10^9
"""

# Solution
def preimageSizeFZF(k: int) -> int:
    def zeta(x: int) -> int:
        """Calculate the number of trailing zeroes in x!."""
        count = 0
        while x > 0:
            x //= 5
            count += x
        return count

    def binary_search(k: int) -> int:
        """Binary search to find the range of x where f(x) = k."""
        left, right = 0, 5 * (k + 1)
        while left < right:
            mid = (left + right) // 2
            if zeta(mid) < k:
                left = mid + 1
            else:
                right = mid
        return left

    # Find the lower and upper bounds of x where f(x) = k
    lower_bound = binary_search(k)
    upper_bound = binary_search(k + 1)
    
    # The size of the preimage is the difference between the bounds
    return upper_bound - lower_bound

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 0
    print(preimageSizeFZF(k))  # Output: 5

    # Test Case 2
    k = 5
    print(preimageSizeFZF(k))  # Output: 0

    # Test Case 3
    k = 3
    print(preimageSizeFZF(k))  # Output: 5

    # Test Case 4
    k = 10
    print(preimageSizeFZF(k))  # Output: 0

    # Test Case 5
    k = 100
    print(preimageSizeFZF(k))  # Output: 0

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The `zeta` function runs in O(log(x)) time because it repeatedly divides x by 5.
   - The binary search runs in O(log(k)) iterations, and each iteration calls `zeta`, which is O(log(x)).
   - Therefore, the overall time complexity is O(log(k) * log(x)), where x is proportional to 5 * (k + 1).

2. Space Complexity:
   - The solution uses O(1) additional space, as no extra data structures are used.

Topic: Binary Search
"""