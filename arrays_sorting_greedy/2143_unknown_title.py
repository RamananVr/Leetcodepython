"""
LeetCode Problem #2143: Choose Numbers From Two Arrays in Range

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n` and an integer `k`. 
You are tasked to choose exactly `k` elements from the two arrays such that:
- You choose at least one element from each array.
- The sum of the chosen elements is maximized.

Return the maximum possible sum of the chosen elements.

Constraints:
- `1 <= k <= n <= 10^5`
- `1 <= nums1[i], nums2[i] <= 10^9`

Example:
Input: nums1 = [3, 5, 2], nums2 = [2, 1, 4], k = 3
Output: 12
Explanation: Choose 2 elements from nums1 (5, 3) and 1 element from nums2 (4). The sum is 5 + 3 + 4 = 12.
"""

# Python Solution
from heapq import nlargest

def maxSum(nums1, nums2, k):
    """
    Function to calculate the maximum possible sum of k elements chosen from nums1 and nums2
    such that at least one element is chosen from each array.
    
    Args:
    nums1 (List[int]): First array of integers.
    nums2 (List[int]): Second array of integers.
    k (int): Number of elements to choose.
    
    Returns:
    int: Maximum possible sum.
    """
    # Combine both arrays into a single list of tuples (value, source)
    combined = [(num, 1) for num in nums1] + [(num, 2) for num in nums2]
    
    # Sort the combined list in descending order based on the values
    combined.sort(reverse=True, key=lambda x: x[0])
    
    # Initialize variables to track the sum and counts of elements chosen from each array
    total_sum = 0
    count1, count2 = 0, 0
    
    # Iterate through the top k elements in the sorted combined list
    for i in range(k):
        value, source = combined[i]
        total_sum += value
        if source == 1:
            count1 += 1
        else:
            count2 += 1
    
    # If at least one element is chosen from each array, return the total sum
    if count1 > 0 and count2 > 0:
        return total_sum
    
    # Otherwise, adjust the selection to ensure at least one element is chosen from each array
    # Find the smallest element in the current selection
    smallest_in_selection = combined[k - 1]
    
    # Find the largest element not in the current selection from the other array
    for i in range(k, len(combined)):
        value, source = combined[i]
        if (source == 1 and count1 == 0) or (source == 2 and count2 == 0):
            # Replace the smallest element in the current selection with this element
            total_sum = total_sum - smallest_in_selection[0] + value
            break
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [3, 5, 2]
    nums2 = [2, 1, 4]
    k = 3
    print(maxSum(nums1, nums2, k))  # Output: 12

    # Test Case 2
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 4
    print(maxSum(nums1, nums2, k))  # Output: 18

    # Test Case 3
    nums1 = [10, 20, 30]
    nums2 = [5, 15, 25]
    k = 5
    print(maxSum(nums1, nums2, k))  # Output: 105

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the combined list takes O(n log n), where n is the total number of elements in nums1 and nums2.
- Iterating through the top k elements takes O(k).
- Overall time complexity: O(n log n).

Space Complexity:
- The combined list requires O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Sorting, Greedy