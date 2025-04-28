"""
LeetCode Problem #2064: Minimized Maximum of Products Distributed to Any Store

Problem Statement:
You are given an integer `n` denoting the number of stores and an integer array `quantities` of size `m` where `quantities[i]` represents the number of products of the i-th type.

You need to distribute all the products to the stores such that each store gets products of only one type. Each store can get at most one type of product, and the maximum number of products assigned to any store is minimized.

Return the minimized maximum number of products that can be assigned to any store.

Constraints:
- `m == quantities.length`
- `1 <= m <= 10^5`
- `1 <= n <= 10^5`
- `1 <= quantities[i] <= 10^5`
"""

from typing import List

def minimizedMaximum(n: int, quantities: List[int]) -> int:
    def canDistribute(max_products: int) -> bool:
        # Check if it's possible to distribute with max_products per store
        stores_needed = 0
        for quantity in quantities:
            stores_needed += (quantity + max_products - 1) // max_products  # Ceiling division
            if stores_needed > n:
                return False
        return True

    # Binary search for the minimized maximum
    left, right = 1, max(quantities)
    while left < right:
        mid = (left + right) // 2
        if canDistribute(mid):
            right = mid
        else:
            left = mid + 1
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 6
    quantities1 = [11, 6]
    print(minimizedMaximum(n1, quantities1))  # Expected Output: 3

    # Test Case 2
    n2 = 7
    quantities2 = [15, 10, 10]
    print(minimizedMaximum(n2, quantities2))  # Expected Output: 5

    # Test Case 3
    n3 = 1
    quantities3 = [100000]
    print(minimizedMaximum(n3, quantities3))  # Expected Output: 100000

    # Test Case 4
    n4 = 10
    quantities4 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    print(minimizedMaximum(n4, quantities4))  # Expected Output: 1

"""
Time Complexity:
- The binary search runs in O(log(max(quantities))) iterations.
- For each iteration, the `canDistribute` function is called, which iterates through the `quantities` array of size m.
- Therefore, the overall time complexity is O(m * log(max(quantities))).

Space Complexity:
- The space complexity is O(1) since we are using a constant amount of extra space.

Topic: Binary Search
"""