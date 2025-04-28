"""
LeetCode Problem #1308: Running Total for a List

Problem Statement:
Given a list of integers `nums`, write a function that returns a new list where each element at index `i` is the sum of all elements from index `0` to `i` in the original list. This is commonly referred to as the "running total" or "prefix sum."

Example:
Input: nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Constraints:
- 1 <= len(nums) <= 10^4
- -10^6 <= nums[i] <= 10^6
"""

def running_total(nums):
    """
    Calculate the running total (prefix sum) for a list of integers.

    Args:
    nums (List[int]): A list of integers.

    Returns:
    List[int]: A list containing the running total.
    """
    running_sum = 0
    result = []
    for num in nums:
        running_sum += num
        result.append(running_sum)
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3, 4]
    print(running_total(nums1))  # Output: [1, 3, 6, 10]

    # Test Case 2
    nums2 = [5, -2, 3, 8]
    print(running_total(nums2))  # Output: [5, 3, 6, 14]

    # Test Case 3
    nums3 = [0, 0, 0, 0]
    print(running_total(nums3))  # Output: [0, 0, 0, 0]

    # Test Case 4
    nums4 = [-1, -2, -3, -4]
    print(running_total(nums4))  # Output: [-1, -3, -6, -10]

    # Test Case 5
    nums5 = [1000000, -1000000, 1000000, -1000000]
    print(running_total(nums5))  # Output: [1000000, 0, 1000000, 0]

"""
Time and Space Complexity Analysis:

Time Complexity:
The function iterates through the list `nums` once, performing a constant amount of work for each element (addition and appending to the result list). 
Thus, the time complexity is O(n), where n is the length of the input list.

Space Complexity:
The function uses a list `result` to store the running totals, which has the same size as the input list `nums`. 
Thus, the space complexity is O(n), where n is the length of the input list.

Topic: Arrays
"""