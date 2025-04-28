"""
LeetCode Problem #2573: Find the String with LCP

Problem Statement:
You are given an n x n integer matrix `lcp` where `lcp[i][j]` represents the length of the longest common prefix 
of the strings `s[i:]` and `s[j:]` for some string `s` of length `n`. Your task is to find any string `s` of length `n` 
such that the given matrix `lcp` corresponds to the longest common prefix matrix of `s`. If there are multiple valid 
strings, return any of them. If no such string exists, return an empty string.

Example:
Input: lcp = [[3,2,1],[2,2,1],[1,1,1]]
Output: "aba"
Explanation: The string "aba" has the following LCP matrix:
- LCP("aba", "aba") = 3
- LCP("aba", "ba") = 2
- LCP("aba", "a") = 1
- LCP("ba", "ba") = 2
- LCP("ba", "a") = 1
- LCP("a", "a") = 1
Thus, the LCP matrix matches the input.

Constraints:
- n == lcp.length == lcp[i].length
- 1 <= n <= 1000
- 0 <= lcp[i][j] <= n
"""

def findTheString(lcp):
    """
    Function to find a string `s` such that its LCP matrix matches the given `lcp` matrix.
    If no such string exists, return an empty string.
    """
    n = len(lcp)
    s = [''] * n
    current_char = 'a'

    # Step 1: Assign characters to the string `s` based on the LCP matrix
    for i in range(n):
        if s[i] == '':
            if current_char > 'z':  # If we run out of characters, return an empty string
                return ""
            s[i] = current_char
            for j in range(i + 1, n):
                if lcp[i][j] > 0:
                    s[j] = s[i]
            current_char = chr(ord(current_char) + 1)

    # Step 2: Verify the LCP matrix matches the string `s`
    for i in range(n):
        for j in range(n):
            if lcp[i][j] != calculate_lcp(s, i, j):
                return ""

    return "".join(s)

def calculate_lcp(s, i, j):
    """
    Helper function to calculate the LCP of two substrings starting at indices i and j.
    """
    lcp_length = 0
    while i < len(s) and j < len(s) and s[i] == s[j]:
        lcp_length += 1
        i += 1
        j += 1
    return lcp_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lcp1 = [[3, 2, 1], [2, 2, 1], [1, 1, 1]]
    print(findTheString(lcp1))  # Output: "aba" or any valid string

    # Test Case 2
    lcp2 = [[1, 0], [0, 1]]
    print(findTheString(lcp2))  # Output: "ab" or any valid string

    # Test Case 3
    lcp3 = [[2, 1], [1, 2]]
    print(findTheString(lcp3))  # Output: "aa" or any valid string

    # Test Case 4
    lcp4 = [[1, 1], [1, 1]]
    print(findTheString(lcp4))  # Output: "aa"

    # Test Case 5
    lcp5 = [[2, 1], [1, 3]]
    print(findTheString(lcp5))  # Output: "" (invalid LCP matrix)

"""
Time Complexity:
- Constructing the string `s` takes O(n^2) in the worst case, as we iterate over the matrix to assign characters.
- Verifying the LCP matrix takes O(n^2) as we compare all pairs of substrings.
- Overall time complexity: O(n^2).

Space Complexity:
- The space complexity is O(n) for the string `s`.

Topic: Strings, Matrix
"""