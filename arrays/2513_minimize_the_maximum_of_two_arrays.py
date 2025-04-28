"""
LeetCode Question #2513: Minimize the Maximum of Two Arrays

Problem Statement:
You are given two arrays `nums1` and `nums2` of size `n` and `m` respectively. 
You need to minimize the maximum value of the two arrays after performing the following operation:
- You can remove any number of elements from either array (including zero elements).
- After removing elements, the maximum value of the two arrays is defined as the maximum of the largest element in `nums1` and the largest element in `nums2`.

Return the minimized maximum value of the two arrays.

Constraints:
- 1 <= n, m <= 10^5
- 1 <= nums1[i], nums2[j] <= 10^9
"""

# Solution
def minimize_maximum(nums1, nums2):
    """
    Minimize the maximum value of two arrays after removing elements.

    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.

    Returns:
    int: The minimized maximum value of the two arrays.
    """
    # Find the maximum value in each array
    max1 = max(nums1) if nums1 else float('-inf')
    max2 = max(nums2) if nums2 else float('-inf')
    
    # Return the minimum of the two maximums
    return min(max1, max2)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 7]
    nums2 = [2, 6, 8]
    print(minimize_maximum(nums1, nums2))  # Expected Output: 7

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(minimize_maximum(nums1, nums2))  # Expected Output: 6

    # Test Case 3
    nums1 = [10, 20, 30]
    nums2 = [5, 15, 25]
    print(minimize_maximum(nums1, nums2))  # Expected Output: 25

    # Test Case 4
    nums1 = [100]
    nums2 = [200]
    print(minimize_maximum(nums1, nums2))  # Expected Output: 100

    # Test Case 5
    nums1 = []
    nums2 = [1, 2, 3]
    print(minimize_maximum(nums1, nums2))  # Expected Output: 3

# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the maximum value in an array takes O(n) time.
- Therefore, the time complexity is O(n + m), where n is the size of nums1 and m is the size of nums2.

Space Complexity:
- The solution uses constant space, so the space complexity is O(1).
"""

# Topic: Arrays