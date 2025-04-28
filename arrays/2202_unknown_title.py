"""
LeetCode Problem #2202: Maximize the Topmost Element After K Moves

Problem Statement:
You are given a 0-indexed integer array `nums` representing a stack, and an integer `k`. You are tasked with performing the following operation exactly `k` times:

1. If the stack is not empty, remove the topmost element of the stack.
2. If the stack is empty, you cannot perform any operations.
3. After removing the topmost element, you may choose to add it back to the stack.

You can choose to perform the operation in any order. Your goal is to maximize the value of the topmost element of the stack after exactly `k` operations. If the stack is empty after `k` operations, return `-1`.

Constraints:
- `1 <= nums.length <= 10^5`
- `0 <= nums[i] <= 10^9`
- `0 <= k <= 10^9`

Example:
Input: nums = [5, 2, 2, 4, 0, 6], k = 4
Output: 5

Explanation:
- After 4 operations, the topmost element can be maximized to 5.

Follow-up:
Can you solve the problem in O(n) time complexity?
"""

def maximizeTop(nums, k):
    """
    Function to maximize the topmost element of the stack after k moves.

    Args:
    nums (List[int]): The stack represented as a list of integers.
    k (int): The number of operations to perform.

    Returns:
    int: The maximum value of the topmost element after k moves, or -1 if the stack is empty.
    """
    n = len(nums)
    
    # If k == 0, no operations can be performed, return the current topmost element
    if k == 0:
        return nums[0] if nums else -1
    
    # If k == 1, we can only remove the topmost element
    if k == 1:
        return nums[1] if n > 1 else -1
    
    # If k > n, we can remove all elements and the stack will be empty
    if k > n:
        return max(nums)
    
    # If k == n, we can remove all elements except the last one
    if k == n:
        return max(nums[:-1])
    
    # Otherwise, we can remove up to k elements and replace the topmost element
    return max(max(nums[:k-1]), nums[k]) if k < n else max(nums[:k])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums = [5, 2, 2, 4, 0, 6]
    k = 4
    print(maximizeTop(nums, k))  # Output: 5

    # Test Case 2
    nums = [2]
    k = 1
    print(maximizeTop(nums, k))  # Output: -1

    # Test Case 3
    nums = [1, 2, 3, 4, 5]
    k = 2
    print(maximizeTop(nums, k))  # Output: 3

    # Test Case 4
    nums = [10, 20, 30]
    k = 3
    print(maximizeTop(nums, k))  # Output: 20

    # Test Case 5
    nums = [1, 2, 3, 4, 5]
    k = 6
    print(maximizeTop(nums, k))  # Output: 5

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function primarily involves slicing the array and finding the maximum value in a subset of the array.
- In the worst case, we compute the maximum of up to `k` elements, which is O(k).
- However, since k <= n (or we only consider up to n elements), the time complexity is O(n).

Space Complexity:
- The function uses constant space for computation, so the space complexity is O(1).

Topic: Arrays
"""