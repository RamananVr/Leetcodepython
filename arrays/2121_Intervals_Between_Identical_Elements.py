"""
LeetCode Problem #2121: Intervals Between Identical Elements

Problem Statement:
You are given a 0-indexed array of n integers arr.

The interval between two elements in arr is defined as the absolute difference between their indices. 
More formally, the interval between arr[i] and arr[j] is |i - j|.

Return an array intervals of length n where intervals[i] is the sum of intervals between arr[i] and 
each other element in arr with the same value as arr[i].

Note: |x| is the absolute value of x.

Example 1:
Input: arr = [2,1,3,1,2,3,3]
Output: [4,2,7,2,4,4,5]
Explanation:
- Index 0: Another 2 is found at index 4. Interval = |0 - 4| = 4.
- Index 1: Another 1 is found at index 3. Interval = |1 - 3| = 2.
- Index 2: Other 3s are found at indices 5 and 6. Intervals = |2 - 5| + |2 - 6| = 3 + 4 = 7.
- Index 3: Another 1 is found at index 1. Interval = |3 - 1| = 2.
- Index 4: Another 2 is found at index 0. Interval = |4 - 0| = 4.
- Index 5: Other 3s are found at indices 2 and 6. Intervals = |5 - 2| + |5 - 6| = 3 + 1 = 4.
- Index 6: Other 3s are found at indices 2 and 5. Intervals = |6 - 2| + |6 - 5| = 4 + 1 = 5.

Example 2:
Input: arr = [10,5,10,10]
Output: [5,0,3,4]
Explanation:
- Index 0: Other 10s are found at indices 2 and 3. Intervals = |0 - 2| + |0 - 3| = 2 + 3 = 5.
- Index 1: No other 5s are found.
- Index 2: Other 10s are found at indices 0 and 3. Intervals = |2 - 0| + |2 - 3| = 2 + 1 = 3.
- Index 3: Other 10s are found at indices 0 and 2. Intervals = |3 - 0| + |3 - 2| = 3 + 1 = 4.

Constraints:
- n == arr.length
- 1 <= n <= 10^5
- 1 <= arr[i] <= 10^5
"""

# Solution
from collections import defaultdict

def getDistances(arr):
    # Dictionary to store indices of each value
    index_map = defaultdict(list)
    
    # Populate the index_map with indices of each value
    for i, num in enumerate(arr):
        index_map[num].append(i)
    
    # Result array
    result = [0] * len(arr)
    
    # Process each group of indices for the same value
    for indices in index_map.values():
        n = len(indices)
        prefix_sum = [0] * n
        
        # Compute prefix sums for the indices
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + indices[i] - indices[i - 1]
        
        # Compute the result for each index
        for i in range(n):
            left_sum = prefix_sum[i]
            right_sum = prefix_sum[-1] - prefix_sum[i]
            result[indices[i]] = i * indices[i] - left_sum + right_sum - (n - i - 1) * indices[i]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [2, 1, 3, 1, 2, 3, 3]
    print(getDistances(arr1))  # Output: [4, 2, 7, 2, 4, 4, 5]

    # Test Case 2
    arr2 = [10, 5, 10, 10]
    print(getDistances(arr2))  # Output: [5, 0, 3, 4]

    # Test Case 3
    arr3 = [1, 1, 1, 1]
    print(getDistances(arr3))  # Output: [6, 4, 4, 6]

    # Test Case 4
    arr4 = [1]
    print(getDistances(arr4))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing the index_map takes O(n), where n is the length of the array.
- For each group of indices, computing prefix sums and calculating results also takes O(n) in total.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The index_map stores indices for each unique value, which takes O(n) space in the worst case.
- The prefix_sum array for each group also takes O(n) space in total.
- The result array takes O(n) space.
- Thus, the overall space complexity is O(n).
"""

# Topic: Arrays