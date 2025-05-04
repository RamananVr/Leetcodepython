"""
LeetCode Problem #2495: Number of Subarrays Having Even Product

Problem Statement:
Given an integer array `nums`, return the number of contiguous subarrays where the product of all the elements in the subarray is even.

A product is even if at least one of the numbers in the subarray is even.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^6
"""

def numOfSubarraysWithEvenProduct(nums):
    """
    Function to calculate the number of subarrays with an even product.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The number of subarrays with an even product.
    """
    n = len(nums)
    count_even = 0
    count_odd = 0
    result = 0

    for num in nums:
        if num % 2 == 0:  # If the current number is even
            count_even += 1
            result += count_even
            count_odd = 0
        else:  # If the current number is odd
            count_odd += 1
            result += count_even

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(numOfSubarraysWithEvenProduct(nums1))  # Expected Output: 6

    # Test Case 2
    nums2 = [1, 3, 5]
    print(numOfSubarraysWithEvenProduct(nums2))  # Expected Output: 0

    # Test Case 3
    nums3 = [2, 4, 6]
    print(numOfSubarraysWithEvenProduct(nums3))  # Expected Output: 6

    # Test Case 4
    nums4 = [1, 2, 1, 2]
    print(numOfSubarraysWithEvenProduct(nums4))  # Expected Output: 7

"""
Time Complexity Analysis:
- The algorithm iterates through the array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space for variables like `count_even`, `count_odd`, and `result`.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""