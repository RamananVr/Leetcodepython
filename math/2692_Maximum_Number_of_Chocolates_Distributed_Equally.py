"""
LeetCode Problem #2692: Maximum Number of Chocolates Distributed Equally

Problem Statement:
You are given an integer `n` representing the total number of chocolates and an integer `k` representing the number of friends. 
You want to distribute the chocolates equally among your friends such that each friend gets the same number of chocolates, 
and the remaining chocolates (if any) are kept aside. Return the maximum number of chocolates each friend can get.

Constraints:
- 1 <= n, k <= 10^9
"""

def maximum_chocolates(n: int, k: int) -> int:
    """
    Function to calculate the maximum number of chocolates each friend can get.

    Parameters:
    n (int): Total number of chocolates.
    k (int): Number of friends.

    Returns:
    int: Maximum number of chocolates each friend can get.
    """
    return n // k

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 10, 3
    print(maximum_chocolates(n1, k1))  # Expected Output: 3

    # Test Case 2
    n2, k2 = 15, 5
    print(maximum_chocolates(n2, k2))  # Expected Output: 3

    # Test Case 3
    n3, k3 = 7, 4
    print(maximum_chocolates(n3, k3))  # Expected Output: 1

    # Test Case 4
    n4, k4 = 100, 10
    print(maximum_chocolates(n4, k4))  # Expected Output: 10

    # Test Case 5
    n5, k5 = 1, 1
    print(maximum_chocolates(n5, k5))  # Expected Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function performs a single division operation, which is O(1).
- Therefore, the time complexity is O(1).

Space Complexity:
- The function uses a constant amount of space for computation.
- Therefore, the space complexity is O(1).

Topic: Math
"""