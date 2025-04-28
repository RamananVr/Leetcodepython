"""
LeetCode Question #1220: Count Vowels Permutation

Problem Statement:
Given an integer n, your task is to count how many strings of length n can be formed under the following rules:
1. Each character is a vowel ('a', 'e', 'i', 'o', 'u').
2. Each vowel 'a' may only be followed by 'e'.
3. Each vowel 'e' may only be followed by 'a' or 'i'.
4. Each vowel 'i' may not be followed by another 'i'.
5. Each vowel 'o' may only be followed by 'i' or 'u'.
6. Each vowel 'u' may only be followed by 'a'.

Return the count of strings modulo 10^9 + 7.

Constraints:
- 1 <= n <= 2 * 10^4
"""

# Python Solution
def countVowelPermutation(n: int) -> int:
    MOD = 10**9 + 7

    # Initialize counts for strings of length 1
    a_count = e_count = i_count = o_count = u_count = 1

    for _ in range(1, n):
        # Update counts based on the rules
        new_a_count = (e_count + i_count + u_count) % MOD
        new_e_count = (a_count + i_count) % MOD
        new_i_count = (e_count + o_count) % MOD
        new_o_count = i_count % MOD
        new_u_count = (i_count + o_count) % MOD

        # Assign new counts to current counts
        a_count, e_count, i_count, o_count, u_count = (
            new_a_count,
            new_e_count,
            new_i_count,
            new_o_count,
            new_u_count,
        )

    # Return the total count modulo 10^9 + 7
    return (a_count + e_count + i_count + o_count + u_count) % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    # Explanation: There are 5 strings of length 1: "a", "e", "i", "o", "u".
    print(countVowelPermutation(1))  # Output: 5

    # Test Case 2: n = 2
    # Explanation: Strings of length 2 are formed based on the rules.
    print(countVowelPermutation(2))  # Output: 10

    # Test Case 3: n = 5
    # Explanation: Count strings of length 5 based on the rules.
    print(countVowelPermutation(5))  # Output: 68

    # Test Case 4: n = 10
    print(countVowelPermutation(10))  # Output: 1739


# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the range of n, performing constant-time operations at each step.
# - Therefore, the time complexity is linear in terms of n.

# Space Complexity: O(1)
# - We use a constant amount of space to store the counts for each vowel.
# - No additional data structures are used, so the space complexity is constant.

# Topic: Dynamic Programming (DP)