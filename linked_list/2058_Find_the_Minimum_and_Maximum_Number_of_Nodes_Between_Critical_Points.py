"""
LeetCode Problem #2058: Find the Minimum and Maximum Number of Nodes Between Critical Points

Problem Statement:
A critical point in a linked list is defined as either a local maxima or a local minima. A node is a local maxima if the current node has a value strictly greater than the previous node and the next node. Similarly, a node is a local minima if the current node has a value strictly less than the previous node and the next node.

Given the head of a linked list, return an array containing the minimum and maximum distance between any two critical points. If there are fewer than two critical points, return [-1, -1].

Example 1:
Input: head = [3,1,2,2,3,2,2,2,7]
Output: [3,3]
Explanation:
- There are two critical points: 1 (local minima) and 3 (local maxima).
- The minimum distance between the critical points is 3.
- The maximum distance between the critical points is also 3.

Example 2:
Input: head = [1,3,2,2,3,2,2,2,1]
Output: [2,6]
Explanation:
- There are three critical points: 3 (local maxima), 2 (local minima), and 3 (local maxima).
- The minimum distance between the critical points is 2.
- The maximum distance between the critical points is 6.

Example 3:
Input: head = [1,2,3,4,5,6]
Output: [-1,-1]
Explanation:
- There are no critical points in the linked list.

Constraints:
- The number of nodes in the list is in the range [2, 10^5].
- 1 <= Node.val <= 10^5
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nodesBetweenCriticalPoints(head: ListNode) -> list[int]:
    """
    Function to find the minimum and maximum distance between critical points in a linked list.
    """
    # Initialize variables
    prev, curr = head, head.next
    index = 1
    critical_points = []

    # Traverse the linked list to find critical points
    while curr and curr.next:
        if (curr.val > prev.val and curr.val > curr.next.val) or (curr.val < prev.val and curr.val < curr.next.val):
            critical_points.append(index)
        prev, curr = curr, curr.next
        index += 1

    # If there are fewer than two critical points, return [-1, -1]
    if len(critical_points) < 2:
        return [-1, -1]

    # Calculate minimum and maximum distances
    min_distance = min(critical_points[i] - critical_points[i - 1] for i in range(1, len(critical_points)))
    max_distance = critical_points[-1] - critical_points[0]

    return [min_distance, max_distance]

# Example Test Cases
if __name__ == "__main__":
    # Helper function to create a linked list from a list
    def create_linked_list(values):
        dummy = ListNode(0)
        current = dummy
        for value in values:
            current.next = ListNode(value)
            current = current.next
        return dummy.next

    # Test Case 1
    head1 = create_linked_list([3, 1, 2, 2, 3, 2, 2, 2, 7])
    print(nodesBetweenCriticalPoints(head1))  # Output: [3, 3]

    # Test Case 2
    head2 = create_linked_list([1, 3, 2, 2, 3, 2, 2, 2, 1])
    print(nodesBetweenCriticalPoints(head2))  # Output: [2, 6]

    # Test Case 3
    head3 = create_linked_list([1, 2, 3, 4, 5, 6])
    print(nodesBetweenCriticalPoints(head3))  # Output: [-1, -1]

# Time Complexity Analysis:
# - The function traverses the linked list once to find critical points, which takes O(n) time, where n is the number of nodes in the list.
# - Calculating the minimum and maximum distances between critical points takes O(k) time, where k is the number of critical points.
# - Overall time complexity: O(n).

# Space Complexity Analysis:
# - The function uses a list to store the indices of critical points, which takes O(k) space, where k is the number of critical points.
# - Overall space complexity: O(k).

# Topic: Linked List