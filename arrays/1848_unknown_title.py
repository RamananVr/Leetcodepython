"""
LeetCode Problem #1848: Minimum Distance to the Target Element

Problem Statement:
Given an integer array `nums` (0-indexed) and two integers `target` and `start`, find the minimum distance between `start` and any index `i` such that `nums[i] == target`. The distance between two indices `i` and `j` is `abs(i - j)`.

Return the minimum distance. If there is no such index, return -1.

Constraints:
1. 1 <= nums.length <= 1000
2. 1 <= nums[i] <= 10^4
3. 0 <= start < nums.length
4. 1 <= target <= 10^4
"""

def getMinDistance(nums, target, start):
    """
    Finds the minimum distance between the start index and any index i such that nums[i] == target.

    :param nums: List[int] - The input array of integers.
    :param target: int - The target value to find in the array.
    :param start: int - The starting index.
    :return: int - The minimum distance to the target element.
    """
    min_distance = float('inf')  # Initialize with a large value
    for i in range(len(nums)):
        if nums[i] == target:
            min_distance = min(min_distance, abs(i - start))
    return min_distance if min_distance != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4, 5]
    target1 = 5
    start1 = 3
    print(getMinDistance(nums1, target1, start1))  # Expected Output: 1

    # Test Case 2
    nums2 = [1]
    target2 = 1
    start2 = 0
    print(getMinDistance(nums2, target2, start2))  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 1, 1, 1, 1]
    target3 = 1
    start3 = 2
    print(getMinDistance(nums3, target3, start3))  # Expected Output: 0

    # Test Case 4
    nums4 = [5, 3, 6, 1, 3]
    target4 = 3
    start4 = 2
    print(getMinDistance(nums4, target4, start4))  # Expected Output: 1

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    target5 = 6
    start5 = 2
    print(getMinDistance(nums5, target5, start5))  # Expected Output: -1

"""
Time Complexity:
- The function iterates through the entire array once, so the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""