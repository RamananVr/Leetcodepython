"""
LeetCode Problem #2783: Minimum Number of Moves to Make All Array Elements Equal

Problem Statement:
You are given an integer array `nums` of size `n`. In one move, you can increment or decrement an element of the array by 1.

Return the minimum number of moves required to make all the elements of the array equal.

Example 1:
Input: nums = [1, 2, 3]
Output: 2
Explanation: 
- Increment 1 to 2 (1 move).
- Decrement 3 to 2 (1 move).
Total moves = 2.

Example 2:
Input: nums = [1, 10, 2, 9]
Output: 16
Explanation:
- Increment 1 to 5 (4 moves).
- Increment 2 to 5 (3 moves).
- Decrement 10 to 5 (5 moves).
- Decrement 9 to 5 (4 moves).
Total moves = 16.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

# Python Solution
def minMoves2(nums):
    """
    Function to calculate the minimum number of moves to make all array elements equal.
    
    Args:
    nums (List[int]): The input array of integers.

    Returns:
    int: The minimum number of moves required.
    """
    nums.sort()
    median = nums[len(nums) // 2]  # Find the median of the sorted array
    return sum(abs(num - median) for num in nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Test Case 1: {minMoves2(nums1)}")  # Expected Output: 2

    # Test Case 2
    nums2 = [1, 10, 2, 9]
    print(f"Test Case 2: {minMoves2(nums2)}")  # Expected Output: 16

    # Test Case 3
    nums3 = [1, 0, 0, 8, 6]
    print(f"Test Case 3: {minMoves2(nums3)}")  # Expected Output: 14

    # Test Case 4
    nums4 = [1]
    print(f"Test Case 4: {minMoves2(nums4)}")  # Expected Output: 0

    # Test Case 5
    nums5 = [1, 2, 3, 4, 5]
    print(f"Test Case 5: {minMoves2(nums5)}")  # Expected Output: 6

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- Calculating the sum of absolute differences takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- Sorting the array may require O(n) additional space depending on the sorting algorithm used.
- The space complexity is O(1) if the sorting is done in-place.
- Overall space complexity: O(n) or O(1) depending on the implementation.

Topic: Arrays, Sorting, Greedy
"""