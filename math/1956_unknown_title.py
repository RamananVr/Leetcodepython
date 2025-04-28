"""
LeetCode Problem #1956: Minimum Time For K Virus Variants to Spread

Problem Statement:
You are given an integer `n` representing the number of cities, and an integer `k` representing the number of virus variants. 
The cities are arranged in a straight line, and the virus variants start spreading from the first city. Each variant spreads 
to the next city in one unit of time. You need to determine the minimum time required for all `k` virus variants to spread 
to all `n` cities.

Constraints:
- 1 <= n <= 10^5
- 1 <= k <= n

Write a function `minimumTimeToSpread(n: int, k: int) -> int` that returns the minimum time required for all `k` virus variants 
to spread to all `n` cities.
"""

def minimumTimeToSpread(n: int, k: int) -> int:
    """
    Calculate the minimum time required for k virus variants to spread to all n cities.

    Args:
    n (int): Number of cities.
    k (int): Number of virus variants.

    Returns:
    int: Minimum time required for all k virus variants to spread to all n cities.
    """
    # If the number of variants is greater than or equal to the number of cities,
    # all cities can be infected in one unit of time.
    if k >= n:
        return 1
    
    # Otherwise, calculate the minimum time using the formula:
    # Time = ceil((n - 1) / (k - 1))
    # This accounts for the fact that k variants can spread simultaneously.
    return (n - 1 + k - 2) // (k - 1)  # Equivalent to math.ceil((n - 1) / (k - 1))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Small number of cities and variants
    n1, k1 = 5, 2
    print(minimumTimeToSpread(n1, k1))  # Expected Output: 3

    # Test Case 2: Number of variants equals number of cities
    n2, k2 = 4, 4
    print(minimumTimeToSpread(n2, k2))  # Expected Output: 1

    # Test Case 3: Large number of cities and few variants
    n3, k3 = 10, 3
    print(minimumTimeToSpread(n3, k3))  # Expected Output: 4

    # Test Case 4: Single city
    n4, k4 = 1, 1
    print(minimumTimeToSpread(n4, k4))  # Expected Output: 1

    # Test Case 5: Large number of cities and variants
    n5, k5 = 100000, 100
    print(minimumTimeToSpread(n5, k5))  # Expected Output: 1001

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves a simple arithmetic calculation, which is O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The solution uses a constant amount of space, independent of the input size.
- Therefore, the space complexity is O(1).

Topic: Math
"""