"""
LeetCode Problem #2211: Count Collisions on a Road

Problem Statement:
There are `n` cars on an infinitely long road. The cars are numbered from `0` to `n - 1` from left to right based on their initial positions. 
You are given a 0-indexed string `directions` of length `n`. `directions[i]` can be one of three values:
- `'L'`: The `i-th` car is moving to the left.
- `'R'`: The `i-th` car is moving to the right.
- `'S'`: The `i-th` car is stationary.

Each car can collide with other cars. When two cars collide, they become stationary. 
More formally:
- If a moving car collides with a stationary car, the moving car becomes stationary.
- If two moving cars collide, they both become stationary.

Your task is to return the total number of collisions that will happen on the road.

Example 1:
Input: directions = "RLRSLL"
Output: 5
Explanation:
- The cars at index 0 and 1 will collide, and they become stationary.
- The cars at index 2 and 3 will collide, and they become stationary.
- The cars at index 3 and 4 will collide, and they become stationary.
- The cars at index 4 and 5 will collide, and they become stationary.
There are a total of 5 collisions, so we return 5.

Example 2:
Input: directions = "LLRR"
Output: 0
Explanation:
No cars will collide, so we return 0.

Constraints:
- 1 <= directions.length <= 10^5
- directions[i] is either 'L', 'R', or 'S'.
"""

def countCollisions(directions: str) -> int:
    """
    Function to count the total number of collisions on the road.
    
    Args:
    directions (str): A string representing the directions of cars.
    
    Returns:
    int: The total number of collisions.
    """
    collisions = 0
    # Remove all leading 'L' and trailing 'R' as they will never collide
    trimmed_directions = directions.lstrip('L').rstrip('R')
    
    # Count all non-'S' characters in the trimmed string
    for char in trimmed_directions:
        if char != 'S':
            collisions += 1
    
    return collisions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    directions1 = "RLRSLL"
    print(countCollisions(directions1))  # Output: 5

    # Test Case 2
    directions2 = "LLRR"
    print(countCollisions(directions2))  # Output: 0

    # Test Case 3
    directions3 = "SSRSSRLLRSLLRSRSSRLRRRRLLRRLSSRR"
    print(countCollisions(directions3))  # Output: 20

    # Test Case 4
    directions4 = "R"
    print(countCollisions(directions4))  # Output: 0

    # Test Case 5
    directions5 = "L"
    print(countCollisions(directions5))  # Output: 0

"""
Time Complexity Analysis:
- Trimming the string using `lstrip` and `rstrip` takes O(n), where n is the length of the string.
- Iterating through the trimmed string to count collisions takes O(n).
- Overall, the time complexity is O(n).

Space Complexity Analysis:
- The space complexity is O(1) as we are using a constant amount of extra space.

Topic: Strings
"""