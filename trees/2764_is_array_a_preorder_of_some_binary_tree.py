"""
LeetCode Problem 2764: Is Array a Preorder of Some Binary Tree

Given a 0-indexed integer array nodes, where nodes[i] is the value of the ith node of a binary tree. Return true if the array represents the preorder traversal of some binary tree, otherwise return false.

A preorder traversal of a binary tree visits nodes in the order: root -> left subtree -> right subtree.

Constraints:
- 1 <= nodes.length <= 10^5
- 0 <= nodes[i] <= 10^5
- All values in nodes are distinct.

Example 1:
Input: nodes = [2,1,3]
Output: true
Explanation: We can construct the binary tree shown above whose preorder traversal is [2,1,3].

Example 2:
Input: nodes = [2,1,3,4]
Output: false
Explanation: There is no valid binary tree whose preorder traversal is [2,1,3,4].

Topics: Stack, Tree, Binary Tree, Simulation
"""

class Solution:
    def isPreorder(self, nodes: list[int]) -> bool:
        """
        Approach 1: Stack-based simulation
        
        Simulate the preorder traversal process:
        - Use a stack to track the path from root to current node
        - For each node, check if it can be a valid child of the current parent
        - A node can be a left child if we haven't seen a left child yet
        - A node can be a right child if we've finished the left subtree
        
        Time: O(n) - each node pushed/popped at most once
        Space: O(n) - stack can contain up to n nodes
        """
        if not nodes:
            return True
        
        stack = []  # Stack to simulate recursion
        i = 0
        
        def build_tree():
            nonlocal i
            if i >= len(nodes):
                return False
            
            # Current node value
            val = nodes[i]
            i += 1
            
            # Try to build left subtree
            if i < len(nodes) and nodes[i] < val:
                if not build_tree():
                    return False
            
            # Try to build right subtree
            if i < len(nodes) and nodes[i] > val:
                if not build_tree():
                    return False
            
            return True
        
        return build_tree() and i == len(nodes)
    
    def isPreorder_stack_iterative(self, nodes: list[int]) -> bool:
        """
        Approach 2: Iterative stack approach
        
        Use a stack to track the valid range for the next node.
        For BST property: left child < parent < right child.
        
        Time: O(n)
        Space: O(n)
        """
        if not nodes:
            return True
        
        stack = []  # (min_val, max_val) ranges
        stack.append((float('-inf'), float('inf')))
        
        for val in nodes:
            # Check if current value is in valid range
            if not stack:
                return False
            
            min_val, max_val = stack[-1]
            if val < min_val or val > max_val:
                return False
            
            # Pop ranges that can't have more children
            while stack and val > stack[-1][1]:
                stack.pop()
            
            if not stack:
                return False
            
            # Update range for potential right child
            min_val, max_val = stack[-1]
            if val > min_val:
                # This could be a right child, update min bound
                stack[-1] = (val, max_val)
            
            # Add range for potential children of current node
            stack.append((min_val, val))  # Left child range
            
        return True
    
    def isPreorder_recursive(self, nodes: list[int]) -> bool:
        """
        Approach 3: Recursive approach with bounds
        
        Recursively check if we can build a valid BST.
        
        Time: O(n)
        Space: O(n) - recursion stack
        """
        def helper(min_val, max_val):
            nonlocal idx
            if idx >= len(nodes):
                return True
            
            val = nodes[idx]
            if val < min_val or val > max_val:
                return True  # This node doesn't belong to current subtree
            
            idx += 1
            
            # Build left subtree (values < val)
            helper(min_val, val)
            
            # Build right subtree (values > val)
            helper(val, max_val)
            
            return True
        
        idx = 0
        helper(float('-inf'), float('inf'))
        return idx == len(nodes)
    
    def isPreorder_simple(self, nodes: list[int]) -> bool:
        """
        Approach 4: Simple stack approach
        
        Use stack to track ancestors and validate BST property.
        
        Time: O(n)
        Space: O(n)
        """
        stack = [float('inf')]
        min_val = float('-inf')
        
        for val in nodes:
            # If current value is less than minimum allowed, invalid
            if val < min_val:
                return False
            
            # Pop all values greater than current (we're in right subtree)
            while stack[-1] < val:
                min_val = stack.pop()
            
            stack.append(val)
        
        return True

def test_is_preorder():
    """Test the is preorder solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Valid preorder
    assert solution.isPreorder([2, 1, 3]) == True
    
    # Test case 2: Invalid preorder
    assert solution.isPreorder([2, 1, 3, 4]) == False
    
    # Test case 3: Single node
    assert solution.isPreorder([1]) == True
    
    # Test case 4: Valid BST preorder
    assert solution.isPreorder([5, 3, 1, 4, 7, 6, 8]) == True
    
    # Test case 5: Invalid - violates BST property
    assert solution.isPreorder([5, 3, 6, 1, 4]) == False
    
    # Test case 6: Empty array
    assert solution.isPreorder([]) == True
    
    # Test case 7: Decreasing sequence (all left children)
    assert solution.isPreorder([5, 4, 3, 2, 1]) == True
    
    # Test case 8: Increasing sequence (all right children)
    assert solution.isPreorder([1, 2, 3, 4, 5]) == True
    
    # Test case 9: Invalid mixed
    assert solution.isPreorder([1, 3, 2, 5, 4]) == False
    
    # Compare different approaches
    test_cases = [
        [2, 1, 3],
        [2, 1, 3, 4],
        [1],
        [5, 3, 1, 4, 7, 6, 8],
        [5, 3, 6, 1, 4],
        [],
        [5, 4, 3, 2, 1],
        [1, 2, 3, 4, 5]
    ]
    
    for nodes in test_cases:
        result1 = solution.isPreorder(nodes)
        result2 = solution.isPreorder_simple(nodes)
        assert result1 == result2, f"Mismatch for {nodes}: {result1} vs {result2}"
    
    print("All is preorder tests passed!")

if __name__ == "__main__":
    test_is_preorder()
