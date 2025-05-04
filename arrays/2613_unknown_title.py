"""
LeetCode Problem #2613: Beautiful Pairs

Problem Statement:
You are given two integer arrays `nums1` and `nums2` of length `n`.

A pair `(i, j)` is called beautiful if:
1. `0 <= i, j < n`
2. `i != j`
3. `nums1[i] + nums1[j] == nums2[i] + nums2[j]`

Return the total number of beautiful pairs.

Constraints:
- `n == nums1.length == nums2.length`
- `2 <= n <= 1000`
- `-10^5 <= nums1[i], nums2[i] <= 10^5`
"""

def countBeautifulPairs(nums1, nums2):
    """
    Function to count the number of beautiful pairs in the given arrays.

    Args:
    nums1 (List[int]): First list of integers.
    nums2 (List[int]): Second list of integers.

    Returns:
    int: Total number of beautiful pairs.
    """
    n = len(nums1)
    count = 0

    for i in range(n):
        for j in range(n):
            if i != j and nums1[i] + nums1[j] == nums2[i] + nums2[j]:
                count += 1

    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [1, 2, 3]
    nums2 = [4, 5, 6]
    print(countBeautifulPairs(nums1, nums2))  # Expected Output: 0

    # Test Case 2
    nums1 = [1, 2, 3, 4]
    nums2 = [4, 3, 2, 1]
    print(countBeautifulPairs(nums1, nums2))  # Expected Output: 4

    # Test Case 3
    nums1 = [0, 0, 0]
    nums2 = [0, 0, 0]
    print(countBeautifulPairs(nums1, nums2))  # Expected Output: 6

"""
Time Complexity Analysis:
- The function uses two nested loops to iterate over all pairs of indices `(i, j)`.
- For each pair, it performs a constant-time operation to check the condition.
- Therefore, the time complexity is O(n^2), where `n` is the length of the input arrays.

Space Complexity Analysis:
- The function uses a constant amount of extra space, so the space complexity is O(1).

Topic: Arrays
"""