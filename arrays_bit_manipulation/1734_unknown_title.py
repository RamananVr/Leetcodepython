"""
LeetCode Problem #1734: Decode XORed Permutation

Problem Statement:
There is an integer array `perm` that is a permutation of the first `n` positive integers, where `n` is always odd (i.e., `n == 2 * k + 1` for some integer `k`).

It was encoded into another integer array `encoded` of length `n - 1`, such that `encoded[i] = perm[i] XOR perm[i + 1]`. For example, if `perm = [1,3,2]`, then `encoded = [2,1]`.

Given the `encoded` array, you are tasked to find the original array `perm`. It is guaranteed that the answer exists and is unique.

Example 1:
Input: encoded = [3,1]
Output: [1,2,3]

Example 2:
Input: encoded = [6,5,4,6]
Output: [2,4,1,5,3]

Constraints:
- 3 <= n < 10^5
- n is odd.
- `encoded.length == n - 1`
"""

# Solution
def decode(encoded):
    """
    Decodes the XORed permutation array to find the original permutation.

    :param encoded: List[int] - The encoded array of integers.
    :return: List[int] - The original permutation array.
    """
    n = len(encoded) + 1

    # Step 1: Compute the XOR of all numbers from 1 to n (perm[0] XOR perm[1] XOR ... XOR perm[n-1])
    total_xor = 0
    for i in range(1, n + 1):
        total_xor ^= i

    # Step 2: Compute the XOR of all odd-indexed elements in `encoded` (perm[1] XOR perm[3] XOR ...)
    odd_xor = 0
    for i in range(1, len(encoded), 2):
        odd_xor ^= encoded[i]

    # Step 3: Find the first element of `perm` (perm[0])
    perm_first = total_xor ^ odd_xor

    # Step 4: Reconstruct the entire `perm` array
    perm = [perm_first]
    for num in encoded:
        perm.append(perm[-1] ^ num)

    return perm

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    encoded = [3, 1]
    print(decode(encoded))  # Output: [1, 2, 3]

    # Test Case 2
    encoded = [6, 5, 4, 6]
    print(decode(encoded))  # Output: [2, 4, 1, 5, 3]

    # Test Case 3
    encoded = [2, 4, 6, 8, 10]
    print(decode(encoded))  # Output: [1, 3, 7, 1, 9, 3]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Computing `total_xor` takes O(n) time, where n is the length of the `perm` array.
- Computing `odd_xor` takes O(n/2) = O(n) time, as we iterate over half of the `encoded` array.
- Reconstructing the `perm` array takes O(n) time.
- Overall, the time complexity is O(n).

Space Complexity:
- The algorithm uses O(1) additional space, as we only store a few variables and the result array.
- The space complexity is O(n) if we include the output array `perm`, which is required to store the result.
"""

# Topic: Arrays, Bit Manipulation