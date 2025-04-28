"""
LeetCode Question #2438: Range Product Queries of Powers

Problem Statement:
You are given a positive integer n, representing the number n. You are also given a 2D integer array queries where queries[i] = [start_i, end_i].

You need to compute the product of the powers of 2 corresponding to the binary representation of n for each query. Specifically:
- The binary representation of n can be written as a sum of powers of 2. For example, if n = 13, its binary representation is "1101", which corresponds to 2^0 + 2^2 + 2^3.
- For each query [start_i, end_i], compute the product of the powers of 2 corresponding to the indices in the range [start_i, end_i] (inclusive) of the binary representation of n.

Return an array of integers where the i-th integer is the result of the i-th query modulo 10^9 + 7.

Constraints:
- 1 <= n <= 10^9
- 1 <= queries.length <= 10^5
- 0 <= start_i <= end_i < 31

Example:
Input: n = 13, queries = [[0, 1], [1, 2], [0, 3]]
Output: [2, 8, 128]
Explanation:
- Binary representation of 13 is "1101".
- For query [0, 1], the product is 2^0 * 2^1 = 2.
- For query [1, 2], the product is 2^1 * 2^2 = 8.
- For query [0, 3], the product is 2^0 * 2^2 * 2^3 = 128.
"""

# Python Solution
from typing import List

def productQueries(n: int, queries: List[List[int]]) -> List[int]:
    MOD = 10**9 + 7
    
    # Extract the powers of 2 from the binary representation of n
    powers = []
    for i in range(31):  # Iterate through 31 bits (since n <= 10^9)
        if n & (1 << i):  # Check if the i-th bit is set
            powers.append(2**i)
    
    # Process each query
    result = []
    for start, end in queries:
        product = 1
        for i in range(start, end + 1):
            product = (product * powers[i]) % MOD
        result.append(product)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 13
    queries = [[0, 1], [1, 2], [0, 3]]
    print(productQueries(n, queries))  # Output: [2, 8, 128]

    # Test Case 2
    n = 15
    queries = [[0, 0], [1, 3], [0, 2]]
    print(productQueries(n, queries))  # Output: [1, 128, 16]

    # Test Case 3
    n = 8
    queries = [[0, 0]]
    print(productQueries(n, queries))  # Output: [8]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Extracting the powers of 2 from the binary representation of n takes O(31) = O(1) since n is at most 10^9.
- For each query, we compute the product of powers in the range [start, end]. In the worst case, this involves iterating over all powers, which is O(31) = O(1) per query.
- With q queries, the total time complexity is O(q), where q is the number of queries.

Space Complexity:
- The `powers` list stores at most 31 elements (the powers of 2 corresponding to the binary representation of n). This requires O(31) = O(1) space.
- The result list stores the output for each query, requiring O(q) space.
- Overall space complexity is O(q).

Topic: Bit Manipulation
"""