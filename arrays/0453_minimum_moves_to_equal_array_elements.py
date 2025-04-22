"""
LeetCode Question #453: Minimum Moves to Equal Array Elements

Problem Statement:
Given an integer array `nums` of size `n`, return the minimum number of moves required to make all array elements equal.
In one move, you can increment `n - 1` elements of the array by 1.

Example 1:
Input: nums = [1, 2, 3]
Output: 3
Explanation:
- In the first move, increment 1 and 2 to make the array [2, 3, 3].
- In the second move, increment 2 and 3 to make the array [3, 4, 3].
- In the third move, increment 3 and 4 to make the array [4, 4, 4].

Example 2:
Input: nums = [1, 1, 1]
Output: 0
Explanation: All elements are already equal.

Constraints:
- `n == nums.length`
- `1 <= n <= 10^5`
- `-10^9 <= nums[i] <= 10^9`
- The answer is guaranteed to fit in a 32-bit integer.
"""

# Clean and Correct Python Solution
def minMoves(nums):
    """
    Calculate the minimum number of moves to make all elements in the array equal.
    
    Args:
    nums (List[int]): The input array of integers.
    
    Returns:
    int: The minimum number of moves required.
    """
    # The optimal solution is to calculate the total difference between all elements and the minimum element.
    return sum(nums) - len(nums) * min(nums)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    print(f"Test Case 1: {minMoves(nums1)}")  # Expected Output: 3

    # Test Case 2
    nums2 = [1, 1, 1]
    print(f"Test Case 2: {minMoves(nums2)}")  # Expected Output: 0

    # Test Case 3
    nums3 = [5, 6, 8, 8]
    print(f"Test Case 3: {minMoves(nums3)}")  # Expected Output: 6

    # Test Case 4
    nums4 = [0, 0, 0]
    print(f"Test Case 4: {minMoves(nums4)}")  # Expected Output: 0

    # Test Case 5
    nums5 = [-1, 2, 3]
    print(f"Test Case 5: {minMoves(nums5)}")  # Expected Output: 6

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of the array takes O(n) time.
- Finding the minimum element in the array also takes O(n) time.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays