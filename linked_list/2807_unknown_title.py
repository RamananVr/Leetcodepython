"""
LeetCode Problem #2807: Insert Greatest Common Divisors in Linked List

Problem Statement:
You are given the head of a linked list `head` and a positive integer `k`. The linked list contains integers. 
Your task is to insert a new node with the value equal to the greatest common divisor (GCD) of the values of 
two consecutive nodes in the linked list. The new node should be inserted between the two consecutive nodes.

Return the head of the modified linked list.

Constraints:
- The number of nodes in the linked list is in the range [2, 1000].
- Each node's value is in the range [1, 1000].

Example:
Input: head = [18, 6, 10], k = 2
Output: [18, 6, 2, 10]

Explanation:
- The GCD of 18 and 6 is 6.
- The GCD of 6 and 10 is 2.
- Insert these values between the respective nodes.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from math import gcd

def insertGreatestCommonDivisors(head: ListNode) -> ListNode:
    """
    Inserts a new node with the GCD of consecutive nodes' values into the linked list.
    """
    current = head
    while current and current.next:
        # Calculate GCD of current node and next node
        gcd_value = gcd(current.val, current.next.val)
        
        # Create a new node with the GCD value
        new_node = ListNode(gcd_value)
        
        # Insert the new node between current and next
        new_node.next = current.next
        current.next = new_node
        
        # Move to the next pair of nodes
        current = new_node.next
    
    return head

# Helper function to create a linked list from a list
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    head = create_linked_list([18, 6, 10])
    modified_head = insertGreatestCommonDivisors(head)
    print(linked_list_to_list(modified_head))  # Output: [18, 6, 2, 10]

    # Test Case 2
    head = create_linked_list([12, 15, 21])
    modified_head = insertGreatestCommonDivisors(head)
    print(linked_list_to_list(modified_head))  # Output: [12, 3, 15, 3, 21]

    # Test Case 3
    head = create_linked_list([7, 14, 28])
    modified_head = insertGreatestCommonDivisors(head)
    print(linked_list_to_list(modified_head))  # Output: [7, 7, 14, 14, 28]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the linked list once, performing a constant-time GCD calculation for each pair of nodes.
- Let `n` be the number of nodes in the linked list. The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for the GCD calculation and new node creation.
- The space complexity is O(1).

Topic: Linked List
"""