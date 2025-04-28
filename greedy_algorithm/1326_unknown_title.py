"""
LeetCode Problem #1326: Minimum Number of Taps to Open to Water a Garden

Problem Statement:
There is a one-dimensional garden on the x-axis. The garden starts at the point 0 and ends at the point n. 
(n + 1) taps are placed along this axis at points [0, 1, ..., n].

Given an integer n and an integer array ranges of length n + 1 where ranges[i] (0-indexed) means the i-th tap 
can water the area [i - ranges[i], i + ranges[i]] if it is open.

Return the minimum number of taps that need to be open to water the whole garden, or -1 if the garden cannot 
be watered.

Example 1:
Input: n = 5, ranges = [3, 4, 1, 1, 0, 0]
Output: 1
Explanation: The tap at position 0 can cover the entire garden [0, 5].

Example 2:
Input: n = 3, ranges = [0, 0, 0, 0]
Output: -1
Explanation: Even if you activate all the taps, you cannot water the whole garden.

Constraints:
- 1 <= n <= 10^4
- ranges.length == n + 1
- 0 <= ranges[i] <= 100
"""

def minTaps(n: int, ranges: list[int]) -> int:
    # Create an array to store the maximum range each point can cover
    max_range = [0] * (n + 1)
    
    # Populate the max_range array
    for i in range(n + 1):
        left = max(0, i - ranges[i])
        right = min(n, i + ranges[i])
        max_range[left] = max(max_range[left], right)
    
    # Initialize variables for the greedy approach
    taps = 0
    curr_end = 0
    farthest = 0
    
    # Iterate through the garden
    for i in range(n + 1):
        if i > farthest:
            # If we cannot reach this point, return -1
            return -1
        if i > curr_end:
            # Open a new tap
            taps += 1
            curr_end = farthest
        # Update the farthest point we can reach
        farthest = max(farthest, max_range[i])
    
    return taps if curr_end >= n else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 5
    ranges1 = [3, 4, 1, 1, 0, 0]
    print(minTaps(n1, ranges1))  # Output: 1

    # Test Case 2
    n2 = 3
    ranges2 = [0, 0, 0, 0]
    print(minTaps(n2, ranges2))  # Output: -1

    # Test Case 3
    n3 = 7
    ranges3 = [1, 2, 1, 0, 2, 1, 0, 1]
    print(minTaps(n3, ranges3))  # Output: 3

    # Test Case 4
    n4 = 8
    ranges4 = [4, 0, 0, 0, 0, 0, 0, 0, 4]
    print(minTaps(n4, ranges4))  # Output: 2

    # Test Case 5
    n5 = 5
    ranges5 = [1, 2, 1, 0, 2, 1]
    print(minTaps(n5, ranges5))  # Output: 2

"""
Time Complexity:
- O(n): We iterate through the `ranges` array to populate the `max_range` array, and then we iterate through 
  the garden once more to determine the minimum number of taps.

Space Complexity:
- O(n): We use an additional array `max_range` of size n + 1.

Topic: Greedy Algorithm
"""