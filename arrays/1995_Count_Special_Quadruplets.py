"""
LeetCode Problem #1995: Count Special Quadruplets

Problem Statement:
Given a 0-indexed integer array `nums` of length `n`, return the number of distinct quadruplets 
(a, b, c, d) such that:
    - 0 <= a < b < c < d < n
    - nums[a] + nums[b] + nums[c] == nums[d]

Constraints:
1. 4 <= nums.length <= 50
2. 1 <= nums[i] <= 100
"""

def countQuadruplets(nums):
    """
    Function to count the number of special quadruplets in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The count of special quadruplets.
    """
    n = len(nums)
    count = 0

    # Iterate through all possible quadruplets
    for a in range(n - 3):
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                for d in range(c + 1, n):
                    if nums[a] + nums[b] + nums[c] == nums[d]:
                        count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 6]
    print(countQuadruplets(nums1))  # Output: 1

    # Test Case 2
    nums2 = [3, 3, 6, 4, 5]
    print(countQuadruplets(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1, 1, 1, 3, 5]
    print(countQuadruplets(nums3))  # Output: 4

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6]
    print(countQuadruplets(nums4))  # Output: 0

"""
Time Complexity:
The solution uses four nested loops to iterate through all possible quadruplets. 
The time complexity is O(n^4), where n is the length of the input array.

Space Complexity:
The solution uses only a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""