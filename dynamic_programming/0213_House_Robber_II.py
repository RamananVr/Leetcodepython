"""
LeetCode Problem #213: House Robber II

Problem Statement:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. 
All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. 
Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 1000
"""

def rob(nums):
    """
    Function to calculate the maximum amount of money that can be robbed without alerting the police.
    """
    def rob_linear(houses):
        """
        Helper function to solve the House Robber problem for a linear street of houses.
        """
        prev, curr = 0, 0
        for money in houses:
            prev, curr = curr, max(curr, prev + money)
        return curr

    n = len(nums)
    if n == 1:
        return nums[0]
    # Rob houses excluding the first or excluding the last
    return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 2]
    print(rob(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 2, 3, 1]
    print(rob(nums2))  # Output: 4

    # Test Case 3
    nums3 = [0]
    print(rob(nums3))  # Output: 0

    # Test Case 4
    nums4 = [5, 1, 1, 5]
    print(rob(nums4))  # Output: 10

    # Test Case 5
    nums5 = [200, 3, 140, 20, 10]
    print(rob(nums5))  # Output: 340

"""
Time Complexity Analysis:
- The helper function `rob_linear` iterates through the list of houses once, which takes O(n) time.
- Since we call `rob_linear` twice (once for nums[:-1] and once for nums[1:]), the overall time complexity is O(n).

Space Complexity Analysis:
- The solution uses O(1) additional space since it only uses a few variables to store intermediate results.

Topic: Dynamic Programming
"""