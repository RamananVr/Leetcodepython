"""
LeetCode Question #702: Search in a Sorted Array of Unknown Size

Problem Statement:
You have a sorted array of unique integers and an integer target. However, the array is not accessible directly. 
Instead, you have an interface ArrayReader that allows you to access the array using the following method:
    - int get(int index): Returns the value at the index-th position of the array (0-indexed).
      - If the index is out of bounds, it returns 2^31 - 1 (a very large value).

You are given an instance of the ArrayReader class called `reader`. You want to find the index of the target in the array.
If the target exists, return its index. Otherwise, return -1.

You must write an algorithm with O(log n) time complexity, where n is the length of the array.

Constraints:
- 1 <= target <= 10^4
- -10^4 <= array[i], target <= 10^4
- array is sorted in strictly increasing order.
- The array contains unique elements.
- The array is of unknown size.

"""

# Clean and Correct Python Solution
class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        # Step 1: Find the search boundary
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right *= 2
        
        # Step 2: Perform binary search within the boundary
        while left <= right:
            mid = left + (right - left) // 2
            value = reader.get(mid)
            
            if value == target:
                return mid
            elif value > target:
                right = mid - 1
            else:
                left = mid + 1
        
        return -1

# Example Test Cases
class ArrayReader:
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index < 0 or index >= len(self.arr):
            return 2**31 - 1
        return self.arr[index]

if __name__ == "__main__":
    # Test Case 1
    reader = ArrayReader([-1, 0, 3, 5, 9, 12])
    target = 9
    solution = Solution()
    print(solution.search(reader, target))  # Output: 4

    # Test Case 2
    reader = ArrayReader([-1, 0, 3, 5, 9, 12])
    target = 2
    print(solution.search(reader, target))  # Output: -1

    # Test Case 3
    reader = ArrayReader([1, 3, 5, 7, 9, 11, 13, 15])
    target = 15
    print(solution.search(reader, target))  # Output: 7

    # Test Case 4
    reader = ArrayReader([1, 3, 5, 7, 9, 11, 13, 15])
    target = 6
    print(solution.search(reader, target))  # Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm consists of two main steps:
  1. Finding the boundary: This step involves doubling the `right` pointer until the target is within the range. 
     This takes O(log n) time, where n is the index of the target or the size of the array.
  2. Binary search: Once the boundary is found, binary search is performed within the range, which also takes O(log n) time.
- Overall time complexity: O(log n).

Space Complexity:
- The algorithm uses a constant amount of extra space (pointers `left`, `right`, and `mid`).
- Overall space complexity: O(1).

Topic: Binary Search
"""