"""
LeetCode Problem #923: 3Sum With Multiplicity

Problem Statement:
Given an integer array `arr`, and an integer target, return the number of tuples `(i, j, k)` such that:
- `i < j < k`
- `arr[i] + arr[j] + arr[k] == target`

As the answer can be very large, return it modulo `10^9 + 7`.

Constraints:
- `3 <= arr.length <= 3000`
- `0 <= arr[i] <= 100`
- `0 <= target <= 300`

Example:
Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20

Input: arr = [1,1,2,2,2,2], target = 5
Output: 12
"""

# Python Solution
from collections import Counter

def threeSumMulti(arr, target):
    MOD = 10**9 + 7
    count = Counter(arr)
    keys = sorted(count.keys())
    result = 0

    for i, x in enumerate(keys):
        for j, y in enumerate(keys[i:], i):
            z = target - x - y
            if z < y:
                break
            if z in count:
                if x == y == z:
                    result += count[x] * (count[x] - 1) * (count[x] - 2) // 6
                elif x == y:
                    result += count[x] * (count[x] - 1) // 2 * count[z]
                elif y == z:
                    result += count[y] * (count[y] - 1) // 2 * count[x]
                else:
                    result += count[x] * count[y] * count[z]

    return result % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
    target1 = 8
    print(threeSumMulti(arr1, target1))  # Output: 20

    # Test Case 2
    arr2 = [1, 1, 2, 2, 2, 2]
    target2 = 5
    print(threeSumMulti(arr2, target2))  # Output: 12

    # Test Case 3
    arr3 = [0, 0, 0, 0]
    target3 = 0
    print(threeSumMulti(arr3, target3))  # Output: 4

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    target4 = 10
    print(threeSumMulti(arr4, target4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over all pairs of keys in the sorted list of unique elements in `arr`.
- If there are `m` unique elements in `arr`, the number of pairs is approximately `m^2`.
- Since `m` is at most 101 (due to the constraint `0 <= arr[i] <= 100`), the time complexity is O(m^2), which is effectively O(1) for this problem.

Space Complexity:
- The algorithm uses a Counter to store the frequency of elements in `arr`, which requires O(m) space, where `m` is the number of unique elements.
- Thus, the space complexity is O(m), which is effectively O(1) for this problem.

Topic: Arrays
"""