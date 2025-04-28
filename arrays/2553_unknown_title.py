"""
LeetCode Problem #2553: Separate the Digits in an Array

Problem Statement:
You are given an array of positive integers `nums`. Return an array `result` that contains the digits of each integer in `nums` in the same order as they appear in `nums`.

For example, if `nums = [13, 25, 83, 77]`, the result should be `[1, 3, 2, 5, 8, 3, 7, 7]`.

Constraints:
- 1 <= nums.length <= 1000
- 1 <= nums[i] <= 10^5
"""

# Solution
def separateDigits(nums):
    """
    Function to separate the digits of each integer in the input array.

    Args:
    nums (List[int]): List of positive integers.

    Returns:
    List[int]: List of digits separated from the integers in the input array.
    """
    result = []
    for num in nums:
        result.extend(map(int, str(num)))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [13, 25, 83, 77]
    print(separateDigits(nums1))  # Output: [1, 3, 2, 5, 8, 3, 7, 7]

    # Test Case 2
    nums2 = [1, 234, 56789]
    print(separateDigits(nums2))  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test Case 3
    nums3 = [100, 200, 300]
    print(separateDigits(nums3))  # Output: [1, 0, 0, 2, 0, 0, 3, 0, 0]

    # Test Case 4
    nums4 = [5]
    print(separateDigits(nums4))  # Output: [5]

    # Test Case 5
    nums5 = [98765, 43210]
    print(separateDigits(nums5))  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through each number in the input list `nums` (O(n), where n is the length of `nums`).
- For each number, converting it to a string and iterating through its digits takes O(d), where d is the number of digits in the number.
- In the worst case, the sum of all digits across all numbers is proportional to the total number of digits in the input (let's call this D).
- Therefore, the overall time complexity is O(D), where D is the total number of digits in the input.

Space Complexity:
- The function uses a list `result` to store the separated digits. The size of this list is proportional to the total number of digits in the input (D).
- The space complexity is O(D).
"""

# Topic: Arrays