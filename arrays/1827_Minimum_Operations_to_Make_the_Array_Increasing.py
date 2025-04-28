"""
LeetCode Problem #1827: Minimum Operations to Make the Array Increasing

Problem Statement:
You are given an integer array `nums` (0-indexed). In one operation, you can choose an element of the array and increment it by 1.

- For example, if `nums = [1,2,3]`, you can choose to increment `nums[1]` to make `nums = [1,3,3]`.

Return the minimum number of operations needed to make `nums` strictly increasing.

An array `nums` is strictly increasing if `nums[i] < nums[i+1]` for all `0 <= i < nums.length - 1`. An array of length 1 is trivially strictly increasing.

Constraints:
- `1 <= nums.length <= 5000`
- `1 <= nums[i] <= 10^4`
"""

def minOperations(nums):
    """
    Function to calculate the minimum number of operations to make the array strictly increasing.

    :param nums: List[int] - The input array of integers
    :return: int - The minimum number of operations required
    """
    operations = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            # Calculate the difference needed to make nums[i] strictly greater than nums[i-1]
            increment = nums[i - 1] - nums[i] + 1
            nums[i] += increment
            operations += increment

    return operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 1, 1]
    print(minOperations(nums1))  # Output: 3

    # Test Case 2
    nums2 = [1, 5, 2, 4, 1]
    print(minOperations(nums2))  # Output: 14

    # Test Case 3
    nums3 = [8]
    print(minOperations(nums3))  # Output: 0

    # Test Case 4
    nums4 = [3, 3, 3, 3]
    print(minOperations(nums4))  # Output: 6

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(minOperations(nums5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The algorithm modifies the input array in place and uses a constant amount of extra space.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""