"""
LeetCode Problem #1313: Decompress Run-Length Encoded List

Problem Statement:
We are given a list `nums` of integers representing a run-length encoded list. 
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0). 
For each such pair, there are `freq` occurrences of `val` in the decompressed list.

Return the decompressed list.

Example 1:
Input: nums = [1,2,3,4]
Output: [2,4,4,4]

Explanation:
The pairs are [1,2] and [3,4]. 
This means the output should be [2] followed by [4,4,4].

Example 2:
Input: nums = [1,1,2,3]
Output: [1,3,3]

Constraints:
- 2 <= nums.length <= 100
- nums.length % 2 == 0
- 1 <= nums[i] <= 100
"""

# Clean, Correct Python Solution
def decompressRLElist(nums):
    """
    Decompresses a run-length encoded list.

    Args:
    nums (List[int]): The input list of integers.

    Returns:
    List[int]: The decompressed list.
    """
    decompressed = []
    for i in range(0, len(nums), 2):
        freq = nums[i]
        val = nums[i + 1]
        decompressed.extend([val] * freq)
    return decompressed

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(decompressRLElist(nums1))  # Output: [2, 4, 4, 4]

    # Test Case 2
    nums2 = [1, 1, 2, 3]
    print(decompressRLElist(nums2))  # Output: [1, 3, 3]

    # Test Case 3
    nums3 = [5, 10]
    print(decompressRLElist(nums3))  # Output: [10, 10, 10, 10, 10]

    # Test Case 4
    nums4 = [2, 5, 3, 8]
    print(decompressRLElist(nums4))  # Output: [5, 5, 8, 8, 8]

# Time and Space Complexity Analysis
"""
Time Complexity:
The function iterates through the input list `nums` in steps of 2, so the loop runs `len(nums) / 2` times.
For each pair [freq, val], we extend the list with `freq` elements, which takes O(freq) time.
In the worst case, the sum of all frequencies is equal to the total number of elements in the decompressed list.
Thus, the overall time complexity is O(n), where n is the size of the decompressed list.

Space Complexity:
The space complexity is O(n), where n is the size of the decompressed list, as we store the decompressed list in memory.
"""

# Topic: Arrays