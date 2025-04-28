"""
LeetCode Problem #2848: Points That Intersect With Cars

Problem Statement:
You are given a 2D integer array `cars` where each `cars[i] = [start_i, end_i]` represents the start and end positions 
of the i-th car on a number line. The start and end positions are inclusive.

Return the number of integer points on the number line that are covered by at least one car.

Example 1:
Input: cars = [[1, 3], [2, 5], [7, 8]]
Output: 6
Explanation: The points covered by the cars are {1, 2, 3, 4, 5, 7, 8}. There are 6 unique points.

Example 2:
Input: cars = [[1, 2], [2, 3], [3, 4]]
Output: 4
Explanation: The points covered by the cars are {1, 2, 3, 4}. There are 4 unique points.

Constraints:
- 1 <= cars.length <= 1000
- cars[i].length == 2
- 0 <= start_i <= end_i <= 1000
"""

# Python Solution
def number_of_points(cars):
    """
    This function calculates the number of unique integer points on the number line
    that are covered by at least one car.

    :param cars: List[List[int]] - A list of intervals representing the start and end positions of cars.
    :return: int - The number of unique points covered by at least one car.
    """
    covered_points = set()
    
    for start, end in cars:
        for point in range(start, end + 1):
            covered_points.add(point)
    
    return len(covered_points)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cars1 = [[1, 3], [2, 5], [7, 8]]
    print(number_of_points(cars1))  # Output: 6

    # Test Case 2
    cars2 = [[1, 2], [2, 3], [3, 4]]
    print(number_of_points(cars2))  # Output: 4

    # Test Case 3
    cars3 = [[0, 0], [1, 1], [2, 2]]
    print(number_of_points(cars3))  # Output: 3

    # Test Case 4
    cars4 = [[0, 5], [3, 7], [6, 10]]
    print(number_of_points(cars4))  # Output: 11

    # Test Case 5
    cars5 = [[0, 1000]]
    print(number_of_points(cars5))  # Output: 1001

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n be the number of cars.
- For each car, we iterate over the range from start to end (inclusive). In the worst case, the range can be up to 1000.
- Therefore, the time complexity is O(n * k), where k is the average range length of the cars.

Space Complexity:
- We use a set to store the unique points. In the worst case, the set can contain up to 1001 points (0 to 1000).
- Therefore, the space complexity is O(1001) = O(1) (constant space with respect to the input size).
"""

# Topic: Arrays, HashSet