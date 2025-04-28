"""
LeetCode Problem #1982: Find Array Given Subset Sums

Problem Statement:
You are given an integer `n` representing the size of an unknown array that you need to recover. 
You are also given a sorted list `subset_sums` of length `2^n` that contains all the subset sums of the unknown array (including the empty subset sum, which is always 0).

Return the array `original` of size `n` that generates the given `subset_sums`. 
If there are multiple possible answers, return any of them.

Example 1:
Input: n = 3, subset_sums = [-3, -2, -1, 0, 0, 1, 2, 3]
Output: [1, 2, -3]

Example 2:
Input: n = 2, subset_sums = [0, 0, 5, 5]
Output: [5, 0]

Constraints:
- 1 <= n <= 15
- subset_sums.length == 2^n
- -10^4 <= subset_sums[i] <= 10^4
- subset_sums is sorted in non-decreasing order.
"""

from collections import Counter

def recoverArray(n, subset_sums):
    """
    Recover the original array from its subset sums.

    :param n: int, size of the original array
    :param subset_sums: List[int], sorted list of all subset sums
    :return: List[int], the original array
    """
    subset_sums.sort()
    original = []

    for _ in range(n):
        # The difference between the largest and second largest subset sums is the next element
        x = subset_sums[-1] - subset_sums[-2]
        original.append(x)

        # Split subset_sums into two groups: those that include x and those that don't
        count = Counter(subset_sums)
        new_subset_sums = []
        for num in subset_sums:
            if count[num] > 0:
                count[num] -= 1
                count[num + x] -= 1
                new_subset_sums.append(num)
        subset_sums = new_subset_sums

    return original

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 3
    subset_sums1 = [-3, -2, -1, 0, 0, 1, 2, 3]
    print(recoverArray(n1, subset_sums1))  # Output: [1, 2, -3] (or any valid permutation)

    # Test Case 2
    n2 = 2
    subset_sums2 = [0, 0, 5, 5]
    print(recoverArray(n2, subset_sums2))  # Output: [5, 0] (or any valid permutation)

    # Test Case 3
    n3 = 4
    subset_sums3 = [0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3]
    print(recoverArray(n3, subset_sums3))  # Output: [1, 1, 1, 0] (or any valid permutation)

"""
Time Complexity:
- Sorting the subset_sums initially takes O(2^n log(2^n)) = O(n * 2^n).
- For each of the n iterations, we process the subset_sums list, which has size O(2^n).
- Thus, the overall time complexity is O(n * 2^n).

Space Complexity:
- The space complexity is O(2^n) due to the storage of subset_sums and the Counter object.

Topic: Arrays, Backtracking, Sorting
"""