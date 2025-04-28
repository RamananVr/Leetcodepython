"""
LeetCode Problem #1625: Lexicographically Smallest String After Applying Operations

Problem Statement:
You are given a string `s` of even length consisting of digits from 0 to 9, and two integers `a` and `b`.

You can apply either of the following two operations any number of times and in any order on `s`:
1. Add `a` to all odd-indexed digits of `s` (0-indexed). Note that the resulting digit must be a single digit, so we only take `a % 10`.
2. Rotate the string to the right by `b` positions.

Return the lexicographically smallest string that you can obtain by applying the above operations any number of times on `s`.

Constraints:
- `2 <= s.length <= 100`
- `s.length` is even.
- `0 <= a <= 9`
- `1 <= b <= s.length - 1`

Example:
Input: s = "5525", a = 9, b = 2
Output: "2050"
Explanation: We can apply the operations as follows:
- Rotate: "5525" -> "2555"
- Add: "2555" -> "2050"
- Rotate: "2050" -> "5020"
- Add: "5020" -> "5525"
The lexicographically smallest string is "2050".
"""

from collections import deque

def findLexSmallestString(s: str, a: int, b: int) -> str:
    def add_to_odd_indices(s, a):
        """Add `a` to all odd-indexed digits of the string `s`."""
        s_list = list(s)
        for i in range(1, len(s), 2):
            s_list[i] = str((int(s_list[i]) + a) % 10)
        return ''.join(s_list)

    def rotate(s, b):
        """Rotate the string `s` to the right by `b` positions."""
        return s[-b:] + s[:-b]

    visited = set()
    queue = deque([s])
    smallest = s

    while queue:
        current = queue.popleft()
        if current in visited:
            continue
        visited.add(current)

        # Update the smallest string
        smallest = min(smallest, current)

        # Apply the two operations
        added = add_to_odd_indices(current, a)
        rotated = rotate(current, b)

        # Add the results to the queue
        if added not in visited:
            queue.append(added)
        if rotated not in visited:
            queue.append(rotated)

    return smallest

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, a1, b1 = "5525", 9, 2
    print(findLexSmallestString(s1, a1, b1))  # Output: "2050"

    # Test Case 2
    s2, a2, b2 = "74", 5, 1
    print(findLexSmallestString(s2, a2, b2))  # Output: "24"

    # Test Case 3
    s3, a3, b3 = "0011", 4, 2
    print(findLexSmallestString(s3, a3, b3))  # Output: "0011"

    # Test Case 4
    s4, a4, b4 = "43987654", 7, 3
    print(findLexSmallestString(s4, a4, b4))  # Output: "00553311"

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The number of unique strings that can be generated is bounded by the length of `s` and the operations.
   - In the worst case, we explore all possible rotations and additions, which is O(n * 10), where `n` is the length of the string.
   - Therefore, the time complexity is O(n * 10).

2. Space Complexity:
   - We use a set to store visited strings and a queue for BFS. The space complexity is proportional to the number of unique strings, which is O(n * 10).
   - Therefore, the space complexity is O(n * 10).

Topic: String Manipulation, Breadth-First Search (BFS)
"""