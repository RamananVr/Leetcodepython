"""
LeetCode Question #2616: Minimize the Maximum Difference of Pairs

Problem Statement:
You are given a 0-indexed integer array `nums` and an integer `p`. Find `p` pairs of indices `(i, j)` such that:
- `0 <= i < j < nums.length`
- The maximum difference among all pairs `(i, j)` is minimized.

Also, ensure no index appears in more than one pair.

Return the minimized maximum difference.

Example:
Input: nums = [1, 3, 6, 19, 20], p = 2
Output: 2
Explanation: We can form pairs (1, 2) and (3, 4) with differences 3 and 1 respectively. The maximum difference is 2.

Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= p <= nums.length / 2`
"""

# Solution
def minimizeMax(nums, p):
    def can_form_pairs(max_diff):
        count = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i + 1] - nums[i] <= max_diff:
                count += 1
                i += 2  # Skip the next index since it's part of the pair
            else:
                i += 1
        return count >= p

    nums.sort()
    left, right = 0, nums[-1] - nums[0]
    result = right

    while left <= right:
        mid = (left + right) // 2
        if can_form_pairs(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 6, 19, 20]
    p1 = 2
    print(minimizeMax(nums1, p1))  # Output: 2

    # Test Case 2
    nums2 = [10, 1, 2, 7, 1, 3]
    p2 = 3
    print(minimizeMax(nums2, p2))  # Output: 1

    # Test Case 3
    nums3 = [4, 2, 1, 10, 5]
    p3 = 1
    print(minimizeMax(nums3, p3))  # Output: 1

    # Test Case 4
    nums4 = [1, 1000000000]
    p4 = 0
    print(minimizeMax(nums4, p4))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of `nums`.
- The binary search runs for O(log(max_diff)), where max_diff is the difference between the largest and smallest elements in `nums`.
- The `can_form_pairs` function iterates through the array, taking O(n) time.
- Overall complexity: O(n log n + n log(max_diff)).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from variables.

Topic: Binary Search
"""