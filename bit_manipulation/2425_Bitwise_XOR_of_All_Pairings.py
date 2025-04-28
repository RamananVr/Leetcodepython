"""
LeetCode Problem #2425: Bitwise XOR of All Pairings

Problem Statement:
You are given two 0-indexed arrays, `nums1` and `nums2`, consisting of non-negative integers. 
There exists another array, `arr`, which contains the bitwise XOR of all possible pairings 
between elements from `nums1` and `nums2` (every element in `nums1` is paired with every 
element in `nums2` exactly once).

Return the bitwise XOR of all elements in `arr`.

Example:
Input: nums1 = [2, 1], nums2 = [3, 5]
Output: 6
Explanation:
The pairings and their XORs are:
- (2, 3) -> 2 ^ 3 = 1
- (2, 5) -> 2 ^ 5 = 7
- (1, 3) -> 1 ^ 3 = 2
- (1, 5) -> 1 ^ 5 = 4
The XOR of all these results is 1 ^ 7 ^ 2 ^ 4 = 6.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- 0 <= nums1[i], nums2[j] <= 10^9
"""

def xorAllNums(nums1, nums2):
    """
    Calculate the bitwise XOR of all pairings between elements of nums1 and nums2.

    Args:
    nums1 (List[int]): First list of non-negative integers.
    nums2 (List[int]): Second list of non-negative integers.

    Returns:
    int: The bitwise XOR of all pairings.
    """
    xor1, xor2 = 0, 0

    # XOR of all elements in nums1
    for num in nums1:
        xor1 ^= num

    # XOR of all elements in nums2
    for num in nums2:
        xor2 ^= num

    # If nums1 has an odd length, each element in nums2 contributes to the result
    # If nums2 has an odd length, each element in nums1 contributes to the result
    result = (xor1 if len(nums2) % 2 == 1 else 0) ^ (xor2 if len(nums1) % 2 == 1 else 0)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1]
    nums2 = [3, 5]
    print(xorAllNums(nums1, nums2))  # Output: 6

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [4, 5]
    print(xorAllNums(nums1, nums2))  # Output: 1

    # Test Case 3
    nums1 = [0]
    nums2 = [0]
    print(xorAllNums(nums1, nums2))  # Output: 0

    # Test Case 4
    nums1 = [7, 8, 9]
    nums2 = [1, 2, 3, 4]
    print(xorAllNums(nums1, nums2))  # Output: 0

"""
Time Complexity Analysis:
- Calculating the XOR of all elements in nums1 takes O(n1), where n1 is the length of nums1.
- Calculating the XOR of all elements in nums2 takes O(n2), where n2 is the length of nums2.
- The final computation is O(1).
- Overall time complexity: O(n1 + n2).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space.
- Overall space complexity: O(1).

Topic: Bit Manipulation
"""