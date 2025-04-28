"""
LeetCode Problem #1695: Maximum Erasure Value

Problem Statement:
You are given an array of positive integers `nums` and want to erase a subarray containing unique elements. 
The score you get by erasing the subarray is equal to the sum of its elements.

Return the maximum score you can get by erasing exactly one subarray.

An array `b` is a subarray of array `a` if it forms a contiguous subsequence of `a`, that is, 
it is equal to `a[l], a[l+1], ..., a[r]` for some `(l, r)`.

Constraints:
- 1 <= nums.length <= 10^5
- 1 <= nums[i] <= 10^4
"""

def maximumUniqueSubarray(nums):
    """
    Finds the maximum score by erasing a subarray with unique elements.

    :param nums: List[int] - The input array of positive integers.
    :return: int - The maximum score achievable.
    """
    seen = set()  # To track unique elements in the current window
    left = 0  # Left pointer of the sliding window
    current_sum = 0  # Sum of the current window
    max_sum = 0  # Maximum sum found so far

    for right in range(len(nums)):
        # If nums[right] is already in the window, shrink the window from the left
        while nums[right] in seen:
            seen.remove(nums[left])
            current_sum -= nums[left]
            left += 1

        # Add nums[right] to the window
        seen.add(nums[right])
        current_sum += nums[right]

        # Update the maximum sum
        max_sum = max(max_sum, current_sum)

    return max_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 2, 4, 5, 6]
    print("Test Case 1:", maximumUniqueSubarray(nums1))  # Expected Output: 17

    # Test Case 2
    nums2 = [5, 2, 1, 2, 5, 2, 1, 2, 5]
    print("Test Case 2:", maximumUniqueSubarray(nums2))  # Expected Output: 8

    # Test Case 3
    nums3 = [1, 2, 3, 4, 5]
    print("Test Case 3:", maximumUniqueSubarray(nums3))  # Expected Output: 15

    # Test Case 4
    nums4 = [1, 1, 1, 1, 1]
    print("Test Case 4:", maximumUniqueSubarray(nums4))  # Expected Output: 1

    # Test Case 5
    nums5 = [10000, 1, 10000, 1, 10000]
    print("Test Case 5:", maximumUniqueSubarray(nums5))  # Expected Output: 10001

"""
Time Complexity Analysis:
- The algorithm uses a sliding window approach with two pointers (left and right).
- Each element is added to or removed from the `seen` set at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity Analysis:
- The space complexity is O(u), where u is the number of unique elements in the array.
- In the worst case, u = n (all elements are unique), so the space complexity is O(n).

Topic: Arrays, Sliding Window
"""