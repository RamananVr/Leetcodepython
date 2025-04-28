"""
LeetCode Problem #1577: Number of Ways Where Square of Number Is Equal to Product of Two Numbers

Problem Statement:
Given two arrays of integers `nums1` and `nums2`, return the number of triplets (i, j, k) such that:
- 0 <= i < nums1.length, 0 <= j < nums2.length, 0 <= k < nums2.length
- nums1[i]^2 == nums2[j] * nums2[k], where j != k

Similarly, return the number of triplets (i, j, k) such that:
- 0 <= i < nums2.length, 0 <= j < nums1.length, 0 <= k < nums1.length
- nums2[i]^2 == nums1[j] * nums1[k], where j != k

In total, return the sum of these two results.

Constraints:
- 1 <= nums1.length, nums2.length <= 1000
- 1 <= nums1[i], nums2[i] <= 10^5
"""

from collections import Counter

def numTriplets(nums1, nums2):
    def countTriplets(arr1, arr2):
        count = 0
        freq = Counter(arr2)
        for num in arr1:
            target = num * num
            for x in arr2:
                if target % x == 0:  # Check if x divides target
                    y = target // x
                    if y in freq:
                        if x == y:
                            count += freq[x] - 1  # Avoid double-counting
                        else:
                            count += freq[y]
        return count

    return countTriplets(nums1, nums2) + countTriplets(nums2, nums1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [7, 4]
    nums2 = [5, 2, 8, 9]
    print(numTriplets(nums1, nums2))  # Expected Output: 1

    # Test Case 2
    nums1 = [1, 1]
    nums2 = [1, 1, 1]
    print(numTriplets(nums1, nums2))  # Expected Output: 9

    # Test Case 3
    nums1 = [4, 7, 9]
    nums2 = [1, 2, 3, 4]
    print(numTriplets(nums1, nums2))  # Expected Output: 1

"""
Time Complexity Analysis:
- Let n = len(nums1) and m = len(nums2).
- For each element in nums1 (O(n)), we iterate through nums2 (O(m)) and check divisors, which is O(m) in the worst case.
- Similarly, we repeat the process for nums2 and nums1.
- Overall time complexity: O(n * m^2 + m * n^2).

Space Complexity Analysis:
- We use a Counter to store the frequency of elements in nums2 or nums1, which takes O(max(n, m)) space.
- Overall space complexity: O(max(n, m)).

Topic: Arrays, Hash Table
"""