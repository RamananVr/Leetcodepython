"""
LeetCode Question #259: 3Sum Smaller

Problem Statement:
Given an array of `n` integers nums and a target, find the number of index triplets 
`i, j, k` with `0 <= i < j < k < n` that satisfy the condition `nums[i] + nums[j] + nums[k] < target`.

Example:
Input: nums = [-2, 0, 1, 3], target = 2
Output: 2
Explanation: Because there are two triplets which sums are less than 2:
             [-2, 0, 1] = -1
             [-2, 0, 3] = 1

Constraints:
- `n == nums.length`
- `0 <= n <= 3500`
- `-100 <= nums[i] <= 100`
- `-100 <= target <= 100`
"""

def threeSumSmaller(nums, target):
    """
    Function to count the number of triplets in the array such that their sum is less than the target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target sum.
    :return: int - The number of triplets with a sum less than the target.
    """
    nums.sort()  # Sort the array to use the two-pointer technique
    count = 0
    n = len(nums)

    for i in range(n - 2):
        left, right = i + 1, n - 1
        while left < right:
            current_sum = nums[i] + nums[left] + nums[right]
            if current_sum < target:
                # If the sum is less than the target, all triplets between left and right are valid
                count += (right - left)
                left += 1
            else:
                right -= 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-2, 0, 1, 3]
    target1 = 2
    print(threeSumSmaller(nums1, target1))  # Output: 2

    # Test Case 2
    nums2 = []
    target2 = 0
    print(threeSumSmaller(nums2, target2))  # Output: 0

    # Test Case 3
    nums3 = [0]
    target3 = 0
    print(threeSumSmaller(nums3, target3))  # Output: 0

    # Test Case 4
    nums4 = [-1, 1, -1, -1]
    target4 = 0
    print(threeSumSmaller(nums4, target4))  # Output: 4

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    target5 = 10
    print(threeSumSmaller(nums5, target5))  # Output: 4

"""
Time Complexity:
- Sorting the array takes O(n log n).
- The two-pointer traversal for each element takes O(n^2) in the worst case.
- Overall time complexity: O(n^2).

Space Complexity:
- The sorting operation uses O(log n) space due to the sorting algorithm.
- No additional data structures are used, so the space complexity is O(1) (excluding input).

Topic: Arrays, Two Pointers
"""