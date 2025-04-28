"""
LeetCode Question #1095: Find in Mountain Array

Problem Statement:
(This is an interactive problem.)

You may recall that an array `arr` is a mountain array if and only if:
- `arr.length >= 3`
- There exists some `i` with `0 < i < arr.length - 1` such that:
  - `arr[0] < arr[1] < ... < arr[i - 1] < arr[i]`
  - `arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`

Given a mountain array `mountainArr`, return the minimum index such that `mountainArr.get(index) == target`. If such an index does not exist, return `-1`.

You cannot access the mountain array directly. You may only access the array using a `MountainArray` interface:
- `mountainArr.get(index)` returns the element at index `index` (0-indexed).
- `mountainArr.length()` returns the length of the array.

Submissions making more than 100 calls to `mountainArr.get` will be judged as incorrect.

Constraints:
- 3 <= mountainArr.length() <= 10^4
- 0 <= target <= 10^9
- 0 <= mountainArr.get(index) <= 10^9

"""

# Python Solution
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        # Helper function to find the peak index
        def find_peak_index():
            left, right = 0, mountainArr.length() - 1
            while left < right:
                mid = (left + right) // 2
                if mountainArr.get(mid) < mountainArr.get(mid + 1):
                    left = mid + 1
                else:
                    right = mid
            return left

        # Helper function for binary search in ascending order
        def binary_search_asc(left, right):
            while left <= right:
                mid = (left + right) // 2
                value = mountainArr.get(mid)
                if value == target:
                    return mid
                elif value < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Helper function for binary search in descending order
        def binary_search_desc(left, right):
            while left <= right:
                mid = (left + right) // 2
                value = mountainArr.get(mid)
                if value == target:
                    return mid
                elif value > target:
                    left = mid + 1
                else:
                    right = mid - 1
            return -1

        # Step 1: Find the peak index
        peak_index = find_peak_index()

        # Step 2: Search in the ascending part
        result = binary_search_asc(0, peak_index)
        if result != -1:
            return result

        # Step 3: Search in the descending part
        return binary_search_desc(peak_index + 1, mountainArr.length() - 1)


# Example Test Cases
class MountainArray:
    def __init__(self, arr):
        self.arr = arr

    def get(self, index):
        return self.arr[index]

    def length(self):
        return len(self.arr)


if __name__ == "__main__":
    # Test Case 1
    mountainArr = MountainArray([1, 2, 3, 4, 5, 3, 1])
    target = 3
    solution = Solution()
    print(solution.findInMountainArray(target, mountainArr))  # Output: 2

    # Test Case 2
    mountainArr = MountainArray([0, 1, 2, 4, 2, 1])
    target = 3
    print(solution.findInMountainArray(target, mountainArr))  # Output: -1

    # Test Case 3
    mountainArr = MountainArray([1, 5, 2])
    target = 2
    print(solution.findInMountainArray(target, mountainArr))  # Output: 2


# Time and Space Complexity Analysis
"""
Time Complexity:
- Finding the peak index takes O(log n) time using binary search.
- Binary search in the ascending part takes O(log n) time.
- Binary search in the descending part takes O(log n) time.
Overall time complexity: O(log n).

Space Complexity:
- The solution uses constant space for variables and does not use any additional data structures.
Overall space complexity: O(1).
"""

# Topic: Binary Search