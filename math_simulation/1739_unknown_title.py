"""
LeetCode Problem #1739: Building Boxes

Problem Statement:
You have a number of boxes `n`. You want to build a pyramid with these boxes. A pyramid is constructed as follows:
- The first row has 1 box.
- The second row has 2 boxes.
- The third row has 3 boxes, and so on.

Each row must contain strictly more boxes than the previous row. You want to use all `n` boxes to build the pyramid, but you may not be able to use all of them. Return the minimum number of boxes required to build the largest possible pyramid.

Constraints:
- 1 <= n <= 10^9
"""

def minimumBoxes(n: int) -> int:
    """
    Calculate the minimum number of boxes required to build the largest pyramid
    using n boxes.
    """
    # Step 1: Find the maximum number of complete layers that can be formed
    total_layers = 0
    layer_sum = 0
    while layer_sum + (total_layers + 1) * (total_layers + 2) // 2 <= n:
        total_layers += 1
        layer_sum += total_layers * (total_layers + 1) // 2

    # Step 2: Calculate the remaining boxes needed to complete the pyramid
    remaining_boxes = n - layer_sum
    base_boxes = 0
    while base_boxes * (base_boxes + 1) // 2 < remaining_boxes:
        base_boxes += 1

    return total_layers * (total_layers + 1) // 2 + base_boxes


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 10
    print(minimumBoxes(n))  # Expected Output: 6

    # Test Case 2
    n = 15
    print(minimumBoxes(n))  # Expected Output: 10

    # Test Case 3
    n = 20
    print(minimumBoxes(n))  # Expected Output: 10

    # Test Case 4
    n = 1
    print(minimumBoxes(n))  # Expected Output: 1

    # Test Case 5
    n = 1000000000
    print(minimumBoxes(n))  # Expected Output: Large number, depends on calculation


"""
Time and Space Complexity Analysis:

Time Complexity:
- The first loop iterates to find the maximum number of complete layers. This involves summing up triangular numbers, which is logarithmic in nature due to the quadratic growth of triangular numbers. Thus, the complexity is O(sqrt(n)).
- The second loop iterates to find the minimum number of base boxes required to cover the remaining boxes. This is also logarithmic in nature, resulting in O(sqrt(n)).
- Overall, the time complexity is O(sqrt(n)).

Space Complexity:
- The algorithm uses a constant amount of space for variables. Thus, the space complexity is O(1).

Topic: Math, Simulation
"""