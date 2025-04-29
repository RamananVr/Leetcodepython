"""
LeetCode Problem #2912: Number of Ways to Reach Destination After K Steps

Problem Statement:
You are given two positive integers `startPos` and `endPos`. Initially, you are standing at position `startPos` on an infinite number line. With one step, you can move either one position to the left or one position to the right.

Given a positive integer `k`, return the number of different ways to reach the position `endPos` starting from `startPos` in exactly `k` steps. Since the answer may be large, return it modulo 10^9 + 7.

Two ways are considered different if the sequence of moves is different.

Constraints:
1 <= startPos, endPos, k <= 1000
"""

# Solution using Combinatorics and Modular Arithmetic
MOD = 10**9 + 7

# Precompute factorials and their modular inverses
MAX_K = 1001 # Max value of k + buffer
fact = [1] * MAX_K
inv_fact = [1] * MAX_K

for i in range(1, MAX_K):
    fact[i] = (fact[i - 1] * i) % MOD

# Calculate modular inverse using Fermat's Little Theorem: a^(MOD-2) % MOD
inv_fact[MAX_K - 1] = pow(fact[MAX_K - 1], MOD - 2, MOD)
for i in range(MAX_K - 2, -1, -1):
    inv_fact[i] = (inv_fact[i + 1] * (i + 1)) % MOD

def nCr_mod(n, r):
    """Calculates nCr % MOD using precomputed factorials and inverses."""
    if r < 0 or r > n:
        return 0
    num = fact[n]
    den = (inv_fact[r] * inv_fact[n - r]) % MOD
    return (num * den) % MOD

def numberOfWays(startPos: int, endPos: int, k: int) -> int:
    """
    Calculates the number of ways to reach endPos from startPos in k steps.

    Args:
        startPos: The starting position.
        endPos: The target ending position.
        k: The exact number of steps allowed.

    Returns:
        The number of ways modulo 10^9 + 7.
    """
    diff = endPos - startPos
    abs_diff = abs(diff)

    # Check feasibility
    if abs_diff > k:
        return 0 # Cannot reach if distance > steps
    if (k - abs_diff) % 2 != 0:
        return 0 # Parity mismatch: difference in steps must be even

    # Calculate number of right steps (R)
    # R + L = k
    # R - L = diff
    # 2R = k + diff => R = (k + diff) // 2
    # Since we passed the checks, k + diff is non-negative and even
    right_steps = (k + diff) // 2

    # The number of ways is C(k, right_steps)
    return nCr_mod(k, right_steps)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    startPos1, endPos1, k1 = 1, 2, 3
    expected_output1 = 3 # RLR, LRR, RRL
    result1 = numberOfWays(startPos1, endPos1, k1)
    assert result1 == expected_output1, f"Test Case 1 Failed: Expected {expected_output1}, Got {result1}"
    print(f"Test Case 1 Passed: Result = {result1}")

    # Test Case 2
    startPos2, endPos2, k2 = 2, 5, 10
    expected_output2 = 0 # diff=3, k=10. (10-3)%2=1 != 0. Impossible.
    result2 = numberOfWays(startPos2, endPos2, k2)
    assert result2 == expected_output2, f"Test Case 2 Failed: Expected {expected_output2}, Got {result2}"
    print(f"Test Case 2 Passed: Result = {result2}")

    # Test Case 3
    startPos3, endPos3, k3 = 1, 1, 4
    expected_output3 = 6 # RRLL, RLRL, RLLR, LRRL, LRLR, LLRR
    result3 = numberOfWays(startPos3, endPos3, k3)
    assert result3 == expected_output3, f"Test Case 3 Failed: Expected {expected_output3}, Got {result3}"
    print(f"Test Case 3 Passed: Result = {result3}")

    # Test Case 4
    startPos4, endPos4, k4 = 5, 1, 4
    expected_output4 = 1 # LLLL
    result4 = numberOfWays(startPos4, endPos4, k4)
    assert result4 == expected_output4, f"Test Case 4 Failed: Expected {expected_output4}, Got {result4}"
    print(f"Test Case 4 Passed: Result = {result4}")

    # Test Case 5 (Larger k)
    startPos5, endPos5, k5 = 1, 1000, 999
    expected_output5 = 1 # Must go right 999 times
    result5 = numberOfWays(startPos5, endPos5, k5)
    assert result5 == expected_output5, f"Test Case 5 Failed: Expected {expected_output5}, Got {result5}"
    print(f"Test Case 5 Passed: Result = {result5}")

    print("\nAll provided test cases passed!")


"""
Time and Space Complexity Analysis:

Time Complexity:
- Precomputation of factorials and inverse factorials takes O(MAX_K + log(MOD)) time. This is done once.
- Each call to `numberOfWays` involves basic arithmetic operations and one call to `nCr_mod`, which takes O(1) time due to precomputation.
- Overall time complexity per test case (after precomputation) is O(1).

Space Complexity:
- We store factorials and inverse factorials up to MAX_K.
- Space complexity is O(MAX_K) for the precomputed tables.

Topic: Math, Combinatorics, Dynamic Programming (Implicit)
"""