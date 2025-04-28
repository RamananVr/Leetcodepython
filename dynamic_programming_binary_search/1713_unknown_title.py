"""
LeetCode Problem #1713: Minimum Operations to Make a Subsequence

Problem Statement:
You are given two arrays `target` and `arr`, both of which consist of unique integers. You can perform the following operation on `arr` any number of times:

- Insert any integer at any position in `arr`.

Return the minimum number of operations needed to make `target` a subsequence of `arr`.

A subsequence of an array is a new array generated from the original array by deleting some elements (possibly none) without changing the order of the remaining elements.

Constraints:
- `1 <= target.length, arr.length <= 10^5`
- `1 <= target[i], arr[i] <= 10^9`
- All the integers in `target` are unique.
- All the integers in `arr` are unique.
"""

# Solution
from bisect import bisect_left

def minOperations(target, arr):
    """
    Finds the minimum number of operations to make `target` a subsequence of `arr`.

    Args:
    target (List[int]): The target array.
    arr (List[int]): The array to modify.

    Returns:
    int: Minimum number of operations.
    """
    # Map each value in `target` to its index
    target_index = {val: idx for idx, val in enumerate(target)}
    
    # Filter `arr` to only include values present in `target`, and map them to their indices in `target`
    filtered_arr = [target_index[val] for val in arr if val in target_index]
    
    # Find the length of the longest increasing subsequence (LIS) in `filtered_arr`
    lis = []
    for num in filtered_arr:
        pos = bisect_left(lis, num)
        if pos == len(lis):
            lis.append(num)
        else:
            lis[pos] = num
    
    # The minimum operations is the difference between the length of `target` and the LIS
    return len(target) - len(lis)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = [5, 1, 3]
    arr = [9, 4, 2, 3, 4]
    print(minOperations(target, arr))  # Output: 2

    # Test Case 2
    target = [6, 4, 8, 1, 3]
    arr = [4, 7, 6, 2, 3, 8, 6, 1]
    print(minOperations(target, arr))  # Output: 3

    # Test Case 3
    target = [1, 2, 3, 4]
    arr = [2, 4, 1, 3]
    print(minOperations(target, arr))  # Output: 0

    # Test Case 4
    target = [1, 2, 3]
    arr = [3, 2, 1]
    print(minOperations(target, arr))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Mapping `target` to indices: O(n), where n is the length of `target`.
- Filtering `arr` and mapping to indices: O(m), where m is the length of `arr`.
- Finding the LIS using binary search: O(k * log(k)), where k is the length of `filtered_arr`.
  In the worst case, k = min(n, m).
- Overall: O(n + m + k * log(k)) ≈ O(n + m + min(n, m) * log(min(n, m))).

Space Complexity:
- Space for `target_index`: O(n).
- Space for `filtered_arr`: O(min(n, m)).
- Space for `lis`: O(min(n, m)).
- Overall: O(n + min(n, m)).

Topic: Dynamic Programming, Binary Search
"""