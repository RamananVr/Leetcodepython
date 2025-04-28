"""
LeetCode Problem #1603: Design Parking System

Problem Statement:
Design a parking system for a parking lot. The parking lot has three kinds of parking spaces: big, medium, and small, with a fixed number of slots for each size.

Implement the `ParkingSystem` class:
- `ParkingSystem(int big, int medium, int small)` Initializes object of the `ParkingSystem` class. The number of slots for each parking space are given as part of the constructor.
- `bool addCar(int carType)` Checks whether there is a parking space of `carType` for the car that wants to get into the parking lot. `carType` can be of three kinds:
  - `1` for big cars
  - `2` for medium cars
  - `3` for small cars
  If there is a space available, the car is parked in that space and the method returns `true`. Otherwise, it returns `false`.

Constraints:
- `0 <= big, medium, small <= 1000`
- `carType` is `1`, `2`, or `3`
- At most `1000` calls will be made to `addCar`

Example:
Input:
    ["ParkingSystem", "addCar", "addCar", "addCar", "addCar"]
    [[1, 1, 0], [1], [2], [3], [1]]
Output:
    [null, true, true, false, false]

Explanation:
    ParkingSystem parkingSystem = new ParkingSystem(1, 1, 0);
    parkingSystem.addCar(1); // return true because there is 1 available slot for a big car
    parkingSystem.addCar(2); // return true because there is 1 available slot for a medium car
    parkingSystem.addCar(3); // return false because there is no available slot for a small car
    parkingSystem.addCar(1); // return false because there is no available slot for a big car
"""

# Python Solution
class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        # Initialize the parking slots for each type of car
        self.spaces = {1: big, 2: medium, 3: small}

    def addCar(self, carType: int) -> bool:
        # Check if there is space available for the given car type
        if self.spaces[carType] > 0:
            self.spaces[carType] -= 1  # Reduce the available space
            return True
        return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    parkingSystem = ParkingSystem(1, 1, 0)
    print(parkingSystem.addCar(1))  # Output: True (1 big slot available)
    print(parkingSystem.addCar(2))  # Output: True (1 medium slot available)
    print(parkingSystem.addCar(3))  # Output: False (no small slots available)
    print(parkingSystem.addCar(1))  # Output: False (no big slots left)

    # Test Case 2
    parkingSystem = ParkingSystem(2, 2, 2)
    print(parkingSystem.addCar(1))  # Output: True (2 big slots available)
    print(parkingSystem.addCar(1))  # Output: True (1 big slot left)
    print(parkingSystem.addCar(1))  # Output: False (no big slots left)
    print(parkingSystem.addCar(2))  # Output: True (2 medium slots available)
    print(parkingSystem.addCar(3))  # Output: True (2 small slots available)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The `addCar` method runs in O(1) time since it involves a simple lookup and update operation.

Space Complexity:
- The space complexity is O(1) since we only store three integers in the `spaces` dictionary to represent the available slots for each car type.

Overall, the solution is efficient and scales well with the constraints provided.
"""

# Topic: Design