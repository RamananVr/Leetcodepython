"""
LeetCode Problem #2130: Maximum Twin Sum of a Linked List

Problem Statement:
In a linked list of size `n`, where `n` is even, the ith node (0-indexed) of the linked list is paired with the (n-1-i)th node. 
- For example, if `n = 4`, the nodes are paired as follows:
  - Node 0 is paired with Node 3
  - Node 1 is paired with Node 2

The *twin sum* is defined as the sum of a pair of nodes. In other words, for each pair `(i, n-1-i)`, the twin sum is `node[i].val + node[n-1-i].val`.

Return the maximum twin sum of the linked list.

Constraints:
- The number of nodes in the list is an even integer in the range `[2, 10^5]`.
- `1 <= Node.val <= 10^5`
"""

# Solution
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def pairSum(head: ListNode) -> int:
    """
    Function to calculate the maximum twin sum of a linked list.
    """
    # Step 1: Convert the linked list to an array
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Step 2: Calculate twin sums and find the maximum
    n = len(values)
    max_twin_sum = 0
    for i in range(n // 2):
        twin_sum = values[i] + values[n - 1 - i]
        max_twin_sum = max(max_twin_sum, twin_sum)
    
    return max_twin_sum

# Example Test Cases
def create_linked_list(values):
    """
    Helper function to create a linked list from a list of values.
    """
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
    head1 = create_linked_list([5, 4, 2, 1])
    print(pairSum(head1))  # Output: 6 (5+1 and 4+2)

    # Test Case 2
    head2 = create_linked_list([1, 100000])
    print(pairSum(head2))  # Output: 100001 (1+100000)

    # Test Case 3
    head3 = create_linked_list([1, 2, 3, 4, 5, 6])
    print(pairSum(head3))  # Output: 7 (1+6, 2+5, 3+4)

"""
Time and Space Complexity Analysis:

Time Complexity:
- Converting the linked list to an array takes O(n), where n is the number of nodes in the linked list.
- Calculating the twin sums and finding the maximum takes O(n/2), which simplifies to O(n).
- Overall time complexity: O(n).

Space Complexity:
- The array `values` stores all the node values, which requires O(n) space.
- Overall space complexity: O(n).

Topic: Linked List
"""