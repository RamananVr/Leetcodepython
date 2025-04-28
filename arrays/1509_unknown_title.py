"""
LeetCode Problem #1509: Minimum Difference Between Largest and Smallest Value in Three Moves

Problem Statement:
You are given an integer array `nums`. In one move, you can choose any element of the array and change it to any value.

Return the minimum difference between the largest and smallest value of `nums` after performing at most three moves.

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

def minDifference(nums):
    """
    Returns the minimum difference between the largest and smallest value of nums
    after performing at most three moves.

    :param nums: List[int] - The input array of integers
    :return: int - The minimum difference
    """
    if len(nums) <= 4:
        return 0  # If there are 4 or fewer elements, we can make all elements equal in 3 moves.

    # Sort the array to focus on the smallest and largest values
    nums.sort()

    # Consider the four possible scenarios:
    # 1. Remove the 3 largest elements
    # 2. Remove the 2 largest elements and 1 smallest element
    # 3. Remove the 1 largest element and 2 smallest elements
    # 4. Remove the 3 smallest elements
    return min(
        nums[-1] - nums[3],  # Remove the 3 smallest elements
        nums[-2] - nums[2],  # Remove 2 smallest and 1 largest
        nums[-3] - nums[1],  # Remove 1 smallest and 2 largest
        nums[-4] - nums[0]   # Remove the 3 largest elements
    )

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [5, 3, 2, 4]
    print(minDifference(nums1))  # Output: 0

    # Test Case 2
    nums2 = [1, 5, 0, 10, 14]
    print(minDifference(nums2))  # Output: 1

    # Test Case 3
    nums3 = [6, 6, 0, 1, 1, 4, 6]
    print(minDifference(nums3))  # Output: 2

    # Test Case 4
    nums4 = [1, 5, 6, 14, 15]
    print(minDifference(nums4))  # Output: 1

    # Test Case 5
    nums5 = [1, 1, 1, 1]
    print(minDifference(nums5))  # Output: 0

"""
Time Complexity Analysis:
- Sorting the array takes O(n log n), where n is the length of the array.
- The rest of the operations (calculating the minimum difference) take O(1).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation is in-place, so the space complexity is O(1) (ignoring the input array).

Topic: Arrays
"""