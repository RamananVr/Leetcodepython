"""
LeetCode Problem #525: Contiguous Array

Problem Statement:
Given a binary array `nums`, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

Example 1:
Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a contiguous subarray with an equal number of 0 and 1.

Constraints:
- 1 <= nums.length <= 10^5
- nums[i] is either 0 or 1.
"""

def findMaxLength(nums):
    """
    Function to find the maximum length of a contiguous subarray with an equal number of 0 and 1.

    Args:
    nums (List[int]): A binary array.

    Returns:
    int: The maximum length of the subarray.
    """
    # Initialize a dictionary to store the first occurrence of a cumulative sum
    prefix_sum_map = {0: -1}
    max_length = 0
    cumulative_sum = 0

    for i, num in enumerate(nums):
        # Treat 0 as -1 to balance the sum
        cumulative_sum += 1 if num == 1 else -1

        if cumulative_sum in prefix_sum_map:
            # If the cumulative sum has been seen before, calculate the subarray length
            max_length = max(max_length, i - prefix_sum_map[cumulative_sum])
        else:
            # Store the first occurrence of this cumulative sum
            prefix_sum_map[cumulative_sum] = i

    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1]
    print(f"Test Case 1: {findMaxLength(nums1)}")  # Expected Output: 2

    # Test Case 2
    nums2 = [0, 1, 0]
    print(f"Test Case 2: {findMaxLength(nums2)}")  # Expected Output: 2

    # Test Case 3
    nums3 = [0, 0, 1, 0, 1, 1, 0]
    print(f"Test Case 3: {findMaxLength(nums3)}")  # Expected Output: 6

    # Test Case 4
    nums4 = [1, 1, 1, 0, 0, 0, 1, 0]
    print(f"Test Case 4: {findMaxLength(nums4)}")  # Expected Output: 8

    # Test Case 5
    nums5 = [0, 0, 0, 1, 1, 1]
    print(f"Test Case 5: {findMaxLength(nums5)}")  # Expected Output: 6

"""
Time Complexity:
- O(n): We iterate through the array once, performing O(1) operations for each element.

Space Complexity:
- O(n): In the worst case, we store up to n unique cumulative sums in the dictionary.

Topic: Arrays, Hash Table, Prefix Sum
"""