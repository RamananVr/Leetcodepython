"""
LeetCode Problem #2557: Maximum Number of Integers to Choose From a Range I

Problem Statement:
You are given two integers `n` and `k`. You need to find the maximum number of distinct integers you can choose from the range `[1, n]` such that the sum of the chosen integers is less than or equal to `k`.

Return the maximum number of integers you can choose.

Constraints:
- 1 <= n <= 10^5
- 1 <= k <= 10^9
"""

def maxCount(n: int, k: int) -> int:
    """
    This function calculates the maximum number of distinct integers that can be chosen
    from the range [1, n] such that their sum is less than or equal to k.
    """
    # Initialize variables
    count = 0
    current_sum = 0

    # Iterate through numbers from 1 to n
    for i in range(1, n + 1):
        if current_sum + i <= k:
            current_sum += i
            count += 1
        else:
            break

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 5, 10
    print(maxCount(n1, k1))  # Expected Output: 4 (Choose 1, 2, 3, 4)

    # Test Case 2
    n2, k2 = 10, 15
    print(maxCount(n2, k2))  # Expected Output: 5 (Choose 1, 2, 3, 4, 5)

    # Test Case 3
    n3, k3 = 3, 6
    print(maxCount(n3, k3))  # Expected Output: 3 (Choose 1, 2, 3)

    # Test Case 4
    n4, k4 = 100, 1
    print(maxCount(n4, k4))  # Expected Output: 1 (Choose 1)

    # Test Case 5
    n5, k5 = 10, 55
    print(maxCount(n5, k5))  # Expected Output: 10 (Choose all numbers from 1 to 10)

"""
Time Complexity Analysis:
- The loop runs from 1 to n, but it breaks early when the sum exceeds k.
- In the worst case, the loop runs for all numbers from 1 to n.
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses only a few variables (count, current_sum, and i).
- No additional data structures are used.
- Therefore, the space complexity is O(1).

Topic: Greedy Algorithm
"""