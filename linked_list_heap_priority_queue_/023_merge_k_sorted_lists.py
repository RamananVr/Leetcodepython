"""
LeetCode Question #23: Merge k Sorted Lists

Problem Statement:
You are given an array of k linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted linked-list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []

Constraints:
- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order.
- The sum of lists[i].length will not exceed 10^4.
"""

from typing import List, Optional
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    """
    Merges k sorted linked lists into one sorted linked list.
    """
    # Create a min-heap to store the nodes
    heap = []
    
    # Add the head of each linked list to the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))
    
    # Create a dummy node to start the merged list
    dummy = ListNode()
    current = dummy
    
    # Process the heap until it's empty
    while heap:
        val, i, node = heapq.heappop(heap)
        current.next = node
        current = current.next
        if node.next:
            heapq.heappush(heap, (node.next.val, i, node.next))
    
    return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    dummy = ListNode()
    current = dummy
    for val in arr:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example test cases
if __name__ == "__main__":
    # Test case 1
    lists = [
        list_to_linked_list([1, 4, 5]),
        list_to_linked_list([1, 3, 4]),
        list_to_linked_list([2, 6])
    ]
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

    # Test case 2
    lists = []
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: []

    # Test case 3
    lists = [list_to_linked_list([])]
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: []

# Topic: Linked List, Heap (Priority Queue)