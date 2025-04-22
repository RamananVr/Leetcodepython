"""
LeetCode Problem #492: Construct the Rectangle

Problem Statement:
A web developer needs to design a rectangular web page. Given an area `area`, your task is to design a rectangle with the following requirements:

1. The area of the rectangle must equal the given `area`.
2. The width `W` and the length `L` of the rectangle must satisfy the following conditions:
   - `L * W == area`
   - `L >= W`
   - The difference `L - W` should be as small as possible.

Return an array `[L, W]` where `L` is the length and `W` is the width of the rectangle.

Constraints:
- 1 <= area <= 10^7
"""

def constructRectangle(area: int) -> list[int]:
    """
    Finds the dimensions of the rectangle (L, W) such that:
    - L * W == area
    - L >= W
    - L - W is minimized
    """
    # Start with the largest possible square root of the area
    W = int(area**0.5)
    
    # Decrease W until we find a valid width that divides the area
    while area % W != 0:
        W -= 1
    
    # Calculate the corresponding length
    L = area // W
    
    return [L, W]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    area = 4
    print(constructRectangle(area))  # Output: [2, 2]

    # Test Case 2
    area = 37
    print(constructRectangle(area))  # Output: [37, 1]

    # Test Case 3
    area = 122122
    print(constructRectangle(area))  # Output: [427, 286]

    # Test Case 4
    area = 1
    print(constructRectangle(area))  # Output: [1, 1]

"""
Time Complexity Analysis:
- The algorithm starts with the square root of the area and iteratively decrements W until it finds a divisor.
- In the worst case, W starts at sqrt(area) and decrements to 1, which takes O(sqrt(area)) iterations.
- Each iteration involves a modulo operation, which is O(1).
- Therefore, the overall time complexity is O(sqrt(area)).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Math
"""