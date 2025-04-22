"""
LeetCode Problem #228: Summary Ranges

Problem Statement:
You are given a sorted unique integer array nums.

A range [a,b] is the set of all integers from a to b (inclusive). For example, the range [5,8] includes 5, 6, 7, and 8.

The task is to return the smallest sorted list of ranges that cover all the numbers in the array exactly. That is, each element of nums is covered by exactly one of the ranges, and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
- "a->b" if a != b
- "a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]

Constraints:
- 0 <= nums.length <= 20
- -2^31 <= nums[i] <= 2^31 - 1
- All the values of nums are unique.
- nums is sorted in ascending order.
"""

def summaryRanges(nums):
    """
    Function to generate summary ranges from a sorted unique integer array.

    Args:
    nums (List[int]): A sorted unique integer array.

    Returns:
    List[str]: A list of summary ranges.
    """
    if not nums:
        return []

    ranges = []
    start = nums[0]

    for i in range(1, len(nums)):
        # If the current number is not consecutive, finalize the current range
        if nums[i] != nums[i - 1] + 1:
            if start == nums[i - 1]:
                ranges.append(str(start))
            else:
                ranges.append(f"{start}->{nums[i - 1]}")
            start = nums[i]

    # Finalize the last range
    if start == nums[-1]:
        ranges.append(str(start))
    else:
        ranges.append(f"{start}->{nums[-1]}")

    return ranges

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [0, 1, 2, 4, 5, 7]
    print(summaryRanges(nums1))  # Output: ["0->2", "4->5", "7"]

    # Test Case 2
    nums2 = [0, 2, 3, 4, 6, 8, 9]
    print(summaryRanges(nums2))  # Output: ["0", "2->4", "6", "8->9"]

    # Test Case 3
    nums3 = []
    print(summaryRanges(nums3))  # Output: []

    # Test Case 4
    nums4 = [1]
    print(summaryRanges(nums4))  # Output: ["1"]

    # Test Case 5
    nums5 = [-1, 0, 1, 2, 6, 7, 8]
    print(summaryRanges(nums5))  # Output: ["-1->2", "6->8"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once, making it O(n), where n is the length of the input array.

Space Complexity:
- The function uses a list to store the ranges, which in the worst case can have up to n elements. Thus, the space complexity is O(n).

Topic: Arrays
"""