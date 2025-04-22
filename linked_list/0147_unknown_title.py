"""
LeetCode Problem #147: Insertion Sort List

Problem Statement:
Given the head of a singly linked list, sort the list using insertion sort, and return the sorted list's head.

The steps of the insertion sort algorithm:
1. Insertion sort iterates, consuming one input element each repetition and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

The algorithm should be implemented on the linked list directly, without converting it to an array.

Constraints:
- The number of nodes in the list is in the range [1, 5000].
- -5000 <= Node.val <= 5000
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # Edge case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        # Dummy node to act as the new head of the sorted list
        dummy = ListNode(0)
        dummy.next = head
        current = head.next
        head.next = None

        while current:
            # Extract the node to be inserted
            temp = current
            current = current.next
            temp.next = None

            # Find the correct position to insert the node in the sorted list
            prev, curr = dummy, dummy.next
            while curr and curr.val < temp.val:
                prev = curr
                curr = curr.next

            # Insert the node
            prev.next = temp
            temp.next = curr

        return dummy.next

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

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    head = create_linked_list([4, 2, 1, 3])
    sorted_head = solution.insertionSortList(head)
    print(linked_list_to_list(sorted_head))  # Output: [1, 2, 3, 4]

    # Test Case 2
    head = create_linked_list([-1, 5, 3, 4, 0])
    sorted_head = solution.insertionSortList(head)
    print(linked_list_to_list(sorted_head))  # Output: [-1, 0, 3, 4, 5]

    # Test Case 3
    head = create_linked_list([1])
    sorted_head = solution.insertionSortList(head)
    print(linked_list_to_list(sorted_head))  # Output: [1]

    # Test Case 4
    head = create_linked_list([2, 1])
    sorted_head = solution.insertionSortList(head)
    print(linked_list_to_list(sorted_head))  # Output: [1, 2]

"""
Time Complexity:
- The outer loop iterates through all the nodes in the list (O(n)).
- For each node, we find its correct position in the sorted part of the list. In the worst case, this requires traversing the entire sorted part, which can take O(n) time.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The algorithm operates directly on the input linked list and uses only a constant amount of extra space (the dummy node and a few pointers).
- Thus, the space complexity is O(1).

Topic: Linked List
"""