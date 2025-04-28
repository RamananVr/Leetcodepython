"""
LeetCode Problem #801: Minimum Swaps To Make Sequences Increasing

Problem Statement:
You are given two integer arrays nums1 and nums2 of the same length. In one operation, you are allowed to swap nums1[i] and nums2[i]. 
- For example, if nums1 = [1,2,3,8] and nums2 = [5,6,7,4], you can swap the element at index 3 to make nums1 = [1,2,3,4] and nums2 = [5,6,7,8].

Return the minimum number of swaps required to make both nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

Constraints:
- 2 <= nums1.length <= 10^5
- 0 <= nums1[i], nums2[i] <= 2 * 10^5
"""

def minSwap(nums1, nums2):
    """
    Dynamic Programming solution to find the minimum number of swaps required to make both sequences strictly increasing.
    """
    n = len(nums1)
    # Initialize two states:
    # keep[i]: Minimum swaps to make sequences increasing up to index i without swapping nums1[i] and nums2[i].
    # swap[i]: Minimum swaps to make sequences increasing up to index i with swapping nums1[i] and nums2[i].
    keep, swap = 0, 1

    for i in range(1, n):
        # Initialize temporary variables for the next state
        keep_next, swap_next = float('inf'), float('inf')

        # Case 1: No swap at index i
        if nums1[i] > nums1[i - 1] and nums2[i] > nums2[i - 1]:
            keep_next = min(keep_next, keep)  # No swap at i-1 and no swap at i
            swap_next = min(swap_next, swap + 1)  # Swap at i-1 and no swap at i

        # Case 2: Swap at index i
        if nums1[i] > nums2[i - 1] and nums2[i] > nums1[i - 1]:
            keep_next = min(keep_next, swap)  # Swap at i-1 and no swap at i
            swap_next = min(swap_next, keep + 1)  # No swap at i-1 and swap at i

        # Update states
        keep, swap = keep_next, swap_next

    # Return the minimum of the two states at the last index
    return min(keep, swap)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 4]
    nums2 = [1, 2, 3, 7]
    print(minSwap(nums1, nums2))  # Output: 1

    # Test Case 2
    nums1 = [0, 3, 5, 8, 9]
    nums2 = [2, 1, 4, 6, 9]
    print(minSwap(nums1, nums2))  # Output: 1

    # Test Case 3
    nums1 = [1, 2, 3, 7]
    nums2 = [1, 2, 3, 8]
    print(minSwap(nums1, nums2))  # Output: 0

"""
Time Complexity:
- The algorithm iterates through the arrays once, performing constant-time operations at each step.
- Therefore, the time complexity is O(n), where n is the length of the input arrays.

Space Complexity:
- The algorithm uses a constant amount of extra space for the variables `keep` and `swap`.
- Therefore, the space complexity is O(1).

Topic: Dynamic Programming
"""