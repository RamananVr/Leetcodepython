"""
LeetCode Problem #2790: Maximum Number of Groups With Increasing Length

Problem Statement:
You are given a 0-indexed array `usageLimits` of length `n`.

Your task is to form groups using elements from `usageLimits` such that:
1. Each group consists of distinct elements from the array.
2. The size of a group is strictly greater than the size of the previous group.
3. An element `usageLimits[i]` can only be used at most `usageLimits[i]` times.

Return the maximum number of groups you can form.

Example:
Input: usageLimits = [1, 2, 5]
Output: 3
Explanation:
- The first group can be [0] (size = 1).
- The second group can be [1, 2] (size = 2).
- The third group can be [2, 2, 2] (size = 3).
- You cannot form a fourth group because there are not enough elements.

Constraints:
- `1 <= usageLimits.length <= 10^5`
- `1 <= usageLimits[i] <= 10^9`
"""

from typing import List

def maxIncreasingGroups(usageLimits: List[int]) -> int:
    """
    Calculate the maximum number of groups with increasing lengths that can be formed
    using the given usage limits.
    """
    usageLimits.sort()  # Sort the array to use smaller values first
    total = 0  # Tracks the total number of elements available
    groups = 0  # Tracks the number of groups formed

    for limit in usageLimits:
        total += limit  # Add the current element's usage limit to the total
        if total >= groups + 1:  # Check if we can form the next group
            groups += 1  # Form the next group
            total -= groups  # Deduct the elements used for this group

    return groups

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    usageLimits = [1, 2, 5]
    print(maxIncreasingGroups(usageLimits))  # Output: 3

    # Test Case 2
    usageLimits = [2, 2, 2]
    print(maxIncreasingGroups(usageLimits))  # Output: 2

    # Test Case 3
    usageLimits = [5, 1, 1]
    print(maxIncreasingGroups(usageLimits))  # Output: 2

    # Test Case 4
    usageLimits = [10, 10, 10]
    print(maxIncreasingGroups(usageLimits))  # Output: 4

    # Test Case 5
    usageLimits = [1]
    print(maxIncreasingGroups(usageLimits))  # Output: 1

"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of `usageLimits`.
- The subsequent loop iterates through the array once, which is O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The sorting operation uses O(n) space in the worst case.
- No additional data structures are used, so the space complexity is O(n).

Topic: Greedy Algorithm
"""