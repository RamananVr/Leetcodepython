"""
LeetCode Question #1874: Minimize Product Sum of Two Arrays

Problem Statement:
The product sum of two equal-length arrays `nums1` and `nums2` is defined as:
    nums1[0] * nums2[0] + nums1[1] * nums2[1] + ... + nums1[n-1] * nums2[n-1]
(where `n` is the length of the arrays).

- Given two arrays `nums1` and `nums2` of length `n`, return the minimum product sum if you are allowed to rearrange the order of elements in `nums1`.

Constraints:
1. `n == nums1.length == nums2.length`
2. `1 <= n <= 10^5`
3. `1 <= nums1[i], nums2[i] <= 100`

Example:
Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
Output: 40
Explanation: We can rearrange nums1 to become [2,3,4,5]. The product sum is:
    (2*5) + (3*4) + (4*2) + (5*2) = 40.
"""

# Python Solution
def minProductSum(nums1, nums2):
    """
    Calculate the minimum product sum of two arrays by rearranging nums1.

    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.

    Returns:
    int: Minimum product sum.
    """
    # Sort nums1 in ascending order
    nums1.sort()
    # Sort nums2 in descending order
    nums2.sort(reverse=True)
    
    # Calculate the product sum
    product_sum = sum(a * b for a, b in zip(nums1, nums2))
    return product_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 3, 4, 2]
    nums2 = [4, 2, 2, 5]
    print(minProductSum(nums1, nums2))  # Output: 40

    # Test Case 2
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    print(minProductSum(nums1, nums2))  # Output: 20

    # Test Case 3
    nums1 = [1, 1, 1, 1]
    nums2 = [1, 1, 1, 1]
    print(minProductSum(nums1, nums2))  # Output: 4

    # Test Case 4
    nums1 = [10, 20, 30]
    nums2 = [30, 20, 10]
    print(minProductSum(nums1, nums2))  # Output: 1000

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting nums1 takes O(n log n).
- Sorting nums2 takes O(n log n).
- Calculating the product sum takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting operations are in-place, so no additional space is used.
- The space complexity is O(1).
"""

# Topic: Arrays