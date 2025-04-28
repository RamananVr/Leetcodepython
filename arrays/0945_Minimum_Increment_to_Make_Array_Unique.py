"""
LeetCode Problem #945: Minimum Increment to Make Array Unique

Problem Statement:
You are given an integer array `nums`. In one move, you can pick an index `i` where `0 <= i < nums.length` and increment `nums[i]` by 1.

Return the minimum number of moves to make every value in `nums` unique.

Example 1:
Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].

Example 2:
Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 6 moves that it is possible for the array to have all unique values.

Constraints:
- 1 <= nums.length <= 10^5
- 0 <= nums[i] <= 10^5
"""

def minIncrementForUnique(nums):
    """
    Function to calculate the minimum number of moves to make all elements in the array unique.

    :param nums: List[int] - The input array of integers.
    :return: int - The minimum number of moves required.
    """
    nums.sort()  # Sort the array to handle duplicates in order
    moves = 0

    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:  # If the current number is not greater than the previous
            increment = nums[i - 1] - nums[i] + 1  # Calculate the increment needed
            nums[i] += increment  # Increment the current number
            moves += increment  # Add the increment to the total moves

    return moves

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2]
    print(f"Test Case 1: {minIncrementForUnique(nums1)}")  # Expected Output: 1

    # Test Case 2
    nums2 = [3, 2, 1, 2, 1, 7]
    print(f"Test Case 2: {minIncrementForUnique(nums2)}")  # Expected Output: 6

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(f"Test Case 3: {minIncrementForUnique(nums3)}")  # Expected Output: 6

    # Test Case 4
    nums4 = [10, 20, 30]
    print(f"Test Case 4: {minIncrementForUnique(nums4)}")  # Expected Output: 0

    # Test Case 5
    nums5 = [1, 1, 1, 1, 1]
    print(f"Test Case 5: {minIncrementForUnique(nums5)}")  # Expected Output: 10

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- The single pass through the array to calculate the moves takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the input array).

Topic: Arrays
"""