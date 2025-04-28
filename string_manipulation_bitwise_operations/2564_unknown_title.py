"""
LeetCode Problem #2564: Substring XOR Queries

Problem Statement:
You are given a binary string `s` and a 2D integer array `queries` where `queries[i] = [first_i, second_i]`.

For each `queries[i]`, find the shortest substring of `s` such that the bitwise XOR of its decimal values is equal to `first_i ^ second_i`. If no such substring exists, return [-1, -1].

Return an array `result` where `result[i] = [start_i, end_i]` is the starting and ending indices (0-based) of the substring corresponding to `queries[i]`.

A substring is a contiguous non-empty sequence of characters within a string.

Constraints:
- 1 <= s.length <= 10^5
- `s` consists of only '0' and '1'.
- 1 <= queries.length <= 10^5
- 0 <= first_i, second_i <= 10^9
"""

# Python Solution
def substringXorQueries(s, queries):
    # Precompute all possible XOR values for substrings
    n = len(s)
    xor_map = {}
    
    for i in range(n):
        value = 0
        for j in range(i, min(i + 32, n)):  # Limit substring length to 32 bits
            value = (value << 1) | int(s[j])
            if value not in xor_map:
                xor_map[value] = (i, j)
    
    # Process each query
    result = []
    for first, second in queries:
        target = first ^ second
        if target in xor_map:
            result.append(list(xor_map[target]))
        else:
            result.append([-1, -1])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "101101"
    queries = [[0, 5], [1, 2], [3, 4], [2, 2]]
    print(substringXorQueries(s, queries))  # Expected: [[0, 2], [2, 3], [0, 1], [3, 3]]

    # Test Case 2
    s = "111000"
    queries = [[0, 7], [1, 6], [2, 5], [3, 4]]
    print(substringXorQueries(s, queries))  # Expected: [[-1, -1], [-1, -1], [-1, -1], [-1, -1]]

    # Test Case 3
    s = "0000"
    queries = [[0, 0], [1, 1], [2, 2]]
    print(substringXorQueries(s, queries))  # Expected: [[0, 0], [-1, -1], [-1, -1]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Precomputing XOR values for substrings: O(n * 32) = O(n), where n is the length of the string `s`.
- Processing queries: O(q), where q is the number of queries.
- Overall: O(n + q).

Space Complexity:
- The `xor_map` dictionary stores at most 2^32 keys (limited by substring length of 32 bits), but in practice, it is much smaller due to constraints on `s`. Thus, space complexity is O(n) for the dictionary and O(q) for the result list.
- Overall: O(n + q).
"""

# Topic: String Manipulation, Bitwise Operations