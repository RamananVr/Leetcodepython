"""
LeetCode Question #1471: The k Strongest Values in an Array

Problem Statement:
Given an array of integers `arr` and an integer `k`, the strongest values in an array are defined as follows:
- Let `m` be the median of the array. If the array has an odd length, the median is the middle element after sorting. If the array has an even length, the median is the smaller of the two middle elements.
- A value `x` is stronger than a value `y` if:
  - |x - m| > |y - m|, or
  - |x - m| == |y - m| and x > y.

Return a list of the `k` strongest values in the array. The result can be returned in any order.

Example 1:
Input: arr = [1,2,3,4,5], k = 2
Output: [5,1]
Explanation: Median is 3, strongest values are 5 and 1.

Example 2:
Input: arr = [1,1,3,5,5], k = 2
Output: [5,5]
Explanation: Median is 3, strongest values are 5 and 5.

Example 3:
Input: arr = [6,7,11,7,6,8], k = 5
Output: [11,8,6,6,7]
Explanation: Median is 7, strongest values are 11, 8, 6, 6, and 7.

Constraints:
- 1 <= arr.length <= 10^5
- -10^5 <= arr[i] <= 10^5
- 1 <= k <= arr.length
"""

# Python Solution
from typing import List

def getStrongest(arr: List[int], k: int) -> List[int]:
    # Step 1: Sort the array to find the median
    arr.sort()
    n = len(arr)
    median = arr[(n - 1) // 2]  # Median is the middle element (or smaller of two middle elements)

    # Step 2: Sort the array based on the "strength" criteria
    arr.sort(key=lambda x: (abs(x - median), x), reverse=True)

    # Step 3: Return the first k elements
    return arr[:k]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [1, 2, 3, 4, 5]
    k1 = 2
    print(getStrongest(arr1, k1))  # Output: [5, 1]

    # Test Case 2
    arr2 = [1, 1, 3, 5, 5]
    k2 = 2
    print(getStrongest(arr2, k2))  # Output: [5, 5]

    # Test Case 3
    arr3 = [6, 7, 11, 7, 6, 8]
    k3 = 5
    print(getStrongest(arr3, k3))  # Output: [11, 8, 6, 6, 7]

    # Test Case 4
    arr4 = [1, 2, 3, 4, 5, 6]
    k4 = 3
    print(getStrongest(arr4, k4))  # Output: [6, 5, 1]

    # Test Case 5
    arr5 = [-10, -5, 0, 5, 10]
    k5 = 3
    print(getStrongest(arr5, k5))  # Output: [10, -10, 5]

# Time and Space Complexity Analysis
"""
Time Complexity:
1. Sorting the array to find the median: O(n log n), where n is the length of the array.
2. Sorting the array again based on the "strength" criteria: O(n log n).
Overall time complexity: O(n log n).

Space Complexity:
1. Sorting operations are in-place, so no additional space is used apart from the input array.
Overall space complexity: O(1).
"""

# Topic: Arrays