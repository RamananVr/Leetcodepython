"""
LeetCode Question #1564: Put Boxes Into the Warehouse I

Problem Statement:
You are given two arrays of positive integers, `boxes` and `warehouse`, representing the heights of some boxes and the heights of the rooms in a warehouse respectively.

The warehouse's rooms are represented as a series of rooms from left to right, where the `i-th` room has a height `warehouse[i]`. The boxes are also represented as a series of heights, where the `j-th` box has a height `boxes[j]`.

You want to place the boxes in the warehouse such that:
1. You can place the `j-th` box in the `i-th` room if `boxes[j] <= warehouse[i]`.
2. You can place the boxes in the warehouse in any order.
3. Once a box is placed in the warehouse, it occupies that room and cannot be moved to another room.
4. Each room can only hold one box.

Return the maximum number of boxes you can put into the warehouse.

Constraints:
- `1 <= boxes.length, warehouse.length <= 10^5`
- `1 <= boxes[j], warehouse[i] <= 10^9`
"""

# Solution
def maxBoxesInWarehouse(boxes, warehouse):
    # Sort the boxes in ascending order
    boxes.sort()
    
    # Preprocess the warehouse to find the effective heights from left to right
    n = len(warehouse)
    for i in range(1, n):
        warehouse[i] = min(warehouse[i], warehouse[i - 1])
    
    # Use two pointers to place boxes in the warehouse
    box_index = 0
    room_index = n - 1
    count = 0
    
    while box_index < len(boxes) and room_index >= 0:
        if boxes[box_index] <= warehouse[room_index]:
            # Place the box in the current room
            count += 1
            box_index += 1
        # Move to the next room
        room_index -= 1
    
    return count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    boxes = [4, 3, 4, 1]
    warehouse = [5, 3, 3, 4, 1]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 3

    # Test Case 2
    boxes = [1, 2, 2, 3, 4]
    warehouse = [3, 4, 1, 2]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 4

    # Test Case 3
    boxes = [5, 6, 7]
    warehouse = [4, 3, 2, 1]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 0

    # Test Case 4
    boxes = [1, 2, 3]
    warehouse = [3, 3, 3]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `boxes` array takes O(m), where m is the length of the `boxes` array.
- Preprocessing the `warehouse` array takes O(n), where n is the length of the `warehouse` array.
- The two-pointer traversal takes O(max(m, n)).
- Overall time complexity: O(m + n).

Space Complexity:
- The algorithm uses O(1) additional space, as it modifies the `warehouse` array in place and uses a few variables.
- Overall space complexity: O(1).

Topic: Arrays
"""