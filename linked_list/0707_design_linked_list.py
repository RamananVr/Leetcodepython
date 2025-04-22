"""
LeetCode Question #707: Design Linked List

Problem Statement:
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
A node in a singly linked list should have two attributes: `val` and `next`. `val` is the value of the node, and `next` is a pointer/reference to the next node.
If you want to use a doubly linked list, you will need one more attribute `prev` to indicate the previous node in the linked list.

Implement the `MyLinkedList` class:
- `MyLinkedList()` Initializes the `MyLinkedList` object.
- `int get(int index)` Get the value of the `index`th node in the linked list. If the index is invalid, return `-1`.
- `void addAtHead(int val)` Add a node of value `val` before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- `void addAtTail(int val)` Append a node of value `val` as the last element of the linked list.
- `void addAtIndex(int index, int val)` Add a node of value `val` before the `index`th node in the linked list. If `index` equals the length of the linked list, the node will be appended to the end. If `index` is greater than the length, the node will not be inserted.
- `void deleteAtIndex(int index)` Delete the `index`th node in the linked list, if the index is valid.

Constraints:
- 0 <= index <= 1000
- -1000 <= val <= 1000
- The number of calls to `get`, `addAtHead`, `addAtTail`, `addAtIndex`, and `deleteAtIndex` is at most 2000.
"""

class Node:
    def __init__(self, val=0):
        self.val = val
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.val

    def addAtHead(self, val: int) -> None:
        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_node = Node(val)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            new_node = Node(val)
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        self.size -= 1

# Example Test Cases
if __name__ == "__main__":
    linked_list = MyLinkedList()
    linked_list.addAtHead(1)
    linked_list.addAtTail(3)
    linked_list.addAtIndex(1, 2)  # Linked list becomes 1->2->3
    print(linked_list.get(1))  # Output: 2
    linked_list.deleteAtIndex(1)  # Linked list becomes 1->3
    print(linked_list.get(1))  # Output: 3
    linked_list.addAtHead(0)  # Linked list becomes 0->1->3
    print(linked_list.get(0))  # Output: 0
    print(linked_list.get(2))  # Output: 3

"""
Time and Space Complexity Analysis:
1. `get(index)`:
   - Time Complexity: O(index), as we traverse the list up to the given index.
   - Space Complexity: O(1), as no extra space is used.

2. `addAtHead(val)`:
   - Time Complexity: O(1), as we directly insert the node at the head.
   - Space Complexity: O(1), as no extra space is used.

3. `addAtTail(val)`:
   - Time Complexity: O(n), as we traverse the list to find the tail.
   - Space Complexity: O(1), as no extra space is used.

4. `addAtIndex(index, val)`:
   - Time Complexity: O(index), as we traverse the list up to the given index.
   - Space Complexity: O(1), as no extra space is used.

5. `deleteAtIndex(index)`:
   - Time Complexity: O(index), as we traverse the list up to the given index.
   - Space Complexity: O(1), as no extra space is used.

Overall Space Complexity: O(n), where n is the number of nodes in the linked list.

Topic: Linked List
"""