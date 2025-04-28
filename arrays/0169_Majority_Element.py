"""
LeetCode Problem #169: Majority Element

Problem Statement:
Given an array `nums` of size `n`, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. 
You may assume that the majority element always exists in the array.

Constraints:
- `n == nums.length`
- `1 <= n <= 5 * 10^4`
- `-10^9 <= nums[i] <= 10^9`

Follow-up:
Could you solve the problem in O(n) time and O(1) space?
"""

# Solution
def majorityElement(nums):
    """
    Finds the majority element in the array using the Boyer-Moore Voting Algorithm.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The majority element.
    """
    # Boyer-Moore Voting Algorithm
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 2, 3]
    print(majorityElement(nums1))  # Output: 3

    # Test Case 2
    nums2 = [2, 2, 1, 1, 1, 2, 2]
    print(majorityElement(nums2))  # Output: 2

    # Test Case 3
    nums3 = [1]
    print(majorityElement(nums3))  # Output: 1

    # Test Case 4
    nums4 = [6, 5, 5]
    print(majorityElement(nums4))  # Output: 5

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables `count` and `candidate`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""