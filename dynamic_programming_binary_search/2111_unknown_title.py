"""
LeetCode Problem #2111: Minimum Operations to Make the Array K-Increasing

Problem Statement:
You are given an integer array `arr` and an integer `k`. The array is called k-increasing if `arr[i] <= arr[i+k]` for every index `i` where `i + k < len(arr)`.

In one operation, you can choose an index `i` and change `arr[i]` to any value.

Return the minimum number of operations required to make the array k-increasing.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i], k <= 10^5
"""

from bisect import bisect_right

def minOperations(arr, k):
    """
    Function to calculate the minimum number of operations to make the array k-increasing.
    """
    def min_operations_to_make_non_decreasing(subarray):
        """
        Helper function to calculate the minimum operations to make a subarray non-decreasing.
        This is done by finding the length of the Longest Non-Decreasing Subsequence (LNDS).
        """
        lnds = []
        for num in subarray:
            pos = bisect_right(lnds, num)
            if pos == len(lnds):
                lnds.append(num)
            else:
                lnds[pos] = num
        return len(subarray) - len(lnds)

    n = len(arr)
    total_operations = 0

    # Process each group of indices modulo k
    for start in range(k):
        subarray = []
        for i in range(start, n, k):
            subarray.append(arr[i])
        total_operations += min_operations_to_make_non_decreasing(subarray)

    return total_operations

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [5, 4, 3, 2, 1]
    k1 = 1
    print(minOperations(arr1, k1))  # Output: 4

    # Test Case 2
    arr2 = [4, 1, 5, 2, 6, 2]
    k2 = 2
    print(minOperations(arr2, k2))  # Output: 2

    # Test Case 3
    arr3 = [4, 3, 1, 2, 5, 6]
    k3 = 3
    print(minOperations(arr3, k3))  # Output: 2

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5]
    k4 = 1
    print(minOperations(arr4, k4))  # Output: 0

"""
Time Complexity:
- Let `n` be the length of the array and `k` be the given integer.
- We divide the array into `k` groups, each of size approximately `n/k`.
- For each group, we calculate the Longest Non-Decreasing Subsequence (LNDS) using a binary search approach, which takes O((n/k) * log(n/k)).
- Since there are `k` groups, the total time complexity is O(k * (n/k) * log(n/k)) = O(n * log(n/k)).

Space Complexity:
- The space complexity is O(n/k) for storing the subarray for each group and O(n/k) for the LNDS array. Thus, the total space complexity is O(n/k).

Topic: Dynamic Programming, Binary Search
"""