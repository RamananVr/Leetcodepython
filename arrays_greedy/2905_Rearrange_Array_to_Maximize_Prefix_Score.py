"""
LeetCode Problem #2905: Rearrange Array to Maximize Prefix Score

Problem Statement:
You are given a 0-indexed integer array `nums`. You can rearrange the elements of `nums` to any order (including the given order). Let `prefix` be the array containing the prefix sums of `nums` after rearranging it. In other words, `prefix[i]` is the sum of the first `i + 1` elements of `nums` after rearranging it.

The "prefix score" of `nums` is the number of positive integers in the array `prefix`.

Return the maximum prefix score that can be achieved after rearranging `nums`.

Constraints:
- 1 <= nums.length <= 10^5
- -10^6 <= nums[i] <= 10^6
"""

def max_prefix_score(nums):
    """
    Function to calculate the maximum prefix score by rearranging the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The maximum prefix score.
    """
    # Sort the array in descending order
    nums.sort(reverse=True)
    
    # Initialize prefix sum and count of positive prefix sums
    prefix_sum = 0
    positive_count = 0
    
    # Iterate through the sorted array and calculate prefix sums
    for num in nums:
        prefix_sum += num
        if prefix_sum > 0:
            positive_count += 1
        else:
            break  # Stop as soon as prefix sum becomes non-positive
    
    return positive_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, -1, 0, 1, -3, 3]
    print(max_prefix_score(nums1))  # Expected Output: 4

    # Test Case 2
    nums2 = [-1, -2, -3, -4]
    print(max_prefix_score(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [5, 3, -2, -1, 4]
    print(max_prefix_score(nums3))  # Expected Output: 5

    # Test Case 4
    nums4 = [0, 0, 0, 0]
    print(max_prefix_score(nums4))  # Expected Output: 0

    # Test Case 5
    nums5 = [10, -5, -2, 7, -1]
    print(max_prefix_score(nums5))  # Expected Output: 4

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array to calculate prefix sums takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so no additional space is used apart from the input array.
- Overall space complexity: O(1) (excluding input storage).

Topic: Arrays, Greedy
"""