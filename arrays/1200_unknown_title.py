"""
LeetCode Problem #1200: Minimum Absolute Difference

Problem Statement:
Given an array of distinct integers `arr`, find all pairs of elements with the minimum absolute difference of any two elements. Return a list of pairs in ascending order (with respect to pairs), where each pair `[a, b]` follows:
- `a, b` are elements of the array.
- `a < b`.
- `b - a` equals the minimum absolute difference of any two elements in `arr`.

Example 1:
Input: arr = [4,2,1,3]
Output: [[1,2],[2,3],[3,4]]
Explanation: The minimum absolute difference is 1. List all pairs with difference equal to 1 in ascending order.

Example 2:
Input: arr = [1,3,6,10,15]
Output: [[1,3]]
Explanation: The minimum absolute difference is 2.

Example 3:
Input: arr = [3,8,-10,23,19,-4,-14,27]
Output: [[-14,-10],[19,23],[23,27]]
Explanation: The minimum absolute difference is 4.

Constraints:
- 2 <= arr.length <= 10^5
- -10^6 <= arr[i] <= 10^6
"""

# Python Solution
def minimumAbsDifference(arr):
    """
    Finds all pairs of elements with the minimum absolute difference in the array.

    :param arr: List[int] - Array of distinct integers
    :return: List[List[int]] - List of pairs with minimum absolute difference
    """
    # Step 1: Sort the array
    arr.sort()
    
    # Step 2: Find the minimum absolute difference
    min_diff = float('inf')
    for i in range(len(arr) - 1):
        min_diff = min(min_diff, arr[i + 1] - arr[i])
    
    # Step 3: Collect all pairs with the minimum absolute difference
    result = []
    for i in range(len(arr) - 1):
        if arr[i + 1] - arr[i] == min_diff:
            result.append([arr[i], arr[i + 1]])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 2, 1, 3]
    print(minimumAbsDifference(arr1))  # Expected Output: [[1, 2], [2, 3], [3, 4]]

    # Test Case 2
    arr2 = [1, 3, 6, 10, 15]
    print(minimumAbsDifference(arr2))  # Expected Output: [[1, 3]]

    # Test Case 3
    arr3 = [3, 8, -10, 23, 19, -4, -14, 27]
    print(minimumAbsDifference(arr3))  # Expected Output: [[-14, -10], [19, 23], [23, 27]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the array.
- Finding the minimum absolute difference takes O(n).
- Collecting pairs with the minimum absolute difference takes O(n).
Overall, the time complexity is O(n log n).

Space Complexity:
- Sorting the array is done in-place, so no extra space is used for sorting.
- The result list stores pairs, which takes O(k) space, where k is the number of pairs.
Overall, the space complexity is O(k), which is proportional to the number of pairs in the result.
"""

# Topic: Arrays