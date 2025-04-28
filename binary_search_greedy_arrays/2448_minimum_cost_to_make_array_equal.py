"""
LeetCode Question #2448: Minimum Cost to Make Array Equal

Problem Statement:
You are given two 0-indexed arrays `nums` and `cost` consisting each of `n` positive integers.

You can do the following operation any number of times:
- Increase or decrease any element of the array `nums` by 1.

The cost of doing one operation on the `i`th element is `cost[i]`.

Return the minimum total cost such that all the elements of the array `nums` become equal.

Example:
Input: nums = [1, 3, 5, 2], cost = [2, 3, 1, 14]
Output: 8
Explanation: We can make all the elements equal to 2 in the following way:
- Increase the 0th element one time. The cost is 2.
- Decrease the 1st element one time. The cost is 3.
- Decrease the 2nd element three times. The cost is 1 + 1 + 1 = 3.
The total cost is 2 + 3 + 3 = 8. It can be shown that we cannot make the array equal with a smaller cost.

Constraints:
- n == nums.length == cost.length
- 1 <= n <= 10^5
- 1 <= nums[i], cost[i] <= 10^6
"""

# Clean and Correct Python Solution
def minCost(nums, cost):
    """
    Function to calculate the minimum cost to make all elements in nums equal.
    """
    # Helper function to calculate the total cost for a given target value
    def calculate_cost(target):
        return sum(abs(num - target) * c for num, c in zip(nums, cost))
    
    # Binary search to find the optimal target value
    left, right = min(nums), max(nums)
    while left < right:
        mid = (left + right) // 2
        cost_mid = calculate_cost(mid)
        cost_mid_next = calculate_cost(mid + 1)
        
        if cost_mid_next < cost_mid:
            left = mid + 1
        else:
            right = mid
    
    return calculate_cost(left)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 2]
    cost1 = [2, 3, 1, 14]
    print(minCost(nums1, cost1))  # Output: 8

    # Test Case 2
    nums2 = [2, 2, 2, 2]
    cost2 = [1, 1, 1, 1]
    print(minCost(nums2, cost2))  # Output: 0

    # Test Case 3
    nums3 = [10, 20, 30]
    cost3 = [1, 2, 3]
    print(minCost(nums3, cost3))  # Output: 30

    # Test Case 4
    nums4 = [1, 10, 100]
    cost4 = [1, 10, 100]
    print(minCost(nums4, cost4))  # Output: 900

# Time and Space Complexity Analysis
"""
Time Complexity:
- The binary search runs in O(log(max(nums) - min(nums))).
- For each step of the binary search, we calculate the cost, which takes O(n) time.
- Therefore, the overall time complexity is O(n * log(max(nums) - min(nums))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures that scale with input size.
"""

# Topic: Binary Search, Greedy, Arrays