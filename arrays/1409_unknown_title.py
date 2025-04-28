"""
LeetCode Problem #1409: Queries on a Permutation With Key

Problem Statement:
Given the array `queries` of positive integers between 1 and m, you have to process all `queries[i]` (from i=0 to i=queries.length-1) according to the following rules:

- Initially, you have the permutation P=[1,2,3,...,m].
- For the current query queries[i]:
  1. Find the position of queries[i] in the permutation P (the index is 0-based).
  2. Append this position to the result.
  3. Move queries[i] to the front of the permutation P. Note that the position of each element in P changes accordingly.

Return an array of the result of the queries.

Example:
Input: queries = [3,1,2,1], m = 5
Output: [2,1,2,1]
Explanation: 
Initially, P=[1,2,3,4,5].
After processing the first query, P becomes [3,1,2,4,5], and the result is [2].
After processing the second query, P becomes [1,3,2,4,5], and the result is [2,1].
After processing the third query, P becomes [2,1,3,4,5], and the result is [2,1,2].
After processing the fourth query, P becomes [1,2,3,4,5], and the result is [2,1,2,1].

Constraints:
- 1 <= m <= 100
- 1 <= queries.length <= m
- 1 <= queries[i] <= m
"""

# Python Solution
def processQueries(queries, m):
    """
    Process the queries on the permutation P and return the result.

    :param queries: List[int] - The list of queries.
    :param m: int - The size of the permutation.
    :return: List[int] - The result of processing the queries.
    """
    # Initialize the permutation P
    P = list(range(1, m + 1))
    result = []

    for query in queries:
        # Find the index of the current query in P
        index = P.index(query)
        # Append the index to the result
        result.append(index)
        # Move the queried element to the front of P
        P.insert(0, P.pop(index))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    queries = [3, 1, 2, 1]
    m = 5
    print(processQueries(queries, m))  # Output: [2, 1, 2, 1]

    # Test Case 2
    queries = [4, 1, 2, 2]
    m = 4
    print(processQueries(queries, m))  # Output: [3, 1, 2, 0]

    # Test Case 3
    queries = [7, 5, 5, 8, 3]
    m = 8
    print(processQueries(queries, m))  # Output: [6, 4, 0, 7, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each query, we perform the following operations:
  1. Find the index of the query in P, which takes O(m) in the worst case.
  2. Remove the element from P and insert it at the front, which also takes O(m) in the worst case.
- Since there are n queries, the total time complexity is O(n * m).

Space Complexity:
- The space complexity is O(m) for storing the permutation P.
- The result list takes O(n) space, but this is considered output space and not part of the algorithm's auxiliary space.
- Overall, the space complexity is O(m).
"""

# Topic: Arrays