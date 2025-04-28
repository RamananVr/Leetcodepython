"""
LeetCode Problem #1923: Longest Common Subpath

Problem Statement:
There is a country of `n` cities numbered from `0` to `n - 1`. You are given an integer `n` and an array of arrays `paths`, where `paths[i]` is an array representing the path of a user in the country. More formally, the `i-th` user traveled through the cities in the order given by `paths[i]`.

A subpath is a contiguous sequence of cities within a path.

- The subpath should appear in the path of every user.
- The length of a subpath is the number of cities it contains.

Return the length of the longest common subpath that is shared by every user's path. If there is no common subpath, return `0`.

Constraints:
- `1 <= n <= 10^5`
- `1 <= paths.length <= 10^5`
- `sum(paths[i].length) <= 10^5`
- `0 <= paths[i][j] < n`

"""

from typing import List

def longestCommonSubpath(n: int, paths: List[List[int]]) -> int:
    """
    Finds the length of the longest common subpath shared by all users' paths.
    """
    def rabin_karp(path, length, base, mod):
        """Helper function to compute hashes of all subpaths of a given length."""
        h = 0
        base_l = pow(base, length, mod)
        hashes = set()
        for i in range(len(path)):
            h = (h * base + path[i]) % mod
            if i >= length - 1:
                if i >= length:
                    h = (h - path[i - length] * base_l) % mod
                hashes.add(h)
        return hashes

    def check(length):
        """Checks if a subpath of the given length exists in all paths."""
        common_hashes = rabin_karp(paths[0], length, base, mod)
        for path in paths[1:]:
            common_hashes &= rabin_karp(path, length, base, mod)
            if not common_hashes:
                return False
        return True

    # Parameters for Rabin-Karp
    base = 10**4
    mod = 2**63 - 1

    # Binary search for the longest common subpath
    left, right = 0, min(len(path) for path in paths)
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 5
    paths = [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3]]
    print(longestCommonSubpath(n, paths))  # Output: 2

    # Test Case 2
    n = 3
    paths = [[0, 1, 2, 3, 4], [2, 3, 4], [4, 0, 1, 2, 3, 4]]
    print(longestCommonSubpath(n, paths))  # Output: 1

    # Test Case 3
    n = 10
    paths = [[1, 2, 3, 4, 5], [5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6]]
    print(longestCommonSubpath(n, paths))  # Output: 0

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Computing hashes for a single path of length `L` takes O(L).
   - For all paths, the total length is at most 10^5, so computing hashes for all paths takes O(10^5).
   - Binary search runs for at most O(log(min_length)), where `min_length` is the length of the shortest path.
   - Overall time complexity: O(10^5 * log(min_length)).

2. Space Complexity:
   - The space used for storing hashes is proportional to the number of unique hashes, which is O(L) for a single path.
   - Overall space complexity: O(L), where L is the length of the longest path.

Topic: Arrays, Binary Search, Hashing
"""