"""
LeetCode Problem #2739: Total Distance Traveled

Problem Statement:
A truck driver is traveling on a straight road. The truck starts with a full tank of fuel, which can last for `mainTank` liters. 
The truck also has an auxiliary tank that can store `additionalTank` liters of fuel. The truck consumes 1 liter of fuel for every 
mile it travels. When the truck consumes 5 liters of fuel from the main tank, it can transfer 1 liter of fuel from the auxiliary 
tank to the main tank if the auxiliary tank is not empty.

Given two integers `mainTank` and `additionalTank`, return the total distance the truck can travel.

Constraints:
- 1 <= mainTank, additionalTank <= 100
"""

def distanceTraveled(mainTank: int, additionalTank: int) -> int:
    """
    Calculate the total distance the truck can travel given the main and auxiliary tank capacities.

    :param mainTank: Initial fuel in the main tank (in liters).
    :param additionalTank: Initial fuel in the auxiliary tank (in liters).
    :return: Total distance the truck can travel (in miles).
    """
    distance = 0

    while mainTank >= 5:
        # Consume 5 liters from the main tank
        distance += 5
        mainTank -= 5

        # Transfer 1 liter from the auxiliary tank to the main tank if possible
        if additionalTank > 0:
            mainTank += 1
            additionalTank -= 1

    # Add the remaining fuel in the main tank to the distance
    distance += mainTank

    return distance


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    mainTank = 10
    additionalTank = 5
    print(distanceTraveled(mainTank, additionalTank))  # Expected Output: 15

    # Test Case 2
    mainTank = 5
    additionalTank = 10
    print(distanceTraveled(mainTank, additionalTank))  # Expected Output: 6

    # Test Case 3
    mainTank = 1
    additionalTank = 1
    print(distanceTraveled(mainTank, additionalTank))  # Expected Output: 1

    # Test Case 4
    mainTank = 20
    additionalTank = 0
    print(distanceTraveled(mainTank, additionalTank))  # Expected Output: 20

    # Test Case 5
    mainTank = 7
    additionalTank = 3
    print(distanceTraveled(mainTank, additionalTank))  # Expected Output: 10


"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs as long as `mainTank >= 5`. In each iteration, 5 liters are consumed from the main tank, and optionally 
  1 liter is transferred from the auxiliary tank. Therefore, the number of iterations is proportional to `mainTank / 5`.
- The operations inside the loop (subtracting, adding, and transferring fuel) are O(1).
- Thus, the overall time complexity is O(mainTank / 5), which simplifies to O(mainTank).

Space Complexity:
- The solution uses a constant amount of extra space for variables (`distance`, `mainTank`, `additionalTank`).
- Therefore, the space complexity is O(1).

Topic: Greedy
"""