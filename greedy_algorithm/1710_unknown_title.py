"""
LeetCode Problem #1710: Maximum Units on a Truck

Problem Statement:
You are assigned to put some boxes onto one truck. You are given a 2D array `boxTypes`, 
where `boxTypes[i] = [numberOfBoxes_i, numberOfUnitsPerBox_i]`:
    - `numberOfBoxes_i` is the number of boxes of type i.
    - `numberOfUnitsPerBox_i` is the number of units in each box of the type i.

You are also given an integer `truckSize`, which is the maximum number of boxes that can be put on the truck. 
You can choose any boxes to put on the truck as long as the number of boxes does not exceed `truckSize`.

Return the maximum total number of units that can be put on the truck.

Constraints:
- 1 <= boxTypes.length <= 1000
- 1 <= numberOfBoxes_i, numberOfUnitsPerBox_i <= 1000
- 1 <= truckSize <= 10^6
"""

# Solution
def maximumUnits(boxTypes, truckSize):
    """
    Calculate the maximum number of units that can be loaded onto the truck.

    :param boxTypes: List[List[int]] - A list of box types, where each box type is represented as [numberOfBoxes, numberOfUnitsPerBox].
    :param truckSize: int - The maximum number of boxes the truck can carry.
    :return: int - The maximum number of units that can be loaded onto the truck.
    """
    # Sort boxTypes by the number of units per box in descending order
    boxTypes.sort(key=lambda x: x[1], reverse=True)
    
    max_units = 0
    for numberOfBoxes, numberOfUnitsPerBox in boxTypes:
        # Take as many boxes as possible without exceeding the truck size
        boxes_to_take = min(truckSize, numberOfBoxes)
        max_units += boxes_to_take * numberOfUnitsPerBox
        truckSize -= boxes_to_take
        
        # If the truck is full, break out of the loop
        if truckSize == 0:
            break
    
    return max_units

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    boxTypes1 = [[1, 3], [2, 2], [3, 1]]
    truckSize1 = 4
    print(maximumUnits(boxTypes1, truckSize1))  # Expected Output: 8

    # Test Case 2
    boxTypes2 = [[5, 10], [2, 5], [4, 7], [3, 9]]
    truckSize2 = 10
    print(maximumUnits(boxTypes2, truckSize2))  # Expected Output: 91

    # Test Case 3
    boxTypes3 = [[10, 1], [5, 2], [2, 3]]
    truckSize3 = 7
    print(maximumUnits(boxTypes3, truckSize3))  # Expected Output: 17

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the boxTypes array takes O(n log n), where n is the length of the array.
- Iterating through the boxTypes array takes O(n).
- Therefore, the overall time complexity is O(n log n).

Space Complexity:
- The sorting operation is performed in-place, so the space complexity is O(1).
- No additional data structures are used, so the overall space complexity is O(1).
"""

# Topic: Greedy Algorithm