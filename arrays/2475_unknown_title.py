"""
LeetCode Problem #2475: Number of Unequal Triplets in Array

Problem Statement:
You are given a 0-indexed array of positive integers `nums`. Find the number of triplets `(i, j, k)` that meet the following conditions:
1. `0 <= i < j < k < nums.length`
2. `nums[i]`, `nums[j]`, and `nums[k]` are pairwise distinct.

In other words, for a triplet `(i, j, k)` to be valid, the following must hold:
- `nums[i] != nums[j]`
- `nums[i] != nums[k]`
- `nums[j] != nums[k]`

Return the total number of valid triplets.

Constraints:
- `3 <= nums.length <= 100`
- `1 <= nums[i] <= 1000`
"""

def unequalTriplets(nums):
    """
    Function to count the number of unequal triplets in the array.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The number of valid triplets.
    """
    n = len(nums)
    count = 0

    # Iterate through all possible triplets
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                # Check if the triplet is pairwise distinct
                if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
                    count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 4, 2, 4, 3]
    print(unequalTriplets(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    print(unequalTriplets(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [1, 2, 3]
    print(unequalTriplets(nums3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 2, 2, 3, 4]
    print(unequalTriplets(nums4))  # Expected Output: 4

"""
Time Complexity Analysis:
- The solution uses three nested loops to iterate through all possible triplets in the array.
- The number of triplets is proportional to the combination formula C(n, 3) = n * (n-1) * (n-2) / 6.
- Therefore, the time complexity is O(n^3), where n is the length of the input array.

Space Complexity Analysis:
- The solution uses a constant amount of extra space, as no additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""