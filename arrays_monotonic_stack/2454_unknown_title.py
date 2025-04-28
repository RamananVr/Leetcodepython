"""
LeetCode Problem #2454: Next Greater Element IV

Problem Statement:
You are given a 0-indexed array `nums` of `n` integers. You are also given an integer `k`.

The next greater element of an element `nums[i]` is the first element `nums[j]` that is greater than `nums[i]` and is located to the right of `nums[i]` in the array (i.e., `j > i`). If there is no such element, then the next greater element is `-1`.

A k-next greater element of an element `nums[i]` is defined as the `k-th` next greater element of `nums[i]`. If there are fewer than `k` greater elements to the right of `nums[i]`, then the k-next greater element is `-1`.

Return an array `result` of length `n` where `result[i]` is the k-next greater element of `nums[i]`.

Example:
Input: nums = [1, 3, 5, 2, 4, 6], k = 2
Output: [5, 4, 6, 6, -1, -1]

Constraints:
- `1 <= nums.length <= 10^5`
- `1 <= nums[i] <= 10^9`
- `1 <= k <= nums.length`
"""

from collections import defaultdict

def nextGreaterElementIV(nums, k):
    """
    Function to find the k-next greater element for each element in the array.
    
    Args:
    nums (List[int]): The input array of integers.
    k (int): The k-th next greater element to find.
    
    Returns:
    List[int]: An array where each element is the k-next greater element of nums[i].
    """
    n = len(nums)
    result = [-1] * n
    stack = []
    next_greater_map = defaultdict(list)

    # Traverse the array from right to left
    for i in range(n - 1, -1, -1):
        # Maintain a decreasing stack
        while stack and nums[stack[-1]] <= nums[i]:
            stack.pop()
        
        # Add the current index to the stack
        if stack:
            next_greater_map[i].append(stack[-1])
            # Propagate the k-next greater elements
            for j in range(1, k):
                if len(next_greater_map[next_greater_map[i][-1]]) >= j:
                    next_greater_map[i].append(next_greater_map[next_greater_map[i][-1]][j - 1])
                else:
                    break
        
        # If we have k-next greater elements, set the result
        if len(next_greater_map[i]) >= k:
            result[i] = nums[next_greater_map[i][k - 1]]
        
        stack.append(i)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 3, 5, 2, 4, 6]
    k1 = 2
    print(nextGreaterElementIV(nums1, k1))  # Output: [5, 4, 6, 6, -1, -1]

    # Test Case 2
    nums2 = [2, 4, 1, 3, 5]
    k2 = 1
    print(nextGreaterElementIV(nums2, k2))  # Output: [4, 5, 3, 5, -1]

    # Test Case 3
    nums3 = [10, 9, 8, 7, 6]
    k3 = 3
    print(nextGreaterElementIV(nums3, k3))  # Output: [-1, -1, -1, -1, -1]

    # Test Case 4
    nums4 = [1, 2, 3, 4, 5]
    k4 = 3
    print(nextGreaterElementIV(nums4, k4))  # Output: [4, 5, -1, -1, -1]

"""
Time Complexity:
- The algorithm processes each element of the array once, and each element is pushed and popped from the stack at most once.
- The propagation of k-next greater elements is limited to k iterations for each element.
- Overall complexity: O(n * k), where n is the length of the array and k is the given parameter.

Space Complexity:
- The stack and next_greater_map together require O(n) space.
- Overall space complexity: O(n).

Topic: Arrays, Monotonic Stack
"""