"""
LeetCode Problem #16: 3Sum Closest

Problem Statement:
Given an integer array `nums` of length `n` and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers.

You may assume that each input would have exactly one solution.

Constraints:
- 3 <= nums.length <= 500
- -1000 <= nums[i] <= 1000
- -10^4 <= target <= 10^4
"""

def threeSumClosest(nums: list[int], target: int) -> int:
    """
    Finds the sum of three integers in nums such that the sum is closest to the target.

    Args:
    nums (list[int]): The input array of integers.
    target (int): The target integer.

    Returns:
    int: The sum of the three integers closest to the target.
    """
    nums.sort()  # Sort the array to use the two-pointer technique
    closest_sum = float('inf')  # Initialize the closest sum to infinity

    for i in range(len(nums) - 2):
        left, right = i + 1, len(nums) - 1  # Two pointers
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            # Update the closest sum if the current sum is closer to the target
            if abs(current_sum - target) < abs(closest_sum - target):
                closest_sum = current_sum

            # Move pointers based on the comparison with the target
            if current_sum < target:
                left += 1
            elif current_sum > target:
                right -= 1
            else:
                # If the current sum equals the target, it's the closest possible
                return current_sum

    return closest_sum


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-1, 2, 1, -4]
    target1 = 1
    print(threeSumClosest(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = [0, 0, 0]
    target2 = 1
    print(threeSumClosest(nums2, target2))  # Output: 0

    # Test Case 3
    nums3 = [1, 1, 1, 0]
    target3 = -100
    print(threeSumClosest(nums3, target3))  # Output: 2

    # Test Case 4
    nums4 = [1, 2, 5, 10, 11]
    target4 = 12
    print(threeSumClosest(nums4, target4))  # Output: 13


"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- The two-pointer traversal for each element takes O(n) in the worst case.
- Since we iterate through the array (n elements), the overall time complexity is O(n^2).

Space Complexity Analysis:
- The algorithm uses O(1) additional space, as it operates in-place after sorting the array.

Topic: Arrays, Two Pointers
"""