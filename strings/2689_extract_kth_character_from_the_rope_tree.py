"""
LeetCode Question #2689: Extract Kth Character from the Rope Tree

Problem Statement:
You are given the root of a binary tree and an integer k.

Besides the left and right children, every node of this tree has two other properties:
- val: The value stored in the node (could be an empty string).
- len: The total length of all values in the subtree rooted at this node.

This tree represents a rope, which is a data structure that can be used to represent and manipulate strings efficiently.

Return the kth character of the string represented by the rope tree.

Note: The tree is guaranteed to have at least k characters.

Examples:
Example 1:
Input: root = ["Leetcode", null, null], k = 4
Output: "c"
Explanation: In this case, the rope represents the string "Leetcode".
The 4th character is "c".

Example 2:
Input: root = [null, "Le", "et"], k = 3
Output: "e"
Explanation: In this case, the rope represents the string "Leet".
The 3rd character is "e".

Example 3:
Input: root = [null, [null, "L", "e"], [null, "et", "code"]], k = 6
Output: "o"
Explanation: In this case, the rope represents the string "Leetcode".
The 6th character is "o".

Constraints:
- The tree has at most 10^3 nodes.
- node.val contains only lowercase English letters.
- 1 <= k <= node.len <= 10^5
"""

from typing import Optional

class RopeTreeNode:
    """Definition for rope tree node."""
    def __init__(self, val="", left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.len = len(val) if val else 0
        
        # Calculate length including subtrees
        if left:
            self.len += left.len
        if right:
            self.len += right.len

def getKthCharacter(root: Optional[RopeTreeNode], k: int) -> str:
    """
    Extract the kth character from rope tree using DFS traversal.
    
    Time Complexity: O(log n) average case for balanced tree, O(n) worst case
    Space Complexity: O(h) where h is height of tree
    """
    if not root:
        return ""
    
    # If current node has a value, check if k falls within it
    if root.val:
        if k <= len(root.val):
            return root.val[k - 1]  # k is 1-indexed
        else:
            return ""  # k is beyond this node's value
    
    # Calculate left subtree length
    left_len = root.left.len if root.left else 0
    
    # If k is in left subtree
    if k <= left_len:
        return getKthCharacter(root.left, k)
    
    # Otherwise, k is in right subtree
    return getKthCharacter(root.right, k - left_len)

def getKthCharacterIterative(root: Optional[RopeTreeNode], k: int) -> str:
    """
    Iterative approach using explicit stack.
    
    Time Complexity: O(log n) average, O(n) worst case
    Space Complexity: O(h) for stack
    """
    if not root:
        return ""
    
    current = root
    remaining_k = k
    
    while current:
        # If current node has a value
        if current.val:
            if remaining_k <= len(current.val):
                return current.val[remaining_k - 1]
            else:
                return ""  # Should not happen given constraints
        
        # Calculate left subtree length
        left_len = current.left.len if current.left else 0
        
        # Navigate to appropriate subtree
        if remaining_k <= left_len:
            current = current.left
        else:
            current = current.right
            remaining_k -= left_len
    
    return ""

def getKthCharacterBruteForce(root: Optional[RopeTreeNode], k: int) -> str:
    """
    Brute force: construct entire string then return kth character.
    
    Time Complexity: O(n) where n is total length
    Space Complexity: O(n) for storing entire string
    """
    def construct_string(node):
        if not node:
            return ""
        
        if node.val:
            return node.val
        
        left_str = construct_string(node.left)
        right_str = construct_string(node.right)
        return left_str + right_str
    
    full_string = construct_string(root)
    return full_string[k - 1] if k <= len(full_string) else ""

def getKthCharacterInOrder(root: Optional[RopeTreeNode], k: int) -> str:
    """
    In-order traversal approach with character counting.
    
    Time Complexity: O(n) worst case, early termination possible
    Space Complexity: O(h) for recursion stack
    """
    result = ['']
    
    def in_order(node, count):
        if not node or result[0]:
            return count
        
        # Process left subtree first
        count = in_order(node.left, count)
        
        # Process current node
        if node.val and not result[0]:
            for char in node.val:
                count += 1
                if count == k:
                    result[0] = char
                    return count
        
        # Process right subtree
        if not result[0]:
            count = in_order(node.right, count)
        
        return count
    
    in_order(root, 0)
    return result[0]

def buildRopeTreeFromString(s: str) -> RopeTreeNode:
    """
    Helper function to build a simple rope tree from string for testing.
    """
    if not s:
        return None
    
    # Create a simple rope tree with string at leaf
    root = RopeTreeNode(s)
    return root

def buildBalancedRopeTree(s: str) -> RopeTreeNode:
    """
    Build a balanced rope tree from string for better performance testing.
    """
    if not s:
        return None
    
    if len(s) <= 3:  # Base case: small strings as leaf nodes
        return RopeTreeNode(s)
    
    # Split string roughly in half
    mid = len(s) // 2
    left_part = s[:mid]
    right_part = s[mid:]
    
    # Recursively build subtrees
    left_subtree = buildBalancedRopeTree(left_part)
    right_subtree = buildBalancedRopeTree(right_part)
    
    # Create internal node
    root = RopeTreeNode("", left_subtree, right_subtree)
    return root

def getRopeTreeString(root: Optional[RopeTreeNode]) -> str:
    """
    Helper function to get the complete string represented by rope tree.
    """
    if not root:
        return ""
    
    if root.val:
        return root.val
    
    left_str = getRopeTreeString(root.left)
    right_str = getRopeTreeString(root.right)
    return left_str + right_str

def validateRopeTree(root: Optional[RopeTreeNode]) -> bool:
    """
    Validate that the rope tree has correct length calculations.
    """
    if not root:
        return True
    
    expected_len = 0
    
    if root.val:
        expected_len += len(root.val)
    
    if root.left:
        if not validateRopeTree(root.left):
            return False
        expected_len += root.left.len
    
    if root.right:
        if not validateRopeTree(root.right):
            return False
        expected_len += root.right.len
    
    return root.len == expected_len

# Test Cases
if __name__ == "__main__":
    # Test Case 1: Simple string in root
    print("Test Case 1: Simple string")
    root1 = RopeTreeNode("Leetcode")
    k1 = 4
    result1 = getKthCharacter(root1, k1)
    print(f"getKthCharacter(root='Leetcode', k={k1}) = '{result1}', expected = 'c'")
    
    # Test Case 2: String split across nodes
    print("\nTest Case 2: Split string")
    root2 = RopeTreeNode("")
    root2.left = RopeTreeNode("Le")
    root2.right = RopeTreeNode("et")
    root2.len = root2.left.len + root2.right.len
    k2 = 3
    result2 = getKthCharacter(root2, k2)
    print(f"getKthCharacter(root with 'Le'+'et', k={k2}) = '{result2}', expected = 'e'")
    
    # Test Case 3: Complex tree structure
    print("\nTest Case 3: Complex tree")
    # Build tree for "Leetcode"
    root3 = RopeTreeNode("")
    
    # Left subtree: "Lee"
    root3.left = RopeTreeNode("")
    root3.left.left = RopeTreeNode("L")
    root3.left.right = RopeTreeNode("ee")
    root3.left.len = root3.left.left.len + root3.left.right.len
    
    # Right subtree: "tcode"
    root3.right = RopeTreeNode("")
    root3.right.left = RopeTreeNode("t")
    root3.right.right = RopeTreeNode("code")
    root3.right.len = root3.right.left.len + root3.right.right.len
    
    root3.len = root3.left.len + root3.right.len
    k3 = 6
    result3 = getKthCharacter(root3, k3)
    print(f"getKthCharacter(complex tree for 'Leetcode', k={k3}) = '{result3}', expected = 'o'")
    
    # Verify the tree represents "Leetcode"
    full_string = getRopeTreeString(root3)
    print(f"Full string represented by tree: '{full_string}'")
    
    # Test iterative approach
    print("\nTesting iterative approach:")
    result_iter = getKthCharacterIterative(root3, k3)
    print(f"Iterative result for k={k3}: '{result_iter}'")
    
    # Test brute force approach
    print("\nTesting brute force approach:")
    result_brute = getKthCharacterBruteForce(root3, k3)
    print(f"Brute force result for k={k3}: '{result_brute}'")
    
    # Test in-order approach
    print("\nTesting in-order approach:")
    result_inorder = getKthCharacterInOrder(root3, k3)
    print(f"In-order result for k={k3}: '{result_inorder}'")
    
    # Performance test with balanced tree
    print("\nPerformance test with balanced tree:")
    test_string = "This is a longer string for testing balanced rope tree performance"
    balanced_tree = buildBalancedRopeTree(test_string)
    
    # Validate tree
    is_valid = validateRopeTree(balanced_tree)
    print(f"Balanced tree is valid: {is_valid}")
    
    # Test middle character
    mid_k = len(test_string) // 2
    mid_char = getKthCharacter(balanced_tree, mid_k)
    expected_mid = test_string[mid_k - 1]
    print(f"Middle character (k={mid_k}): '{mid_char}', expected: '{expected_mid}', match: {mid_char == expected_mid}")
    
    # Test edge cases
    print("\nEdge case tests:")
    
    # First character
    first_char = getKthCharacter(balanced_tree, 1)
    expected_first = test_string[0]
    print(f"First character: '{first_char}', expected: '{expected_first}', match: {first_char == expected_first}")
    
    # Last character
    last_char = getKthCharacter(balanced_tree, len(test_string))
    expected_last = test_string[-1]
    print(f"Last character: '{last_char}', expected: '{expected_last}', match: {last_char == expected_last}")

"""
Time and Space Complexity Analysis:

Optimal Approach (getKthCharacter):
Time Complexity: O(log n) for balanced tree, O(n) worst case for skewed tree
Space Complexity: O(h) where h is height of tree (recursion stack)

Iterative Approach:
Time Complexity: O(log n) for balanced tree, O(n) worst case
Space Complexity: O(1) excluding input

Brute Force Approach:
Time Complexity: O(n) where n is total string length
Space Complexity: O(n) to store complete string

In-Order Traversal:
Time Complexity: O(k) in best case (early termination), O(n) worst case
Space Complexity: O(h) for recursion stack

Key Insights:
1. Rope tree allows efficient string operations without reconstructing entire string
2. Length information at each node enables O(log n) character access
3. Similar to binary indexed tree for prefix sums
4. Useful for text editors with large documents
5. Supports efficient string concatenation, splitting, and character access

Rope Data Structure Properties:
- Efficient concatenation: O(1)
- Efficient substring extraction: O(log n)
- Memory efficient for large strings
- Supports persistent data structures
- Good for undo/redo operations in text editors

Applications:
- Text editors (VS Code, Emacs)
- Version control systems
- Collaborative editing systems
- String processing in functional languages
- Large document manipulation

Topic: Trees, Binary Trees, String Processing, Data Structures, Rope Data Structure
"""
