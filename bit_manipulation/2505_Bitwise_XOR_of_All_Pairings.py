"""
LeetCode Problem #2505: Bitwise XOR of All Pairings

Problem Statement:
You are given two 0-indexed arrays `nums1` and `nums2` of size `n` and `m` respectively. 
Your task is to find the bitwise XOR of all pairings `(nums1[i], nums2[j])` where `0 <= i < n` and `0 <= j < m`.

More formally, the result is equal to:
    nums1[0] XOR nums2[0] XOR nums1[0] XOR nums2[1] XOR ... XOR nums1[n-1] XOR nums2[m-1].

Return the result of the XOR operation.

Constraints:
- `1 <= nums1.length, nums2.length <= 10^5`
- `0 <= nums1[i], nums2[j] <= 10^9`
"""

# Solution
def xorAllNums(nums1, nums2):
    """
    Calculate the XOR of all pairings between nums1 and nums2.

    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.

    Returns:
    int: The XOR of all pairings.
    """
    xor1 = 0
    xor2 = 0

    # XOR all elements in nums1
    for num in nums1:
        xor1 ^= num

    # XOR all elements in nums2
    for num in nums2:
        xor2 ^= num

    # Calculate the result based on the parity of lengths
    result = 0
    if len(nums2) % 2 == 1:  # If nums2 has odd length, include xor1
        result ^= xor1
    if len(nums1) % 2 == 1:  # If nums1 has odd length, include xor2
        result ^= xor2

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3]
    nums2 = [10, 5]
    print(xorAllNums(nums1, nums2))  # Expected Output: 2

    # Test Case 2
    nums1 = [1, 2]
    nums2 = [3, 4]
    print(xorAllNums(nums1, nums2))  # Expected Output: 0

    # Test Case 3
    nums1 = [0]
    nums2 = [0]
    print(xorAllNums(nums1, nums2))  # Expected Output: 0

    # Test Case 4
    nums1 = [5, 7, 9]
    nums2 = [1, 3, 5, 7]
    print(xorAllNums(nums1, nums2))  # Expected Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the XOR of all elements in nums1 takes O(n), where n is the length of nums1.
- Calculating the XOR of all elements in nums2 takes O(m), where m is the length of nums2.
- The final computation based on the parity of lengths is O(1).
- Overall time complexity: O(n + m).

Space Complexity:
- We use a constant amount of extra space for variables (xor1, xor2, result).
- Overall space complexity: O(1).

Topic: Bit Manipulation
"""