"""
LeetCode Problem #2689: Extract Kth Character From The Rope Tree

Problem Statement:
You are given a "rope tree," which is a binary tree where each node contains:
- A string `val` (non-empty if the node is a leaf).
- An integer `weight` (the total length of the string in the left subtree, or 0 if the node is a leaf).
- Two children: `left` and `right` (both can be None).

The rope tree is used to efficiently represent and manipulate large strings. Your task is to implement a function `getKthCharacter(root, k)` that extracts the k-th (0-indexed) character from the string represented by the rope tree.

Constraints:
- The input `k` is guaranteed to be valid (0 <= k < total length of the string represented by the tree).
- The tree is well-formed, and the total length of the string is the sum of all leaf node string lengths.

Example:
Input:
    Rope Tree:
        root = {
            "val": "",
            "weight": 5,
            "left": {
                "val": "",
                "weight": 3,
                "left": {"val": "abc", "weight": 0, "left": None, "right": None},
                "right": {"val": "de", "weight": 0, "left": None, "right": None}
            },
            "right": {
                "val": "",
                "weight": 4,
                "left": {"val": "fgh", "weight": 0, "left": None, "right": None},
                "right": {"val": "ij", "weight": 0, "left": None, "right": None}
            }
        }
    k = 6

Output:
    "g"
"""

# Definition for a Rope Tree Node
class RopeTreeNode:
    def __init__(self, val="", weight=0, left=None, right=None):
        self.val = val
        self.weight = weight
        self.left = left
        self.right = right

def getKthCharacter(root: RopeTreeNode, k: int) -> str:
    """
    Extracts the k-th character from the string represented by the rope tree.
    """
    # Base case: If the node is a leaf, return the k-th character from its value
    if root.left is None and root.right is None:
        return root.val[k]
    
    # If k is less than the weight, the character is in the left subtree
    if k < root.weight:
        return getKthCharacter(root.left, k)
    else:
        # Otherwise, the character is in the right subtree
        # Adjust k by subtracting the weight of the left subtree
        return getKthCharacter(root.right, k - root.weight)

# Example Test Cases
if __name__ == "__main__":
    # Constructing the example rope tree
    root = RopeTreeNode(
        val="",
        weight=5,
        left=RopeTreeNode(
            val="",
            weight=3,
            left=RopeTreeNode(val="abc", weight=0),
            right=RopeTreeNode(val="de", weight=0)
        ),
        right=RopeTreeNode(
            val="",
            weight=4,
            left=RopeTreeNode(val="fgh", weight=0),
            right=RopeTreeNode(val="ij", weight=0)
        )
    )

    # Test Case 1
    k = 6
    print(getKthCharacter(root, k))  # Output: "g"

    # Test Case 2
    k = 0
    print(getKthCharacter(root, k))  # Output: "a"

    # Test Case 3
    k = 4
    print(getKthCharacter(root, k))  # Output: "e"

    # Test Case 4
    k = 8
    print(getKthCharacter(root, k))  # Output: "i"

    # Test Case 5
    k = 9
    print(getKthCharacter(root, k))  # Output: "j"

"""
Time Complexity:
- In the worst case, we traverse the height of the tree to find the k-th character.
- If the tree is balanced, the height is O(log N), where N is the total number of characters in the string.
- Therefore, the time complexity is O(log N).

Space Complexity:
- The space complexity is O(H), where H is the height of the tree, due to the recursive call stack.
- For a balanced tree, this is O(log N).

Topic: Binary Tree
"""