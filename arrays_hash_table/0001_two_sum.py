"""
LeetCode Question #1: Two Sum

Problem Statement:
Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up:
Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

# Solution
def twoSum(nums, target):
    """
    Finds two indices in the array `nums` such that their values add up to `target`.

    Args:
    nums (List[int]): List of integers.
    target (int): Target sum.

    Returns:
    List[int]: Indices of the two numbers that add up to `target`.
    """
    # Create a dictionary to store the value and its index
    num_to_index = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        # Store the current number and its index in the dictionary
        num_to_index[num] = i
    
    # If no solution is found, return an empty list (this should not happen as per the problem constraints)
    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    print(twoSum(nums1, target1))  # Output: [0, 1]

    # Test Case 2
    nums2 = [3, 2, 4]
    target2 = 6
    print(twoSum(nums2, target2))  # Output: [1, 2]

    # Test Case 3
    nums3 = [3, 3]
    target3 = 6
    print(twoSum(nums3, target3))  # Output: [0, 1]

    # Test Case 4
    nums4 = [1, 5, 7, 8]
    target4 = 13
    print(twoSum(nums4, target4))  # Output: [1, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The algorithm uses a dictionary to store up to n elements (in the worst case).
- Therefore, the space complexity is O(n).

Overall, the solution is efficient and scales well for large input sizes.
"""

# Topic: Arrays, Hash Table