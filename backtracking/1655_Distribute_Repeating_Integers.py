"""
LeetCode Problem #1655: Distribute Repeating Integers

Problem Statement:
You are given an array of integers `nums` where the i-th integer `nums[i]` represents the count of the i-th unique integer. 
You are also given an array `quantity` where the j-th integer `quantity[j]` represents the amount of the j-th customer's order.

Return true if it is possible to distribute integers such that:
1. Each customer gets exactly `quantity[j]` integers.
2. The integers a customer gets are all of the same kind.
3. Every customer is served.

Otherwise, return false.

Example 1:
Input: nums = [1,2,3], quantity = [2,2]
Output: false

Example 2:
Input: nums = [1,2,3,4], quantity = [2]
Output: true

Constraints:
- 1 <= nums.length <= 50
- 1 <= nums[i] <= 10^5
- 1 <= quantity.length <= 10
- 1 <= quantity[j] <= 10^5
"""

from itertools import combinations
from collections import Counter

def canDistribute(nums, quantity):
    """
    Determines if it is possible to distribute integers to satisfy all customer orders.

    :param nums: List[int] - counts of unique integers
    :param quantity: List[int] - required quantities for each customer
    :return: bool - True if distribution is possible, False otherwise
    """
    # Count the frequency of each unique integer
    freq = list(Counter(nums).values())
    
    # Sort the quantity array in descending order for optimization
    quantity.sort(reverse=True)
    
    # Helper function to check if we can fulfill the orders
    def backtrack(index):
        if index == len(quantity):
            return True
        for i in range(len(freq)):
            if freq[i] >= quantity[index]:
                freq[i] -= quantity[index]
                if backtrack(index + 1):
                    return True
                freq[i] += quantity[index]
        return False
    
    return backtrack(0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    quantity1 = [2, 2]
    print(canDistribute(nums1, quantity1))  # Output: False

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    quantity2 = [2]
    print(canDistribute(nums2, quantity2))  # Output: True

    # Test Case 3
    nums3 = [4, 3, 3, 3]
    quantity3 = [2, 2]
    print(canDistribute(nums3, quantity3))  # Output: True

    # Test Case 4
    nums4 = [10, 10, 10]
    quantity4 = [5, 5, 5]
    print(canDistribute(nums4, quantity4))  # Output: True

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    quantity5 = [2, 2, 2]
    print(canDistribute(nums5, quantity5))  # Output: False

"""
Time Complexity:
- The backtracking function explores all possible ways to distribute the quantities. 
  In the worst case, there are O(2^m) subsets of quantities to consider, where m is the length of the `quantity` array.
- For each subset, we iterate over the `freq` array, which has a length of at most 50.
- Thus, the time complexity is approximately O(2^m * n), where m = len(quantity) and n = len(freq).

Space Complexity:
- The space complexity is O(m) due to the recursion stack, where m is the length of the `quantity` array.

Topic: Backtracking
"""