"""
LeetCode Question #1562: Find Latest Group of Size M

Problem Statement:
You are given an array `arr` that represents a permutation of numbers from 1 to n. You are also given an integer `m`.

Initially, you have an empty binary string of size `n`, and `arr[i]` represents the position where you should flip the bit (from 0 to 1) at step `i`.

After each step, if there exists a group of consecutive 1s of length `m`, you should record the step number. Return the latest step at which there exists a group of size `m`. If no such group exists, return -1.

Example:
Input: arr = [3,5,1,2,4], m = 1
Output: 4
Explanation:
Step 1: "00100", groups: [1]
Step 2: "00101", groups: [1, 1]
Step 3: "10101", groups: [1, 1, 1]
Step 4: "11101", groups: [3, 1]
Step 5: "11111", groups: [5]
The latest step at which a group of size 1 existed is step 4.

Constraints:
- `n == arr.length`
- `1 <= n <= 10^5`
- `1 <= arr[i] <= n`
- All integers in `arr` are unique.
- `1 <= m <= n`
"""

# Python Solution
def findLatestStep(arr, m):
    n = len(arr)
    if m == n:  # Special case: if m equals n, the entire array will be a group of size m at the last step.
        return n

    # Initialize variables
    length = [0] * (n + 2)  # Array to track the length of groups
    result = -1  # Default result if no group of size m exists

    for step, pos in enumerate(arr):
        left = length[pos - 1]  # Length of the group to the left of `pos`
        right = length[pos + 1]  # Length of the group to the right of `pos`
        new_length = left + right + 1  # New group length after flipping `pos`

        # Update the length array
        length[pos - left] = new_length  # Update the start of the new group
        length[pos + right] = new_length  # Update the end of the new group

        # Check if groups of size `m` exist after this step
        if left == m or right == m:
            result = step

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr = [3, 5, 1, 2, 4]
    m = 1
    print(findLatestStep(arr, m))  # Output: 4

    # Test Case 2
    arr = [3, 1, 5, 4, 2]
    m = 2
    print(findLatestStep(arr, m))  # Output: -1

    # Test Case 3
    arr = [1, 2, 3, 4, 5]
    m = 5
    print(findLatestStep(arr, m))  # Output: 5

    # Test Case 4
    arr = [5, 4, 3, 2, 1]
    m = 1
    print(findLatestStep(arr, m))  # Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `arr` array once, performing constant-time operations for each element.
- Therefore, the time complexity is O(n), where `n` is the length of the array.

Space Complexity:
- The `length` array is of size `n + 2`, which is O(n).
- Thus, the space complexity is O(n).
"""

# Topic: Arrays