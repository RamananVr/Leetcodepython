"""
LeetCode Problem #2552: Count Increasing Quadruplets

Problem Statement:
You are given a 0-indexed integer array `nums` of size `n`. A quadruplet `(i, j, k, l)` is called an increasing quadruplet if:
- 0 <= i < j < k < l < n, and
- nums[i] < nums[k] < nums[j] < nums[l].

Return the total number of increasing quadruplets in `nums`.

Constraints:
- 4 <= nums.length <= 4000
- 1 <= nums[i] <= 10^9
"""

def countIncreasingQuadruplets(nums):
    """
    Function to count the number of increasing quadruplets in the array.

    :param nums: List[int] - The input array of integers.
    :return: int - The total number of increasing quadruplets.
    """
    n = len(nums)
    count = 0

    # Precompute the number of elements less than nums[k] to the left of k
    left_smaller = [0] * n
    for k in range(n):
        for i in range(k):
            if nums[i] < nums[k]:
                left_smaller[k] += 1

    # Precompute the number of elements greater than nums[k] to the right of k
    right_greater = [0] * n
    for k in range(n):
        for l in range(k + 1, n):
            if nums[k] < nums[l]:
                right_greater[k] += 1

    # Count quadruplets using the precomputed arrays
    for j in range(n):
        for k in range(j + 1, n):
            if nums[j] < nums[k]:
                count += left_smaller[j] * right_greater[k]

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 2, 4, 5]
    print("Test Case 1 Output:", countIncreasingQuadruplets(nums1))  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print("Test Case 2 Output:", countIncreasingQuadruplets(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [4, 3, 2, 1]
    print("Test Case 3 Output:", countIncreasingQuadruplets(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [1, 5, 2, 6, 3, 7]
    print("Test Case 4 Output:", countIncreasingQuadruplets(nums4))  # Expected Output: 5

"""
Time Complexity:
- The solution involves two nested loops to compute `left_smaller` and `right_greater`, each taking O(n^2) time.
- The final nested loop to count quadruplets also takes O(n^2) time.
- Overall time complexity: O(n^2 + n^2 + n^2) = O(n^2).

Space Complexity:
- We use two auxiliary arrays `left_smaller` and `right_greater`, each of size n.
- Overall space complexity: O(n).

Topic: Arrays
"""