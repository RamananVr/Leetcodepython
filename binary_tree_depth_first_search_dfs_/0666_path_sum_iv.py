"""
LeetCode Question #666: Path Sum IV

Problem Statement:
If the depth of a tree is smaller than 5, then this tree can be represented by a list of three-digit integers. 
For each integer in this list:
- The hundreds digit represents the depth D of this node (1 <= D <= 4).
- The tens digit represents the position P of this node in the level it belongs to (1 <= P <= 8). 
  The position is the index of the node in the level, starting from the left.
- The units digit represents the value V of this node (0 <= V <= 9).

You need to find the sum of all paths from the root to the leaves.

Example:
Input: [113, 215, 221]
Output: 12
Explanation:
The tree that the input represents is as follows:
    3
   / \
  5   1
The path sum is (3 + 5) + (3 + 1) = 12.

Constraints:
- The number of nodes in the tree is in the range [1, 15].
- The input list is sorted in ascending order by depth and position.
- The tree will have at most one node at each position.
"""

# Python Solution
def pathSum(nums):
    """
    Calculate the sum of all paths from root to leaves in the tree represented by the input list.

    :param nums: List[int] - List of three-digit integers representing the tree.
    :return: int - Sum of all root-to-leaf path sums.
    """
    tree = {}
    for num in nums:
        depth, pos, value = num // 100, (num // 10) % 10, num % 10
        tree[(depth, pos)] = value

    def dfs(depth, pos, path_sum):
        # If the current node does not exist, return 0
        if (depth, pos) not in tree:
            return 0
        
        # Add the current node's value to the path sum
        path_sum += tree[(depth, pos)]
        
        # Calculate the positions of the left and right children
        left_child = (depth + 1, pos * 2 - 1)
        right_child = (depth + 1, pos * 2)
        
        # If the current node is a leaf, return the path sum
        if left_child not in tree and right_child not in tree:
            return path_sum
        
        # Otherwise, continue DFS on the left and right children
        return dfs(depth + 1, pos * 2 - 1, path_sum) + dfs(depth + 1, pos * 2, path_sum)

    # Start DFS from the root node at depth 1, position 1, with an initial path sum of 0
    return dfs(1, 1, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [113, 215, 221]
    print("Test Case 1 Output:", pathSum(nums1))  # Expected Output: 12

    # Test Case 2
    nums2 = [113, 221]
    print("Test Case 2 Output:", pathSum(nums2))  # Expected Output: 4

    # Test Case 3
    nums3 = [111, 213, 214, 315, 316]
    print("Test Case 3 Output:", pathSum(nums3))  # Expected Output: 15

    # Test Case 4
    nums4 = [111]
    print("Test Case 4 Output:", pathSum(nums4))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the input list once to build the tree dictionary, which takes O(n) time.
- The DFS traversal visits each node once, which also takes O(n) time.
- Therefore, the overall time complexity is O(n), where n is the number of nodes in the tree.

Space Complexity:
- The tree dictionary requires O(n) space to store the nodes.
- The recursion stack in the DFS traversal can go as deep as the height of the tree, which is at most 4 (since the depth is limited to 4).
- Therefore, the overall space complexity is O(n).
"""

# Topic: Binary Tree, Depth-First Search (DFS)