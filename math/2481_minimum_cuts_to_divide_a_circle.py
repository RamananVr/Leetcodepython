"""
LeetCode Question #2481: Minimum Cuts to Divide a Circle

Problem Statement:
A circle is divided into `n` equal slices. You need to determine the minimum number of cuts required to divide the circle into exactly `n` slices.

- If `n == 1`, no cuts are needed since the circle is already a single slice.
- If `n` is even, you can divide the circle into `n` slices with `n / 2` straight cuts.
- If `n` is odd, you need `n` cuts to divide the circle into `n` slices.

Write a function `minCuts(n: int) -> int` that returns the minimum number of cuts required to divide the circle into `n` slices.

Constraints:
- 1 <= n <= 10^9
"""

def minCuts(n: int) -> int:
    """
    Returns the minimum number of cuts required to divide a circle into n slices.
    
    :param n: Number of slices to divide the circle into.
    :return: Minimum number of cuts required.
    """
    if n == 1:
        return 0
    elif n % 2 == 0:
        return n // 2
    else:
        return n

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    # No cuts are needed for a single slice.
    print(minCuts(1))  # Expected output: 0

    # Test Case 2: n = 4
    # For an even number of slices, n / 2 cuts are needed.
    print(minCuts(4))  # Expected output: 2

    # Test Case 3: n = 5
    # For an odd number of slices, n cuts are needed.
    print(minCuts(5))  # Expected output: 5

    # Test Case 4: n = 10
    # For an even number of slices, n / 2 cuts are needed.
    print(minCuts(10))  # Expected output: 5

    # Test Case 5: n = 7
    # For an odd number of slices, n cuts are needed.
    print(minCuts(7))  # Expected output: 7

"""
Time Complexity Analysis:
- The function performs a constant amount of work regardless of the input size.
- The time complexity is O(1).

Space Complexity Analysis:
- The function uses a constant amount of space for variables and does not depend on the input size.
- The space complexity is O(1).

Topic: Math
"""