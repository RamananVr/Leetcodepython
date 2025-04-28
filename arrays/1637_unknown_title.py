"""
LeetCode Problem #1637: Widest Vertical Area Between Two Points Containing No Points

Problem Statement:
Given `points`, a 2D array where `points[i] = [xi, yi]` represents the coordinates of a point on a 2D plane, 
return the widest vertical area between two points such that no points are inside the area. 
A vertical area is defined as a space between two vertical lines.

The widest vertical area is the maximum difference between two consecutive x-coordinates in the sorted order of x-coordinates.

Constraints:
- 2 <= points.length <= 10^5
- points[i].length == 2
- 0 <= xi, yi <= 10^9

Example:
Input: points = [[8,7],[9,9],[7,4],[9,7]]
Output: 1
Explanation: The x-coordinates of the points are [8,9,7,9]. After sorting, we get [7,8,9,9]. 
The maximum difference between consecutive x-coordinates is 1.

"""

# Solution
def maxWidthOfVerticalArea(points):
    """
    Finds the widest vertical area between two points containing no points.

    :param points: List[List[int]] - List of points represented as [xi, yi]
    :return: int - Maximum width of vertical area
    """
    # Extract x-coordinates and sort them
    x_coords = sorted(point[0] for point in points)
    
    # Find the maximum difference between consecutive x-coordinates
    max_width = max(x_coords[i] - x_coords[i - 1] for i in range(1, len(x_coords)))
    
    return max_width

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    points1 = [[8,7],[9,9],[7,4],[9,7]]
    print(maxWidthOfVerticalArea(points1))  # Output: 1

    # Test Case 2
    points2 = [[1,5],[3,8],[6,2],[10,4]]
    print(maxWidthOfVerticalArea(points2))  # Output: 4

    # Test Case 3
    points3 = [[1,1],[2,2],[3,3],[4,4],[5,5]]
    print(maxWidthOfVerticalArea(points3))  # Output: 1

    # Test Case 4
    points4 = [[100,200],[300,400],[500,600],[700,800]]
    print(maxWidthOfVerticalArea(points4))  # Output: 200

    # Test Case 5
    points5 = [[0,0],[1000000000,1000000000]]
    print(maxWidthOfVerticalArea(points5))  # Output: 1000000000

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the x-coordinates takes O(n log n), where n is the number of points.
- Calculating the maximum difference between consecutive x-coordinates takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space required to store the sorted x-coordinates is O(n).
- Overall space complexity: O(n).

Topic: Arrays
"""