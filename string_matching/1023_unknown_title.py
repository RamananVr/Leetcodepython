"""
LeetCode Problem #1023: Camelcase Matching

Problem Statement:
Given an array of strings `queries` and a string `pattern`, return a list of booleans where `ans[i]` is `true` if and only if `queries[i]` matches the `pattern`.

A query matches the pattern if we can insert lowercase English letters into the pattern to match the query. More formally, we can say `query` matches `pattern` if and only if we can remove all lowercase letters from `query` and the result is equal to `pattern`.

Example:
Input: queries = ["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], pattern = "FB"
Output: [true,false,true,true,false]

Constraints:
- 1 <= queries.length <= 100
- 1 <= queries[i].length <= 100
- 1 <= pattern.length <= 100
- `queries[i]` and `pattern` consist of English letters.

"""

# Solution
def camelMatch(queries, pattern):
    def matches(query, pattern):
        i, j = 0, 0
        while i < len(query):
            if j < len(pattern) and query[i] == pattern[j]:
                j += 1
            elif query[i].isupper():
                return False
            i += 1
        return j == len(pattern)

    return [matches(query, pattern) for query in queries]

# Example Test Cases
if __name__ == "__main__":
    queries = ["FooBar", "FooBarTest", "FootBall", "FrameBuffer", "ForceFeedBack"]
    pattern = "FB"
    print(camelMatch(queries, pattern))  # Output: [True, False, True, True, False]

    queries = ["CompetitiveProgramming", "CounterPick", "ControlPanel"]
    pattern = "CooP"
    print(camelMatch(queries, pattern))  # Output: [False, False, True]

    queries = ["HelloWorld", "HiWorld", "HWorld"]
    pattern = "HW"
    print(camelMatch(queries, pattern))  # Output: [True, False, True]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let `n` be the number of queries and `m` be the average length of the queries.
- For each query, we iterate through its characters and compare them to the pattern. This takes O(m) time.
- Therefore, the total time complexity is O(n * m).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures that scale with the input size.
"""

# Topic: String Matching