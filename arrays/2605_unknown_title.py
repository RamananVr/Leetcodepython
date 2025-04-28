"""
LeetCode Problem #2605: Form Smallest Number From Two Digit Arrays

Problem Statement:
You are given two arrays of unique digits `nums1` and `nums2`, both of which are subsets of the set {1, 2, ..., 9}.
Return the smallest number that contains at least one digit from each array.

Example 1:
Input: nums1 = [4, 1, 3], nums2 = [5, 7]
Output: 15
Explanation: The number 15 contains the digit 1 from nums1 and the digit 5 from nums2. It can be formed by concatenating 1 and 5.

Example 2:
Input: nums1 = [3, 5, 2], nums2 = [5, 4, 1]
Output: 5
Explanation: The digit 5 is present in both arrays, so the smallest number is 5.

Example 3:
Input: nums1 = [6, 7], nums2 = [3, 4]
Output: 34
Explanation: The number 34 contains the digit 3 from nums2 and the digit 4 from nums1. It can be formed by concatenating 3 and 4.

Constraints:
- 1 <= nums1.length, nums2.length <= 9
- 1 <= nums1[i], nums2[i] <= 9
- All digits in nums1 and nums2 are unique.
"""

def form_smallest_number(nums1, nums2):
    """
    Function to find the smallest number that contains at least one digit from each array.

    Args:
    nums1 (List[int]): First array of unique digits.
    nums2 (List[int]): Second array of unique digits.

    Returns:
    int: The smallest number that contains at least one digit from each array.
    """
    # Find the intersection of nums1 and nums2
    common_digits = set(nums1) & set(nums2)
    if common_digits:
        return min(common_digits)

    # If no common digits, find the smallest digit from each array
    min_num1 = min(nums1)
    min_num2 = min(nums2)

    # Form the smallest two-digit number
    return int(str(min(min_num1, min_num2)) + str(max(min_num1, min_num2)))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 1, 3]
    nums2 = [5, 7]
    print(form_smallest_number(nums1, nums2))  # Output: 15

    # Test Case 2
    nums1 = [3, 5, 2]
    nums2 = [5, 4, 1]
    print(form_smallest_number(nums1, nums2))  # Output: 5

    # Test Case 3
    nums1 = [6, 7]
    nums2 = [3, 4]
    print(form_smallest_number(nums1, nums2))  # Output: 34

    # Test Case 4
    nums1 = [9]
    nums2 = [1]
    print(form_smallest_number(nums1, nums2))  # Output: 19

    # Test Case 5
    nums1 = [2, 8]
    nums2 = [3, 7]
    print(form_smallest_number(nums1, nums2))  # Output: 23


"""
Time Complexity Analysis:
- Finding the intersection of nums1 and nums2 takes O(n1 + n2), where n1 and n2 are the lengths of nums1 and nums2.
- Finding the minimum of nums1 and nums2 takes O(n1 + n2).
- Overall, the time complexity is O(n1 + n2).

Space Complexity Analysis:
- The space complexity is O(n1 + n2) due to the set operations.

Topic: Arrays
"""