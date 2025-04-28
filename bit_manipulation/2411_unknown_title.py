"""
LeetCode Problem #2411: Smallest Subarrays With Maximum Bitwise OR

Problem Statement:
You are given a 0-indexed array nums of length n consisting of non-negative integers.

For each index i in nums, you need to determine the size of the smallest subarray starting at i 
and ending at j (both inclusive) such that the bitwise OR of all elements in the subarray nums[i...j] 
is equal to the bitwise OR of all elements in nums[i...n-1] (the entire array from index i to the end).

Return an array answer of size n where answer[i] is the length of the smallest subarray starting at i 
and ending at j with the above property.

A subarray is a contiguous non-empty sequence of elements within an array.

Example:
Input: nums = [1,0,2,1,3]
Output: [3,3,2,2,1]

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
"""

def smallestSubarrays(nums):
    """
    Function to compute the smallest subarray lengths for each index such that the bitwise OR
    of the subarray equals the bitwise OR of the entire array from that index onward.

    Args:
    nums (List[int]): The input array of non-negative integers.

    Returns:
    List[int]: An array where each element represents the smallest subarray length for the corresponding index.
    """
    n = len(nums)
    answer = [1] * n
    max_or = 0
    last_seen = [0] * 32  # To track the last seen position of each bit (0 to 31)

    # Compute the maximum OR of the entire array
    for num in nums:
        max_or |= num

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        max_or |= nums[i]
        for bit in range(32):
            if nums[i] & (1 << bit):
                last_seen[bit] = i
        # Calculate the smallest subarray length
        answer[i] = max(1, max(last_seen[bit] - i + 1 for bit in range(32) if last_seen[bit] > 0))

    return answer

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 0, 2, 1, 3]
    print(smallestSubarrays(nums1))  # Output: [3, 3, 2, 2, 1]

    # Test Case 2
    nums2 = [0, 1, 2, 4, 8]
    print(smallestSubarrays(nums2))  # Output: [5, 4, 3, 2, 1]

    # Test Case 3
    nums3 = [5, 1, 3, 4]
    print(smallestSubarrays(nums3))  # Output: [4, 3, 2, 1]

"""
Time Complexity Analysis:
- The algorithm iterates through the array once from right to left, which is O(n).
- For each index, it checks up to 32 bits (constant time), so the overall complexity is O(n).
- Thus, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses an array `last_seen` of size 32 to track the last seen positions of bits, which is O(1) space.
- The output array `answer` requires O(n) space.
- Thus, the space complexity is O(n).

Topic: Bit Manipulation
"""