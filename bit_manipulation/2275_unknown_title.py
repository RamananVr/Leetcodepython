"""
LeetCode Problem #2275: Largest Combination With Bitwise AND Greater Than Zero

Problem Statement:
You are given an array of positive integers `candidates`. An integer `x` is said to be a 
"combination" if it can be obtained by choosing some elements from the array and applying 
the bitwise AND operator on them. A combination is considered "greater than zero" if the 
result of the bitwise AND operation is greater than 0.

Return the size of the largest combination of `candidates` where the bitwise AND of the 
chosen elements is greater than 0.

Example:
Input: candidates = [16, 17, 71, 62, 12, 24, 14]
Output: 4
Explanation: The combination [16, 17, 62, 24] has a bitwise AND greater than 0.

Constraints:
- 1 <= candidates.length <= 10^5
- 1 <= candidates[i] <= 10^7
"""

# Solution
def largestCombination(candidates):
    """
    Finds the size of the largest combination of candidates where the bitwise AND of the 
    chosen elements is greater than 0.

    :param candidates: List[int] - List of positive integers
    :return: int - Size of the largest combination
    """
    max_bit = 24  # Since candidates[i] <= 10^7, we only need to check up to 24 bits
    max_count = 0

    for bit in range(max_bit):
        count = 0
        for num in candidates:
            if num & (1 << bit):  # Check if the current bit is set
                count += 1
        max_count = max(max_count, count)

    return max_count


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    candidates = [16, 17, 71, 62, 12, 24, 14]
    print(largestCombination(candidates))  # Output: 4

    # Test Case 2
    candidates = [8, 8, 8]
    print(largestCombination(candidates))  # Output: 3

    # Test Case 3
    candidates = [1, 2, 4, 8, 16]
    print(largestCombination(candidates))  # Output: 1

    # Test Case 4
    candidates = [31, 31, 31, 31]
    print(largestCombination(candidates))  # Output: 4

    # Test Case 5
    candidates = [1024, 2048, 4096]
    print(largestCombination(candidates))  # Output: 1


# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for `max_bit` iterations, which is at most 24.
- The inner loop iterates over all elements in `candidates`, which is at most 10^5.
- Therefore, the total time complexity is O(max_bit * len(candidates)) = O(24 * len(candidates)) = O(len(candidates)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Bit Manipulation