"""
LeetCode Problem #2091: Removing Minimum and Maximum From Array

Problem Statement:
You are given a 0-indexed array of distinct integers `nums`.

There is an element in `nums` that has the minimum value and an element that has the maximum value. 
Let the indices of the minimum and maximum values be `minIndex` and `maxIndex`, respectively. 
You need to remove both these elements from the array.

You can choose to remove them in one of three ways:
1. Remove the element with the minimum value first, followed by the element with the maximum value.
2. Remove the element with the maximum value first, followed by the element with the minimum value.
3. Remove both the minimum and maximum elements simultaneously.

Return the minimum number of moves required to make the array empty.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
- All the integers of `nums` are distinct.
"""

def minimumDeletions(nums):
    """
    Function to calculate the minimum number of moves required to remove the minimum and maximum elements from the array.

    :param nums: List[int] - The input array of distinct integers.
    :return: int - The minimum number of moves required.
    """
    n = len(nums)
    min_index = nums.index(min(nums))
    max_index = nums.index(max(nums))

    # Ensure min_index is always less than or equal to max_index for simplicity
    if min_index > max_index:
        min_index, max_index = max_index, min_index

    # Option 1: Remove both from the left
    left_removal = max_index + 1

    # Option 2: Remove both from the right
    right_removal = n - min_index

    # Option 3: Remove one from the left and the other from the right
    split_removal = (min_index + 1) + (n - max_index)

    # Return the minimum of the three options
    return min(left_removal, right_removal, split_removal)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 10, 7, 5, 4, 1, 8, 6]
    print(minimumDeletions(nums1))  # Expected Output: 5

    # Test Case 2
    nums2 = [0, -4, 19, 1, 8, -2, -3, 5]
    print(minimumDeletions(nums2))  # Expected Output: 3

    # Test Case 3
    nums3 = [101]
    print(minimumDeletions(nums3))  # Expected Output: 1

    # Test Case 4
    nums4 = [1, 2]
    print(minimumDeletions(nums4))  # Expected Output: 2


"""
Time and Space Complexity Analysis:

Time Complexity:
- Finding the minimum and maximum values in the array takes O(n) time.
- Calculating the three removal options involves constant time operations.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space, as no additional data structures are used.
- Overall, the space complexity is O(1).

Topic: Arrays
"""