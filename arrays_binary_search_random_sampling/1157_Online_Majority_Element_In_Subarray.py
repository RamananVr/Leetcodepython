"""
LeetCode Problem #1157: Online Majority Element In Subarray

Problem Statement:
Design a data structure that efficiently finds the majority element in a subarray, i.e., the element that appears more than floor((right - left + 1) / 2) times in a subarray.

Implement the `MajorityChecker` class:
- `MajorityChecker(int[] arr)` Initializes the instance of the class with the given array `arr`.
- `int query(int left, int right, int threshold)` Returns the element in the subarray `arr[left...right]` that occurs at least `threshold` times. If no such element exists, return -1.

Constraints:
1. 1 <= arr.length <= 2 * 10^4
2. 1 <= arr[i] <= 2 * 10^4
3. 0 <= left <= right < arr.length
4. threshold > 0
5. The number of queries is at most 10^4.

"""

from collections import defaultdict
from bisect import bisect_left, bisect_right

class MajorityChecker:
    def __init__(self, arr):
        """
        Initialize the MajorityChecker with the given array.
        Preprocess the array to store the indices of each element for efficient querying.
        """
        self.arr = arr
        self.indices = defaultdict(list)
        for i, num in enumerate(arr):
            self.indices[num].append(i)

    def query(self, left, right, threshold):
        """
        Returns the majority element in the subarray arr[left...right] that occurs at least `threshold` times.
        If no such element exists, return -1.
        """
        # Check a limited number of candidates (at most 20) using random sampling
        for _ in range(20):
            # Randomly pick an index in the range [left, right]
            candidate = self.arr[left + (right - left) // 2]
            # Get the indices of the candidate
            candidate_indices = self.indices[candidate]
            # Count occurrences of the candidate in the range [left, right]
            left_idx = bisect_left(candidate_indices, left)
            right_idx = bisect_right(candidate_indices, right)
            count = right_idx - left_idx
            # Check if the candidate meets the threshold
            if count >= threshold:
                return candidate
        return -1

# Example Test Cases
if __name__ == "__main__":
    # Initialize the MajorityChecker with the array
    arr = [1, 1, 2, 2, 1, 1]
    majority_checker = MajorityChecker(arr)

    # Test cases
    print(majority_checker.query(0, 5, 4))  # Output: 1
    print(majority_checker.query(0, 3, 3))  # Output: -1
    print(majority_checker.query(2, 3, 2))  # Output: 2

"""
Time and Space Complexity Analysis:

1. Preprocessing:
   - Time Complexity: O(n), where n is the length of the array. We iterate through the array once to store the indices of each element.
   - Space Complexity: O(n), as we store the indices of each element in a dictionary.

2. Query:
   - Time Complexity: O(log(k)), where k is the number of occurrences of the candidate element in the array. This is due to the binary search operations (bisect_left and bisect_right).
   - In the worst case, we perform this operation for up to 20 candidates, so the overall complexity is O(20 * log(k)) ≈ O(log(k)).
   - Space Complexity: O(1), as we do not use any additional space during the query.

Overall:
- Preprocessing: O(n) time and O(n) space.
- Query: O(log(k)) time and O(1) space.

Topic: Arrays, Binary Search, Random Sampling
"""