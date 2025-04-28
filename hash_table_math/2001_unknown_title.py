"""
LeetCode Problem #2001: Number of Pairs of Interchangeable Rectangles

Problem Statement:
You are given n rectangles represented by a 2D integer array rectangles where rectangles[i] = [width_i, height_i] 
denotes the width and height of the ith rectangle.

Two rectangles i and j (i < j) are considered interchangeable if they have the same width-to-height ratio. 
More formally, two rectangles are interchangeable if width_i / height_i == width_j / height_j (using floating-point division).

Return the number of pairs of interchangeable rectangles.

Constraints:
- 1 <= rectangles.length <= 10^5
- 1 <= width_i, height_i <= 10^5
"""

from collections import defaultdict
from math import gcd

def interchangeableRectangles(rectangles):
    """
    Function to calculate the number of pairs of interchangeable rectangles.

    Args:
    rectangles (List[List[int]]): A list of rectangles where each rectangle is represented as [width, height].

    Returns:
    int: The number of pairs of interchangeable rectangles.
    """
    ratio_count = defaultdict(int)
    interchangeable_pairs = 0

    for width, height in rectangles:
        # Reduce the width and height to their simplest ratio using gcd
        g = gcd(width, height)
        reduced_ratio = (width // g, height // g)
        
        # Count the number of pairs that can be formed with the current ratio
        interchangeable_pairs += ratio_count[reduced_ratio]
        
        # Update the count of this ratio
        ratio_count[reduced_ratio] += 1

    return interchangeable_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rectangles1 = [[4, 8], [2, 4], [6, 12], [3, 6]]
    print(interchangeableRectangles(rectangles1))  # Output: 6

    # Test Case 2
    rectangles2 = [[4, 5], [7, 8]]
    print(interchangeableRectangles(rectangles2))  # Output: 0

    # Test Case 3
    rectangles3 = [[10, 20], [5, 10], [2, 4], [8, 16], [1, 2]]
    print(interchangeableRectangles(rectangles3))  # Output: 10

    # Test Case 4
    rectangles4 = [[1, 1], [1, 1], [1, 1]]
    print(interchangeableRectangles(rectangles4))  # Output: 3

"""
Time Complexity Analysis:
- Calculating the gcd for each rectangle takes O(log(min(width, height))).
- Iterating through the rectangles array takes O(n), where n is the number of rectangles.
- Thus, the overall time complexity is O(n * log(min(width, height))).

Space Complexity Analysis:
- The space complexity is O(k), where k is the number of unique reduced ratios stored in the dictionary.

Topic: Hash Table, Math
"""