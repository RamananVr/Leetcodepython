"""
LeetCode Problem #982: Triples with Bitwise AND Equal To Zero

Problem Statement:
Given an array of integers `nums`, return the number of triplets `(i, j, k)` such that:
1. `0 <= i, j, k < nums.length`
2. `nums[i] & nums[j] & nums[k] == 0`

Here, `&` represents the bitwise AND operation.

Constraints:
- 1 <= nums.length <= 1000
- 0 <= nums[i] < 2^16
"""

from collections import Counter

def countTriplets(nums):
    """
    Function to count the number of triplets (i, j, k) such that nums[i] & nums[j] & nums[k] == 0.

    Args:
    nums (List[int]): List of integers.

    Returns:
    int: Number of valid triplets.
    """
    # Step 1: Precompute all pairwise AND results and their frequencies
    pairwise_and_count = Counter()
    for x in nums:
        for y in nums:
            pairwise_and_count[x & y] += 1

    # Step 2: Count valid triplets
    triplet_count = 0
    for z in nums:
        for pair_and, freq in pairwise_and_count.items():
            if pair_and & z == 0:
                triplet_count += freq

    return triplet_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 3]
    print("Test Case 1 Output:", countTriplets(nums1))  # Expected Output: 12

    # Test Case 2
    nums2 = [0, 0, 0]
    print("Test Case 2 Output:", countTriplets(nums2))  # Expected Output: 27

    # Test Case 3
    nums3 = [1, 2, 4]
    print("Test Case 3 Output:", countTriplets(nums3))  # Expected Output: 0

"""
Time Complexity Analysis:
1. Precomputing pairwise AND results:
   - There are `n` elements in the array, and for each pair (x, y), we compute `x & y`.
   - This takes O(n^2) time.
2. Counting valid triplets:
   - For each element `z` in the array, we iterate over all precomputed pairwise AND results.
   - This takes O(n * m) time, where `m` is the number of unique pairwise AND results.
   - In the worst case, `m` can be as large as `n^2`.

Overall time complexity: O(n^2 + n * m), which simplifies to O(n^3) in the worst case.

Space Complexity Analysis:
1. The `pairwise_and_count` dictionary stores at most `n^2` entries in the worst case.
2. The space complexity is therefore O(n^2).

Overall space complexity: O(n^2).

Topic: Bit Manipulation
"""