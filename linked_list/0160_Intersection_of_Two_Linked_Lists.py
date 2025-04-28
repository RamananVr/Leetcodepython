"""
LeetCode Problem #160: Intersection of Two Linked Lists

Problem Statement:
Given the heads of two singly linked lists `headA` and `headB`, return the node at which the two lists intersect. 
If the two linked lists have no intersection at all, return `None`.

The two linked lists intersect at some node if there is a node `c` such that `c` is reachable from both `headA` and `headB` by following the next pointers. 
Note that `c` may not be the first node of either list. Formally, the intersection is defined based on reference, not value. 
In other words, if `c` is the intersection node, then `c` == `cA` == `cB` where `cA` and `cB` are nodes in `headA` and `headB` respectively.

Return `None` if there is no such intersection node.

Constraints:
1. The number of nodes in `headA` is in the range [0, 10^4].
2. The number of nodes in `headB` is in the range [0, 10^4].
3. 1 <= Node.val <= 10^5
4. Each list is guaranteed to be a singly linked list.

Follow-up:
Could you write a solution that runs in O(n) time and uses O(1) memory?
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
    """
    Finds the intersection node of two singly linked lists, if it exists.
    """
    if not headA or not headB:
        return None

    # Use two pointers
    pointerA, pointerB = headA, headB

    # Traverse both lists. When one pointer reaches the end, redirect it to the other list's head.
    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    # Either they meet at the intersection node or both become None (no intersection).
    return pointerA

# Example Test Cases
if __name__ == "__main__":
    # Example 1: Intersection exists
    intersect = ListNode(8, ListNode(4, ListNode(5)))
    headA = ListNode(4, ListNode(1, intersect))
    headB = ListNode(5, ListNode(6, ListNode(1, intersect)))
    print(getIntersectionNode(headA, headB).val)  # Output: 8

    # Example 2: No intersection
    headA = ListNode(2, ListNode(6, ListNode(4)))
    headB = ListNode(1, ListNode(5))
    print(getIntersectionNode(headA, headB))  # Output: None

    # Example 3: Both lists are empty
    headA = None
    headB = None
    print(getIntersectionNode(headA, headB))  # Output: None

    # Example 4: Intersection at the head
    intersect = ListNode(1, ListNode(2, ListNode(3)))
    headA = intersect
    headB = intersect
    print(getIntersectionNode(headA, headB).val)  # Output: 1

"""
Time Complexity Analysis:
- Let `m` be the length of `headA` and `n` be the length of `headB`.
- In the worst case, each pointer traverses both lists once, resulting in a time complexity of O(m + n).

Space Complexity Analysis:
- The solution uses two pointers and no additional data structures, so the space complexity is O(1).

Topic: Linked List
"""