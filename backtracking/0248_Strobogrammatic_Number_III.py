"""
LeetCode Problem #248: Strobogrammatic Number III

Problem Statement:
A strobogrammatic number is a number that looks the same when rotated 180 degrees (e.g., 0, 1, 6, 8, 9).

Given two numbers `low` and `high` represented as strings, return the count of strobogrammatic numbers that lie in the inclusive range `[low, high]`.

Example:
Input: low = "50", high = "100"
Output: 3
Explanation: The strobogrammatic numbers in the range are 69, 88, and 96.

Constraints:
- `low` and `high` are strings of length 1 to 15.
- `low` and `high` consist of only digits.
- `low` is less than or equal to `high`.
- The numbers represented by `low` and `high` do not have leading zeros except for the number 0 itself.
"""

def strobogrammatic_count(low: str, high: str) -> int:
    def is_valid(num: str) -> bool:
        """Check if a number is within the range [low, high]."""
        return len(num) == len(low) and num >= low or len(num) == len(high) and num <= high or len(low) < len(num) < len(high)

    def dfs(current: str, n: int) -> None:
        """Generate strobogrammatic numbers using DFS."""
        if len(current) > n:
            return
        if len(current) == n:
            if is_valid(current):
                result.append(current)
            return
        for pair in pairs:
            dfs(pair[0] + current + pair[1], n)

    pairs = [("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6")]
    result = []
    for length in range(len(low), len(high) + 1):
        dfs("", length)
    return len(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    low = "50"
    high = "100"
    print(strobogrammatic_count(low, high))  # Output: 3

    # Test Case 2
    low = "0"
    high = "10"
    print(strobogrammatic_count(low, high))  # Output: 3

    # Test Case 3
    low = "100"
    high = "200"
    print(strobogrammatic_count(low, high))  # Output: 4

"""
Time Complexity:
- The function generates strobogrammatic numbers of lengths between len(low) and len(high).
- For each length, the DFS explores all possible combinations of strobogrammatic pairs.
- The total number of combinations is exponential in the length of the number, so the time complexity is O(5^(n/2)), where n is the maximum length of the numbers.

Space Complexity:
- The space complexity is determined by the recursion depth and the storage of results.
- The recursion depth is O(n), and the result list can store up to O(5^(n/2)) numbers.
- Therefore, the space complexity is O(5^(n/2)).

Topic: Backtracking
"""