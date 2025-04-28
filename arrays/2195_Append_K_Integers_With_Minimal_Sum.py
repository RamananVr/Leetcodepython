"""
LeetCode Problem #2195: Append K Integers With Minimal Sum

Problem Statement:
You are given an integer array `nums` and an integer `k`. Append `k` unique positive integers that do not exist in `nums` to `nums` such that the resulting sum is minimized. Return the sum of the `k` integers added to `nums`.

Example:
Input: nums = [1,4,25,10,25], k = 2
Output: 5
Explanation: The two integers added can be 2 and 3. The resulting sum is 2 + 3 = 5.

Input: nums = [5,6], k = 6
Output: 25
Explanation: The six integers added can be 1, 2, 3, 4, 7, and 8. The resulting sum is 1 + 2 + 3 + 4 + 7 + 8 = 25.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i], k <= 10^9
"""

# Python Solution
def minimalKSum(nums, k):
    """
    Calculate the minimal sum of k unique positive integers not in nums.

    :param nums: List[int] - The input array of integers.
    :param k: int - The number of integers to append.
    :return: int - The minimal sum of the k integers added.
    """
    nums = sorted(set(nums))  # Remove duplicates and sort the array
    result = 0
    current = 1

    for num in nums:
        if current >= num:
            continue
        count = min(k, num - current)
        result += count * (current + current + count - 1) // 2
        k -= count
        current = num + 1
        if k == 0:
            return result

    # If k integers are still needed, append the remaining integers after the largest in nums
    if k > 0:
        result += k * (current + current + k - 1) // 2

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 4, 25, 10, 25]
    k1 = 2
    print(minimalKSum(nums1, k1))  # Expected Output: 5

    # Test Case 2
    nums2 = [5, 6]
    k2 = 6
    print(minimalKSum(nums2, k2))  # Expected Output: 25

    # Test Case 3
    nums3 = [2, 3, 4]
    k3 = 5
    print(minimalKSum(nums3, k3))  # Expected Output: 15

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    print(minimalKSum(nums4, k4))  # Expected Output: 18

    # Test Case 5
    nums5 = []
    k5 = 4
    print(minimalKSum(nums5, k5))  # Expected Output: 10

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array and removing duplicates takes O(n log n), where n is the length of nums.
- Iterating through the sorted array and calculating the sum takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space complexity is O(n) due to the storage of the sorted set of nums.
- Overall space complexity: O(n).

Topic: Arrays
"""