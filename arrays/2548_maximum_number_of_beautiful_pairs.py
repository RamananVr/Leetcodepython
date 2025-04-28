"""
LeetCode Question #2548: Maximum Number of Beautiful Pairs

Problem Statement:
You are given a 0-indexed integer array `nums`. A pair of indices `(i, j)` is called beautiful if:
1. `0 <= i < j < nums.length`
2. The greatest common divisor (GCD) of `nums[i]` and `nums[j]` is equal to 1.

Return the total number of beautiful pairs in the array.

Constraints:
- `1 <= nums.length <= 10^4`
- `1 <= nums[i] <= 10^6`
"""

from math import gcd

def countBeautifulPairs(nums):
    """
    Function to count the number of beautiful pairs in the array.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The total number of beautiful pairs.
    """
    n = len(nums)
    beautiful_pairs = 0

    # Iterate through all pairs (i, j) where i < j
    for i in range(n):
        for j in range(i + 1, n):
            if gcd(nums[i], nums[j]) == 1:
                beautiful_pairs += 1

    return beautiful_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4, 5]
    print(countBeautifulPairs(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [1, 2, 3]
    print(countBeautifulPairs(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [6, 10, 15]
    print(countBeautifulPairs(nums3))  # Expected Output: 0

    # Test Case 4
    nums4 = [7, 11, 13, 17]
    print(countBeautifulPairs(nums4))  # Expected Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function uses a nested loop to iterate through all pairs of indices (i, j) where i < j.
- The total number of pairs is approximately n * (n - 1) / 2, where n is the length of the array.
- For each pair, the gcd function is called, which has a time complexity of O(log(min(a, b))) for two numbers a and b.
- Therefore, the overall time complexity is O(n^2 * log(max(nums[i]))), where max(nums[i]) is the largest number in the array.

Space Complexity:
- The space complexity is O(1) since no additional data structures are used, and the gcd function operates in constant space.

Topic: Arrays
"""