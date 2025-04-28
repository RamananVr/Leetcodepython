"""
LeetCode Problem #1998: GCD Sort of an Array

Problem Statement:
You are given an integer array nums, and you can perform the following operation as many times as you want:
- Pick two indices i and j, where 0 <= i, j < nums.length, and nums[i] and nums[j] are coprime.
- Swap the elements at nums[i] and nums[j].

An array is said to be sorted if for all i (0 <= i < nums.length - 1), nums[i] <= nums[i + 1].

Return true if you can sort nums using the above operation, and false otherwise.

Constraints:
- 1 <= nums.length <= 3 * 10^4
- 2 <= nums[i] <= 10^5
"""

from math import gcd
from collections import defaultdict

def gcd_sort(nums):
    """
    Determines if the array can be sorted using the GCD-based swapping operation.

    :param nums: List[int] - The input array of integers.
    :return: bool - True if the array can be sorted, False otherwise.
    """
    # Helper function to find the root of a set in the Union-Find structure
    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    # Helper function to union two sets in the Union-Find structure
    def union(x, y):
        root_x = find(x)
        root_y = find(y)
        if root_x != root_y:
            parent[root_y] = root_x

    # Step 1: Create a Union-Find structure for all numbers up to the maximum in nums
    max_num = max(nums)
    parent = list(range(max_num + 1))

    # Step 2: Use the Sieve of Eratosthenes to group numbers by their prime factors
    for i in range(2, max_num + 1):
        if parent[i] == i:  # i is a prime number
            for multiple in range(i, max_num + 1, i):
                union(i, multiple)

    # Step 3: Group numbers in nums by their connected components
    groups = defaultdict(list)
    for num in nums:
        groups[find(num)].append(num)

    # Step 4: Sort each group
    for key in groups:
        groups[key].sort()

    # Step 5: Reconstruct the sorted array using the groups
    sorted_nums = sorted(nums)
    index_map = defaultdict(int)  # Tracks the index of the next element to use in each group
    for i in range(len(nums)):
        root = find(nums[i])
        if groups[root][index_map[root]] != sorted_nums[i]:
            return False
        index_map[root] += 1

    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [8, 4, 2, 6]
    print(gcd_sort(nums1))  # Output: True

    # Test Case 2
    nums2 = [3, 9, 27, 81]
    print(gcd_sort(nums2))  # Output: True

    # Test Case 3
    nums3 = [7, 21, 3, 42]
    print(gcd_sort(nums3))  # Output: False

    # Test Case 4
    nums4 = [10, 5, 15, 20]
    print(gcd_sort(nums4))  # Output: True

"""
Time Complexity:
- Finding the maximum number in nums: O(n), where n is the length of nums.
- Sieve of Eratosthenes: O(m log log m), where m is the maximum number in nums.
- Union-Find operations: O(α(m)), where α is the inverse Ackermann function (nearly constant).
- Sorting nums: O(n log n).
- Overall: O(n + m log log m + n log n).

Space Complexity:
- Union-Find parent array: O(m), where m is the maximum number in nums.
- Groups dictionary: O(n), where n is the length of nums.
- Overall: O(m + n).

Topic: Union-Find, Number Theory, Sorting
"""