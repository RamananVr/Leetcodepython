"""
LeetCode Problem #1306: Jump Game III

Problem Statement:
Given an array of non-negative integers `arr`, you are initially positioned at `start` index of the array. 
When you are at index `i`, you can jump to `i + arr[i]` or `i - arr[i]`, provided the destination index is 
within bounds of the array. Your goal is to determine if you can reach any index with a value of 0.

Return `true` if you can reach any index with a value of 0, otherwise return `false`.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- 0 <= arr[i] < arr.length
- 0 <= start < arr.length
"""

from collections import deque

def canReach(arr, start):
    """
    Determines if you can reach any index with a value of 0 in the array.

    :param arr: List[int] - The array of non-negative integers.
    :param start: int - The starting index.
    :return: bool - True if you can reach an index with value 0, False otherwise.
    """
    n = len(arr)
    visited = [False] * n
    queue = deque([start])

    while queue:
        current = queue.popleft()

        # If the current index is out of bounds or already visited, skip it
        if current < 0 or current >= n or visited[current]:
            continue

        # Mark the current index as visited
        visited[current] = True

        # If the value at the current index is 0, return True
        if arr[current] == 0:
            return True

        # Add the next possible indices to the queue
        queue.append(current + arr[current])
        queue.append(current - arr[current])

    # If we exhaust all possibilities without finding a 0, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [4, 2, 3, 0, 3, 1, 2]
    start1 = 5
    print(canReach(arr1, start1))  # Expected Output: True

    # Test Case 2
    arr2 = [4, 2, 3, 0, 3, 1, 2]
    start2 = 0
    print(canReach(arr2, start2))  # Expected Output: True

    # Test Case 3
    arr3 = [3, 0, 2, 1, 2]
    start3 = 2
    print(canReach(arr3, start3))  # Expected Output: False

    # Test Case 4
    arr4 = [0]
    start4 = 0
    print(canReach(arr4, start4))  # Expected Output: True

    # Test Case 5
    arr5 = [1, 1, 1, 1, 1]
    start5 = 0
    print(canReach(arr5, start5))  # Expected Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each index is visited at most once, and for each index, we perform constant-time operations.
- Therefore, the time complexity is O(n), where n is the length of the array.

Space Complexity:
- The space complexity is O(n) due to the `visited` array and the `queue` used for BFS.
- The `visited` array requires O(n) space, and the queue can hold up to O(n) elements in the worst case.

Topic: Breadth-First Search (BFS)
"""