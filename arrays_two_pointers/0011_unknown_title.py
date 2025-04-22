"""
LeetCode Problem #11: Container With Most Water

Problem Statement:
You are given an integer array `height` of length `n`. There are `n` vertical lines drawn such that the two endpoints of the i-th line are `(i, 0)` and `(i, height[i])`.

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Constraints:
- `n == height.length`
- `2 <= n <= 10^5`
- `0 <= height[i] <= 10^4`
"""

def maxArea(height):
    """
    Function to calculate the maximum area of water a container can store.

    :param height: List[int] - List of heights of vertical lines
    :return: int - Maximum area of water that can be contained
    """
    left, right = 0, len(height) - 1
    max_area = 0

    while left < right:
        # Calculate the area formed by the lines at indices `left` and `right`
        width = right - left
        current_area = min(height[left], height[right]) * width
        max_area = max(max_area, current_area)

        # Move the pointer pointing to the shorter line inward
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return max_area

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    height1 = [1,8,6,2,5,4,8,3,7]
    print("Test Case 1: Expected Output = 49, Actual Output =", maxArea(height1))

    # Test Case 2
    height2 = [1,1]
    print("Test Case 2: Expected Output = 1, Actual Output =", maxArea(height2))

    # Test Case 3
    height3 = [4,3,2,1,4]
    print("Test Case 3: Expected Output = 16, Actual Output =", maxArea(height3))

    # Test Case 4
    height4 = [1,2,1]
    print("Test Case 4: Expected Output = 2, Actual Output =", maxArea(height4))

"""
Time Complexity Analysis:
- The algorithm uses a two-pointer approach, where each pointer moves inward at most `n` times.
- Therefore, the time complexity is O(n), where `n` is the length of the `height` array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space, as it only uses a few variables (`left`, `right`, `max_area`, etc.).
- Therefore, the space complexity is O(1).

Topic: Arrays, Two Pointers
"""