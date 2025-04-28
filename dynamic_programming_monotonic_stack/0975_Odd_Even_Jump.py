"""
LeetCode Problem #975: Odd Even Jump

You are given an integer array `arr`. From some starting index, you can make a series of jumps. 
The (1st, 3rd, 5th, ...) jumps in the series are called odd-numbered jumps, and the (2nd, 4th, 6th, ...) 
jumps in the series are called even-numbered jumps. Note that the jumps are numbered, not the indices.

- You may jump forward from index `i` to index `j` (with `i < j`) in the following way:
  - During odd-numbered jumps (1st, 3rd, 5th, ...), you jump to the index `j` such that:
    - `arr[i] <= arr[j]`
    - `arr[j]` is the smallest possible value.
    - If there are multiple such `j` values, you jump to the smallest `j`.
  - During even-numbered jumps (2nd, 4th, 6th, ...), you jump to the index `j` such that:
    - `arr[i] >= arr[j]`
    - `arr[j]` is the largest possible value.
    - If there are multiple such `j` values, you jump to the smallest `j`.

- A starting index is good if, starting from that index, you can reach the end of the array (index `n - 1`) 
  by jumping some number of times (possibly 0 or more).

Return the number of good starting indices.

Constraints:
- `1 <= arr.length <= 2 * 10^4`
- `0 <= arr[i] < 10^5`
"""

from sortedcontainers import SortedDict

def oddEvenJumps(arr):
    n = len(arr)
    if n == 1:
        return 1

    # Helper function to find the next index for odd/even jumps
    def make_jump_indices(is_odd):
        result = [None] * n
        stack = []
        for i in indices:
            while stack and stack[-1] < i:
                result[stack.pop()] = i
            stack.append(i)
        return result

    # Sort indices for odd and even jumps
    indices = sorted(range(n), key=lambda i: (arr[i], i))
    odd_next = make_jump_indices(True)
    indices = sorted(range(n), key=lambda i: (-arr[i], i))
    even_next = make_jump_indices(False)

    # DP arrays to track if we can reach the end
    odd = [False] * n
    even = [False] * n
    odd[-1] = even[-1] = True

    # Fill DP arrays
    for i in range(n - 2, -1, -1):
        if odd_next[i] is not None:
            odd[i] = even[odd_next[i]]
        if even_next[i] is not None:
            even[i] = odd[even_next[i]]

    # Count good starting indices
    return sum(odd)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [10, 13, 12, 14, 15]
    print(oddEvenJumps(arr1))  # Output: 2

    # Test Case 2
    arr2 = [2, 3, 1, 1, 4]
    print(oddEvenJumps(arr2))  # Output: 3

    # Test Case 3
    arr3 = [5, 1, 3, 4, 2]
    print(oddEvenJumps(arr3))  # Output: 3

"""
Time Complexity:
- Sorting the indices takes O(n log n).
- Constructing the jump indices takes O(n) for each of odd and even jumps.
- Filling the DP arrays takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used by the `odd_next` and `even_next` arrays is O(n).
- The space used by the `odd` and `even` DP arrays is O(n).
- Overall space complexity: O(n).

Topic: Dynamic Programming, Monotonic Stack
"""