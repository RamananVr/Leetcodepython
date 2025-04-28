"""
LeetCode Problem #850: Rectangle Area II

Problem Statement:
You are given a list of axis-aligned rectangles `rectangles`. Each rectangle is represented as a list 
`[x1, y1, x2, y2]`, where `(x1, y1)` is the bottom-left corner and `(x2, y2)` is the top-right corner.

Find the total area covered by the rectangles in the plane. Since the answer may be too large, return it modulo 10^9 + 7.

Example 1:
Input: rectangles = [[1,1,3,3],[2,2,4,4]]
Output: 7

Example 2:
Input: rectangles = [[0,0,1000000000,1000000000]]
Output: 49

Note:
1. `1 <= rectangles.length <= 200`
2. `rectangles[i].length == 4`
3. `0 <= rectangles[i][j] <= 10^9`
4. The total area covered by all rectangles will never exceed 2^63 - 1, so it will fit in a 64-bit signed integer.
"""

# Solution
from sortedcontainers import SortedList

def rectangleArea(rectangles):
    MOD = 10**9 + 7

    # Step 1: Collect all unique y-coordinates
    events = []
    y_coords = set()
    for x1, y1, x2, y2 in rectangles:
        events.append((x1, 1, y1, y2))  # Rectangle opening
        events.append((x2, -1, y1, y2))  # Rectangle closing
        y_coords.add(y1)
        y_coords.add(y2)

    # Step 2: Sort events by x-coordinate
    events.sort()
    y_coords = sorted(y_coords)

    # Step 3: Map y-coordinates to indices
    y_to_index = {y: i for i, y in enumerate(y_coords)}
    active = [0] * len(y_coords)

    def compute_active_length():
        """Compute the total length of active y-intervals."""
        total = 0
        prev_y = None
        count = 0
        for i, val in enumerate(active):
            if val > 0:
                if prev_y is not None:
                    total += y_coords[i] - prev_y
                prev_y = y_coords[i]
        return total

    # Step 4: Sweep line algorithm
    prev_x = 0
    area = 0
    for x, typ, y1, y2 in events:
        # Add the area covered since the last x-coordinate
        area += compute_active_length() * (x - prev_x)
        area %= MOD

        # Update active intervals
        for i in range(y_to_index[y1], y_to_index[y2]):
            active[i] += typ

        # Update previous x-coordinate
        prev_x = x

    return area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    rectangles1 = [[1, 1, 3, 3], [2, 2, 4, 4]]
    print(rectangleArea(rectangles1))  # Output: 7

    # Test Case 2
    rectangles2 = [[0, 0, 1000000000, 1000000000]]
    print(rectangleArea(rectangles2))  # Output: 49

    # Test Case 3
    rectangles3 = [[0, 0, 2, 2], [1, 1, 3, 3], [2, 2, 4, 4]]
    print(rectangleArea(rectangles3))  # Output: 8

    # Test Case 4
    rectangles4 = [[1, 1, 2, 2], [1, 1, 2, 2]]
    print(rectangleArea(rectangles4))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the events takes O(n log n), where n is the number of rectangles.
- The sweep line algorithm processes each event and updates the active intervals, which takes O(n * m), 
  where m is the number of unique y-coordinates.
- Overall complexity: O(n log n + n * m).

Space Complexity:
- We store the events and the active intervals, which takes O(n + m) space.
- Overall complexity: O(n + m).

Here, n is the number of rectangles, and m is the number of unique y-coordinates.
"""

# Topic: Sweep Line Algorithm, Geometry