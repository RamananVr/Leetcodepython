"""
LeetCode Problem #1726: Tuple with Same Product

Problem Statement:
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) such that:
    - a * b = c * d
    - a, b, c, and d are distinct elements of nums.

Example:
Input: nums = [2, 3, 4, 6]
Output: 8
Explanation: There are 8 valid tuples:
(2, 6, 3, 4), (2, 6, 4, 3), (6, 2, 3, 4), (6, 2, 4, 3),
(3, 4, 2, 6), (3, 4, 6, 2), (4, 3, 2, 6), (4, 3, 6, 2).

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- All elements in nums are distinct.
"""

# Solution
from collections import defaultdict

def tupleSameProduct(nums):
    """
    Function to calculate the number of tuples (a, b, c, d) such that a * b = c * d
    and a, b, c, d are distinct elements of nums.

    :param nums: List[int] - Array of distinct positive integers
    :return: int - Number of valid tuples
    """
    product_map = defaultdict(int)
    n = len(nums)
    
    # Count pairs with the same product
    for i in range(n):
        for j in range(i + 1, n):
            product = nums[i] * nums[j]
            product_map[product] += 1
    
    # Calculate the number of tuples
    result = 0
    for count in product_map.values():
        if count > 1:
            # For each product with `count` pairs, we can form count * (count - 1) / 2 combinations
            # Each combination contributes 8 tuples
            result += 8 * (count * (count - 1)) // 2
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4, 6]
    print(tupleSameProduct(nums1))  # Output: 8

    # Test Case 2
    nums2 = [1, 2, 4, 5, 10]
    print(tupleSameProduct(nums2))  # Output: 16

    # Test Case 3
    nums3 = [2, 3, 5, 7]
    print(tupleSameProduct(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3, 6]
    print(tupleSameProduct(nums4))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all pairs of elements in nums, resulting in O(n^2) time complexity.
- The inner loop calculates the product and updates the product_map, which is O(1) for each pair.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The space complexity is determined by the size of the product_map, which stores the frequency of products.
- In the worst case, there could be O(n^2) unique products (if all pairs produce distinct products).
- Therefore, the space complexity is O(n^2).

Topic: Hash Map, Arrays
"""