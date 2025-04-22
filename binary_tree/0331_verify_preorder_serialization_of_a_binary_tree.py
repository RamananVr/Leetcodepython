"""
LeetCode Question #331: Verify Preorder Serialization of a Binary Tree

Problem Statement:
One way to serialize a binary tree is to use preorder traversal. When we encounter a non-null node, 
we record the node's value. If it is a null node, we record '#'.

For example, the following binary tree:
    1
   / \
  2   3
     / \
    4   5

is serialized as "1,2,#,#,3,4,#,#,5,#,#".

Given a string of comma-separated values representing the preorder serialization of a binary tree, 
return true if it is a correct preorder serialization. Otherwise, return false.

Constraints:
- The input string is non-empty and contains only commas, numbers, and the character '#'.
- You may assume that the input string is a valid preorder traversal of a binary tree.

Example 1:
Input: preorder = "9,3,4,#,#,1,#,#,2,#,6,#,#"
Output: true

Example 2:
Input: preorder = "1,#"
Output: false

Example 3:
Input: preorder = "9,#,#,1"
Output: false

Follow-up:
Could you do it using only constant space?
"""

# Python Solution
def isValidSerialization(preorder: str) -> bool:
    """
    Verify if the given preorder serialization of a binary tree is valid.

    Args:
    preorder (str): A string representing the preorder serialization of a binary tree.

    Returns:
    bool: True if the serialization is valid, False otherwise.
    """
    # Split the input string into nodes
    nodes = preorder.split(',')
    # Initialize a slot counter (root starts with 1 slot)
    slots = 1

    for node in nodes:
        # Consume one slot for the current node
        slots -= 1
        # If slots become negative, the serialization is invalid
        if slots < 0:
            return False
        # Non-null nodes add two slots (left and right children)
        if node != '#':
            slots += 2

    # All slots should be used up for a valid serialization
    return slots == 0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    preorder1 = "9,3,4,#,#,1,#,#,2,#,6,#,#"
    print(isValidSerialization(preorder1))  # Output: True

    # Test Case 2
    preorder2 = "1,#"
    print(isValidSerialization(preorder2))  # Output: False

    # Test Case 3
    preorder3 = "9,#,#,1"
    print(isValidSerialization(preorder3))  # Output: False

    # Test Case 4
    preorder4 = "#"
    print(isValidSerialization(preorder4))  # Output: True

    # Test Case 5
    preorder5 = "1,#,#,#"
    print(isValidSerialization(preorder5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the input string into nodes takes O(n), where n is the length of the input string.
- Iterating through the nodes also takes O(n).
- Thus, the overall time complexity is O(n).

Space Complexity:
- The solution uses constant space (O(1)) since we only maintain a single integer variable `slots` 
  and do not use any additional data structures like stacks or arrays.

Topic: Binary Tree
"""