"""
LeetCode Question #1265: Print Immutable Linked List in Reverse

Problem Statement:
You are given an immutable linked list, print out all values of each node in reverse with the help of the following interface:

- ImmutableListNode:
  - ImmutableListNode is an interface of immutable linked list, you are given the head of the list.
  - You cannot modify the linked list in any way.
  - You can only access the node using the following functions:
    - ImmutableListNode.printValue(): Print the value of the current node.
    - ImmutableListNode.getNext(): Return the next node.

The input is only given to the function `printLinkedListInReverse`, and you are not allowed to use any other helper function or data structure.

Constraints:
- The number of nodes in the linked list is between [1, 1000].
- The value of each node is between [1, 10^6].

Your task is to implement the function `printLinkedListInReverse(head: ImmutableListNode) -> None` that prints the values of the linked list in reverse order.

"""

# Clean and Correct Python Solution
def printLinkedListInReverse(head: 'ImmutableListNode') -> None:
    """
    Prints the values of an immutable linked list in reverse order.
    """
    if head is None:
        return
    # Recursive call to the next node
    next_node = head.getNext()
    if next_node is not None:
        printLinkedListInReverse(next_node)
    # Print the current node's value after the recursive call
    head.printValue()

# Example Test Cases
class ImmutableListNode:
    """
    Mock implementation of ImmutableListNode for testing purposes.
    """
    def __init__(self, value, next_node=None):
        self.value = value
        self.next_node = next_node

    def printValue(self):
        print(self.value)

    def getNext(self):
        return self.next_node

# Helper function to create an immutable linked list
def create_immutable_linked_list(values):
    if not values:
        return None
    head = ImmutableListNode(values[0])
    current = head
    for value in values[1:]:
        next_node = ImmutableListNode(value)
        current.next_node = next_node
        current = next_node
    return head

# Test Case 1
print("Test Case 1:")
head1 = create_immutable_linked_list([1, 2, 3, 4, 5])
printLinkedListInReverse(head1)  # Expected Output: 5 4 3 2 1 (each on a new line)

# Test Case 2
print("\nTest Case 2:")
head2 = create_immutable_linked_list([10, 20, 30])
printLinkedListInReverse(head2)  # Expected Output: 30 20 10 (each on a new line)

# Test Case 3
print("\nTest Case 3:")
head3 = create_immutable_linked_list([42])
printLinkedListInReverse(head3)  # Expected Output: 42 (single line)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function makes a single recursive call for each node in the linked list.
- If there are `n` nodes in the linked list, the time complexity is O(n).

Space Complexity:
- The function uses the call stack for recursion. In the worst case, the depth of the recursion is equal to the number of nodes in the linked list.
- Therefore, the space complexity is O(n) due to the recursive stack.

Topic: Linked List, Recursion
"""