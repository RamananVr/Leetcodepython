"""
LeetCode Problem #1634: Add Two Polynomials Represented as Linked Lists

Problem Statement:
You are given two linked lists, `poly1` and `poly2`, representing two polynomials. 
- Each node in the linked list contains two integers: `coefficient` and `power`.
- `coefficient` is the coefficient of the term, and `power` is its exponent.
- The linked list represents the polynomial in decreasing order of power.

Write a function `addPoly(poly1, poly2)` that adds the two polynomials and returns the sum as a linked list. 
The resulting linked list should also be in decreasing order of power.

Example:
Input: poly1 = [[1, 1]], poly2 = [[1, 0]]
Output: [[1, 1], [1, 0]]

Constraints:
- The number of nodes in each linked list is in the range [0, 10^4].
- The coefficient of each term is in the range [-10^4, 10^4].
- The power of each term is in the range [0, 10^4].
- poly1 and poly2 are sorted in decreasing order of power.
"""

# Definition for a polynomial term as a linked list node.
class PolyNode:
    def __init__(self, coefficient=0, power=0, next=None):
        self.coefficient = coefficient
        self.power = power
        self.next = next

def addPoly(poly1: PolyNode, poly2: PolyNode) -> PolyNode:
    """
    Adds two polynomials represented as linked lists and returns the result as a linked list.
    """
    dummy = PolyNode()  # Dummy node to simplify result list construction
    current = dummy

    while poly1 and poly2:
        if poly1.power > poly2.power:
            # Add poly1 term to the result
            current.next = PolyNode(poly1.coefficient, poly1.power)
            poly1 = poly1.next
        elif poly1.power < poly2.power:
            # Add poly2 term to the result
            current.next = PolyNode(poly2.coefficient, poly2.power)
            poly2 = poly2.next
        else:
            # Same power, add coefficients
            coefficient_sum = poly1.coefficient + poly2.coefficient
            if coefficient_sum != 0:  # Only add non-zero terms
                current.next = PolyNode(coefficient_sum, poly1.power)
            poly1 = poly1.next
            poly2 = poly2.next

        if current.next:
            current = current.next

    # Add remaining terms from poly1 or poly2
    current.next = poly1 if poly1 else poly2

    return dummy.next

# Helper function to create a linked list from a list of [coefficient, power] pairs
def create_poly_list(terms):
    dummy = PolyNode()
    current = dummy
    for coefficient, power in terms:
        current.next = PolyNode(coefficient, power)
        current = current.next
    return dummy.next

# Helper function to convert a linked list to a list of [coefficient, power] pairs
def poly_to_list(poly):
    result = []
    while poly:
        result.append([poly.coefficient, poly.power])
        poly = poly.next
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    poly1 = create_poly_list([[1, 1]])
    poly2 = create_poly_list([[1, 0]])
    result = addPoly(poly1, poly2)
    print(poly_to_list(result))  # Expected Output: [[1, 1], [1, 0]]

    # Test Case 2
    poly1 = create_poly_list([[2, 2], [4, 1], [3, 0]])
    poly2 = create_poly_list([[3, 2], [1, 1]])
    result = addPoly(poly1, poly2)
    print(poly_to_list(result))  # Expected Output: [[5, 2], [5, 1], [3, 0]]

    # Test Case 3
    poly1 = create_poly_list([[5, 3], [4, 2], [2, 1]])
    poly2 = create_poly_list([[3, 3], [-4, 2], [1, 0]])
    result = addPoly(poly1, poly2)
    print(poly_to_list(result))  # Expected Output: [[8, 3], [2, 1], [1, 0]]

"""
Time and Space Complexity Analysis:
- Time Complexity: O(n + m), where n is the number of terms in poly1 and m is the number of terms in poly2.
  This is because we traverse both linked lists once.
- Space Complexity: O(n + m), as we create a new linked list to store the result.

Topic: Linked List
"""