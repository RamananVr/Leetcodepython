"""
LeetCode Problem #1345: Jump Game IV

Problem Statement:
Given an array of integers `arr`, you are initially positioned at the first index of the array.

In one step, you can:
1. Jump to the next index (i + 1) if it exists.
2. Jump to the previous index (i - 1) if it exists.
3. Jump to any index with the same value as `arr[i]`.

Return the minimum number of steps to reach the last index of the array.

Constraints:
- 1 <= arr.length <= 5 * 10^4
- -10^8 <= arr[i] <= 10^8
"""

from collections import defaultdict, deque

def minJumps(arr):
    """
    Function to find the minimum number of steps to reach the last index of the array.
    """
    n = len(arr)
    if n == 1:
        return 0  # Already at the last index

    # Map each value to the list of indices where it appears
    value_to_indices = defaultdict(list)
    for i, val in enumerate(arr):
        value_to_indices[val].append(i)

    # BFS initialization
    queue = deque([0])  # Start from the first index
    visited = set([0])  # Mark the first index as visited
    steps = 0

    while queue:
        for _ in range(len(queue)):
            curr = queue.popleft()

            # If we reach the last index, return the number of steps
            if curr == n - 1:
                return steps

            # Explore neighbors: i + 1, i - 1, and all indices with the same value
            neighbors = []
            if curr + 1 < n:
                neighbors.append(curr + 1)
            if curr - 1 >= 0:
                neighbors.append(curr - 1)
            neighbors.extend(value_to_indices[arr[curr]])

            for neighbor in neighbors:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

            # Clear the list of indices for the current value to avoid redundant processing
            value_to_indices[arr[curr]].clear()

        steps += 1

    return -1  # If we cannot reach the last index (should not happen due to constraints)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [100, -23, -23, 404, 100, 23, 23, 23, 3, 404]
    print(minJumps(arr1))  # Expected Output: 3

    # Test Case 2
    arr2 = [7]
    print(minJumps(arr2))  # Expected Output: 0

    # Test Case 3
    arr3 = [7, 6, 9, 6, 9, 6, 9, 7]
    print(minJumps(arr3))  # Expected Output: 1

    # Test Case 4
    arr4 = [6, 1, 9]
    print(minJumps(arr4))  # Expected Output: 2

    # Test Case 5
    arr5 = [1, 2, 3, 4, 5]
    print(minJumps(arr5))  # Expected Output: 4

"""
Time Complexity:
- O(n): Each index is visited at most once, and the total number of neighbors processed is proportional to the array size.
- The `value_to_indices` dictionary ensures that we process each value's indices only once.

Space Complexity:
- O(n): Space is used for the `visited` set, the `queue`, and the `value_to_indices` dictionary.

Topic: Breadth-First Search (BFS)
"""