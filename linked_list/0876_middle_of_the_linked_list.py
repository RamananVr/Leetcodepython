"""
LeetCode Question #876: Middle of the Linked List

Problem Statement:
Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
Explanation: The middle node of the list is node 3.

Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
Explanation: Since the list has two middle nodes with values 3 and 4, we return the second one.

Constraints:
- The number of nodes in the list is in the range [1, 100].
- 1 <= Node.val <= 100
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middleNode(head: ListNode) -> ListNode:
    """
    Finds the middle node of a singly linked list.
    If there are two middle nodes, returns the second one.
    """
    # Initialize two pointers: slow and fast
    slow = fast = head
    
    # Move fast pointer twice as fast as the slow pointer
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # When fast pointer reaches the end, slow pointer is at the middle
    return slow

# Example Test Cases
def test_middleNode():
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
        while head:
            result.append(head.val)
            head = head.next
        return result

    # Test Case 1
    head1 = create_linked_list([1, 2, 3, 4, 5])
    result1 = middleNode(head1)
    assert linked_list_to_list(result1) == [3, 4, 5], f"Test Case 1 Failed: {linked_list_to_list(result1)}"

    # Test Case 2
    head2 = create_linked_list([1, 2, 3, 4, 5, 6])
    result2 = middleNode(head2)
    assert linked_list_to_list(result2) == [4, 5, 6], f"Test Case 2 Failed: {linked_list_to_list(result2)}"

    # Test Case 3
    head3 = create_linked_list([1])
    result3 = middleNode(head3)
    assert linked_list_to_list(result3) == [1], f"Test Case 3 Failed: {linked_list_to_list(result3)}"

    print("All test cases passed!")

# Run the test cases
if __name__ == "__main__":
    test_middleNode()

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once using the fast and slow pointers.
- Each pointer moves through the list in O(n) time, where n is the number of nodes in the list.
- Therefore, the time complexity is O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (two pointers: slow and fast).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Linked List
"""