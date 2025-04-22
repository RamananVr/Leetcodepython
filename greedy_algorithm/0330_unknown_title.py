"""
LeetCode Problem #330: Patching Array

Problem Statement:
Given a sorted integer array `nums` and an integer `n`, add the minimum number of patches (numbers) to the array such that any number in the range [1, n] inclusive can be formed by the sum of some elements of the array.

Return the minimum number of patches required.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^4
- nums is sorted in ascending order.
- 1 <= n <= 2^31 - 1
"""

def minPatches(nums, n):
    """
    Function to calculate the minimum number of patches required to cover the range [1, n].
    
    Args:
    nums (List[int]): A sorted list of integers.
    n (int): The target range [1, n].
    
    Returns:
    int: The minimum number of patches required.
    """
    patches = 0
    miss = 1
    i = 0

    while miss <= n:
        if i < len(nums) and nums[i] <= miss:
            miss += nums[i]
            i += 1
        else:
            miss += miss
            patches += 1

    return patches

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3]
    n1 = 6
    print(f"Test Case 1: {minPatches(nums1, n1)}")  # Expected Output: 1

    # Test Case 2
    nums2 = [1, 5, 10]
    n2 = 20
    print(f"Test Case 2: {minPatches(nums2, n2)}")  # Expected Output: 2

    # Test Case 3
    nums3 = [1, 2, 2]
    n3 = 5
    print(f"Test Case 3: {minPatches(nums3, n3)}")  # Expected Output: 0

    # Test Case 4
    nums4 = []
    n4 = 7
    print(f"Test Case 4: {minPatches(nums4, n4)}")  # Expected Output: 3

    # Test Case 5
    nums5 = [1, 2, 31, 33]
    n5 = 2147483647
    print(f"Test Case 5: {minPatches(nums5, n5)}")  # Expected Output: 28

"""
Time Complexity:
- The algorithm iterates through the array `nums` and also potentially adds patches to cover the range [1, n].
- In the worst case, the number of patches added is proportional to log(n), as each patch approximately doubles the range of numbers that can be formed.
- Therefore, the time complexity is O(len(nums) + log(n)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy Algorithm
"""