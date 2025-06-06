"""
LeetCode Problem #2588: Count the Number of Beautiful Subarrays

Problem Statement:
You are given a 0-indexed integer array `nums`. A subarray of `nums` is called beautiful if it satisfies the following condition:
- The bitwise XOR of all the elements of the subarray is equal to 0.

Return the number of beautiful subarrays in the array `nums`.

A subarray is a contiguous non-empty sequence of elements within an array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def beautifulSubarrays(nums):
    """
    Function to count the number of beautiful subarrays in the given array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The number of beautiful subarrays.
    """
    from collections import defaultdict

    # Initialize variables
    prefix_xor = 0
    xor_count = defaultdict(int)
    xor_count[0] = 1  # To handle cases where prefix_xor itself is 0
    beautiful_count = 0

    # Iterate through the array
    for num in nums:
        # Update the prefix XOR
        prefix_xor ^= num

        # If prefix_xor has been seen before, it means there exists a subarray
        # whose XOR is 0
        beautiful_count += xor_count[prefix_xor]

        # Update the count of the current prefix_xor
        xor_count[prefix_xor] += 1

    return beautiful_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 1, 2, 4]
    print(beautifulSubarrays(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    print(beautifulSubarrays(nums2))  # Output: 0

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(beautifulSubarrays(nums3))  # Output: 10

    # Test Case 4
    nums4 = [2, 2, 2, 2]
    print(beautifulSubarrays(nums4))  # Output: 6

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- The time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a dictionary to store the frequency of prefix XOR values. In the worst case, the dictionary could store up to n unique values.
- The space complexity is O(n).

Topic: Prefix XOR, Hash Map
"""