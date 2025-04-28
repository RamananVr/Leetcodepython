"""
LeetCode Problem #2654: Minimum Number of Operations to Make All Array Elements Equal

Problem Statement:
You are given an integer array `nums` of size `n`. In one operation, you can choose any two indices `i` and `j` 
(1 <= i, j <= n) and set `nums[i] = nums[j]`. Your goal is to make all the elements in the array equal using 
the minimum number of operations.

Return the minimum number of operations required to make all the elements in the array equal.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^5
"""

# Solution
from collections import Counter

def min_operations(nums):
    """
    Function to calculate the minimum number of operations to make all elements in the array equal.

    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum number of operations required.
    """
    # Count the frequency of each element in the array
    freq = Counter(nums)
    
    # Find the maximum frequency of any element
    max_freq = max(freq.values())
    
    # The minimum operations required is the total number of elements minus the frequency of the most common element
    return len(nums) - max_freq

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 3]
    print(min_operations(nums1))  # Output: 2

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    print(min_operations(nums2))  # Output: 0

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print(min_operations(nums3))  # Output: 4

    # Test Case 4
    nums4 = [5, 5, 5, 6, 6, 6, 6]
    print(min_operations(nums4))  # Output: 3

    # Test Case 5
    nums5 = [10]
    print(min_operations(nums5))  # Output: 0

"""
Time Complexity Analysis:
- Counting the frequency of elements in the array using `Counter` takes O(n), where n is the length of the array.
- Finding the maximum frequency from the frequency dictionary takes O(k), where k is the number of unique elements in the array.
- Overall, the time complexity is O(n + k). Since k <= n, the time complexity simplifies to O(n).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique elements in the array, as we store the frequency of each element in a dictionary.
- In the worst case, when all elements are unique, k = n. Thus, the space complexity is O(n).

Topic: Arrays, Hash Table
"""