"""
LeetCode Question #1232: Check If It Is a Straight Line

Problem Statement:
You are given an array `coordinates`, `coordinates[i] = [x, y]`, where `[x, y]` represents the coordinates of a point on a 2D plane. 
Determine if these points make a straight line in the 2D plane.

Example 1:
Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true

Example 2:
Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false

Constraints:
- 2 <= coordinates.length <= 1000
- coordinates[i].length == 2
- -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
- coordinates contains no duplicate point.
"""

def checkStraightLine(coordinates):
    """
    Function to check if the given points lie on a straight line.

    :param coordinates: List[List[int]] - List of points on a 2D plane
    :return: bool - True if points lie on a straight line, False otherwise
    """
    # Extract the first two points to calculate the slope
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    
    # Calculate the slope using the difference in x and y
    # Instead of using division (to avoid floating-point precision issues), use cross multiplication
    dx, dy = x1 - x0, y1 - y0
    
    # Check the slope for all subsequent points
    for i in range(2, len(coordinates)):
        x, y = coordinates[i]
        # Use cross multiplication to check if the slopes are equal
        if (y - y0) * dx != (x - x0) * dy:
            return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Points lie on a straight line
    coordinates1 = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    print(checkStraightLine(coordinates1))  # Output: True

    # Test Case 2: Points do not lie on a straight line
    coordinates2 = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
    print(checkStraightLine(coordinates2))  # Output: False

    # Test Case 3: Only two points (always a straight line)
    coordinates3 = [[0,0],[1,1]]
    print(checkStraightLine(coordinates3))  # Output: True

    # Test Case 4: Horizontal line
    coordinates4 = [[1,5],[2,5],[3,5],[4,5]]
    print(checkStraightLine(coordinates4))  # Output: True

    # Test Case 5: Vertical line
    coordinates5 = [[3,1],[3,2],[3,3],[3,4]]
    print(checkStraightLine(coordinates5))  # Output: True

"""
Time Complexity:
- The function iterates through the list of coordinates once, performing constant-time operations for each point.
- Let n = len(coordinates). The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables (dx, dy, etc.).
- The space complexity is O(1).

Topic: Geometry
"""