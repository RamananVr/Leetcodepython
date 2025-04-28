"""
LeetCode Question #1515: Best Position for a Service Centre

Problem Statement:
A delivery company wants to build a new service center in a new city. The company has selected several possible locations for the service center based on the positions of their customers. The positions of the customers are given as a 2D array `positions` where `positions[i] = [xi, yi]` represents the position of the ith customer.

The service center should be positioned such that the sum of the Euclidean distances from the service center to all customers is minimized.

Return the minimum sum of Euclidean distances between the service center and all customers.

The answer should be within 10^-5 of the actual value.

Constraints:
- 1 <= positions.length <= 50
- positions[i].length == 2
- 0 <= positions[i][0], positions[i][1] <= 100
"""

from typing import List
import math

def getMinDistSum(positions: List[List[int]]) -> float:
    """
    Finds the best position for a service center to minimize the sum of Euclidean distances
    to all customers.
    """
    def calculate_total_distance(x, y):
        """Calculate the total Euclidean distance from (x, y) to all customer positions."""
        return sum(math.sqrt((x - px)**2 + (y - py)**2) for px, py in positions)

    # Gradient descent parameters
    learning_rate = 0.1
    precision = 1e-6
    max_iterations = 10000

    # Start at the centroid of the positions
    x = sum(pos[0] for pos in positions) / len(positions)
    y = sum(pos[1] for pos in positions) / len(positions)

    for _ in range(max_iterations):
        # Calculate the gradient
        grad_x = sum((x - px) / math.sqrt((x - px)**2 + (y - py)**2) for px, py in positions)
        grad_y = sum((y - py) / math.sqrt((x - px)**2 + (y - py)**2) for px, py in positions)

        # Update the position using the gradient
        new_x = x - learning_rate * grad_x
        new_y = y - learning_rate * grad_y

        # Check for convergence
        if abs(new_x - x) < precision and abs(new_y - y) < precision:
            break

        x, y = new_x, new_y

    return calculate_total_distance(x, y)

# Example Test Cases
if __name__ == "__main__":
    positions1 = [[0, 1], [1, 0], [1, 2], [2, 1]]
    positions2 = [[1, 1], [3, 3]]
    positions3 = [[0, 0], [0, 100], [100, 0], [100, 100]]

    print(f"Test Case 1: {getMinDistSum(positions1)}")  # Expected output: ~4.0
    print(f"Test Case 2: {getMinDistSum(positions2)}")  # Expected output: ~2.82843
    print(f"Test Case 3: {getMinDistSum(positions3)}")  # Expected output: ~200.0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses gradient descent, which iteratively updates the position of the service center.
- For each iteration, we compute the gradient, which involves calculating the Euclidean distance for all positions.
- Let n = len(positions). Each iteration takes O(n) time, and the number of iterations is bounded by max_iterations.
- Therefore, the time complexity is O(n * max_iterations).

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `x`, `y`, `grad_x`, and `grad_y`.
- The space complexity is O(1).

Topic: Geometry, Optimization
"""