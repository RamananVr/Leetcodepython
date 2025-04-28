"""
LeetCode Problem #496: Next Greater Element I

Problem Statement:
You are given two integer arrays `nums1` and `nums2` where `nums1` is a subset of `nums2`.
Find all the next greater numbers for `nums1`'s elements in the corresponding places of `nums2`.

The Next Greater Number of a number `x` in `nums1` is the first greater number to its right in `nums2`.
If it does not exist, output -1 for this number.

Constraints:
- 1 <= nums1.length <= nums2.length <= 1000
- 0 <= nums1[i], nums2[i] <= 10^4
- All integers in `nums1` and `nums2` are unique.
- All the integers of `nums1` also appear in `nums2`.

Example 1:
Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation:
- For number 4 in the first array, there is no next greater number in the second array, so output -1.
- For number 1, the next greater number is 3.
- For number 2, there is no next greater number, so output -1.

Example 2:
Input: nums1 = [2,4], nums2 = [1,2,3,4]
Output: [3,-1]
Explanation:
- For number 2 in the first array, the next greater number is 3.
- For number 4, there is no next greater number, so output -1.

Follow-up:
Could you find an O(nums1.length + nums2.length) solution?
"""

# Python Solution
def nextGreaterElement(nums1, nums2):
    """
    Finds the next greater element for each element in nums1 based on nums2.

    Args:
    nums1 (List[int]): A subset of nums2.
    nums2 (List[int]): A list of unique integers.

    Returns:
    List[int]: A list of integers representing the next greater element for each element in nums1.
    """
    # Dictionary to store the next greater element for each number in nums2
    next_greater = {}
    # Monotonic decreasing stack
    stack = []

    # Traverse nums2 to populate the next_greater dictionary
    for num in nums2:
        # While the stack is not empty and the current number is greater than the top of the stack
        while stack and num > stack[-1]:
            smaller_num = stack.pop()
            next_greater[smaller_num] = num
        # Push the current number onto the stack
        stack.append(num)

    # For any remaining numbers in the stack, there is no next greater element
    while stack:
        next_greater[stack.pop()] = -1

    # Map the results for nums1 based on the next_greater dictionary
    return [next_greater[num] for num in nums1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(nextGreaterElement(nums1, nums2))  # Output: [-1, 3, -1]

    # Test Case 2
    nums1 = [2, 4]
    nums2 = [1, 2, 3, 4]
    print(nextGreaterElement(nums1, nums2))  # Output: [3, -1]

    # Test Case 3
    nums1 = [1, 3, 5]
    nums2 = [6, 5, 4, 3, 2, 1, 7]
    print(nextGreaterElement(nums1, nums2))  # Output: [7, 7, 7]

    # Test Case 4
    nums1 = [10]
    nums2 = [10, 20, 30]
    print(nextGreaterElement(nums1, nums2))  # Output: [20]

# Time Complexity Analysis:
# - The algorithm processes each element of nums2 exactly once, either by pushing it onto the stack or popping it off.
# - Thus, the time complexity is O(nums2.length).
# - Mapping the results for nums1 takes O(nums1.length).
# - Overall time complexity: O(nums1.length + nums2.length).

# Space Complexity Analysis:
# - The stack can hold at most nums2.length elements, so the space complexity for the stack is O(nums2.length).
# - The next_greater dictionary stores at most nums2.length key-value pairs, so its space complexity is O(nums2.length).
# - Overall space complexity: O(nums2.length).

# Topic: Arrays, Stack, Hash Map