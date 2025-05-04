"""
LeetCode Problem #2074: Reverse Nodes in Even Length Groups

Problem Statement:
You are given the head of a linked list. The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). In other words, 
- The 1st node is assigned to the first group.
- The 2nd and the 3rd nodes are assigned to the second group.
- The 4th, 5th, 6th nodes are assigned to the third group, and so on.

Note that the length of the last group may be less than or equal to the length of the sequence it is associated with.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

Example 1:
Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The first group consists of a single node [5], which is not reversed.
- The second group consists of 2 nodes [2,6], which is reversed.
- The third group consists of 3 nodes [3,9,1], which is not reversed.
- The fourth group consists of 4 nodes [7,3,8,4], which is reversed.

Example 2:
Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The first group consists of a single node [1], which is not reversed.
- The second group consists of 2 nodes [1,0], which is reversed.
- The third group consists of 1 node [6], which is not reversed.

Example 3:
Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The first group consists of a single node [1], which is not reversed.
- The second group consists of 2 nodes [1,0], which is reversed.
- The third group consists of 2 nodes [6,5], which is reversed.

Constraints:
- The number of nodes in the list is in the range [1, 10^5].
- 0 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseEvenLengthGroups(self, head: ListNode) -> ListNode:
        # Helper function to reverse a linked list segment
        def reverse_segment(start, end):
            prev, curr = None, start
            while curr != end:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        dummy = ListNode(0)
        dummy.next = head
        prev_group_end = dummy
        current = head
        group_size = 1

        while current:
            # Find the end of the current group
            group_start = current
            count = 0
            while current and count < group_size:
                current = current.next
                count += 1

            # Reverse the group if its length is even
            if count % 2 == 0:
                reversed_group_start = reverse_segment(group_start, current)
                prev_group_end.next = reversed_group_start
                group_start.next = current
                prev_group_end = group_start
            else:
                prev_group_end = group_start
                for _ in range(count - 1):
                    prev_group_end = prev_group_end.next

            group_size += 1

        return dummy.next

# Helper function to create a linked list from a list
def create_linked_list(values):
    dummy = ListNode(0)
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next

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
    head = create_linked_list([5, 2, 6, 3, 9, 1, 7, 3, 8, 4])
    result = solution.reverseEvenLengthGroups(head)
    print(linked_list_to_list(result))  # Output: [5, 6, 2, 3, 9, 1, 4, 8, 3, 7]

    # Test Case 2
    head = create_linked_list([1, 1, 0, 6])
    result = solution.reverseEvenLengthGroups(head)
    print(linked_list_to_list(result))  # Output: [1, 0, 1, 6]

    # Test Case 3
    head = create_linked_list([1, 1, 0, 6, 5])
    result = solution.reverseEvenLengthGroups(head)
    print(linked_list_to_list(result))  # Output: [1, 0, 1, 5, 6]

"""
Time Complexity:
- O(n): We traverse the linked list once to process all groups, and reversing a group takes O(k) time where k is the group size. Since the sum of group sizes is n, the total time complexity is O(n).

Space Complexity:
- O(1): We use constant extra space for pointers and variables.

Topic: Linked List
"""