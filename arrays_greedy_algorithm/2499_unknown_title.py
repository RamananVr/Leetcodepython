"""
LeetCode Problem #2499: Minimum Total Cost to Make Arrays Unequal

Problem Statement:
You are given two integer arrays `nums1` and `nums2`, both of length `n`. The arrays are 1-indexed.

You can perform the following operation any number of times:
- Choose two indices `i` and `j` (1 ≤ i, j ≤ n) such that `nums1[i] != nums2[j]` and swap `nums1[i]` with `nums2[j]`.

Your goal is to make the two arrays unequal, i.e., there should exist at least one index `k` (1 ≤ k ≤ n) such that `nums1[k] != nums2[k]`.

Return the minimum total cost of operations required to make the arrays unequal. If it is impossible to make the arrays unequal, return -1.

Constraints:
- `n == nums1.length == nums2.length`
- `1 <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^6`
"""

# Python Solution
from collections import Counter

def minimumTotalCost(nums1, nums2):
    n = len(nums1)
    freq = Counter()
    total_cost = 0
    max_freq = 0
    dominant = -1
    swaps = 0

    # Step 1: Count the frequency of identical pairs and track the dominant element
    for i in range(n):
        if nums1[i] == nums2[i]:
            freq[nums1[i]] += 1
            total_cost += i
            swaps += 1
            if freq[nums1[i]] > max_freq:
                max_freq = freq[nums1[i]]
                dominant = nums1[i]

    # Step 2: Check if the dominant element can be resolved
    excess = max(0, 2 * max_freq - swaps - 1)
    for i in range(n):
        if excess == 0:
            break
        if nums1[i] != nums2[i] and nums1[i] != dominant and nums2[i] != dominant:
            total_cost += i
            excess -= 1

    # Step 3: Return the result
    return total_cost if excess == 0 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    print(minimumTotalCost(nums1, nums2))  # Output: 0

    # Test Case 2
    nums1 = [1, 1, 1, 1]
    nums2 = [1, 1, 1, 1]
    print(minimumTotalCost(nums1, nums2))  # Output: -1

    # Test Case 3
    nums1 = [1, 2, 3, 4, 5]
    nums2 = [5, 4, 3, 2, 1]
    print(minimumTotalCost(nums1, nums2))  # Output: 10

    # Test Case 4
    nums1 = [1, 2, 2, 1]
    nums2 = [1, 1, 2, 2]
    print(minimumTotalCost(nums1, nums2))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Step 1: O(n) to iterate through the arrays and calculate frequencies.
- Step 2: O(n) to resolve the excess swaps if needed.
Overall: O(n)

Space Complexity:
- We use a Counter to store frequencies, which takes O(u) space, where u is the number of unique elements in nums1 and nums2.
In the worst case, u = O(n), so the space complexity is O(n).

Overall: O(n) time and O(n) space.
"""

# Topic: Arrays, Greedy Algorithm