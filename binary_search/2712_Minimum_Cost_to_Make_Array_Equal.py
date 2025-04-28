"""
LeetCode Problem #2712: Minimum Cost to Make Array Equal

Problem Statement:
You are given two arrays `nums` and `cost` consisting of positive integers of the same length.

You can perform the following operation any number of times:
- Increase or decrease any element of the array `nums` by 1. The cost of performing this operation on the ith element is `cost[i]`.

Return the minimum cost required to make all the elements of the array `nums` equal.

Example:
Input: nums = [1, 2, 3], cost = [10, 100, 1000]
Output: 120

Constraints:
- 1 <= nums.length == cost.length <= 10^5
- 1 <= nums[i], cost[i] <= 10^6
"""

# Solution
def minCost(nums, cost):
    """
    Calculate the minimum cost to make all elements in nums equal.

    Args:
    nums (List[int]): The array of numbers.
    cost (List[int]): The array of costs associated with changing each number.

    Returns:
    int: The minimum cost to make all elements in nums equal.
    """
    # Helper function to calculate the total cost to make all elements equal to target
    def calculate_cost(target):
        return sum(abs(num - target) * c for num, c in zip(nums, cost))
    
    # Binary search to find the optimal target value
    left, right = min(nums), max(nums)
    while left < right:
        mid = (left + right) // 2
        cost_mid = calculate_cost(mid)
        cost_next = calculate_cost(mid + 1)
        
        if cost_mid <= cost_next:
            right = mid
        else:
            left = mid + 1
    
    return calculate_cost(left)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    cost1 = [10, 100, 1000]
    print(minCost(nums1, cost1))  # Output: 120

    # Test Case 2
    nums2 = [1, 1, 1]
    cost2 = [1, 1, 1]
    print(minCost(nums2, cost2))  # Output: 0

    # Test Case 3
    nums3 = [10, 20, 30]
    cost3 = [5, 10, 15]
    print(minCost(nums3, cost3))  # Output: 150

    # Test Case 4
    nums4 = [5, 5, 5, 5]
    cost4 = [1, 2, 3, 4]
    print(minCost(nums4, cost4))  # Output: 0

    # Test Case 5
    nums5 = [1, 100]
    cost5 = [1, 100]
    print(minCost(nums5, cost5))  # Output: 99

# Time and Space Complexity Analysis
"""
Time Complexity:
- The binary search runs in O(log(max(nums) - min(nums))) iterations.
- For each iteration, we calculate the cost using a loop over nums and cost, which takes O(n) time.
- Therefore, the overall time complexity is O(n * log(max(nums) - min(nums))).

Space Complexity:
- The space complexity is O(1) since we are only using a few variables for calculations and no additional data structures.

Topic: Binary Search
"""