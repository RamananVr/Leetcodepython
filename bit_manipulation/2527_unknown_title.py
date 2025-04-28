"""
LeetCode Problem #2527: Find Xor-Beauty of Array

Problem Statement:
------------------
You are given an integer array `nums`. The XOR-beauty of the array is defined as the XOR of the XOR of all subsets of the array.

Return the XOR-beauty of the array.

Notes:
- The XOR of an empty subset is defined to be 0.
- A subset of an array is any array that can be obtained by deleting some (possibly zero or all) elements from the array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

def xorBeauty(nums):
    """
    Function to calculate the XOR-beauty of the array.

    Args:
    nums (List[int]): The input array.

    Returns:
    int: The XOR-beauty of the array.
    """
    # The XOR-beauty of the array is simply the XOR of all elements in the array.
    # This is derived from the mathematical properties of XOR and subsets.
    return reduce(lambda x, y: x ^ y, nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4]
    print(xorBeauty(nums1))  # Output: 5

    # Test Case 2
    nums2 = [15, 45, 20, 2, 34, 35, 5, 44, 32, 30]
    print(xorBeauty(nums2))  # Output: 34

    # Test Case 3
    nums3 = [0, 0, 0]
    print(xorBeauty(nums3))  # Output: 0

    # Test Case 4
    nums4 = [1, 2, 3]
    print(xorBeauty(nums4))  # Output: 0

"""
Time Complexity Analysis:
-------------------------
The time complexity of the solution is O(n), where n is the length of the input array `nums`. 
This is because we iterate through the array once to compute the XOR of all elements.

Space Complexity Analysis:
--------------------------
The space complexity of the solution is O(1), as we use a constant amount of extra space.

Topic: Bit Manipulation
"""