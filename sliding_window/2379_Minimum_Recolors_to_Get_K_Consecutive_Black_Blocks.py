"""
LeetCode Problem #2379: Minimum Recolors to Get K Consecutive Black Blocks

Problem Statement:
You are given a string `blocks` of length `n`, where each block is either 'W' (white) or 'B' (black), 
and an integer `k`. You need to recolor some of the white blocks such that there are at least `k` 
consecutive black blocks. Return the minimum number of recolors needed.

Constraints:
- `n == len(blocks)`
- `1 <= n <= 100`
- `blocks[i]` is either 'W' or 'B'.
- `1 <= k <= n`
"""

def minimumRecolors(blocks: str, k: int) -> int:
    """
    This function calculates the minimum number of recolors needed to get at least k consecutive black blocks.
    
    Args:
    blocks (str): A string consisting of 'W' and 'B' representing white and black blocks.
    k (int): The number of consecutive black blocks required.

    Returns:
    int: The minimum number of recolors needed.
    """
    # Initialize the minimum recolors to a large value
    min_recolors = float('inf')
    
    # Use a sliding window of size k
    for i in range(len(blocks) - k + 1):
        # Count the number of 'W' in the current window
        window = blocks[i:i + k]
        recolors = window.count('W')
        # Update the minimum recolors
        min_recolors = min(min_recolors, recolors)
    
    return min_recolors

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    blocks = "WBBWWBBWBW"
    k = 7
    print(minimumRecolors(blocks, k))  # Output: 3

    # Test Case 2
    blocks = "WBWBBBW"
    k = 2
    print(minimumRecolors(blocks, k))  # Output: 0

    # Test Case 3
    blocks = "WWWW"
    k = 3
    print(minimumRecolors(blocks, k))  # Output: 3

    # Test Case 4
    blocks = "BBBB"
    k = 4
    print(minimumRecolors(blocks, k))  # Output: 0

    # Test Case 5
    blocks = "WBWBWBWB"
    k = 1
    print(minimumRecolors(blocks, k))  # Output: 0

"""
Time Complexity Analysis:
- The sliding window iterates over the string `blocks` with a window size of `k`.
- For each window, we count the number of 'W' in O(k) time.
- The total time complexity is O(n * k), where `n` is the length of the string.

Space Complexity Analysis:
- The space complexity is O(1) since we are only using a few variables to store intermediate results.

Topic: Sliding Window
"""