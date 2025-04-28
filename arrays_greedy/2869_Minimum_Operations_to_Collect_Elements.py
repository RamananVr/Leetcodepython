"""
LeetCode Problem #2869: Minimum Operations to Collect Elements

Problem Statement:
You are given an array `nums` consisting of `n` integers, and an integer `k`. 
You need to collect all the integers from `1` to `k` (inclusive) in the minimum number of operations. 
In one operation, you can select any subarray of `nums` and remove it from the array. 
The remaining parts of the array are concatenated together.

Return the minimum number of operations required to collect all integers from `1` to `k`.

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= k`
- `1 <= k <= 10^5`
"""

def min_operations(nums, k):
    """
    Function to calculate the minimum number of operations required to collect all integers from 1 to k.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The target range of integers to collect.

    Returns:
    int: The minimum number of operations required.
    """
    # Use a set to track the numbers we need to collect
    needed = set(range(1, k + 1))
    operations = 0

    # Traverse the array from the end to the beginning
    for i in range(len(nums) - 1, -1, -1):
        # If the current number is in the needed set, remove it
        if nums[i] in needed:
            needed.remove(nums[i])
        # Increment the operation count when all numbers are collected
        if not needed:
            operations = len(nums) - i
            break

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k1 = 5
    print(min_operations(nums1, k1))  # Expected Output: 6

    # Test Case 2
    nums2 = [1, 2, 3, 4, 5]
    k2 = 5
    print(min_operations(nums2, k2))  # Expected Output: 5

    # Test Case 3
    nums3 = [5, 4, 3, 2, 1]
    k3 = 3
    print(min_operations(nums3, k3))  # Expected Output: 3

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    k4 = 1
    print(min_operations(nums4, k4))  # Expected Output: 1

    # Test Case 5
    nums5 = [2, 3, 1, 5, 4]
    k5 = 5
    print(min_operations(nums5, k5))  # Expected Output: 5

"""
Time Complexity Analysis:
- The algorithm iterates through the array once in reverse order, which takes O(n) time.
- Checking and removing elements from the set takes O(1) on average for each operation.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(k) due to the set `needed` which stores integers from 1 to k.

Topic: Arrays, Greedy
"""