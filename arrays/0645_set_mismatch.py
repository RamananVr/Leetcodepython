"""
LeetCode Question #645: Set Mismatch

Problem Statement:
You have a set of integers `nums` where `nums` contains `n` numbers ranging from `1` to `n`. 
However, the set has been modified such that one of the numbers in the set is duplicated, 
resulting in another number missing. 

Return a tuple `(duplicate, missing)`:
- `duplicate`: the number that is duplicated in the array.
- `missing`: the number that is missing from the array.

Example:
Input: nums = [1, 2, 2, 4]
Output: [2, 3]

Constraints:
- n == nums.length
- 2 <= n <= 10^4
- 1 <= nums[i] <= n
"""

# Solution
def findErrorNums(nums):
    """
    Finds the duplicate and missing numbers in the given array.

    Args:
    nums (List[int]): The input array containing numbers from 1 to n.

    Returns:
    List[int]: A list containing the duplicate and missing numbers.
    """
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    actual_set_sum = sum(set(nums))
    
    duplicate = actual_sum - actual_set_sum
    missing = expected_sum - actual_set_sum
    
    return [duplicate, missing]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 2, 4]
    print(findErrorNums(nums1))  # Output: [2, 3]

    # Test Case 2
    nums2 = [1, 1]
    print(findErrorNums(nums2))  # Output: [1, 2]

    # Test Case 3
    nums3 = [3, 2, 3, 4, 6, 5]
    print(findErrorNums(nums3))  # Output: [3, 1]

    # Test Case 4
    nums4 = [1, 5, 3, 2, 2, 6, 7]
    print(findErrorNums(nums4))  # Output: [2, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the sum of the array takes O(n).
- Calculating the sum of the set of the array takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space complexity is O(n) due to the creation of a set from the array.
- No additional space is used beyond this, so the space complexity is O(n).
"""

# Topic: Arrays