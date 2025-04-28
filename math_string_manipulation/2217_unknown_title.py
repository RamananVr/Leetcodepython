"""
LeetCode Problem #2217: Find Palindrome With Fixed Length

Problem Statement:
You are given an integer array `queries` and a positive integer `intLength`. Each query `queries[i]` represents the `i-th` smallest **positive palindrome** of length `intLength`.

Return an array `answer` where `answer[i]` is the `i-th` smallest palindrome of length `intLength` if it exists, or `-1` if no such palindrome exists.

A palindrome is a number that reads the same backward as forward. For example, `121` is a palindrome, while `123` is not.

Constraints:
- `1 <= queries.length <= 5 * 10^4`
- `1 <= queries[i] <= 10^9`
- `1 <= intLength <= 15`
"""

def kthPalindrome(queries, intLength):
    """
    Finds the k-th smallest palindrome of a given fixed length for each query.

    :param queries: List[int] - List of queries representing the k-th smallest palindrome to find.
    :param intLength: int - The fixed length of the palindrome.
    :return: List[int] - List of results for each query.
    """
    # Determine the half-length of the palindrome
    half_length = (intLength + 1) // 2
    start = 10 ** (half_length - 1)  # Smallest number with `half_length` digits
    end = 10 ** half_length          # Largest number with `half_length` digits

    # Total number of palindromes of length `intLength`
    total_palindromes = end - start

    result = []
    for query in queries:
        if query > total_palindromes:
            result.append(-1)  # Query exceeds the number of possible palindromes
        else:
            # Find the base half of the palindrome
            half = start + query - 1
            half_str = str(half)

            # Construct the full palindrome
            if intLength % 2 == 0:
                palindrome = int(half_str + half_str[::-1])
            else:
                palindrome = int(half_str + half_str[-2::-1])

            result.append(palindrome)

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    queries = [1, 2, 3, 4, 5, 90]
    intLength = 3
    print(kthPalindrome(queries, intLength))  # Output: [101, 111, 121, 131, 141, 999]

    # Test Case 2
    queries = [2, 4, 6]
    intLength = 2
    print(kthPalindrome(queries, intLength))  # Output: [22, 44, 66]

    # Test Case 3
    queries = [1, 2, 3]
    intLength = 1
    print(kthPalindrome(queries, intLength))  # Output: [1, 2, 3]

    # Test Case 4
    queries = [1000000000]
    intLength = 15
    print(kthPalindrome(queries, intLength))  # Output: [-1]

"""
Time Complexity:
- Let `n` be the length of the `queries` array.
- For each query, we perform constant-time operations to calculate the palindrome.
- Thus, the time complexity is O(n).

Space Complexity:
- The space complexity is O(1) for the algorithm itself, as we only use a few variables.
- The output list `result` requires O(n) space to store the results.

Topic: Math, String Manipulation
"""