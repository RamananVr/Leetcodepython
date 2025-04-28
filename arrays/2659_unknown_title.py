"""
LeetCode Problem #2659: Make Array Empty

Problem Statement:
You are given an array `nums` consisting of positive integers. You can perform the following operation on the array any number of times:

1. Choose any element `x` from the array.
2. Remove `x` from the array.
3. Remove all elements from the array that are equal to `x`.

Return the minimum number of operations required to make the array empty.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
"""

# Solution
from collections import Counter

def min_operations(nums):
    """
    Calculate the minimum number of operations required to make the array empty.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The minimum number of operations.
    """
    # Count the frequency of each number in the array
    freq = Counter(nums)
    
    # The number of unique elements in the array is the minimum number of operations
    return len(freq)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 3, 3, 3]
    print(min_operations(nums1))  # Expected Output: 3

    # Test Case 2
    nums2 = [4, 4, 4, 4]
    print(min_operations(nums2))  # Expected Output: 1

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(min_operations(nums3))  # Expected Output: 5

    # Test Case 4
    nums4 = [10, 10, 20, 20, 30, 30, 30]
    print(min_operations(nums4))  # Expected Output: 3

    # Test Case 5
    nums5 = [1000000000, 1000000000, 1000000000]
    print(min_operations(nums5))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting the frequency of elements in the array using `Counter(nums)` takes O(n), where n is the length of the array.
- Calculating the length of the frequency dictionary takes O(1).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(u), where u is the number of unique elements in the array. This is because the `Counter` object stores the frequency of each unique element.
- In the worst case, u = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays
"""