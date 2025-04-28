"""
LeetCode Problem #2587: Rearrange Array to Maximize Prefix Score

Problem Statement:
You are given a 0-indexed integer array `nums`. You can rearrange the elements of `nums` to any order (including the given order). Let `prefix` be the array containing the prefix sums of `nums` after rearranging it. In other words, `prefix[i]` is the sum of the elements from `nums[0]` to `nums[i]` in the rearranged array.

The score of `nums` is the number of positive integers in the array `prefix`.

Return the maximum score you can achieve.

Example:
Input: nums = [2, -1, 0, 1, -3, 3, -3]
Output: 6
Explanation: We can rearrange nums to [2, 3, 1, -1, 0, -3, -3].
The prefix sums are [2, 5, 6, 5, 5, 2, -1]. The score is 6 since there are 6 positive integers.

Constraints:
- 1 <= nums.length <= 10^5
- -10^6 <= nums[i] <= 10^6
"""

# Python Solution
def maxScore(nums):
    """
    Rearranges the array to maximize the prefix score.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum score (number of positive prefix sums).
    """
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Calculate prefix sums and count positive ones
    prefix_sum = 0
    score = 0
    for num in nums:
        prefix_sum += num
        if prefix_sum > 0:
            score += 1
        else:
            break  # No need to continue if prefix sum becomes non-positive
    
    return score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, -1, 0, 1, -3, 3, -3]
    print(maxScore(nums1))  # Output: 6

    # Test Case 2
    nums2 = [-1, -2, -3, -4]
    print(maxScore(nums2))  # Output: 0

    # Test Case 3
    nums3 = [5, 3, -2, -1, 0, 4]
    print(maxScore(nums3))  # Output: 5

    # Test Case 4
    nums4 = [1]
    print(maxScore(nums4))  # Output: 1

    # Test Case 5
    nums5 = [0, 0, 0]
    print(maxScore(nums5))  # Output: 0

"""
Time Complexity Analysis:
1. Sorting the array takes O(n log n), where n is the length of the array.
2. Calculating the prefix sums and counting positive ones takes O(n).
Overall, the time complexity is O(n log n).

Space Complexity Analysis:
1. The sorting operation is in-place, so it uses O(1) additional space.
2. The prefix sum and score variables use O(1) space.
Overall, the space complexity is O(1).

Topic: Arrays, Greedy
"""