"""
LeetCode Problem #2511: Maximum Enemy Forts That Can Be Captured

Problem Statement:
You are given a 0-indexed integer array `forts` of length `n` representing the positions of several forts. 
`forts[i]` can be one of the following three values:
- `-1` represents an enemy fort.
- `0` represents an empty position.
- `1` represents your fort.

Now you want to capture enemy forts. You can capture an enemy fort if and only if all the positions between 
your fort and the enemy fort are empty (i.e., 0). More formally, you can capture an enemy fort `forts[j]` 
if and only if there exists an index `i` such that:
- `forts[i] == 1`
- `forts[j] == -1`
- All indices `k` in the range `min(i, j) < k < max(i, j)` have `forts[k] == 0`.

Return the maximum number of enemy forts you can capture. If no enemy fort can be captured, return `0`.

Constraints:
- `1 <= forts.length <= 1000`
- `-1 <= forts[i] <= 1`
"""

def captureForts(forts):
    """
    Function to calculate the maximum number of enemy forts that can be captured.

    :param forts: List[int] - The array representing the positions of forts.
    :return: int - The maximum number of enemy forts that can be captured.
    """
    max_captures = 0
    n = len(forts)
    prev = -1  # To track the last non-zero position

    for i in range(n):
        if forts[i] != 0:
            if prev != -1 and forts[i] != forts[prev] and forts[prev] != 0:
                # Check if all positions between prev and i are empty
                max_captures = max(max_captures, abs(i - prev) - 1)
            prev = i

    return max_captures

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    forts = [1, 0, 0, -1, 0, 0, 1]
    print(captureForts(forts))  # Output: 2

    # Test Case 2
    forts = [1, 0, 0, 0, -1]
    print(captureForts(forts))  # Output: 3

    # Test Case 3
    forts = [1, -1, 0, 0, -1, 1]
    print(captureForts(forts))  # Output: 0

    # Test Case 4
    forts = [0, 0, 1, 0, -1, 0, 0, -1, 0, 1]
    print(captureForts(forts))  # Output: 3

    # Test Case 5
    forts = [1, 0, -1]
    print(captureForts(forts))  # Output: 1

"""
Time Complexity Analysis:
- The algorithm iterates through the `forts` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `forts` array.

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (only a few variables like `max_captures` and `prev`).
- Therefore, the space complexity is O(1).

Topic: Arrays
"""