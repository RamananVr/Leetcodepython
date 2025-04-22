"""
LeetCode Problem #229: Majority Element II

Problem Statement:
Given an integer array `nums`, find all elements that appear more than ⌊ n/3 ⌋ times. 
You must solve the problem in O(n) time and O(1) space.

Constraints:
- 1 <= nums.length <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9

Follow-up:
Could you solve the problem in linear time and in O(1) space?
"""

def majorityElement(nums):
    """
    Finds all elements in the array that appear more than ⌊ n/3 ⌋ times.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    List[int]: A list of integers that appear more than ⌊ n/3 ⌋ times.
    """
    if not nums:
        return []

    # Boyer-Moore Voting Algorithm
    candidate1, candidate2, count1, count2 = None, None, 0, 0

    # First pass: Find potential candidates
    for num in nums:
        if candidate1 == num:
            count1 += 1
        elif candidate2 == num:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Second pass: Verify the candidates
    count1, count2 = 0, 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    result = []
    n = len(nums)
    if count1 > n // 3:
        result.append(candidate1)
    if count2 > n // 3:
        result.append(candidate2)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 3]
    print(majorityElement(nums1))  # Output: [3]

    # Test Case 2
    nums2 = [1]
    print(majorityElement(nums2))  # Output: [1]

    # Test Case 3
    nums3 = [1, 2]
    print(majorityElement(nums3))  # Output: [1, 2]

    # Test Case 4
    nums4 = [1, 1, 1, 3, 3, 2, 2, 2]
    print(majorityElement(nums4))  # Output: [1, 2]

    # Test Case 5
    nums5 = [2, 2, 9, 3, 9, 3, 9, 3, 9, 3, 9, 3, 9]
    print(majorityElement(nums5))  # Output: [9, 3]

"""
Time Complexity Analysis:
- The algorithm consists of two passes over the input array:
  1. The first pass identifies the two potential majority candidates.
  2. The second pass verifies the counts of these candidates.
  Both passes are O(n), where n is the length of the input array.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space to store the two candidates and their counts.
- Overall space complexity: O(1).

Topic: Arrays
"""