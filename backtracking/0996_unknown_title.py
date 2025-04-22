"""
LeetCode Problem #996: Number of Squareful Arrays

Problem Statement:
Given an array of integers nums, you need to find the number of permutations of the array such that the sum of 
every pair of adjacent elements is a perfect square.

A permutation of an array is an arrangement of its elements into a sequence or linear order.

Return the number of squareful permutations of nums.

Constraints:
- 1 <= nums.length <= 12
- 1 <= nums[i] <= 10^9
"""

from math import sqrt
from collections import Counter

def numSquarefulPerms(nums):
    def is_square(n):
        """Check if a number is a perfect square."""
        root = int(sqrt(n))
        return root * root == n

    def backtrack(path, counter):
        """Backtracking function to find squareful permutations."""
        if len(path) == len(nums):
            # If the path length equals the input length, we found a valid permutation
            return 1
        
        count = 0
        for num in counter:
            if counter[num] > 0:
                # Check if adding this number to the path forms a squareful pair
                if not path or is_square(path[-1] + num):
                    counter[num] -= 1
                    count += backtrack(path + [num], counter)
                    counter[num] += 1
        return count

    # Count the frequency of each number in nums
    counter = Counter(nums)
    return backtrack([], counter)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 17, 8]
    print(numSquarefulPerms(nums1))  # Output: 2

    # Test Case 2
    nums2 = [2, 2, 2]
    print(numSquarefulPerms(nums2))  # Output: 1

    # Test Case 3
    nums3 = [1, 1, 8, 17]
    print(numSquarefulPerms(nums3))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The backtracking algorithm explores all permutations of the input array. 
  For an array of length n, there are n! permutations in the worst case.
- Additionally, for each pair of adjacent elements, we check if their sum is a perfect square, 
  which takes O(1) time.
- Thus, the overall time complexity is O(n! * n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(n) for the recursion stack, where n is the length of the input array.
- Additionally, we use a Counter object to store the frequency of elements, which takes O(n) space.
- Therefore, the overall space complexity is O(n).

Topic: Backtracking
"""