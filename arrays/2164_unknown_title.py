"""
LeetCode Problem #2164: Sort Even and Odd Indices Independently

Problem Statement:
You are given a 0-indexed integer array `nums`. Rearrange the values of `nums` according to the following rules:
1. Sort the values at odd indices of `nums` in descending order.
2. Sort the values at even indices of `nums` in ascending order.

Return the array formed after rearranging the values of `nums`.

Example 1:
Input: nums = [4,1,2,3]
Output: [2,3,4,1]
Explanation:
- Indices 0 and 2 are even, so we sort [4,2] in ascending order to get [2,4].
- Indices 1 and 3 are odd, so we sort [1,3] in descending order to get [3,1].
- Combining these, we get [2,3,4,1].

Example 2:
Input: nums = [2,1]
Output: [2,1]
Explanation:
- Indices 0 are even, so we sort [2] in ascending order to get [2].
- Indices 1 are odd, so we sort [1] in descending order to get [1].
- Combining these, we get [2,1].

Constraints:
- 1 <= nums.length <= 100
- 1 <= nums[i] <= 100
"""

# Python Solution
def sortEvenOdd(nums):
    # Separate even and odd indexed elements
    even_indices = [nums[i] for i in range(len(nums)) if i % 2 == 0]
    odd_indices = [nums[i] for i in range(len(nums)) if i % 2 == 1]
    
    # Sort even indices in ascending order and odd indices in descending order
    even_indices.sort()
    odd_indices.sort(reverse=True)
    
    # Merge the sorted even and odd indices back into the original array
    result = []
    even_pointer, odd_pointer = 0, 0
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(even_indices[even_pointer])
            even_pointer += 1
        else:
            result.append(odd_indices[odd_pointer])
            odd_pointer += 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 1, 2, 3]
    print(sortEvenOdd(nums1))  # Output: [2, 3, 4, 1]

    # Test Case 2
    nums2 = [2, 1]
    print(sortEvenOdd(nums2))  # Output: [2, 1]

    # Test Case 3
    nums3 = [7, 5, 2, 9, 4, 3]
    print(sortEvenOdd(nums3))  # Output: [2, 9, 4, 5, 7, 3]

    # Test Case 4
    nums4 = [1]
    print(sortEvenOdd(nums4))  # Output: [1]

    # Test Case 5
    nums5 = [10, 20, 30, 40, 50, 60]
    print(sortEvenOdd(nums5))  # Output: [10, 60, 30, 40, 50, 20]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Separating even and odd indices: O(n), where n is the length of the input array.
- Sorting even indices: O(k * log(k)), where k is the number of even indices (approximately n/2).
- Sorting odd indices: O(m * log(m)), where m is the number of odd indices (approximately n/2).
- Merging the sorted arrays: O(n).
Overall: O(n + k * log(k) + m * log(m)) ≈ O(n * log(n)).

Space Complexity:
- Storing even_indices and odd_indices: O(n) additional space.
- Result array: O(n) additional space.
Overall: O(n).
"""

# Topic: Arrays