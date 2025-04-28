"""
LeetCode Problem #2779: Maximum Beauty of an Array After Applying Operation

Problem Statement:
You are given a 0-indexed array `nums` and a positive integer `k`. You can apply the following operation on the array any number of times:
- Choose an index `i` in the array and increase or decrease `nums[i]` by any value from the range `[0, k]` (inclusive).

The beauty of the array is the length of the longest subsequence consisting of equal elements.

Return the maximum possible beauty of the array that can be achieved after applying the operation any number of times.

Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= nums[i], k <= 10^5`
"""

# Solution
def maximumBeauty(nums, k):
    """
    Function to calculate the maximum beauty of the array after applying the operation.

    Args:
    nums (List[int]): The input array of integers.
    k (int): The maximum value that can be added or subtracted from each element.

    Returns:
    int: The maximum possible beauty of the array.
    """
    # Step 1: Calculate the range [nums[i] - k, nums[i] + k] for each element
    ranges = []
    for num in nums:
        ranges.append((num - k, num + k))
    
    # Step 2: Sort the ranges by their start points
    ranges.sort()

    # Step 3: Use a sliding window to find the maximum overlap
    max_beauty = 0
    active_ranges = []
    
    for start, end in ranges:
        # Remove ranges that are no longer overlapping
        while active_ranges and active_ranges[0] < start:
            active_ranges.pop(0)
        
        # Add the current range's end to the active ranges
        active_ranges.append(end)
        
        # Update the maximum beauty
        max_beauty = max(max_beauty, len(active_ranges))
    
    return max_beauty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 6, 1, 2]
    k1 = 2
    print(maximumBeauty(nums1, k1))  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 1, 1, 1]
    k2 = 0
    print(maximumBeauty(nums2, k2))  # Expected Output: 4

    # Test Case 3
    nums3 = [1, 3, 6, 10]
    k3 = 3
    print(maximumBeauty(nums3, k3))  # Expected Output: 2

    # Test Case 4
    nums4 = [10, 20, 30, 40]
    k4 = 10
    print(maximumBeauty(nums4, k4))  # Expected Output: 4

"""
Time Complexity Analysis:
- Calculating the ranges takes O(n), where n is the length of the array.
- Sorting the ranges takes O(n log n).
- The sliding window approach iterates through the ranges, which takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The `ranges` list takes O(n) space.
- The `active_ranges` list takes O(n) space in the worst case.
- Overall space complexity: O(n).

Topic: Arrays, Sorting, Sliding Window
"""