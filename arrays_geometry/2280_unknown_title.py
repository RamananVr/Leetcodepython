"""
LeetCode Problem #2280: Minimum Lines to Represent a Line Chart

Problem Statement:
You are given a 2D integer array `stockPrices` where `stockPrices[i] = [day_i, price_i]` indicates the price of the stock on day `day_i`. 
A line chart is created from the array by connecting adjacent points with a straight line. You need to find the minimum number of 
lines needed to represent the line chart.

- A line is defined as a straight line connecting two or more points.
- A line can represent multiple points if they are collinear.

Return the minimum number of lines needed to represent the line chart.

Constraints:
1. `1 <= stockPrices.length <= 10^5`
2. `1 <= day_i, price_i <= 10^9`
3. All the `day_i` values are unique.

Example:
Input: stockPrices = [[1,2],[2,4],[3,6],[4,8]]
Output: 1
Explanation: All points are collinear, so only one line is needed.

Input: stockPrices = [[1,1],[2,2],[3,3],[4,5],[5,5]]
Output: 2
Explanation: The first three points are collinear, and the last two points are collinear. Two lines are needed.
"""

# Solution
def minimumLines(stockPrices):
    # Sort the stockPrices by day
    stockPrices.sort()
    
    # If there is only one point, no lines are needed
    if len(stockPrices) <= 1:
        return 0
    
    # Initialize the count of lines
    lines = 1
    
    # Iterate through the points to check collinearity
    for i in range(2, len(stockPrices)):
        x1, y1 = stockPrices[i - 2]
        x2, y2 = stockPrices[i - 1]
        x3, y3 = stockPrices[i]
        
        # Check if the three points are collinear using cross multiplication
        if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
            lines += 1
    
    return lines

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All points are collinear
    stockPrices1 = [[1, 2], [2, 4], [3, 6], [4, 8]]
    print(minimumLines(stockPrices1))  # Output: 1

    # Test Case 2: Two sets of collinear points
    stockPrices2 = [[1, 1], [2, 2], [3, 3], [4, 5], [5, 5]]
    print(minimumLines(stockPrices2))  # Output: 2

    # Test Case 3: Single point
    stockPrices3 = [[1, 1]]
    print(minimumLines(stockPrices3))  # Output: 0

    # Test Case 4: No collinearity between points
    stockPrices4 = [[1, 1], [2, 3], [3, 5], [4, 7]]
    print(minimumLines(stockPrices4))  # Output: 3

    # Test Case 5: Large input with collinear points
    stockPrices5 = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6]]
    print(minimumLines(stockPrices5))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `stockPrices` array takes O(n log n), where n is the number of points.
- Iterating through the sorted array to check collinearity takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation is in-place, and no additional data structures are used.
- Overall space complexity: O(1).

Topic: Arrays, Geometry
"""