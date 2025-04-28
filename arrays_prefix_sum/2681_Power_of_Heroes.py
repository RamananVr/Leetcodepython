"""
LeetCode Problem #2681: Power of Heroes

Problem Statement:
You are given an array of positive integers `nums` representing the power of heroes. 
The power of a group of heroes is defined as the product of the sum of their powers 
and the maximum power among them.

More formally, if the group contains heroes with powers `x1, x2, ..., xk`, then the 
power of this group is `(x1 + x2 + ... + xk) * max(x1, x2, ..., xk)`.

Return the sum of the power of all non-empty groups of heroes possible modulo `10^9 + 7`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

# Solution
def sumOfPower(nums):
    """
    Calculate the sum of the power of all non-empty groups of heroes modulo 10^9 + 7.

    :param nums: List[int] - Array of positive integers representing the power of heroes.
    :return: int - Sum of the power of all non-empty groups modulo 10^9 + 7.
    """
    MOD = 10**9 + 7
    nums.sort()
    result = 0
    prefix_sum = 0

    for num in nums:
        # Add the current number to the prefix sum
        prefix_sum += num
        prefix_sum %= MOD

        # Calculate the power of the current group
        result += num * num * prefix_sum
        result %= MOD

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 1, 4]
    print(sumOfPower(nums1))  # Expected Output: 141

    # Test Case 2
    nums2 = [1, 2, 3]
    print(sumOfPower(nums2))  # Expected Output: 50

    # Test Case 3
    nums3 = [5]
    print(sumOfPower(nums3))  # Expected Output: 125

    # Test Case 4
    nums4 = [1, 1, 1]
    print(sumOfPower(nums4))  # Expected Output: 15

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- The loop iterates through the array once, performing constant-time operations for each element. 
  This takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The algorithm uses O(1) additional space for variables like `prefix_sum` and `result`.
- Sorting the array may require O(n) space depending on the sorting algorithm used.
- Overall space complexity: O(n).

Topic: Arrays, Prefix Sum
"""