"""
LeetCode Problem #2832: Find the Minimum Possible Sum of a Beautiful Array

Problem Statement:
You are given two integers `n` and `k`. A beautiful array is an array that satisfies the following conditions:
1. It contains exactly `n` distinct positive integers.
2. There does not exist two distinct integers `a` and `b` in the array such that `a + b = k`.

Return the minimum possible sum of a beautiful array.

Constraints:
- 1 <= n, k <= 10^5
"""

def minimumPossibleSum(n: int, k: int) -> int:
    """
    Function to find the minimum possible sum of a beautiful array.
    
    Args:
    n (int): The number of elements in the array.
    k (int): The forbidden sum condition.

    Returns:
    int: The minimum possible sum of a beautiful array.
    """
    beautiful_set = set()
    current = 1
    total_sum = 0

    while len(beautiful_set) < n:
        # Check if the current number can be added to the beautiful array
        if k - current not in beautiful_set:
            beautiful_set.add(current)
            total_sum += current
        current += 1

    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 4
    print(f"Test Case 1: n={n1}, k={k1} => Output: {minimumPossibleSum(n1, k1)}")  # Expected Output: 6

    # Test Case 2
    n2, k2 = 5, 7
    print(f"Test Case 2: n={n2}, k={k2} => Output: {minimumPossibleSum(n2, k2)}")  # Expected Output: 15

    # Test Case 3
    n3, k3 = 10, 5
    print(f"Test Case 3: n={n3}, k={k3} => Output: {minimumPossibleSum(n3, k3)}")  # Expected Output: 55

    # Test Case 4
    n4, k4 = 1, 2
    print(f"Test Case 4: n={n4}, k={k4} => Output: {minimumPossibleSum(n4, k4)}")  # Expected Output: 1

    # Test Case 5
    n5, k5 = 6, 10
    print(f"Test Case 5: n={n5}, k={k5} => Output: {minimumPossibleSum(n5, k5)}")  # Expected Output: 21

"""
Time Complexity Analysis:
- The while loop runs until we have `n` elements in the beautiful array.
- For each iteration, we check if `k - current` is in the set, which is an O(1) operation.
- In the worst case, we may iterate up to `2n` times (if many numbers are skipped due to the forbidden condition).
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- We use a set to store the elements of the beautiful array, which takes O(n) space.
- The total space complexity is O(n).

Topic: Arrays, Greedy
"""