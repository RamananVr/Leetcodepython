"""
LeetCode Question #2326: Spiral Matrix IV

Problem Statement:
You are given two integers `m` and `n`, which represent the dimensions of a matrix. You are also given a linked list with `m * n` nodes, where each node contains an integer. You need to construct a matrix of dimensions `m x n` in a spiral order using the values from the linked list. The spiral order starts from the top-left corner and proceeds clockwise.

Return the constructed matrix.

Constraints:
- The number of nodes in the linked list is exactly `m * n`.
- 1 <= m, n <= 1000
- -10^6 <= Node.val <= 10^6

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def spiralMatrix(m: int, n: int, head: ListNode) -> list[list[int]]:
    """
    Constructs a matrix of dimensions m x n in spiral order using values from the linked list.
    """
    # Initialize the matrix with -1
    matrix = [[-1] * n for _ in range(m)]
    
    # Define the boundaries for the spiral traversal
    top, bottom, left, right = 0, m - 1, 0, n - 1
    
    # Pointer to traverse the linked list
    current = head
    
    while current:
        # Fill the top row
        for col in range(left, right + 1):
            if current:
                matrix[top][col] = current.val
                current = current.next
        top += 1
        
        # Fill the right column
        for row in range(top, bottom + 1):
            if current:
                matrix[row][right] = current.val
                current = current.next
        right -= 1
        
        # Fill the bottom row
        for col in range(right, left - 1, -1):
            if current:
                matrix[bottom][col] = current.val
                current = current.next
        bottom -= 1
        
        # Fill the left column
        for row in range(bottom, top - 1, -1):
            if current:
                matrix[row][left] = current.val
                current = current.next
        left += 1
    
    return matrix

# Example Test Cases
def create_linked_list(values):
    """Helper function to create a linked list from a list of values."""
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

if __name__ == "__main__":
    # Test Case 1
    m, n = 3, 3
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    head = create_linked_list(values)
    print(spiralMatrix(m, n, head))
    # Expected Output:
    # [[1, 2, 3],
    #  [8, 9, 4],
    #  [7, 6, 5]]

    # Test Case 2
    m, n = 4, 1
    values = [1, 2, 3, 4]
    head = create_linked_list(values)
    print(spiralMatrix(m, n, head))
    # Expected Output:
    # [[1],
    #  [2],
    #  [3],
    #  [4]]

    # Test Case 3
    m, n = 2, 2
    values = [1, 2, 3, 4]
    head = create_linked_list(values)
    print(spiralMatrix(m, n, head))
    # Expected Output:
    # [[1, 2],
    #  [4, 3]]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through all `m * n` elements of the matrix exactly once.
- Therefore, the time complexity is O(m * n).

Space Complexity:
- The matrix requires O(m * n) space to store the result.
- No additional space is used apart from the matrix and a few variables.
- Therefore, the space complexity is O(m * n).

Topic: Matrix
"""