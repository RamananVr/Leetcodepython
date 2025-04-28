"""
LeetCode Problem #360: Sort Transformed Array

Problem Statement:
Given a sorted array of integers `nums` and integer values `a`, `b`, and `c`, apply a quadratic function of the form 
f(x) = ax^2 + bx + c to each element `x` in the array. The transformed values should be sorted in ascending order.

Return the resulting sorted array.

Example:
Input: nums = [-4, -2, 2, 4], a = 1, b = 3, c = 5
Output: [3, 9, 15, 33]

Input: nums = [-4, -2, 2, 4], a = -1, b = 3, c = 5
Output: [-23, -5, 1, 7]

Constraints:
- 1 <= nums.length <= 200
- -100 <= nums[i] <= 100
- -100 <= a, b, c <= 100
"""

def sortTransformedArray(nums, a, b, c):
    """
    Sorts the transformed array based on the quadratic function f(x) = ax^2 + bx + c.

    :param nums: List[int] - A sorted array of integers.
    :param a: int - Coefficient of x^2 in the quadratic function.
    :param b: int - Coefficient of x in the quadratic function.
    :param c: int - Constant term in the quadratic function.
    :return: List[int] - Sorted array after applying the quadratic function.
    """
    def quadratic(x):
        return a * x ** 2 + b * x + c

    n = len(nums)
    result = [0] * n
    left, right = 0, n - 1
    index = n - 1 if a >= 0 else 0

    while left <= right:
        left_val = quadratic(nums[left])
        right_val = quadratic(nums[right])
        if a >= 0:
            if left_val > right_val:
                result[index] = left_val
                left += 1
            else:
                result[index] = right_val
                right -= 1
            index -= 1
        else:
            if left_val < right_val:
                result[index] = left_val
                left += 1
            else:
                result[index] = right_val
                right -= 1
            index += 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-4, -2, 2, 4]
    a1, b1, c1 = 1, 3, 5
    print(sortTransformedArray(nums1, a1, b1, c1))  # Output: [3, 9, 15, 33]

    # Test Case 2
    nums2 = [-4, -2, 2, 4]
    a2, b2, c2 = -1, 3, 5
    print(sortTransformedArray(nums2, a2, b2, c2))  # Output: [-23, -5, 1, 7]

    # Test Case 3
    nums3 = [0, 1, 2]
    a3, b3, c3 = 2, -3, 1
    print(sortTransformedArray(nums3, a3, b3, c3))  # Output: [1, 0, 3]

    # Test Case 4
    nums4 = [-3, -1, 0, 2]
    a4, b4, c4 = -2, 4, -1
    print(sortTransformedArray(nums4, a4, b4, c4))  # Output: [-19, -7, -1, 3]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the array once using a two-pointer approach, which takes O(n) time.
- Calculating the quadratic function for each element is O(1).
- Overall time complexity: O(n).

Space Complexity:
- The function uses a result array of size n to store the transformed values.
- No additional space is used apart from the result array.
- Overall space complexity: O(n).

Topic: Arrays, Two Pointers
"""