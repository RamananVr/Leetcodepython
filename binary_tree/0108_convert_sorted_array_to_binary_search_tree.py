"""
LeetCode Question #108: Convert Sorted Array to Binary Search Tree

Problem Statement:
Given an integer array `nums` where the elements are sorted in ascending order, 
convert it to a height-balanced binary search tree.

A height-balanced binary tree is a binary tree in which the depth of the two 
subtrees of every node never differs by more than one.

Example 1:
Input: nums = [-10, -3, 0, 5, 9]
Output: [0, -3, 9, -10, null, 5]
Explanation: [0, -10, 5, null, -3, null, 9] is also accepted.

Example 2:
Input: nums = [1, 3]
Output: [3, 1]
Explanation: [1, 3] and [3, 1] are both height-balanced BSTs.

Constraints:
- The number of nodes in `nums` is in the range [1, 10^4].
- `-10^4 <= nums[i] <= 10^4`
- `nums` is sorted in a strictly increasing order.
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums):
    """
    Converts a sorted array into a height-balanced binary search tree.

    :param nums: List[int] - A sorted array of integers.
    :return: TreeNode - The root of the height-balanced binary search tree.
    """
    if not nums:
        return None

    # Find the middle element to use as the root
    mid = len(nums) // 2
    root = TreeNode(nums[mid])

    # Recursively build the left and right subtrees
    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root

# Helper function to print the tree in level-order for testing
def levelOrderTraversal(root):
    """
    Performs level-order traversal of a binary tree.

    :param root: TreeNode - The root of the binary tree.
    :return: List[int] - Level-order traversal of the tree.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values for cleaner output
    while result and result[-1] is None:
        result.pop()

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [-10, -3, 0, 5, 9]
    root1 = sortedArrayToBST(nums1)
    print("Test Case 1:", levelOrderTraversal(root1))  # Expected Output: [0, -3, 9, -10, None, 5]

    # Test Case 2
    nums2 = [1, 3]
    root2 = sortedArrayToBST(nums2)
    print("Test Case 2:", levelOrderTraversal(root2))  # Expected Output: [3, 1]

    # Test Case 3
    nums3 = [0]
    root3 = sortedArrayToBST(nums3)
    print("Test Case 3:", levelOrderTraversal(root3))  # Expected Output: [0]

    # Test Case 4
    nums4 = []
    root4 = sortedArrayToBST(nums4)
    print("Test Case 4:", levelOrderTraversal(root4))  # Expected Output: []

"""
Time Complexity:
- The function recursively divides the array into halves, and each element is processed once.
- Therefore, the time complexity is O(n), where n is the number of elements in the array.

Space Complexity:
- The space complexity is O(log n) due to the recursive call stack. In the worst case, the depth of the recursion is proportional to the height of the tree, which is log n for a balanced binary search tree.

Topic: Binary Tree
"""