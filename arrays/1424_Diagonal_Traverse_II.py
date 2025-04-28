"""
LeetCode Problem #1424: Diagonal Traverse II

Problem Statement:
Given a list of lists of integers `nums`, return all elements of `nums` in diagonal order as described below:

- Each diagonal starts from some element in the first row and goes in the bottom-left direction until reaching the last row or the last column.
- For example, `nums = [[1,2,3],[4,5,6],[7,8,9]]` will have diagonals:
  - [1]
  - [2,4]
  - [3,5,7]
  - [6,8]
  - [9]

Return the elements of `nums` in the order they appear in these diagonals.

Constraints:
1. `1 <= nums.length <= 10^5`
2. `1 <= nums[i].length <= 10^5`
3. `1 <= nums[i][j] <= 10^5`
4. The total number of elements in `nums` is at most `10^5`.

Example:
Input: nums = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,3,5,7,6,8,9]
"""

from collections import defaultdict

def findDiagonalOrder(nums):
    """
    This function returns the elements of the 2D list `nums` in diagonal order.
    """
    diagonal_map = defaultdict(list)

    # Traverse the 2D list and group elements by their diagonal index (i + j)
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            diagonal_map[i + j].append(nums[i][j])

    # Collect the results from the diagonal map
    result = []
    for key in sorted(diagonal_map.keys()):
        # Reverse the order of elements in each diagonal before appending
        result.extend(reversed(diagonal_map[key]))

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    nums1 = [[1,2,3],[4,5,6],[7,8,9]]
    print(findDiagonalOrder(nums1))  # Output: [1,2,4,3,5,7,6,8,9]

    # Test Case 2
    nums2 = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
    print(findDiagonalOrder(nums2))  # Output: [1,2,6,3,7,8,4,9,5,10,12,11,13,14,15,16]

    # Test Case 3
    nums3 = [[1,2,3],[4],[5,6,7],[8],[9,10,11]]
    print(findDiagonalOrder(nums3))  # Output: [1,2,4,3,5,6,8,7,9,10,11]

    # Test Case 4
    nums4 = [[1,2,3,4,5,6]]
    print(findDiagonalOrder(nums4))  # Output: [1,2,3,4,5,6]

    # Test Case 5
    nums5 = [[1],[2],[3],[4],[5]]
    print(findDiagonalOrder(nums5))  # Output: [1,2,3,4,5]

"""
Time Complexity:
- The traversal of the 2D list `nums` takes O(N) time, where N is the total number of elements in `nums`.
- Sorting the keys of the diagonal map takes O(D log D), where D is the number of diagonals. Since D is at most N, this is O(N log N).
- Collecting the results from the diagonal map takes O(N) time.
- Overall, the time complexity is O(N + N log N), which simplifies to O(N log N) in the worst case.

Space Complexity:
- The diagonal map stores all elements of `nums`, so it requires O(N) space.
- The result list also requires O(N) space.
- Overall, the space complexity is O(N).

Topic: Arrays
"""