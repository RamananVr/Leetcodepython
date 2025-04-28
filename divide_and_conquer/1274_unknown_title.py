"""
LeetCode Problem #1274: Number of Ships in a Rectangle

Problem Statement:
On the sea represented as a Cartesian plane, there are `ships` located at integer coordinates. Each ship can be considered as a single point. You have a function `Sea.hasShips(topRight, bottomLeft)` which returns `true` if there is at least one ship in the rectangle represented by `topRight` and `bottomLeft` coordinates, otherwise it returns `false`.

Given two points `topRight` and `bottomLeft` which define a rectangle, return the number of ships present in that rectangle. The rectangle's edges are parallel to the coordinate axes.

Constraints:
- `topRight` and `bottomLeft` are integer coordinates.
- `bottomLeft.x <= topRight.x` and `bottomLeft.y <= topRight.y`.
- The function `Sea.hasShips(topRight, bottomLeft)` can be called with any coordinates as long as they fall within the input rectangle.
- You cannot call `Sea.hasShips` more than 400 times.
- There are at most 10 ships in the rectangle.

Note:
- This problem is an interactive problem, meaning you need to implement the solution using the provided `Sea` class interface.

"""

# Python Solution
class Solution:
    def countShips(self, sea: 'Sea', topRight: List[int], bottomLeft: List[int]) -> int:
        # Base case: If the rectangle is reduced to a single point
        if bottomLeft[0] > topRight[0] or bottomLeft[1] > topRight[1]:
            return 0
        
        # Check if there are ships in the current rectangle
        if not sea.hasShips(topRight, bottomLeft):
            return 0
        
        # If the rectangle is a single point and has a ship
        if bottomLeft == topRight:
            return 1
        
        # Divide the rectangle into four smaller rectangles
        midX = (bottomLeft[0] + topRight[0]) // 2
        midY = (bottomLeft[1] + topRight[1]) // 2
        
        # Recursively count ships in each sub-rectangle
        topLeftCount = self.countShips(sea, [midX, topRight[1]], [bottomLeft[0], midY + 1])
        topRightCount = self.countShips(sea, topRight, [midX + 1, midY + 1])
        bottomLeftCount = self.countShips(sea, [midX, midY], bottomLeft)
        bottomRightCount = self.countShips(sea, [topRight[0], midY], [midX + 1, bottomLeft[1]])
        
        # Sum up the counts from all sub-rectangles
        return topLeftCount + topRightCount + bottomLeftCount + bottomRightCount

# Example Test Cases
class Sea:
    def __init__(self, ships: List[List[int]]):
        self.ships = set(tuple(ship) for ship in ships)
    
    def hasShips(self, topRight: List[int], bottomLeft: List[int]) -> bool:
        for x in range(bottomLeft[0], topRight[0] + 1):
            for y in range(bottomLeft[1], topRight[1] + 1):
                if (x, y) in self.ships:
                    return True
        return False

# Test Case 1
sea = Sea([[1, 1], [2, 2], [3, 3]])
solution = Solution()
print(solution.countShips(sea, [4, 4], [0, 0]))  # Output: 3

# Test Case 2
sea = Sea([[1, 1]])
solution = Solution()
print(solution.countShips(sea, [1, 1], [0, 0]))  # Output: 1

# Test Case 3
sea = Sea([])
solution = Solution()
print(solution.countShips(sea, [4, 4], [0, 0]))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm uses a divide-and-conquer approach, splitting the rectangle into four smaller rectangles at each step.
- In the worst case, the rectangle is divided until it reaches individual points, resulting in O(log(maxX) * log(maxY)) recursive calls, where maxX and maxY are the dimensions of the rectangle.
- Each call to `Sea.hasShips` is O(1), so the overall complexity is O(log(maxX) * log(maxY)).

Space Complexity:
- The space complexity is determined by the recursion stack. In the worst case, the depth of the recursion is O(log(maxX) + log(maxY)).
- Therefore, the space complexity is O(log(maxX) + log(maxY)).
"""

# Topic: Divide and Conquer