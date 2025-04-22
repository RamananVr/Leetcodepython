"""
LeetCode Problem #898: Bitwise ORs of Subarrays

Problem Statement:
Given an array `arr` of nonnegative integers, consider all possible subarrays of the array. 
A subarray is a contiguous subsequence of the array. For each subarray, calculate the 
bitwise OR of its elements. Return the number of distinct values that can be obtained 
from these calculations.

Example:
Input: arr = [1, 2, 4]
Output: 6
Explanation: The possible subarrays are [1], [2], [4], [1,2], [2,4], [1,2,4]. 
These yield the results 1, 2, 4, 3, 6, 7 respectively. There are 6 distinct values.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- 0 <= arr[i] <= 10^9
"""

# Solution
def subarrayBitwiseORs(arr):
    """
    Calculate the number of distinct bitwise OR results from all subarrays of the input array.

    :param arr: List[int] - The input array of nonnegative integers.
    :return: int - The number of distinct bitwise OR results.
    """
    result_set = set()
    current_set = set()
    
    for num in arr:
        # Update the current set with the OR of the current number and all previous results
        current_set = {num | x for x in current_set} | {num}
        # Add all results to the global result set
        result_set.update(current_set)
    
    return len(result_set)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 4]
    print(subarrayBitwiseORs(arr1))  # Expected Output: 6

    # Test Case 2
    arr2 = [1, 1, 2]
    print(subarrayBitwiseORs(arr2))  # Expected Output: 3

    # Test Case 3
    arr3 = [0, 1, 2, 3]
    print(subarrayBitwiseORs(arr3))  # Expected Output: 7

    # Test Case 4
    arr4 = [5, 6, 7]
    print(subarrayBitwiseORs(arr4))  # Expected Output: 6

    # Test Case 5
    arr5 = [10]
    print(subarrayBitwiseORs(arr5))  # Expected Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop iterates over the array, so it runs O(n) times.
- For each element, the inner operation (set comprehension) processes the current set, 
  which can grow up to O(n) in the worst case. Thus, the total complexity is O(n^2).

Space Complexity:
- The `result_set` stores all distinct OR results, which can be at most O(n^2) in the worst case.
- The `current_set` stores intermediate results, which can grow up to O(n) in the worst case.
- Therefore, the space complexity is O(n^2) in the worst case.
"""

# Topic: Arrays, Bit Manipulation