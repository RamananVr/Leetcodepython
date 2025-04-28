"""
LeetCode Problem #2105: Watering Plants II

Problem Statement:
Alice and Bob want to water n plants in their garden. The plants are arranged in a row and are labeled from 0 to n - 1 from left to right where the ith plant is located at position i. Each plant needs a specific amount of water. Alice and Bob have a watering can each, initially full. They water the plants in the following way:

- Alice waters the plants in order from left to right, starting with the 0th plant. Bob waters the plants in order from right to left, starting with the (n - 1)th plant.
- They begin watering the plants simultaneously.
- It takes the same amount of time to water each plant regardless of how much water it needs.
- Alice and Bob cannot water the same plant.
- If one person reaches a plant that the other person is currently watering, they immediately stop watering.

You are given an integer array `plants` of length n, where `plants[i]` is the amount of water the ith plant needs, and two integers `capacityA` and `capacityB` representing the capacities of Alice's and Bob's watering cans respectively. Return the number of times Alice and Bob have to refill their watering cans to complete watering all the plants.

Constraints:
- n == plants.length
- 1 <= n <= 10^5
- 1 <= plants[i] <= 10^6
- max(plants[i]) <= capacityA, capacityB <= 10^9
"""

def minimumRefill(plants, capacityA, capacityB):
    """
    Calculate the minimum number of refills Alice and Bob need to water all the plants.

    :param plants: List[int] - The amount of water each plant needs.
    :param capacityA: int - The capacity of Alice's watering can.
    :param capacityB: int - The capacity of Bob's watering can.
    :return: int - The minimum number of refills required.
    """
    n = len(plants)
    left, right = 0, n - 1
    alice_water, bob_water = capacityA, capacityB
    refills = 0

    while left <= right:
        if left == right:  # If Alice and Bob meet at the same plant
            if alice_water >= plants[left] or bob_water >= plants[left]:
                break
            else:
                refills += 1
                break

        # Alice waters the left plant
        if alice_water >= plants[left]:
            alice_water -= plants[left]
        else:
            refills += 1
            alice_water = capacityA - plants[left]
        left += 1

        # Bob waters the right plant
        if bob_water >= plants[right]:
            bob_water -= plants[right]
        else:
            refills += 1
            bob_water = capacityB - plants[right]
        right -= 1

    return refills


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    plants = [2, 4, 5, 1, 2]
    capacityA = 5
    capacityB = 7
    print(minimumRefill(plants, capacityA, capacityB))  # Output: 0

    # Test Case 2
    plants = [2, 2, 3, 3]
    capacityA = 5
    capacityB = 5
    print(minimumRefill(plants, capacityA, capacityB))  # Output: 1

    # Test Case 3
    plants = [5]
    capacityA = 10
    capacityB = 8
    print(minimumRefill(plants, capacityA, capacityB))  # Output: 0

    # Test Case 4
    plants = [1, 2, 4, 4, 5]
    capacityA = 6
    capacityB = 5
    print(minimumRefill(plants, capacityA, capacityB))  # Output: 2


"""
Time Complexity:
- O(n): We iterate through the plants array once, with Alice moving from left to right and Bob moving from right to left.

Space Complexity:
- O(1): We use a constant amount of extra space.

Topic: Two Pointers
"""