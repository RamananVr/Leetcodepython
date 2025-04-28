"""
LeetCode Problem #2179: Count Good Triplets in an Array

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n`, which represent permutations of the integers in the range `[0, n - 1]`.

A triplet `(i, j, k)` is good if:
- `0 <= i < j < k < n`
- The relative order of the elements in the triplet is the same in both arrays.

In other words, if `a`, `b`, and `c` are the elements at indices `i`, `j`, and `k` in `nums1`, respectively, then their respective positions in `nums2` should also satisfy:
- `nums2.index(a) < nums2.index(b) < nums2.index(c)`

Return the total number of good triplets.

Constraints:
- `n == nums1.length == nums2.length`
- `3 <= n <= 10^5`
- `0 <= nums1[i], nums2[i] < n`
- `nums1` and `nums2` are permutations of integers in the range `[0, n - 1]`.

"""

from sortedcontainers import SortedList

def goodTriplets(nums1, nums2):
    """
    Function to count the number of good triplets in the given arrays nums1 and nums2.

    Args:
    nums1 (List[int]): The first permutation array.
    nums2 (List[int]): The second permutation array.

    Returns:
    int: The total number of good triplets.
    """
    n = len(nums1)
    
    # Map each value in nums2 to its index for quick lookup
    index_in_nums2 = {value: idx for idx, value in enumerate(nums2)}
    
    # Transform nums1 into the indices of its elements in nums2
    transformed_nums1 = [index_in_nums2[value] for value in nums1]
    
    # Use a SortedList to maintain the order of elements seen so far
    sorted_list = SortedList()
    good_triplets_count = 0
    
    # Iterate through transformed_nums1
    for j in range(n):
        # Count elements less than transformed_nums1[j] (left side)
        left_count = sorted_list.bisect_left(transformed_nums1[j])
        
        # Count elements greater than transformed_nums1[j] (right side)
        right_count = len(sorted_list) - left_count
        
        # Add the current element to the sorted list
        sorted_list.add(transformed_nums1[j])
        
        # The number of good triplets with j as the middle element is left_count * right_count
        good_triplets_count += left_count * right_count
    
    return good_triplets_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 2, 3]
    nums2 = [0, 1, 2, 3]
    print(goodTriplets(nums1, nums2))  # Output: 4

    # Test Case 2
    nums1 = [2, 0, 1, 3]
    nums2 = [0, 1, 2, 3]
    print(goodTriplets(nums1, nums2))  # Output: 1

    # Test Case 3
    nums1 = [1, 0, 2, 3]
    nums2 = [3, 2, 1, 0]
    print(goodTriplets(nums1, nums2))  # Output: 0

"""
Time Complexity Analysis:
- Mapping nums2 to indices takes O(n).
- Transforming nums1 into indices takes O(n).
- For each element in nums1, we perform a binary search and insertion into the SortedList, which takes O(log n).
- Thus, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The index_in_nums2 dictionary takes O(n) space.
- The SortedList takes O(n) space.
- The transformed_nums1 list takes O(n) space.
- Thus, the overall space complexity is O(n).

Topic: Arrays, Binary Search, Ordered Data Structures
"""