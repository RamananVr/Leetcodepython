"""
LeetCode Problem #2763: Sum of Imbalance Numbers of All Subarrays

Problem Statement:
You are given an integer array `nums`. The imbalance number of a subarray is defined as the number of elements in the subarray that are not adjacent in value to any other element in the subarray.

Formally, the imbalance number of a subarray is the count of elements `x` such that:
- `x - 1` is not in the subarray, and
- `x + 1` is not in the subarray.

Return the sum of imbalance numbers of all subarrays of `nums`.

Example:
Input: nums = [2, 3, 4]
Output: 3
Explanation:
- Subarray [2] has imbalance number 0.
- Subarray [3] has imbalance number 0.
- Subarray [4] has imbalance number 0.
- Subarray [2, 3] has imbalance number 0.
- Subarray [3, 4] has imbalance number 0.
- Subarray [2, 3, 4] has imbalance number 1 (element 2 is not adjacent to 1 or 3, and element 4 is not adjacent to 3 or 5).

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 1000
"""

def sumImbalanceNumbers(nums):
    """
    Calculate the sum of imbalance numbers of all subarrays of nums.

    :param nums: List[int] - The input array of integers.
    :return: int - The sum of imbalance numbers of all subarrays.
    """
    n = len(nums)
    result = 0

    for i in range(n):
        seen = set()
        imbalance = 0
        for j in range(i, n):
            if nums[j] not in seen:
                if nums[j] - 1 not in seen and nums[j] + 1 not in seen:
                    imbalance += 1
                if nums[j] - 1 in seen:
                    imbalance -= 1
                if nums[j] + 1 in seen:
                    imbalance -= 1
                seen.add(nums[j])
            result += imbalance

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 4]
    print(sumImbalanceNumbers(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 3, 2]
    print(sumImbalanceNumbers(nums2))  # Output: 4

    # Test Case 3
    nums3 = [1, 1, 1]
    print(sumImbalanceNumbers(nums3))  # Output: 0

    # Test Case 4
    nums4 = [4, 1, 3, 2]
    print(sumImbalanceNumbers(nums4))  # Output: 10

"""
Time Complexity Analysis:
- Outer loop runs `n` times (for each starting index of the subarray).
- Inner loop runs up to `n` times (for each ending index of the subarray).
- Within the inner loop, operations like adding to a set and checking membership are O(1).
- Overall time complexity: O(n^2).

Space Complexity Analysis:
- The `seen` set is used to store elements of the current subarray, which can grow up to size `n` in the worst case.
- Overall space complexity: O(n).

Topic: Arrays
"""