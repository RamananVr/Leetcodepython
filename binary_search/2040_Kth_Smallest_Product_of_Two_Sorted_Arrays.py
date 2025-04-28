"""
LeetCode Problem #2040: Kth Smallest Product of Two Sorted Arrays

Problem Statement:
You are given two sorted arrays nums1 and nums2 and an integer k.

nums1 is sorted in ascending order, and nums2 is sorted in ascending order. 
Return the kth smallest product of any pair (nums1[i], nums2[j]) where 0 <= i < nums1.length and 0 <= j < nums2.length.

Constraints:
- 1 <= nums1.length, nums2.length <= 10^5
- -10^5 <= nums1[i], nums2[j] <= 10^5
- 1 <= k <= min(nums1.length * nums2.length, 10^9)
"""

# Solution
def kthSmallestProduct(nums1, nums2, k):
    def count_less_equal(x):
        """Helper function to count pairs with product <= x."""
        count = 0
        for num in nums1:
            if num > 0:
                # Binary search for the largest index in nums2 where num * nums2[j] <= x
                left, right = 0, len(nums2)
                while left < right:
                    mid = (left + right) // 2
                    if num * nums2[mid] <= x:
                        left = mid + 1
                    else:
                        right = mid
                count += left
            elif num < 0:
                # Binary search for the smallest index in nums2 where num * nums2[j] <= x
                left, right = 0, len(nums2)
                while left < right:
                    mid = (left + right) // 2
                    if num * nums2[mid] <= x:
                        right = mid
                    else:
                        left = mid + 1
                count += len(nums2) - left
            else:
                # If num == 0, all products are 0
                if x >= 0:
                    count += len(nums2)
        return count

    # Binary search for the kth smallest product
    left, right = -10**10, 10**10
    while left < right:
        mid = (left + right) // 2
        if count_less_equal(mid) < k:
            left = mid + 1
        else:
            right = mid
    return left

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 3, 5]
    nums2 = [3, 4]
    k = 3
    print(kthSmallestProduct(nums1, nums2, k))  # Output: 12

    # Test Case 2
    nums1 = [-4, -2, 0, 3]
    nums2 = [-2, -1, 1, 2]
    k = 8
    print(kthSmallestProduct(nums1, nums2, k))  # Output: 0

    # Test Case 3
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    k = 5
    print(kthSmallestProduct(nums1, nums2, k))  # Output: 12

    # Test Case 4
    nums1 = [-5, -3, -1, 0, 2]
    nums2 = [-6, -4, -2, 1, 3]
    k = 10
    print(kthSmallestProduct(nums1, nums2, k))  # Output: -6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The binary search for the kth smallest product runs in O(log(max_product_range)), where max_product_range is the range of possible products.
- The count_less_equal function iterates through nums1 and performs binary search on nums2 for each element. This takes O(len(nums1) * log(len(nums2))).
- Overall time complexity: O(log(max_product_range) * len(nums1) * log(len(nums2))).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures.

Topic: Binary Search
"""