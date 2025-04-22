"""
LeetCode Problem #477: Total Hamming Distance

Problem Statement:
The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given an integer array `nums`, return the sum of Hamming distances between all the pairs of the integers in the array.

Example 1:
Input: nums = [4, 14, 2]
Output: 6
Explanation: 
    - Hamming distance between 4 and 14 is 2 (binary: 0100 vs 1110).
    - Hamming distance between 4 and 2 is 2 (binary: 0100 vs 0010).
    - Hamming distance between 14 and 2 is 2 (binary: 1110 vs 0010).
    - Total = 2 + 2 + 2 = 6.

Example 2:
Input: nums = [4, 14, 4]
Output: 4

Constraints:
- 1 <= nums.length <= 10^4
- 0 <= nums[i] <= 10^9
- The answer for the given input will fit in a 32-bit integer.
"""

def totalHammingDistance(nums):
    """
    Calculate the total Hamming distance between all pairs of integers in the array.

    :param nums: List[int] - List of integers
    :return: int - Total Hamming distance
    """
    n = len(nums)
    total_distance = 0

    # Iterate over all 32 bit positions (since nums[i] <= 10^9, which fits in 32 bits)
    for bit in range(32):
        count_ones = 0
        count_zeros = 0

        # Count the number of 1s and 0s at the current bit position
        for num in nums:
            if (num >> bit) & 1:
                count_ones += 1
            else:
                count_zeros += 1

        # The Hamming distance contributed by this bit position is count_ones * count_zeros
        total_distance += count_ones * count_zeros

    return total_distance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 14, 2]
    print(f"Total Hamming Distance for {nums1}: {totalHammingDistance(nums1)}")  # Expected Output: 6

    # Test Case 2
    nums2 = [4, 14, 4]
    print(f"Total Hamming Distance for {nums2}: {totalHammingDistance(nums2)}")  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 2, 3]
    print(f"Total Hamming Distance for {nums3}: {totalHammingDistance(nums3)}")  # Expected Output: 4

    # Test Case 4
    nums4 = [0, 0, 0]
    print(f"Total Hamming Distance for {nums4}: {totalHammingDistance(nums4)}")  # Expected Output: 0

"""
Time Complexity:
- The algorithm iterates over 32 bit positions (constant time).
- For each bit position, it iterates over all `n` elements in the array.
- Thus, the time complexity is O(32 * n) = O(n), where `n` is the length of the input array.

Space Complexity:
- The algorithm uses a constant amount of extra space (variables to store counts and the result).
- Thus, the space complexity is O(1).

Topic: Bit Manipulation
"""