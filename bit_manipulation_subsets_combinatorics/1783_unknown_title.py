"""
LeetCode Problem #1783: Grand Total XOR

Problem Statement:
You are given an array nums consisting of positive integers. You are also given an integer k.

A subset of nums is called a k-subset if the XOR of all the elements in the subset is equal to k.

Return the number of k-subsets of nums.

Note:
- A subset is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements.
- Two subsets are different if the indices of the elements chosen are different.

Constraints:
- 1 <= nums.length <= 16
- 1 <= nums[i] <= 100
- 0 <= k <= 100
"""

# Solution
from itertools import combinations

def countKSubsets(nums, k):
    """
    Function to count the number of k-subsets in the given array.

    Args:
    nums (List[int]): The input array of positive integers.
    k (int): The target XOR value.

    Returns:
    int: The number of k-subsets.
    """
    n = len(nums)
    count = 0

    # Iterate over all possible subset sizes
    for subset_size in range(n + 1):
        # Generate all subsets of the current size
        for subset in combinations(nums, subset_size):
            # Check if the XOR of the subset equals k
            if reduce(lambda x, y: x ^ y, subset, 0) == k:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    k1 = 0
    print(countKSubsets(nums1, k1))  # Expected Output: 2

    # Test Case 2
    nums2 = [5, 1, 6]
    k2 = 5
    print(countKSubsets(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    k3 = 4
    print(countKSubsets(nums3, k3))  # Expected Output: 4

    # Test Case 4
    nums4 = [1]
    k4 = 1
    print(countKSubsets(nums4, k4))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The total number of subsets of an array of size n is 2^n.
- For each subset, we compute the XOR of its elements, which takes O(subset_size) time.
- In the worst case, the total time complexity is O(n * 2^n), where n is the size of the input array.

Space Complexity:
- The space complexity is O(n) due to the storage of subsets during the computation.
"""

# Topic: Bit Manipulation, Subsets, Combinatorics