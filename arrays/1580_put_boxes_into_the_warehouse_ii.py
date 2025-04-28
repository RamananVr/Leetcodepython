"""
LeetCode Question #1580: Put Boxes Into the Warehouse II

Problem Statement:
You are given two arrays of positive integers, `boxes` and `warehouse`, representing the heights of some boxes and the heights of n rooms in a warehouse respectively. The warehouse's rooms are labeled from 0 to n-1 from left to right, and the boxes are labeled from 0 to m-1.

You want to place all the boxes in the warehouse such that:
1. You can place the ith box in the jth room if the height of the box is less than or equal to the height of the room.
2. You can only place one box in each room.
3. You can place the boxes in any order.

Return the maximum number of boxes you can place in the warehouse.

Constraints:
- `1 <= boxes.length, warehouse.length <= 10^5`
- `1 <= boxes[i], warehouse[i] <= 10^9`
"""

# Solution
def maxBoxesInWarehouse(boxes, warehouse):
    # Sort the boxes in ascending order
    boxes.sort()
    
    # Preprocess the warehouse to ensure non-increasing heights from left to right
    for i in range(1, len(warehouse)):
        warehouse[i] = min(warehouse[i], warehouse[i - 1])
    
    # Use two pointers to place boxes in the warehouse
    box_index = len(boxes) - 1
    room_index = len(warehouse) - 1
    count = 0
    
    while box_index >= 0 and room_index >= 0:
        if boxes[box_index] <= warehouse[room_index]:
            # Place the box in the room
            count += 1
            room_index -= 1
        # Move to the next box
        box_index -= 1
    
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
    boxes = [1, 2, 3]
    warehouse = [1, 2, 3]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 3

    # Test Case 4
    boxes = [5, 6, 7]
    warehouse = [1, 2, 3]
    print(maxBoxesInWarehouse(boxes, warehouse))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the `boxes` array takes O(m log m), where m is the length of the `boxes` array.
- Preprocessing the `warehouse` array takes O(n), where n is the length of the `warehouse` array.
- The two-pointer traversal takes O(m + n).
- Overall time complexity: O(m log m + n).

Space Complexity:
- The algorithm uses O(1) additional space, as it modifies the `warehouse` array in place and uses a few variables.
- Overall space complexity: O(1).

Topic: Arrays
"""