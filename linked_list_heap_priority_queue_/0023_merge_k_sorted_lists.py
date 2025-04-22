"""
LeetCode Question #23: Merge k Sorted Lists

Problem Statement:
You are given an array of k linked-lists, each linked-list is sorted in ascending order.
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
    # Create a min-heap to store the nodes based on their values
    min_heap = []
    
    # Initialize the heap with the head of each linked list
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(min_heap, (node.val, i, node))
    
    # Dummy node to start the merged linked list
    dummy = ListNode()
    current = dummy
    
    # Process the heap until it's empty
    while min_heap:
        # Pop the smallest element from the heap
        val, i, node = heapq.heappop(min_heap)
        current.next = node
        current = current.next
        
        # If the current node has a next node, push it into the heap
        if node.next:
            heapq.heappush(min_heap, (node.next.val, i, node.next))
    
    return dummy.next

# Helper function to convert a list to a linked list
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert a linked list to a list
def linked_list_to_list(node: Optional[ListNode]) -> List[int]:
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lists = [
        list_to_linked_list([1, 4, 5]),
        list_to_linked_list([1, 3, 4]),
        list_to_linked_list([2, 6])
    ]
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: [1, 1, 2, 3, 4, 4, 5, 6]

    # Test Case 2
    lists = []
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: []

    # Test Case 3
    lists = [list_to_linked_list([])]
    merged = mergeKLists(lists)
    print(linked_list_to_list(merged))  # Output: []

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let n be the total number of nodes across all k linked lists.
- Inserting and removing elements from the heap takes O(log(k)) time.
- Since we process each node exactly once, the total time complexity is O(n * log(k)).

Space Complexity:
- The heap can contain at most k elements at any time, so the space complexity of the heap is O(k).
- Additionally, we use O(1) space for the dummy node and pointers.

Overall Space Complexity: O(k)

Topic: Linked List, Heap (Priority Queue)
"""