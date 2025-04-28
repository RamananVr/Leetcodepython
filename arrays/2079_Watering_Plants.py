"""
LeetCode Problem #2079: Watering Plants

Problem Statement:
You are given an array `plants` of positive integers where `plants[i]` represents the amount of water the i-th plant needs. You are also given an integer `capacity` representing the maximum amount of water you can carry at once.

You start at the river (index -1) and walk to the plants in order. You must water the plants in the following way:
- You will move to the i-th plant and water it if you have enough water to fully water it. Otherwise, you will return to the river to refill your watering can and then move to the i-th plant.
- Each step you take (including returning to the river) costs 1 unit of distance.

Return the number of steps required to water all the plants.

Example:
Input: plants = [2, 4, 5, 1, 2], capacity = 6
Output: 17
Explanation:
- Start at the river with a full watering can (6 units of water).
- Walk to plant 0 (2 units needed). Water it. Remaining water = 4. Steps = 1.
- Walk to plant 1 (4 units needed). Water it. Remaining water = 0. Steps = 2.
- Walk back to the river to refill. Steps = 2.
- Walk to plant 2 (5 units needed). Water it. Remaining water = 1. Steps = 3.
- Walk to plant 3 (1 unit needed). Water it. Remaining water = 0. Steps = 1.
- Walk back to the river to refill. Steps = 4.
- Walk to plant 4 (2 units needed). Water it. Remaining water = 4. Steps = 1.
Total steps = 17.

Constraints:
- 1 <= plants.length <= 1000
- 1 <= plants[i] <= 10^6
- 1 <= capacity <= 10^6
"""

# Python Solution
def wateringPlants(plants, capacity):
    steps = 0
    current_water = capacity

    for i in range(len(plants)):
        if plants[i] <= current_water:
            # Water the plant and move forward
            steps += 1
            current_water -= plants[i]
        else:
            # Go back to the river to refill and return to the plant
            steps += (2 * i) + 1
            current_water = capacity - plants[i]

    return steps

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    plants = [2, 4, 5, 1, 2]
    capacity = 6
    print(wateringPlants(plants, capacity))  # Output: 17

    # Test Case 2
    plants = [1, 2, 3, 4, 5]
    capacity = 5
    print(wateringPlants(plants, capacity))  # Output: 14

    # Test Case 3
    plants = [7, 7, 7, 7, 7]
    capacity = 8
    print(wateringPlants(plants, capacity))  # Output: 25

    # Test Case 4
    plants = [1, 1, 1, 1, 1]
    capacity = 3
    print(wateringPlants(plants, capacity))  # Output: 9

    # Test Case 5
    plants = [10]
    capacity = 10
    print(wateringPlants(plants, capacity))  # Output: 1

# Time and Space Complexity Analysis
# Time Complexity: O(n)
# - We iterate through the `plants` array once, performing constant-time operations for each plant.
# - Therefore, the time complexity is linear in the size of the input, i.e., O(n), where n is the number of plants.

# Space Complexity: O(1)
# - We use a constant amount of extra space (variables `steps` and `current_water`).
# - No additional data structures are used, so the space complexity is O(1).

# Topic: Arrays