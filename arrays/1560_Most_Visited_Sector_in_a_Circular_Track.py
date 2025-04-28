"""
LeetCode Problem #1560: Most Visited Sector in a Circular Track

Problem Statement:
Given an integer `n` and an integer array `rounds`, the track is a circular track with `n` sectors numbered from 1 to `n`. The rounds array represents a race. The first element of `rounds` is the starting sector, and the last element of `rounds` is the ending sector. Each element in `rounds` represents the sector visited at the start of a lap.

You need to return an array of the most visited sectors sorted in ascending order.

Constraints:
- 2 <= n <= 100
- 1 <= rounds.length <= 1000
- 1 <= rounds[i] <= n
- rounds[0] == rounds[rounds.length - 1]

Example:
Input: n = 4, rounds = [1, 3, 1, 2]
Output: [1, 2]
Explanation: The race starts at sector 1, goes through sectors 2 and 3, and ends at sector 2. Sectors 1 and 2 are the most visited.

Input: n = 2, rounds = [2, 1, 2, 1, 2]
Output: [2]
Explanation: The race starts at sector 2, goes through sector 1, and ends at sector 2. Sector 2 is the most visited.

Follow-up:
Can you solve this problem in O(n + rounds.length) time complexity?
"""

def mostVisited(n: int, rounds: list[int]) -> list[int]:
    """
    Returns the most visited sectors in a circular track.

    Args:
    n (int): Number of sectors in the circular track.
    rounds (list[int]): List of sectors visited during the race.

    Returns:
    list[int]: List of most visited sectors sorted in ascending order.
    """
    start = rounds[0]
    end = rounds[-1]

    # If the start is less than or equal to the end, the most visited sectors are in the range [start, end].
    if start <= end:
        return list(range(start, end + 1))
    else:
        # If the start is greater than the end, the most visited sectors wrap around the circular track.
        return list(range(1, end + 1)) + list(range(start, n + 1))


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 4
    rounds1 = [1, 3, 1, 2]
    print(mostVisited(n1, rounds1))  # Output: [1, 2]

    # Test Case 2
    n2 = 2
    rounds2 = [2, 1, 2, 1, 2]
    print(mostVisited(n2, rounds2))  # Output: [2]

    # Test Case 3
    n3 = 7
    rounds3 = [3, 5, 7, 2]
    print(mostVisited(n3, rounds3))  # Output: [1, 2, 3, 7]

    # Test Case 4
    n4 = 3
    rounds4 = [3, 1, 2]
    print(mostVisited(n4, rounds4))  # Output: [1, 2, 3]


"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution involves determining the range of sectors visited, which takes O(1) time.
- Constructing the list of most visited sectors involves iterating over a range of at most `n` elements.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The space complexity is O(1) for variables and O(k) for the output list, where `k` is the number of most visited sectors.
- In the worst case, `k` can be equal to `n`, so the space complexity is O(n).

Topic: Arrays
"""