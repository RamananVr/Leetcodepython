# filepath: q:\source\AgentGeneratedLeetcode\strings\2673_make_costs_of_paths_equal_in_a_binary_tree.py
"""
LeetCode Question #2673: Make Costs of Paths Equal in a Binary Tree

Problem Statement:
You are given an integer n representing the number of nodes in a perfect binary tree consisting of nodes numbered from 1 to n. The root of the tree is node 1 and each node i in the tree has two children: node 2 * i and node 2 * i + 1.

Each node in the tree also has a cost represented by a given 0-indexed array cost of size n, where cost[i] is the cost of node i + 1. You are allowed to increment the cost of any node by 1 any number of times.

Return the minimum number of increments needed to make the costs of all paths from the root to each leaf node equal.

Note: A perfect binary tree is a tree where each internal node has exactly two children and all leaf nodes are at the same level.

Examples:
Example 1:
Input: n = 7, cost = [1,5,2,2,3,3,1]
Output: 6
Explanation: We can do the following increments:
- Increase the cost of node 4 once (2->3).
- Increase the cost of node 3 twice (2->4).
- Increase the cost of node 7 twice (1->3).
This ensures that all root-to-leaf paths have the same cost of 9.

Example 2:
Input: n = 3, cost = [5,3,3]
Output: 0
Explanation: The two paths already have equal cost, so no increments are needed.

Constraints:
- 3 <= n <= 10^5
- n + 1 is a power of 2
- cost.length == n
- 1 <= cost[i] <= 10^4
"""

from typing import List
import math

def minIncrements(n: int, cost: List[int]) -> int:
    """
    Make all root-to-leaf paths have equal cost using minimum increments.
    
    Time: O(n)
    Space: O(1) - excluding input
    """
    total_increments = 0
    
    # Process from bottom to top (reverse level order)
    # For each internal node, ensure both subtrees have equal max path cost
    for i in range(n // 2, 0, -1):  # Internal nodes in reverse order
        left_child = 2 * i
        right_child = 2 * i + 1
        
        # Find the difference between left and right subtree costs
        diff = abs(cost[left_child - 1] - cost[right_child - 1])
        total_increments += diff
        
        # Update the current node's cost to include the maximum of its children
        cost[i - 1] += max(cost[left_child - 1], cost[right_child - 1])
    
    return total_increments

def minIncrementsRecursive(n: int, cost: List[int]) -> int:
    """
    Recursive approach to solve the problem.
    
    Time: O(n)
    Space: O(log n) - recursion stack
    """
    def dfs(node: int) -> int:
        """
        Returns the total increments needed for subtree rooted at node.
        Also updates cost[node-1] to represent the max path cost from this node to leaf.
        """
        if node > n:
            return 0
        
        left_child = 2 * node
        right_child = 2 * node + 1
        
        # If it's a leaf node
        if left_child > n:
            return 0
        
        # Process children
        left_increments = dfs(left_child)
        right_increments = dfs(right_child)
        
        # Calculate increments needed to make both paths equal
        left_cost = cost[left_child - 1]
        right_cost = cost[right_child - 1]
        increments = abs(left_cost - right_cost)
        
        # Update current node's cost to include the maximum path
        cost[node - 1] += max(left_cost, right_cost)
        
        return left_increments + right_increments + increments
    
    return dfs(1)

def minIncrementsBottomUp(n: int, cost: List[int]) -> int:
    """
    Bottom-up approach with clear level processing.
    
    Time: O(n)
    Space: O(1)
    """
    # Make a copy to avoid modifying input
    costs = cost[:]
    total_increments = 0
    
    # Number of levels in the tree
    levels = int(math.log2(n + 1))
    
    # Process from second-to-last level up to root
    for level in range(levels - 2, -1, -1):
        level_start = 2 ** level
        level_end = min(2 ** (level + 1), n + 1)
        
        for node in range(level_start, level_end):
            if node * 2 <= n:  # Has children
                left_child = node * 2
                right_child = node * 2 + 1
                
                if right_child <= n:  # Both children exist
                    left_cost = costs[left_child - 1]
                    right_cost = costs[right_child - 1]
                    
                    # Add increments needed
                    total_increments += abs(left_cost - right_cost)
                    
                    # Update parent to include max child cost
                    costs[node - 1] += max(left_cost, right_cost)
    
    return total_increments

def minIncrementsExplained(n: int, cost: List[int]) -> int:
    """
    Version with detailed explanation of the algorithm.
    """
    print(f"Initial costs: {cost}")
    print(f"Tree structure (1-indexed): Root=1, for node i: left=2*i, right=2*i+1")
    
    costs = cost[:]
    total_increments = 0
    
    # Process internal nodes from bottom to top
    for i in range(n // 2, 0, -1):
        left_child = 2 * i
        right_child = 2 * i + 1
        
        if right_child <= n:  # Both children exist
            left_cost = costs[left_child - 1]
            right_cost = costs[right_child - 1]
            
            print(f"\nProcessing node {i}:")
            print(f"  Left child {left_child}: cost = {left_cost}")
            print(f"  Right child {right_child}: cost = {right_cost}")
            
            increments = abs(left_cost - right_cost)
            total_increments += increments
            
            print(f"  Increments needed: {increments}")
            
            # Update parent cost
            max_child_cost = max(left_cost, right_cost)
            costs[i - 1] += max_child_cost
            
            print(f"  Updated node {i} cost: {costs[i - 1]}")
    
    print(f"\nTotal increments needed: {total_increments}")
    return total_increments

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (7, [1, 5, 2, 2, 3, 3, 1], 6),
        (3, [5, 3, 3], 0),
        (15, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], 63),
        (7, [2, 2, 2, 2, 2, 2, 2], 0),
    ]
    
    print("Testing main approach:")
    for n, cost, expected in test_cases:
        result = minIncrements(n, cost.copy())
        print(f"n={n}, cost={cost}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    print("Testing recursive approach:")
    for n, cost, expected in test_cases:
        result = minIncrementsRecursive(n, cost.copy())
        print(f"n={n}, cost={cost}")
        print(f"Result: {result}, Expected: {expected}, {'✓' if result == expected else '✗'}")
        print()
    
    # Detailed explanation for first test case
    print("Detailed explanation for first test case:")
    minIncrementsExplained(7, [1, 5, 2, 2, 3, 3, 1])

"""
Time and Space Complexity Analysis:

Main Approach (minIncrements):
Time Complexity: O(n) - single pass through internal nodes
Space Complexity: O(1) - only using constant extra space

Recursive Approach:
Time Complexity: O(n) - each node visited once
Space Complexity: O(log n) - recursion stack depth

Bottom-Up Approach:
Time Complexity: O(n) - processing each level once
Space Complexity: O(1) - constant extra space

Key Insights:
1. The problem can be solved using a bottom-up approach
2. For each internal node, we need to balance the costs of its subtrees
3. The minimum increments = sum of absolute differences between sibling subtrees
4. We work from leaves to root, ensuring balance at each level
5. Perfect binary tree structure allows efficient indexing

Topic: Trees, Binary Tree, Greedy, Bottom-Up Processing
"""
