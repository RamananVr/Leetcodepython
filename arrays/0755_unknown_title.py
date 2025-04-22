"""
LeetCode Problem #755: Pour Water

Problem Statement:
You are given an elevation map representing the heights of terrain along a 1D line, 
and a volume of water to pour across the terrain. You must simulate the water pouring 
process and return the resulting elevation map after all the water has been poured.

In the elevation map, heights[i] represents the height of the terrain at index i. 
You are also given an integer V representing the volume of water (in units) to pour, 
and an integer K representing the index where the water will be poured.

Rules for pouring water:
1. Water first tries to move left. It moves left if the height at the current index is 
   greater than the height at the next index to the left. If there are multiple indices 
   with the same height, water will settle at the leftmost index.
2. If water cannot move left, it tries to move right. It moves right if the height at 
   the current index is greater than the height at the next index to the right. If there 
   are multiple indices with the same height, water will settle at the rightmost index.
3. If water cannot move left or right, it settles at the current index.

Return the resulting elevation map after all the water has been poured.

Constraints:
- heights is a list of integers with length between 1 and 100.
- heights[i] is an integer between 0 and 100.
- V is an integer between 0 and 1000.
- K is an integer between 0 and len(heights) - 1.
"""

def pourWater(heights, V, K):
    """
    Simulates pouring water on the elevation map.

    :param heights: List[int] - The elevation map.
    :param V: int - The volume of water to pour.
    :param K: int - The index where water is poured.
    :return: List[int] - The resulting elevation map after pouring water.
    """
    for _ in range(V):
        # Try to move left
        pos = K
        while pos > 0 and heights[pos] >= heights[pos - 1]:
            pos -= 1
        if pos != K and heights[pos] < heights[pos + 1]:
            heights[pos] += 1
            continue

        # Try to move right
        pos = K
        while pos < len(heights) - 1 and heights[pos] >= heights[pos + 1]:
            pos += 1
        if pos != K and heights[pos] < heights[pos - 1]:
            heights[pos] += 1
            continue

        # Settle at the current position
        heights[K] += 1

    return heights

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    heights = [2, 1, 1, 2, 1, 2, 2]
    V = 4
    K = 3
    print(pourWater(heights, V, K))  # Expected Output: [2, 2, 2, 3, 2, 2, 2]

    # Test Case 2
    heights = [1, 2, 3, 4]
    V = 2
    K = 2
    print(pourWater(heights, V, K))  # Expected Output: [1, 2, 4, 4]

    # Test Case 3
    heights = [3, 1, 3]
    V = 5
    K = 1
    print(pourWater(heights, V, K))  # Expected Output: [4, 4, 4]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each unit of water (V), we may traverse the elevation map up to its full length (len(heights)).
- Therefore, the time complexity is O(V * len(heights)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays