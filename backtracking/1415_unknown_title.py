"""
LeetCode Problem #1415: The k-th Lexicographical String of All Happy Strings of Length n

Problem Statement:
A happy string is a string that:
- Consists only of the letters ['a', 'b', 'c'].
- Does not have any two consecutive characters that are the same.

Given two integers n and k, consider a list of all happy strings of length n sorted in lexicographical order. Return the k-th string of this list or return an empty string if there are fewer than k happy strings of length n.

Constraints:
- 1 <= n <= 10
- 1 <= k <= 100

Example:
Input: n = 3, k = 9
Output: "cab"

Input: n = 1, k = 4
Output: ""

Input: n = 2, k = 7
Output: ""
"""

# Solution
def getHappyString(n: int, k: int) -> str:
    def backtrack(current):
        # If the current string has reached the desired length, add it to the result
        if len(current) == n:
            result.append(current)
            return
        
        # Try adding each character 'a', 'b', 'c' to the current string
        for char in 'abc':
            # Ensure no two consecutive characters are the same
            if not current or current[-1] != char:
                backtrack(current + char)
    
    # List to store all happy strings
    result = []
    # Start backtracking with an empty string
    backtrack("")
    
    # If k is greater than the number of happy strings, return an empty string
    return result[k - 1] if k <= len(result) else ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1, k1 = 3, 9
    print(getHappyString(n1, k1))  # Output: "cab"

    # Test Case 2
    n2, k2 = 1, 4
    print(getHappyString(n2, k2))  # Output: ""

    # Test Case 3
    n3, k3 = 2, 7
    print(getHappyString(n3, k3))  # Output: ""

    # Test Case 4
    n4, k4 = 3, 1
    print(getHappyString(n4, k4))  # Output: "aba"

    # Test Case 5
    n5, k5 = 4, 15
    print(getHappyString(n5, k5))  # Output: "abac"

"""
Time Complexity Analysis:
- The backtracking function generates all possible happy strings of length n.
- There are at most 3 * 2^(n-1) happy strings of length n (each character has 3 choices for the first position and 2 choices for subsequent positions).
- Thus, the time complexity is O(3 * 2^(n-1)).

Space Complexity Analysis:
- The space complexity is O(n) for the recursion stack, where n is the length of the string being generated.
- Additionally, the result list stores all happy strings, which can take up to O(3 * 2^(n-1)) space in the worst case.

Primary Topic: Backtracking
"""