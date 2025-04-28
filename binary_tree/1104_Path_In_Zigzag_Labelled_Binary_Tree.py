"""
LeetCode Problem #1104: Path In Zigzag Labelled Binary Tree

Problem Statement:
In an infinite binary tree where every node has two children, the nodes are labelled in row order. In the odd-numbered rows 
(from the root), the labelling is left to right, while in the even-numbered rows, the labelling is right to left.

Given the label of a node in this tree, return the labels in the path from the root of the tree to the node with that label.

Example 1:
Input: label = 14
Output: [1, 3, 4, 14]

Example 2:
Input: label = 26
Output: [1, 2, 6, 10, 26]

Constraints:
- 1 <= label <= 10^6
"""

def pathInZigZagTree(label: int) -> list[int]:
    """
    Returns the path from the root to the given label in a zigzag labelled binary tree.
    """
    # Initialize the path list
    path = []
    
    # Traverse from the given label to the root
    while label > 0:
        path.append(label)
        # Calculate the level of the current label
        level = label.bit_length() - 1
        # Calculate the parent in a zigzag tree
        label = (2 ** level + 2 ** (level + 1) - 1 - label) // 2
    
    # Reverse the path to get the path from root to the label
    return path[::-1]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    label = 14
    print(f"Input: {label}, Output: {pathInZigZagTree(label)}")  # Output: [1, 3, 4, 14]

    # Test Case 2
    label = 26
    print(f"Input: {label}, Output: {pathInZigZagTree(label)}")  # Output: [1, 2, 6, 10, 26]

    # Test Case 3
    label = 1
    print(f"Input: {label}, Output: {pathInZigZagTree(label)}")  # Output: [1]

    # Test Case 4
    label = 16
    print(f"Input: {label}, Output: {pathInZigZagTree(label)}")  # Output: [1, 3, 4, 15, 16]

"""
Time Complexity:
- The while loop runs in O(log(label)) iterations because the label is halved at each step.
- Each iteration involves constant-time operations, so the overall time complexity is O(log(label)).

Space Complexity:
- The space complexity is O(log(label)) because the path list stores at most O(log(label)) elements.

Topic: Binary Tree
"""