"""
LeetCode Problem #2813: Maximum Elegance of a K-Length Subsequence

Problem Statement:
You are given an array `nums` of integers and an integer `k`. A subsequence of `nums` is a sequence that can be derived 
from `nums` by deleting some or no elements without changing the order of the remaining elements.

The elegance of a subsequence is defined as the sum of its elements multiplied by the number of distinct elements in the subsequence.

Return the maximum elegance of a subsequence of length `k`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^9
- 1 <= k <= nums.length
"""

from collections import Counter
import heapq

def findMaximumElegance(nums, k):
    """
    Function to find the maximum elegance of a k-length subsequence.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The length of the subsequence.

    Returns:
    int: The maximum elegance of a k-length subsequence.
    """
    # Step 1: Sort the numbers in descending order
    nums.sort(reverse=True)
    
    # Step 2: Select the first k elements
    subsequence = nums[:k]
    
    # Step 3: Calculate the sum of the subsequence
    subsequence_sum = sum(subsequence)
    
    # Step 4: Count the number of distinct elements
    distinct_count = len(set(subsequence))
    
    # Step 5: Calculate the elegance
    elegance = subsequence_sum * distinct_count
    
    return elegance

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 3, 6, 2, 1]
    k1 = 3
    print(findMaximumElegance(nums1, k1))  # Expected Output: 39

    # Test Case 2
    nums2 = [10, 10, 10, 10]
    k2 = 2
    print(findMaximumElegance(nums2, k2))  # Expected Output: 20

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    k3 = 4
    print(findMaximumElegance(nums3, k3))  # Expected Output: 40

    # Test Case 4
    nums4 = [7, 7, 7, 7, 7]
    k4 = 5
    print(findMaximumElegance(nums4, k4))  # Expected Output: 35

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- Selecting the first k elements takes O(k).
- Calculating the sum of the subsequence takes O(k).
- Calculating the number of distinct elements takes O(k) in the worst case.
Overall time complexity: O(n log n + k).

Space Complexity Analysis:
- Sorting the array is done in-place, so no extra space is used for sorting.
- The subsequence array takes O(k) space.
- The set used to calculate distinct elements takes O(k) space in the worst case.
Overall space complexity: O(k).

Topic: Arrays, Sorting
"""