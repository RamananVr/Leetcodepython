"""
LeetCode Problem #2782: Unique Subsequences of Length K

Problem Statement:
You are given a string `s` and an integer `k`. Your task is to find the number of unique subsequences of length `k` that can be formed from the string `s`.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Return the number of unique subsequences of length `k`.

Constraints:
- 1 <= k <= len(s) <= 1000
- `s` consists of lowercase English letters.
"""

# Solution
def uniqueSubsequencesOfLengthK(s: str, k: int) -> int:
    from itertools import combinations

    # Use a set to store unique subsequences of length k
    unique_subsequences = set()

    # Generate all combinations of indices of length k
    for indices in combinations(range(len(s)), k):
        # Form the subsequence using the indices
        subsequence = ''.join(s[i] for i in indices)
        unique_subsequences.add(subsequence)

    # Return the count of unique subsequences
    return len(unique_subsequences)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abc"
    k1 = 2
    print(uniqueSubsequencesOfLengthK(s1, k1))  # Expected Output: 3 ("ab", "ac", "bc")

    # Test Case 2
    s2 = "aaa"
    k2 = 2
    print(uniqueSubsequencesOfLengthK(s2, k2))  # Expected Output: 1 ("aa")

    # Test Case 3
    s3 = "abcd"
    k3 = 3
    print(uniqueSubsequencesOfLengthK(s3, k3))  # Expected Output: 4 ("abc", "abd", "acd", "bcd")

    # Test Case 4
    s4 = "aabbcc"
    k4 = 2
    print(uniqueSubsequencesOfLengthK(s4, k4))  # Expected Output: 6 ("aa", "ab", "ac", "bb", "bc", "cc")

# Time and Space Complexity Analysis
"""
Time Complexity:
- Generating all combinations of indices of length k takes O(C(n, k)), where C(n, k) = n! / (k! * (n-k)!) is the number of combinations.
- For each combination, forming the subsequence takes O(k).
- Therefore, the overall time complexity is O(C(n, k) * k).

Space Complexity:
- The space complexity is dominated by the storage of unique subsequences in the set, which can store up to C(n, k) subsequences.
- Therefore, the space complexity is O(C(n, k) * k), where k is the length of each subsequence.

Note: This solution is not optimal for large values of n and k due to the combinatorial explosion. Optimized solutions may involve dynamic programming or hashing techniques.

Topic: Strings, Combinatorics
"""