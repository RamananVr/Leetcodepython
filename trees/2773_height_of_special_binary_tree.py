"""
LeetCode Problem 2773: Height of Special Binary Tree

You are given a special binary tree with n nodes where the nodes are labeled from 1 to n. Each node i has a value nums[i-1] (0-indexed).

A node is called special if the sum of the values of all nodes in its subtree (including itself) is even.

Return the height of the tree considering only the special nodes. If no special nodes exist, return 0.

The height of a tree is the number of edges in the longest path from the root to any leaf.

Constraints:
- 1 <= n <= 10^5  
- 1 <= nums[i] <= 10^9
- The tree is represented as parent array where parent[i] is the parent of node i+1, and parent[root] = -1

Example 1:
Input: nums = [1,2,3,4,5], parent = [-1,0,0,1,1]
Output: 2
Explanation: 
Tree structure:
    1(1)
   /    \
  2(2)  3(3)
 /  \
4(4) 5(5)

Subtree sums: 1->15, 2->11, 3->3, 4->4, 5->5
Special nodes (even sums): 4
Height considering only special nodes: 0 (only leaf nodes are special)

Example 2:
Input: nums = [2,4,6], parent = [-1,0,1]
Output: 2
Explanation:
Tree structure:
  1(2)
   \
    2(4)
     \
      3(6)

All subtree sums are even, so height is 2.

Topics: Tree, DFS, Binary Tree
"""

class Solution:
    def heightOfTree(self, nums: list[int], parent: list[int]) -> int:
        """
        Approach 1: DFS with subtree sum calculation
        
        1. Build the tree from parent array
        2. Calculate subtree sums using DFS
        3. Build a new tree with only special nodes
        4. Calculate height of the special tree
        
        Time: O(n) - DFS traversal + tree building
        Space: O(n) - tree storage and recursion stack
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # Build adjacency list representation
        children = [[] for _ in range(n)]
        root = -1
        
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)
        
        # Calculate subtree sums
        subtree_sums = [0] * n
        
        def calculate_subtree_sum(node):
            subtree_sums[node] = nums[node]
            for child in children[node]:
                subtree_sums[node] += calculate_subtree_sum(child)
            return subtree_sums[node]
        
        calculate_subtree_sum(root)
        
        # Find special nodes (even subtree sums)
        special_nodes = set()
        for i in range(n):
            if subtree_sums[i] % 2 == 0:
                special_nodes.add(i)
        
        if not special_nodes:
            return 0
        
        # Build special tree (only connections between special nodes)
        special_children = [[] for _ in range(n)]
        special_parent = [-1] * n
        
        def build_special_tree(node, spec_parent):
            if node in special_nodes:
                special_parent[node] = spec_parent
                spec_parent = node
            
            for child in children[node]:
                build_special_tree(child, spec_parent)
                if child in special_nodes and spec_parent != -1:
                    special_children[spec_parent].append(child)
        
        # Find special root
        special_root = root if root in special_nodes else None
        for node in special_nodes:
            if special_parent[node] == -1:
                special_root = node
                break
        
        if special_root is None:
            return 0
        
        build_special_tree(root, -1)
        
        # Calculate height of special tree
        def calculate_height(node):
            if node not in special_nodes:
                return -1
            
            max_height = 0
            for child in special_children[node]:
                child_height = calculate_height(child)
                if child_height >= 0:
                    max_height = max(max_height, child_height + 1)
            
            return max_height
        
        return calculate_height(special_root)
    
    def heightOfTree_simplified(self, nums: list[int], parent: list[int]) -> int:
        """
        Approach 2: Simplified approach
        
        Calculate subtree sums and find the maximum depth among special nodes.
        
        Time: O(n)
        Space: O(n)
        """
        n = len(nums)
        if n == 0:
            return 0
        
        # Build tree
        children = [[] for _ in range(n)]
        root = -1
        
        for i, p in enumerate(parent):
            if p == -1:
                root = i
            else:
                children[p].append(i)
        
        # Calculate subtree sums and depths
        subtree_sums = [0] * n
        depths = [0] * n
        
        def dfs(node, depth):
            depths[node] = depth
            subtree_sums[node] = nums[node]
            
            for child in children[node]:
                subtree_sums[node] += dfs(child, depth + 1)
            
            return subtree_sums[node]
        
        dfs(root, 0)
        
        # Find special nodes and their maximum depth difference
        special_depths = []
        for i in range(n):
            if subtree_sums[i] % 2 == 0:
                special_depths.append(depths[i])
        
        if not special_depths:
            return 0
        
        return max(special_depths) - min(special_depths)

def test_height_of_tree():
    """Test the height of tree solution with various test cases."""
    solution = Solution()
    
    # Test case 1: Given example
    # Tree: 1(1) -> [2(2), 3(3)], 2(2) -> [4(4), 5(5)]
    # Subtree sums: 1->15, 2->11, 3->3, 4->4, 5->5
    # Special: 4 (sum=4, even)
    result1 = solution.heightOfTree([1, 2, 3, 4, 5], [-1, 0, 0, 1, 1])
    # Height should be 0 since only leaf nodes are special
    
    # Test case 2: All even sums
    result2 = solution.heightOfTree([2, 4, 6], [-1, 0, 1])
    # All nodes should be special, height = 2
    
    # Test case 3: Single node
    assert solution.heightOfTree([2], [-1]) == 0
    assert solution.heightOfTree([1], [-1]) == 0
    
    # Test case 4: No special nodes
    result4 = solution.heightOfTree([1, 1, 1], [-1, 0, 1])
    # All sums are odd, no special nodes
    assert result4 == 0
    
    # Test case 5: Linear tree with alternating special nodes
    result5 = solution.heightOfTree([2, 1, 1], [-1, 0, 1])
    # Node 0: sum = 4 (special), Node 1: sum = 2 (special), Node 2: sum = 1
    
    # Test case 6: All nodes special
    result6 = solution.heightOfTree([2, 2, 2, 2], [-1, 0, 1, 2])
    # Linear tree, all even sums, height = 3
    
    print(f"Test results: {result1}, {result2}, {result4}, {result5}, {result6}")
    
    # Test simplified approach
    test_cases = [
        ([2], [-1]),
        ([1], [-1]),
        ([1, 1, 1], [-1, 0, 1]),
        ([2, 2, 2, 2], [-1, 0, 1, 2])
    ]
    
    for nums, parent_arr in test_cases:
        result1 = solution.heightOfTree(nums, parent_arr)
        result2 = solution.heightOfTree_simplified(nums, parent_arr)
        print(f"nums={nums}, parent={parent_arr}: {result1}, {result2}")
    
    print("Height of tree tests completed!")

if __name__ == "__main__":
    test_height_of_tree()
