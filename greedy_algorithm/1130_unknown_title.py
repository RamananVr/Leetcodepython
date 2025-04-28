"""
LeetCode Problem #1130: Minimum Cost Tree From Leaf Values

Problem Statement:
Given an array `arr` of positive integers, consider all binary trees such that:
- Each node has either 0 or 2 children.
- The values of `arr` correspond to the values of each leaf in an in-order traversal of the tree.
- The value of each non-leaf node is equal to the product of the largest leaf value in its left and right subtree.

Among all possible binary trees considered, return the smallest possible sum of the values of each non-leaf node. It is guaranteed that the answer fits into a 32-bit signed integer.

Example 1:
Input: arr = [6, 2, 4]
Output: 32
Explanation:
There are two possible trees:
    - Tree 1: (6 * 4) + (4 * 2) = 24 + 8 = 32
    - Tree 2: (6 * 2) + (6 * 4) = 12 + 24 = 36
The minimum sum is 32.

Example 2:
Input: arr = [4, 11]
Output: 44

Constraints:
- 2 <= arr.length <= 40
- 1 <= arr[i] <= 15
- It is guaranteed that the answer fits into a 32-bit signed integer.
"""

# Clean and Correct Python Solution
def mctFromLeafValues(arr):
    """
    Function to calculate the minimum cost tree from leaf values.
    Uses a greedy approach with a monotonic stack.
    """
    stack = [float('inf')]  # Initialize stack with infinity to handle edge cases
    result = 0

    for num in arr:
        while stack and stack[-1] <= num:
            mid = stack.pop()
            result += mid * min(stack[-1], num)
        stack.append(num)

    # Process remaining elements in the stack
    while len(stack) > 2:
        result += stack.pop() * stack[-1]

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [6, 2, 4]
    print("Test Case 1 Output:", mctFromLeafValues(arr1))  # Expected Output: 32

    # Test Case 2
    arr2 = [4, 11]
    print("Test Case 2 Output:", mctFromLeafValues(arr2))  # Expected Output: 44

    # Test Case 3
    arr3 = [7, 12, 8, 10]
    print("Test Case 3 Output:", mctFromLeafValues(arr3))  # Expected Output: 284

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    print("Test Case 4 Output:", mctFromLeafValues(arr4))  # Expected Output: 40

    # Test Case 5
    arr5 = [15, 13, 5, 3, 15]
    print("Test Case 5 Output:", mctFromLeafValues(arr5))  # Expected Output: 500

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the array once, and each element is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the input array.

Space Complexity:
- The space complexity is O(n) due to the stack used to store elements during processing.
"""

# Topic: Greedy Algorithm