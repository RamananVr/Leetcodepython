"""
LeetCode Problem #217: Contains Duplicate

Problem Statement:
Given an integer array `nums`, return `true` if any value appears at least twice in the array, 
and return `false` if every element is distinct.

Example 1:
Input: nums = [1,2,3,1]
Output: true

Example 2:
Input: nums = [1,2,3,4]
Output: false

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true

Constraints:
- 1 <= nums.length <= 10^5
- -10^9 <= nums[i] <= 10^9
"""

# Solution
def containsDuplicate(nums):
    """
    Determines if the input list contains any duplicate values.

    Args:
    nums (List[int]): The input list of integers.

    Returns:
    bool: True if any value appears at least twice, False otherwise.
    """
    # Use a set to track seen numbers
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 1]
    print(containsDuplicate(nums1))  # Output: True

    # Test Case 2
    nums2 = [1, 2, 3, 4]
    print(containsDuplicate(nums2))  # Output: False

    # Test Case 3
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    print(containsDuplicate(nums3))  # Output: True

    # Test Case 4
    nums4 = []
    print(containsDuplicate(nums4))  # Output: False

    # Test Case 5
    nums5 = [1]
    print(containsDuplicate(nums5))  # Output: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the list `nums` once, performing O(1) operations (set lookup and insertion) for each element.
- Therefore, the time complexity is O(n), where n is the length of the input list.

Space Complexity:
- The function uses a set to store unique elements from the input list. In the worst case, when there are no duplicates, the set will contain all n elements.
- Therefore, the space complexity is O(n), where n is the length of the input list.
"""

# Topic: Arrays