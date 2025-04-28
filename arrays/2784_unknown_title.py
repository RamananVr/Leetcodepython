"""
LeetCode Problem #2784: Check if Array is Good

Problem Statement:
You are given an integer array `nums`. We consider an array good if the following conditions are satisfied:
1. The array contains exactly `n + 1` elements, where `n` is the maximum element in the array.
2. The array contains all integers from `1` to `n` at least once.
3. The maximum element `n` appears exactly twice in the array.

Return `True` if the array is good, otherwise return `False`.

Example 1:
Input: nums = [2, 1, 3, 3]
Output: True
Explanation: The array contains all integers from 1 to 3, and the maximum element 3 appears exactly twice.

Example 2:
Input: nums = [1, 3, 3, 2, 4]
Output: False
Explanation: The array does not contain all integers from 1 to 4.

Example 3:
Input: nums = [1, 1]
Output: False
Explanation: The maximum element 1 appears more than twice.

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

def isGood(nums):
    """
    Function to check if the given array is good.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    bool: True if the array is good, False otherwise.
    """
    # Step 1: Find the maximum element in the array
    n = max(nums)
    
    # Step 2: Check if the array contains exactly n + 1 elements
    if len(nums) != n + 1:
        return False
    
    # Step 3: Count the occurrences of each number in the array
    from collections import Counter
    count = Counter(nums)
    
    # Step 4: Check if all integers from 1 to n are present exactly once
    # and the maximum element n appears exactly twice
    for i in range(1, n):
        if count[i] != 1:
            return False
    if count[n] != 2:
        return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3, 3]
    print(isGood(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 3, 3, 2, 4]
    print(isGood(nums2))  # Output: False

    # Test Case 3
    nums3 = [1, 1]
    print(isGood(nums3))  # Output: False

    # Test Case 4
    nums4 = [1, 2, 2]
    print(isGood(nums4))  # Output: True

    # Test Case 5
    nums5 = [1, 2, 3, 4, 4]
    print(isGood(nums5))  # Output: True

"""
Time Complexity Analysis:
- Finding the maximum element in the array takes O(n), where n is the length of the array.
- Counting the occurrences of each number using Counter takes O(n).
- Checking the conditions for all integers from 1 to n takes O(n).
Overall, the time complexity is O(n).

Space Complexity Analysis:
- The Counter object uses O(n) space to store the frequency of each element in the array.
Overall, the space complexity is O(n).

Topic: Arrays
"""