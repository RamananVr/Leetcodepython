"""
LeetCode Problem #2789: Largest Element in an Array after Merge Operations

Problem Statement:
You are given an integer array `nums`. You can perform the following operation any number of times:
- Choose two adjacent elements in the array, say `nums[i]` and `nums[i+1]`.
- Merge them into a single element by replacing them with their sum.

After performing the operations, return the largest element that can be obtained in the array.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def maxArrayValue(nums):
    """
    Function to find the largest element in the array after performing merge operations.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The largest element that can be obtained in the array.
    """
    n = len(nums)
    max_value = 0
    current_sum = 0

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        if nums[i] <= current_sum:
            current_sum += nums[i]
        else:
            current_sum = nums[i]
        max_value = max(max_value, current_sum)

    return max_value


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 7, 1, 5]
    print(maxArrayValue(nums1))  # Expected Output: 18

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(maxArrayValue(nums2))  # Expected Output: 10

    # Test Case 3
    nums3 = [10, 20, 30]
    print(maxArrayValue(nums3))  # Expected Output: 60

    # Test Case 4
    nums4 = [5]
    print(maxArrayValue(nums4))  # Expected Output: 5

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    print(maxArrayValue(nums5))  # Expected Output: 5


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the array once from right to left, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `current_sum` and `max_value`.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""