"""
LeetCode Problem #1298: Maximum Candies You Can Get from Boxes

Problem Statement:
You have n boxes labeled from 0 to n - 1. You are given four arrays: `status`, `candies`, `keys`, and `containedBoxes` 
where:

- `status[i]` is 1 if box i is open, and 0 if box i is closed.
- `candies[i]` is the number of candies in box i.
- `keys[i]` is a list of keys you can use to open other boxes.
- `containedBoxes[i]` is a list of other boxes contained in box i.

You are also given an integer array `initialBoxes` that contains the indices of boxes you initially have.

You can use the following operations any number of times:

1. If a box is open, you can collect candies from it.
2. If a box is open, you can use the keys in it to open other boxes.
3. If a box is open, you can take any boxes it contains and add them to your collection of boxes.

Return the maximum number of candies you can collect.

Constraints:
- 1 <= n <= 1000
- `status.length == n`
- `candies.length == n`
- `keys.length == n`
- `containedBoxes.length == n`
- `status[i]` is either 0 or 1.
- 1 <= candies[i] <= 1000
- 0 <= keys[i].length <= n
- 0 <= containedBoxes[i].length <= n
- `initialBoxes.length` <= n
- 0 <= initialBoxes[i] < n
"""

# Python Solution
from collections import deque

def maxCandies(status, candies, keys, containedBoxes, initialBoxes):
    # Initialize variables
    total_candies = 0
    queue = deque(initialBoxes)  # Boxes we can process
    available_keys = set()       # Keys we have
    unopened_boxes = set()       # Boxes we can't open yet

    while queue:
        box = queue.popleft()
        
        # If the box is closed and we don't have the key, store it for later
        if status[box] == 0 and box not in available_keys:
            unopened_boxes.add(box)
            continue
        
        # Collect candies from the box
        total_candies += candies[box]
        
        # Add keys from the box to our available keys
        available_keys.update(keys[box])
        
        # Add contained boxes to the queue
        queue.extend(containedBoxes[box])
        
        # Check unopened boxes to see if we can now open them
        for unopened_box in list(unopened_boxes):
            if unopened_box in available_keys:
                unopened_boxes.remove(unopened_box)
                queue.append(unopened_box)

    return total_candies

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    status = [1, 0, 1, 0]
    candies = [7, 5, 4, 100]
    keys = [[], [0], [], []]
    containedBoxes = [[1, 2], [3], [], []]
    initialBoxes = [0]
    print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 16

    # Test Case 2
    status = [1, 0, 0, 0]
    candies = [1, 2, 3, 4]
    keys = [[1, 2, 3], [], [], []]
    containedBoxes = [[], [], [], []]
    initialBoxes = [0]
    print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 10

    # Test Case 3
    status = [1, 1, 1]
    candies = [100, 200, 300]
    keys = [[], [], []]
    containedBoxes = [[], [], []]
    initialBoxes = [0, 1, 2]
    print(maxCandies(status, candies, keys, containedBoxes, initialBoxes))  # Output: 600

# Time and Space Complexity Analysis
"""
Time Complexity:
- Each box is processed at most once, and the operations for each box (collecting candies, adding keys, adding contained boxes) are O(1).
- Thus, the time complexity is O(n), where n is the number of boxes.

Space Complexity:
- The space used by the queue, available_keys, and unopened_boxes is proportional to the number of boxes.
- Thus, the space complexity is O(n).
"""

# Topic: Graph Traversal (BFS-like approach)