"""
LeetCode Problem #1850: Minimum Adjacent Swaps to Reach the Kth Smallest Number

Problem Statement:
You are given a string `num`, representing a large integer, and an integer `k`.
The task is to find the k-th smallest permutation of the string `num` and return
the minimum number of adjacent swaps required to transform the string `num` into
that permutation.

A permutation of an array is a rearrangement of its elements. The k-th smallest
permutation is the k-th permutation when the permutations are sorted in
lexicographical order.

Example:
Input: num = "5489355142", k = 4
Output: 2
Explanation: The 4th smallest permutation of "5489355142" is "5489355214".
To transform "5489355142" into "5489355214", we need at least 2 adjacent swaps.

Constraints:
- 2 <= num.length <= 1000
- 1 <= k <= 1000
- num contains only digits.
"""

# Solution
def getMinSwaps(num: str, k: int) -> int:
    def next_permutation(s):
        """Generate the next lexicographical permutation of the list."""
        n = len(s)
        i = n - 2
        while i >= 0 and s[i] >= s[i + 1]:
            i -= 1
        if i == -1:
            return False
        j = n - 1
        while s[j] <= s[i]:
            j -= 1
        s[i], s[j] = s[j], s[i]
        s[i + 1:] = reversed(s[i + 1:])
        return True

    def count_swaps(original, target):
        """Count the minimum adjacent swaps to transform original into target."""
        original = list(original)
        target = list(target)
        swaps = 0
        i = 0
        while i < len(original):
            if original[i] != target[i]:
                j = i
                while original[j] != target[i]:
                    j += 1
                while j > i:
                    original[j], original[j - 1] = original[j - 1], original[j]
                    swaps += 1
                    j -= 1
            i += 1
        return swaps

    # Generate the k-th smallest permutation
    original = list(num)
    target = list(num)
    for _ in range(k):
        next_permutation(target)

    # Count the minimum adjacent swaps to transform original into target
    return count_swaps(original, target)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num = "5489355142"
    k = 4
    print(getMinSwaps(num, k))  # Output: 2

    # Test Case 2
    num = "11112"
    k = 4
    print(getMinSwaps(num, k))  # Output: 4

    # Test Case 3
    num = "00123"
    k = 1
    print(getMinSwaps(num, k))  # Output: 1

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Generating the k-th permutation: O(k * n), where n is the length of the string.
     Each call to `next_permutation` takes O(n) time.
   - Counting swaps: O(n^2), as we may need to traverse the list multiple times
     to perform adjacent swaps.
   - Overall: O(k * n + n^2).

2. Space Complexity:
   - The space complexity is O(n), as we use lists to store the original and target
     permutations.

Topic: String Manipulation
"""