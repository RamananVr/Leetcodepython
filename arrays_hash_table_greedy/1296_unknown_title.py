"""
LeetCode Problem #1296: Divide Array in Sets of K Consecutive Numbers

Problem Statement:
Given an array of integers `nums` and a positive integer `k`, find whether it is possible to divide this array into sets of `k` consecutive numbers.

Return `true` if it is possible. Otherwise, return `false`.

Example 1:
Input: nums = [1,2,3,3,4,4,5,6], k = 4
Output: true
Explanation: Array can be divided into [1,2,3,4] and [3,4,5,6].

Example 2:
Input: nums = [3,3,2,2,1,1], k = 3
Output: true
Explanation: Array can be divided into [1,2,3] and [1,2,3].

Example 3:
Input: nums = [1,2,3,4], k = 3
Output: false
Explanation: Each set must be exactly 3 consecutive numbers.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length

Note: The frequency of each number in the array must allow for the creation of sets of `k` consecutive numbers.

Follow-up: Could you solve it in O(n log n) time complexity?
"""

from collections import Counter

def isPossibleDivide(nums, k):
    """
    Determines if the array can be divided into sets of k consecutive numbers.

    :param nums: List[int] - The input array of integers.
    :param k: int - The size of each set of consecutive numbers.
    :return: bool - True if the array can be divided into sets of k consecutive numbers, False otherwise.
    """
    if len(nums) % k != 0:
        return False  # If the total number of elements is not divisible by k, return False.

    # Count the frequency of each number in the array.
    num_count = Counter(nums)

    # Sort the keys of the counter to process numbers in ascending order.
    for num in sorted(num_count):
        if num_count[num] > 0:  # If there are occurrences of the current number.
            count = num_count[num]
            # Try to form a group of k consecutive numbers starting from `num`.
            for i in range(num, num + k):
                if num_count[i] < count:
                    return False  # Not enough numbers to form a group.
                num_count[i] -= count  # Reduce the count for each number in the group.

    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 3, 4, 4, 5, 6]
    k1 = 4
    print(isPossibleDivide(nums1, k1))  # Output: True

    # Test Case 2
    nums2 = [3, 3, 2, 2, 1, 1]
    k2 = 3
    print(isPossibleDivide(nums2, k2))  # Output: True

    # Test Case 3
    nums3 = [1, 2, 3, 4]
    k3 = 3
    print(isPossibleDivide(nums3, k3))  # Output: False

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5, 6, 7, 8]
    k4 = 4
    print(isPossibleDivide(nums4, k4))  # Output: True

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    k5 = 2
    print(isPossibleDivide(nums5, k5))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the sorted keys and processing each number takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The Counter object stores the frequency of each number, which takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Arrays, Hash Table, Greedy
"""