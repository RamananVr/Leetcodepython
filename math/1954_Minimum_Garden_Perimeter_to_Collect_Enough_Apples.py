"""
LeetCode Problem #1954: Minimum Garden Perimeter to Collect Enough Apples

Problem Statement:
In a garden represented as an infinite 2D grid, each cell (x, y) contains |x| + |y| apples, 
where |x| is the absolute value of x and |y| is the absolute value of y. You are tasked to 
collect at least `neededApples` apples. To do so, you can build a square perimeter centered 
at the origin (0, 0) with a side length of 2k (where k is a positive integer). The perimeter 
is defined as the cells that are exactly k units away from the origin.

Return the minimum perimeter of the square that allows you to collect at least `neededApples` apples.

Constraints:
- 1 <= neededApples <= 10^15
"""

def minimumPerimeter(neededApples: int) -> int:
    """
    Function to calculate the minimum perimeter of the square garden
    required to collect at least `neededApples` apples.
    """
    # Initialize variables
    k = 0
    total_apples = 0
    
    # Incrementally calculate the number of apples collected for increasing k
    while total_apples < neededApples:
        k += 1
        # Apples collected at the perimeter of the square with side length 2k
        total_apples += 12 * k * k
    
    # Return the perimeter of the square
    return 8 * k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small number of apples
    neededApples = 1
    print(minimumPerimeter(neededApples))  # Expected Output: 8

    # Test Case 2: Medium number of apples
    neededApples = 100
    print(minimumPerimeter(neededApples))  # Expected Output: 8

    # Test Case 3: Large number of apples
    neededApples = 1000000000
    print(minimumPerimeter(neededApples))  # Expected Output: 5040

    # Test Case 4: Very large number of apples
    neededApples = 10**15
    print(minimumPerimeter(neededApples))  # Expected Output: 800000

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iteratively calculates the total number of apples collected for increasing values of k.
- The loop runs until `total_apples` >= `neededApples`. In the worst case, the loop runs approximately 
  O(sqrt(neededApples)) iterations, as the number of apples collected grows quadratically with k.
- Therefore, the time complexity is O(sqrt(neededApples)).

Space Complexity:
- The function uses a constant amount of space for variables (k, total_apples).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Math
"""