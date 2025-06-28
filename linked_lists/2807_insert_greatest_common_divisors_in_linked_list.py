"""
LeetCode Problem 2807: Insert Greatest Common Divisors in Linked List

Given the head of a linked list head, in which each node contains an integer value.

Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.

Return the head of the linked list after insertion.

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

Constraints:
- The number of nodes in the list is in the range [1, 5000].
- 1 <= Node.val <= 1000

Example 1:
Input: head = [18,6,10,3]
Output: [18,6,6,2,10,1,3]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
- We insert the greatest common divisor of 18 and 6 = 6 between the 1st and 2nd nodes.
- We insert the greatest common divisor of 6 and 10 = 2 between the 2nd and 3rd nodes.
- We insert the greatest common divisor of 10 and 3 = 1 between the 3rd and 4th nodes.

Example 2:
Input: head = [7]
Output: [7]
Explanation: The 1st diagram denotes the initial linked list and the 2nd diagram denotes the linked list after inserting the new nodes.
There are no pairs of adjacent nodes, so we return the initial linked list.
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        """Helper method for printing linked lists"""
        result = []
        current = self
        while current:
            result.append(str(current.val))
            current = current.next
        return " -> ".join(result)

def gcd(a, b):
    """
    Helper function to calculate greatest common divisor using Euclidean algorithm.
    
    Time Complexity: O(log(min(a, b)))
    Space Complexity: O(1)
    """
    while b:
        a, b = b, a % b
    return a

def insert_greatest_common_divisors(head):
    """
    Approach 1: Iterative Traversal with GCD Insertion
    
    Traverse the linked list and insert GCD nodes between adjacent nodes.
    
    Time Complexity: O(n * log(max_val)) where n is number of nodes
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    current = head
    
    while current and current.next:
        # Calculate GCD of current and next node values
        gcd_value = gcd(current.val, current.next.val)
        
        # Create new node with GCD value
        gcd_node = ListNode(gcd_value)
        
        # Insert the GCD node between current and current.next
        gcd_node.next = current.next
        current.next = gcd_node
        
        # Move to the node after the inserted GCD node
        current = gcd_node.next
    
    return head

def insert_greatest_common_divisors_recursive(head):
    """
    Approach 2: Recursive Solution
    
    Use recursion to insert GCD nodes.
    
    Time Complexity: O(n * log(max_val))
    Space Complexity: O(n) for recursion stack
    """
    if not head or not head.next:
        return head
    
    # Calculate GCD for current pair
    gcd_value = gcd(head.val, head.next.val)
    
    # Create GCD node
    gcd_node = ListNode(gcd_value)
    
    # Store reference to next node
    next_node = head.next
    
    # Insert GCD node
    head.next = gcd_node
    gcd_node.next = next_node
    
    # Recursively process the rest of the list
    insert_greatest_common_divisors_recursive(next_node)
    
    return head

def insert_greatest_common_divisors_two_pass(head):
    """
    Approach 3: Two-Pass Solution
    
    First pass: collect values, second pass: build new list.
    
    Time Complexity: O(n * log(max_val))
    Space Complexity: O(n)
    """
    if not head or not head.next:
        return head
    
    # First pass: collect all values
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    
    # Calculate GCDs between adjacent values
    result_values = [values[0]]
    for i in range(1, len(values)):
        gcd_value = gcd(values[i-1], values[i])
        result_values.append(gcd_value)
        result_values.append(values[i])
    
    # Second pass: build new linked list
    new_head = ListNode(result_values[0])
    current = new_head
    
    for i in range(1, len(result_values)):
        current.next = ListNode(result_values[i])
        current = current.next
    
    return new_head

def insert_greatest_common_divisors_optimized_gcd(head):
    """
    Approach 4: Optimized GCD Calculation
    
    Use optimized GCD with built-in math library.
    
    Time Complexity: O(n * log(max_val))
    Space Complexity: O(1)
    """
    import math
    
    if not head or not head.next:
        return head
    
    current = head
    
    while current and current.next:
        # Use built-in GCD function (Python 3.5+)
        gcd_value = math.gcd(current.val, current.next.val)
        
        # Create and insert GCD node
        gcd_node = ListNode(gcd_value)
        gcd_node.next = current.next
        current.next = gcd_node
        
        # Move to next original node
        current = gcd_node.next
    
    return head

def insert_greatest_common_divisors_in_place(head):
    """
    Approach 5: In-place with Careful Pointer Management
    
    More explicit pointer management for educational purposes.
    
    Time Complexity: O(n * log(max_val))
    Space Complexity: O(1)
    """
    if not head or not head.next:
        return head
    
    prev = head
    curr = head.next
    
    while curr:
        # Calculate GCD
        gcd_value = gcd(prev.val, curr.val)
        
        # Create new GCD node
        gcd_node = ListNode(gcd_value)
        
        # Insert between prev and curr
        prev.next = gcd_node
        gcd_node.next = curr
        
        # Move pointers: skip the GCD node we just inserted
        prev = curr
        curr = curr.next
    
    return head

class LinkedListWithGCD:
    """
    Approach 6: Object-Oriented Solution
    
    Encapsulate the logic in a class for better organization.
    """
    def __init__(self):
        self.head = None
    
    def from_list(self, values):
        """Create linked list from Python list"""
        if not values:
            return None
        
        self.head = ListNode(values[0])
        current = self.head
        
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        return self.head
    
    def to_list(self):
        """Convert linked list to Python list"""
        result = []
        current = self.head
        while current:
            result.append(current.val)
            current = current.next
        return result
    
    def insert_gcds(self):
        """Insert GCD nodes between adjacent nodes"""
        if not self.head or not self.head.next:
            return self.head
        
        current = self.head
        
        while current and current.next:
            gcd_value = gcd(current.val, current.next.val)
            gcd_node = ListNode(gcd_value)
            gcd_node.next = current.next
            current.next = gcd_node
            current = gcd_node.next
        
        return self.head

# Helper functions for testing
def create_linked_list(values):
    """Create linked list from list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

def linked_list_to_list(head):
    """Convert linked list to list of values"""
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

# Test cases
def test_insert_greatest_common_divisors():
    test_cases = [
        ([18, 6, 10, 3], [18, 6, 6, 2, 10, 1, 3]),
        ([7], [7]),
        ([2, 4], [2, 2, 4]),
        ([1, 2, 3], [1, 1, 2, 1, 3]),
        ([12, 18, 24], [12, 6, 18, 6, 24]),
        ([5], [5]),
        ([100, 50, 25], [100, 50, 50, 25, 25])
    ]
    
    approaches = [
        ("Iterative", insert_greatest_common_divisors),
        ("Recursive", insert_greatest_common_divisors_recursive),
        ("Two-Pass", insert_greatest_common_divisors_two_pass),
        ("Optimized GCD", insert_greatest_common_divisors_optimized_gcd),
        ("In-place", insert_greatest_common_divisors_in_place)
    ]
    
    for approach_name, func in approaches:
        print(f"Testing {approach_name} approach:")
        all_passed = True
        
        for input_vals, expected in test_cases:
            # Create fresh linked list for each test
            head = create_linked_list(input_vals)
            result_head = func(head)
            result_vals = linked_list_to_list(result_head)
            
            passed = result_vals == expected
            if not passed:
                all_passed = False
            
            print(f"  Input: {input_vals}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result_vals}")
            print(f"  {'✓' if passed else '✗'}\n")
        
        print(f"  Overall: {'✓ All Passed' if all_passed else '✗ Some Failed'}\n")
    
    # Test OOP approach
    print("Testing Object-Oriented approach:")
    ll = LinkedListWithGCD()
    
    for input_vals, expected in test_cases:
        ll.from_list(input_vals)
        ll.insert_gcds()
        result_vals = ll.to_list()
        
        passed = result_vals == expected
        print(f"  Input: {input_vals}")
        print(f"  Expected: {expected}")
        print(f"  Got: {result_vals}")
        print(f"  {'✓' if passed else '✗'}\n")

if __name__ == "__main__":
    test_insert_greatest_common_divisors()

"""
Topics: Linked List, Math, GCD
Difficulty: Medium

Key Insights:
1. GCD calculation using Euclidean algorithm
2. Careful pointer management when inserting nodes
3. Handle edge cases: single node, empty list
4. Can be solved iteratively or recursively
5. Built-in math.gcd() available in Python 3.5+

Companies: Microsoft, Amazon, Google, Apple
"""
