"""
LeetCode Question #255: Verify Preorder Sequence in Binary Search Tree

Problem Statement:
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Constraints:
- The input array will have at most 10^4 elements.

Example:
Input: [5, 2, 1, 3, 6]
Output: True

Explanation:
The given array represents the preorder traversal of the following binary search tree:
    5
   / \
  2   6
 / \
1   3

Input: [5, 2, 6, 1, 3]
Output: False

Explanation:
The given array does not represent a valid preorder traversal of a binary search tree.

Follow-up:
Could you do it using only constant space complexity?
"""

def verifyPreorder(preorder):
    """
    Verify whether the given array is a valid preorder traversal of a binary search tree.

    :param preorder: List[int] - The preorder traversal sequence.
    :return: bool - True if valid, False otherwise.
    """
    stack = []
    lower_bound = float('-inf')

    for value in preorder:
        # If we encounter a value less than the lower bound, it's invalid
        if value < lower_bound:
            return False

        # Pop from the stack while the current value is greater than the top of the stack
        while stack and value > stack[-1]:
            lower_bound = stack.pop()

        # Push the current value onto the stack
        stack.append(value)

    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid preorder traversal
    preorder1 = [5, 2, 1, 3, 6]
    print(verifyPreorder(preorder1))  # Output: True

    # Test Case 2: Invalid preorder traversal
    preorder2 = [5, 2, 6, 1, 3]
    print(verifyPreorder(preorder2))  # Output: False

    # Test Case 3: Single element (valid)
    preorder3 = [1]
    print(verifyPreorder(preorder3))  # Output: True

    # Test Case 4: Empty array (valid)
    preorder4 = []
    print(verifyPreorder(preorder4))  # Output: True

    # Test Case 5: Large valid sequence
    preorder5 = [8, 5, 1, 7, 10, 9, 12]
    print(verifyPreorder(preorder5))  # Output: True

    # Test Case 6: Large invalid sequence
    preorder6 = [8, 5, 10, 1, 7, 9, 12]
    print(verifyPreorder(preorder6))  # Output: False


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm processes each element of the `preorder` array exactly once.
- Each element is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the `preorder` array.

Space Complexity:
- The stack is used to store elements of the `preorder` array.
- In the worst case (e.g., strictly decreasing sequence), the stack can grow to the size of the input array.
- However, the problem asks for a constant space solution. By reusing the input array as a stack, we can achieve O(1) space complexity.
- The current implementation uses O(n) space due to the stack, but it can be optimized to O(1) if required.

Topic: Binary Search Tree (BST), Stack
"""