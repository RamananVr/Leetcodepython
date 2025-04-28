"""
LeetCode Problem #2294: Partition Array Such That Maximum Difference Is K

Problem Statement:
You are given an integer array `nums` and an integer `k`. You may partition `nums` into one or more subsequences such that:
1. The difference between the maximum and minimum values in each subsequence is at most `k`.

Return the minimum number of subsequences needed.

Example:
Input: nums = [3, 6, 1, 2, 5], k = 2
Output: 2
Explanation: We can partition nums into the subsequences [1, 2, 3] and [5, 6]. The difference between the maximum and minimum values in each subsequence is at most 2.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^9
- 0 <= k <= 10^9
"""

# Solution
def partitionArray(nums, k):
    """
    Partition the array into the minimum number of subsequences such that
    the difference between the maximum and minimum values in each subsequence
    is at most k.

    :param nums: List[int] - The input array of integers.
    :param k: int - The maximum allowed difference in each subsequence.
    :return: int - The minimum number of subsequences needed.
    """
    # Sort the array to group numbers with small differences together
    nums.sort()
    
    # Initialize variables
    subsequences = 0
    start = 0  # Start of the current subsequence
    
    # Iterate through the sorted array
    for i in range(len(nums)):
        # If the difference between the current number and the start of the subsequence exceeds k,
        # start a new subsequence
        if nums[i] - nums[start] > k:
            subsequences += 1
            start = i  # Update the start of the new subsequence
    
    # Count the last subsequence
    subsequences += 1
    
    return subsequences

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [3, 6, 1, 2, 5]
    k = 2
    print(partitionArray(nums, k))  # Output: 2

    # Test Case 2
    nums = [1, 2, 3, 4]
    k = 1
    print(partitionArray(nums, k))  # Output: 2

    # Test Case 3
    nums = [10, 20, 30, 40]
    k = 10
    print(partitionArray(nums, k))  # Output: 4

    # Test Case 4
    nums = [1, 5, 9, 13]
    k = 4
    print(partitionArray(nums, k))  # Output: 4

    # Test Case 5
    nums = [1, 1, 1, 1]
    k = 0
    print(partitionArray(nums, k))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Iterating through the array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The space complexity is O(1) if we ignore the space used by the sorting algorithm.
- Sorting in Python typically uses O(n) additional space, so the space complexity is O(n) in the worst case.
"""

# Topic: Arrays