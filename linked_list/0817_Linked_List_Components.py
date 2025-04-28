"""
LeetCode Problem #817: Linked List Components

Problem Statement:
You are given the head of a linked list and an array nums of integers. 
The integers in nums are a subset of the integers in the linked list. 
Return the number of connected components in nums where two values are 
connected if they appear consecutively in the linked list.

Example 1:
Input: head = [0,1,2,3], nums = [0,1,3]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] forms one component. 3 is not connected to any other number, so it forms another component.

Example 2:
Input: head = [0,1,2,3,4], nums = [0,3,1,4]
Output: 2
Explanation: 0 and 1 are connected, so [0, 1] forms one component. 3 and 4 are connected, so [3, 4] forms another component.

Constraints:
- The number of nodes in the linked list is n.
- 1 <= n <= 10^4
- 0 <= Node.val < n
- All the values Node.val are unique.
- nums is a subset of the values in the linked list.
- 1 <= nums.length <= n
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def numComponents(head: ListNode, nums: list[int]) -> int:
    """
    Function to calculate the number of connected components in nums based on the linked list.
    """
    # Convert nums to a set for O(1) lookup
    num_set = set(nums)
    current = head
    components = 0

    # Traverse the linked list
    while current:
        # If the current node is in nums and either the next node is not in nums or is None,
        # it marks the end of a component.
        if current.val in num_set and (current.next is None or current.next.val not in num_set):
            components += 1
        current = current.next

    return components

# Example Test Cases
if __name__ == "__main__":
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

    # Test Case 1
    head1 = create_linked_list([0, 1, 2, 3])
    nums1 = [0, 1, 3]
    print(numComponents(head1, nums1))  # Output: 2

    # Test Case 2
    head2 = create_linked_list([0, 1, 2, 3, 4])
    nums2 = [0, 3, 1, 4]
    print(numComponents(head2, nums2))  # Output: 2

    # Test Case 3
    head3 = create_linked_list([0, 1, 2, 3, 4, 5])
    nums3 = [0, 2, 4]
    print(numComponents(head3, nums3))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm traverses the linked list once, which takes O(n) time, where n is the number of nodes in the linked list.
- Checking membership in the set num_set takes O(1) on average for each node.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a set to store nums, which takes O(m) space, where m is the length of nums.
- The linked list itself is not modified, so no additional space is used for the list traversal.
- Overall space complexity: O(m).

Topic: Linked List
"""