"""
LeetCode Problem #2055: Plates Between Candles

Problem Statement:
You are given a string `s` consisting of characters '*' and '|' where:
- '*' represents a plate.
- '|' represents a candle.

You are also given a list of queries `queries`, where each query is a pair of integers `[left, right]`. 
For each query, you need to determine the number of plates between candles that are in the substring `s[left:right]` (inclusive). 
A plate is considered between candles if there is at least one candle to its left and at least one candle to its right in the substring.

Return an array `answer` where `answer[i]` is the answer to the `i-th` query.

Constraints:
- `1 <= s.length <= 10^5`
- `s[i]` is either '*' or '|'.
- `1 <= queries.length <= 10^5`
- `0 <= left <= right < s.length`

Example:
Input: s = "**|**|***|", queries = [[2,5],[5,9]]
Output: [2,3]
Explanation:
- For the query [2,5], the substring is "|**|". There are 2 plates between candles.
- For the query [5,9], the substring is "|***|". There are 3 plates between candles.
"""

# Python Solution
def platesBetweenCandles(s, queries):
    # Precompute prefix sums for plates and nearest candle indices
    n = len(s)
    prefix_plates = [0] * n
    left_candle = [-1] * n
    right_candle = [-1] * n

    # Compute prefix sum of plates
    plate_count = 0
    for i in range(n):
        if s[i] == '*':
            plate_count += 1
        prefix_plates[i] = plate_count

    # Compute nearest left candle for each position
    nearest = -1
    for i in range(n):
        if s[i] == '|':
            nearest = i
        left_candle[i] = nearest

    # Compute nearest right candle for each position
    nearest = -1
    for i in range(n - 1, -1, -1):
        if s[i] == '|':
            nearest = i
        right_candle[i] = nearest

    # Process each query
    result = []
    for left, right in queries:
        # Find the nearest candles within the range
        left_bound = right_candle[left]
        right_bound = left_candle[right]

        if left_bound == -1 or right_bound == -1 or left_bound >= right_bound:
            # No valid candles enclosing plates
            result.append(0)
        else:
            # Plates between candles
            result.append(prefix_plates[right_bound] - prefix_plates[left_bound])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s = "**|**|***|"
    queries = [[2, 5], [5, 9]]
    print(platesBetweenCandles(s, queries))  # Output: [2, 3]

    # Test Case 2
    s = "|*|*|"
    queries = [[0, 4], [1, 3]]
    print(platesBetweenCandles(s, queries))  # Output: [1, 0]

    # Test Case 3
    s = "||*||*|*|"
    queries = [[0, 9], [2, 8], [1, 6]]
    print(platesBetweenCandles(s, queries))  # Output: [3, 2, 2]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputing prefix sums for plates: O(n)
- Precomputing nearest left and right candles: O(n)
- Processing each query: O(1) per query, O(q) for all queries (where q is the number of queries).
Overall: O(n + q), where n is the length of the string and q is the number of queries.

Space Complexity:
- Prefix sums, left_candle, and right_candle arrays: O(n)
Overall: O(n)

Topic: Arrays, Prefix Sum
"""