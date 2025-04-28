"""
LeetCode Problem #2570: Merge Two 2D Arrays by Summing Values

Problem Statement:
You are given two 2D integer arrays `nums1` and `nums2`.

- `nums1[i] = [id_i, val_i]` indicates that the ID `id_i` has a value equal to `val_i`.
- `nums2[j] = [id_j, val_j]` indicates that the ID `id_j` has a value equal to `val_j`.

Each array contains unique IDs and is sorted in ascending order by ID.

Merge the two arrays into a new 2D array `result` such that:
1. Each unique ID from both arrays is included in `result`.
2. The value of each ID in `result` is the sum of the values of that ID in `nums1` and `nums2`. If the ID is not present in one of the arrays, consider its value as `0`.
3. `result` should be sorted in ascending order by ID.

Return the resulting array `result`.

Constraints:
- `1 <= nums1.length, nums2.length <= 200`
- `nums1[i].length == nums2[j].length == 2`
- `1 <= id_i, id_j <= 10^4`
- `-10^4 <= val_i, val_j <= 10^4`
- Both arrays are sorted in ascending order by ID.

Example:
Input: nums1 = [[1, 2], [2, 3], [4, 5]], nums2 = [[1, 4], [3, 2], [4, 1]]
Output: [[1, 6], [2, 3], [3, 2], [4, 6]]
Explanation: The resulting array contains:
- ID 1: 2 + 4 = 6
- ID 2: 3 + 0 = 3 (not present in nums2)
- ID 3: 0 + 2 = 2 (not present in nums1)
- ID 4: 5 + 1 = 6
"""

# Python Solution
from collections import defaultdict

def mergeArrays(nums1, nums2):
    """
    Merges two 2D arrays by summing values for matching IDs.

    Args:
    nums1 (List[List[int]]): First 2D array of [id, value] pairs.
    nums2 (List[List[int]]): Second 2D array of [id, value] pairs.

    Returns:
    List[List[int]]: Merged 2D array sorted by ID.
    """
    id_to_value = defaultdict(int)

    # Add values from nums1
    for id_, value in nums1:
        id_to_value[id_] += value

    # Add values from nums2
    for id_, value in nums2:
        id_to_value[id_] += value

    # Convert the dictionary to a sorted list of [id, value] pairs
    result = [[id_, value] for id_, value in sorted(id_to_value.items())]
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [[1, 2], [2, 3], [4, 5]]
    nums2 = [[1, 4], [3, 2], [4, 1]]
    print(mergeArrays(nums1, nums2))  # Output: [[1, 6], [2, 3], [3, 2], [4, 6]]

    # Test Case 2
    nums1 = [[2, 10], [3, 5]]
    nums2 = [[1, 7], [3, 3], [4, 2]]
    print(mergeArrays(nums1, nums2))  # Output: [[1, 7], [2, 10], [3, 8], [4, 2]]

    # Test Case 3
    nums1 = [[1, 1]]
    nums2 = [[2, 2]]
    print(mergeArrays(nums1, nums2))  # Output: [[1, 1], [2, 2]]

    # Test Case 4
    nums1 = []
    nums2 = [[1, 5], [2, 10]]
    print(mergeArrays(nums1, nums2))  # Output: [[1, 5], [2, 10]]

    # Test Case 5
    nums1 = [[1, 3], [2, 4], [5, 6]]
    nums2 = [[2, 1], [3, 2], [5, 4]]
    print(mergeArrays(nums1, nums2))  # Output: [[1, 3], [2, 5], [3, 2], [5, 10]]

# Time Complexity Analysis:
# - Iterating through nums1 and nums2 takes O(n1 + n2), where n1 and n2 are the lengths of nums1 and nums2.
# - Sorting the dictionary keys takes O(k * log(k)), where k is the number of unique IDs.
# - Constructing the result array takes O(k).
# Overall Time Complexity: O(n1 + n2 + k * log(k))

# Space Complexity Analysis:
# - The dictionary `id_to_value` stores up to k unique IDs, where k <= n1 + n2.
# - The result array also takes O(k) space.
# Overall Space Complexity: O(k)

# Topic: Arrays, Hash Map