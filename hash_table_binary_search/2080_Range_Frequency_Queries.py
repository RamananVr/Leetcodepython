"""
LeetCode Problem #2080: Range Frequency Queries

Problem Statement:
Design a data structure to find the frequency of a given value in a given subarray.

Implement the `RangeFreqQuery` class:
- `RangeFreqQuery(int[] arr)` Initializes the object with the array `arr`.
- `int query(int left, int right, int value)` Returns the frequency of `value` in the subarray `arr[left...right]`.

Constraints:
- 1 <= arr.length <= 10^5
- 1 <= arr[i], value <= 10^4
- 0 <= left <= right < arr.length
- At most 10^5 calls will be made to `query`.

Example:
Input:
    ["RangeFreqQuery", "query", "query"]
    [[[12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56, 34]], [1, 2, 4], [0, 11, 33]]
Output:
    [null, 1, 2]

Explanation:
    RangeFreqQuery rangeFreqQuery = new RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56, 34]);
    rangeFreqQuery.query(1, 2, 4); // return 1. The value 4 occurs once in the subarray [33, 4].
    rangeFreqQuery.query(0, 11, 33); // return 2. The value 33 occurs twice in the subarray [12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56].
"""

from collections import defaultdict
from bisect import bisect_left, bisect_right

class RangeFreqQuery:
    def __init__(self, arr):
        """
        Initializes the RangeFreqQuery object with the array `arr`.
        Preprocesses the array to store the indices of each value in a dictionary.
        """
        self.index_map = defaultdict(list)
        for i, num in enumerate(arr):
            self.index_map[num].append(i)

    def query(self, left, right, value):
        """
        Returns the frequency of `value` in the subarray arr[left...right].
        Uses binary search to efficiently count the indices of `value` within the range.
        """
        if value not in self.index_map:
            return 0
        
        indices = self.index_map[value]
        # Find the leftmost index >= left
        left_idx = bisect_left(indices, left)
        # Find the rightmost index <= right
        right_idx = bisect_right(indices, right) - 1
        
        # If no valid indices are found, return 0
        if left_idx > right_idx:
            return 0
        
        # Return the count of indices in the range
        return right_idx - left_idx + 1


# Example Test Cases
if __name__ == "__main__":
    # Initialize the RangeFreqQuery object
    rangeFreqQuery = RangeFreqQuery([12, 33, 4, 56, 22, 2, 34, 33, 22, 12, 34, 56, 34])
    
    # Test Case 1
    print(rangeFreqQuery.query(1, 2, 4))  # Output: 1
    
    # Test Case 2
    print(rangeFreqQuery.query(0, 11, 33))  # Output: 2
    
    # Test Case 3
    print(rangeFreqQuery.query(0, 6, 34))  # Output: 1
    
    # Test Case 4
    print(rangeFreqQuery.query(3, 10, 22))  # Output: 2
    
    # Test Case 5
    print(rangeFreqQuery.query(0, 12, 100))  # Output: 0


"""
Time and Space Complexity Analysis:

1. Preprocessing:
   - Time Complexity: O(n), where n is the length of the input array `arr`. We iterate through the array once to build the `index_map`.
   - Space Complexity: O(n), as we store the indices of each value in the dictionary.

2. Query:
   - Time Complexity: O(log k), where k is the number of occurrences of `value` in the array. This is due to the binary search operations (`bisect_left` and `bisect_right`).
   - Space Complexity: O(1), as we only use a constant amount of extra space during the query.

3. Overall:
   - Preprocessing: O(n) time and O(n) space.
   - Query: O(log k) time and O(1) space.

Primary Topic: Hash Table, Binary Search
"""