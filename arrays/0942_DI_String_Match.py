"""
LeetCode Problem #942: DI String Match

Problem Statement:
A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
- s[i] == 'I' if perm[i] < perm[i + 1], and
- s[i] == 'D' if perm[i] > perm[i + 1].

Given a string s, reconstruct the permutation perm and return it. 
If there are multiple valid permutations perm, return any of them.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'I' or 'D'
"""

def diStringMatch(s: str) -> list[int]:
    """
    Reconstructs a permutation based on the given DI string.

    Args:
    s (str): A string consisting of 'I' and 'D' characters.

    Returns:
    list[int]: A permutation of integers satisfying the DI string.
    """
    n = len(s)
    low, high = 0, n
    result = []

    for char in s:
        if char == 'I':
            result.append(low)
            low += 1
        else:  # char == 'D'
            result.append(high)
            high -= 1

    # Append the last remaining number
    result.append(low)  # At this point, low == high
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "IDID"
    print(f"Input: {s1} -> Output: {diStringMatch(s1)}")

    # Test Case 2
    s2 = "III"
    print(f"Input: {s2} -> Output: {diStringMatch(s2)}")

    # Test Case 3
    s3 = "DDI"
    print(f"Input: {s3} -> Output: {diStringMatch(s3)}")

    # Test Case 4
    s4 = "DIDI"
    print(f"Input: {s4} -> Output: {diStringMatch(s4)}")

"""
Time Complexity Analysis:
- The algorithm iterates through the string `s` once, performing O(1) operations for each character.
- Therefore, the time complexity is O(n), where n is the length of the string `s`.

Space Complexity Analysis:
- The algorithm uses a result list of size n + 1 to store the permutation.
- Therefore, the space complexity is O(n).

Topic: Arrays
"""