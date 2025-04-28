"""
LeetCode Question #1630: Arithmetic Subarrays

Problem Statement:
A sequence of numbers is called arithmetic if it consists of at least two elements, and the difference between consecutive elements is the same. For example, these are arithmetic sequences:
1, 3, 5, 7, 9
7, 7, 7
3, -1, -5, -9

Given an array `nums` of integers and two arrays `l` and `r` of the same length, where `l[i]` and `r[i]` represent the start and end indices (inclusive) of the subarray `nums[l[i]:r[i]+1]`, return a list of boolean values `answer` where `answer[i]` is `true` if the subarray `nums[l[i]:r[i]+1]` can be rearranged to form an arithmetic sequence, and `false` otherwise.

Example:
Input: nums = [4, 6, 5, 9, 3, 7], l = [0, 0, 2], r = [2, 3, 5]
Output: [true, false, true]

Constraints:
- 2 <= nums.length <= 500
- 1 <= nums[i] <= 10^5
- 1 <= l.length == r.length <= 500
- 0 <= l[i] < r[i] < nums.length
"""

# Solution
def checkArithmeticSubarrays(nums, l, r):
    def is_arithmetic(arr):
        if len(arr) < 2:
            return False
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr)):
            if arr[i] - arr[i - 1] != diff:
                return False
        return True

    result = []
    for start, end in zip(l, r):
        subarray = nums[start:end + 1]
        result.append(is_arithmetic(subarray))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [4, 6, 5, 9, 3, 7]
    l = [0, 0, 2]
    r = [2, 3, 5]
    print(checkArithmeticSubarrays(nums, l, r))  # Output: [True, False, True]

    # Test Case 2
    nums = [1, 2, 3, 4]
    l = [0, 1, 0]
    r = [3, 3, 2]
    print(checkArithmeticSubarrays(nums, l, r))  # Output: [True, True, True]

    # Test Case 3
    nums = [10, 20, 30, 40, 50]
    l = [0, 1, 2]
    r = [4, 3, 4]
    print(checkArithmeticSubarrays(nums, l, r))  # Output: [True, True, True]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting each subarray takes O(k log k), where k is the length of the subarray.
- For each query, we extract and check the subarray, which takes O(k).
- If there are m queries, the total complexity is O(m * k log k), where k is the average length of the subarrays.

Space Complexity:
- The space complexity is O(k) for storing the subarray during each query.
- The result list takes O(m) space, where m is the number of queries.
- Overall space complexity is O(k + m).
"""

# Topic: Arrays