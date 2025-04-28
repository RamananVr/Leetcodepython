"""
LeetCode Problem #1480: Running Sum of 1d Array

Problem Statement:
Given an array `nums`, return a running sum of the array. 
The running sum of an array is defined as `runningSum[i] = sum(nums[0]...nums[i])`.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
- 1 <= nums.length <= 1000
- -10^6 <= nums[i] <= 10^6
"""

# Clean, Correct Python Solution
def runningSum(nums):
    """
    Calculate the running sum of a 1d array.

    :param nums: List[int] - Input array
    :return: List[int] - Running sum of the array
    """
    running_sum = []
    current_sum = 0
    for num in nums:
        current_sum += num
        running_sum.append(current_sum)
    return running_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(runningSum(nums1))  # Output: [1, 3, 6, 10]

    # Test Case 2
    nums2 = [1, 1, 1, 1, 1]
    print(runningSum(nums2))  # Output: [1, 2, 3, 4, 5]

    # Test Case 3
    nums3 = [3, 1, 2, 10, 1]
    print(runningSum(nums3))  # Output: [3, 4, 6, 16, 17]

    # Test Case 4 (Edge Case: Single Element)
    nums4 = [5]
    print(runningSum(nums4))  # Output: [5]

    # Test Case 5 (Edge Case: Negative Numbers)
    nums5 = [-1, -2, -3, -4]
    print(runningSum(nums5))  # Output: [-1, -3, -6, -10]

# Time and Space Complexity Analysis
"""
Time Complexity:
The solution iterates through the array `nums` once, performing a constant-time operation for each element.
Thus, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
The solution uses a list `running_sum` to store the results, which has the same size as the input array `nums`.
Thus, the space complexity is O(n).
"""

# Topic: Arrays