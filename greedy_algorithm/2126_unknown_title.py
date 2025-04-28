"""
LeetCode Problem #2126: Destroying Asteroids

Problem Statement:
You are given an integer `mass`, which represents the initial mass of a planet. You are also given an integer array `asteroids` where `asteroids[i]` is the mass of the i-th asteroid.

You can destroy an asteroid if your planet's mass is greater than or equal to the asteroid's mass. After destroying an asteroid, your planet's mass increases by the mass of the destroyed asteroid.

Return `true` if you can destroy all the asteroids. Otherwise, return `false`.

Constraints:
- `1 <= mass <= 10^5`
- `1 <= asteroids.length <= 10^5`
- `1 <= asteroids[i] <= 10^5`
"""

def canDestroyAllAsteroids(mass: int, asteroids: list[int]) -> bool:
    """
    Determines if all asteroids can be destroyed given the initial mass of the planet.

    Args:
    mass (int): The initial mass of the planet.
    asteroids (list[int]): List of asteroid masses.

    Returns:
    bool: True if all asteroids can be destroyed, False otherwise.
    """
    # Sort the asteroids in ascending order
    asteroids.sort()

    # Iterate through the sorted asteroids
    for asteroid in asteroids:
        # If the planet's mass is less than the asteroid's mass, return False
        if mass < asteroid:
            return False
        # Otherwise, destroy the asteroid and increase the planet's mass
        mass += asteroid

    # If all asteroids are destroyed, return True
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: All asteroids can be destroyed
    mass = 10
    asteroids = [3, 9, 19, 5, 21]
    print(canDestroyAllAsteroids(mass, asteroids))  # Expected output: True

    # Test Case 2: Not all asteroids can be destroyed
    mass = 5
    asteroids = [4, 9, 23, 4]
    print(canDestroyAllAsteroids(mass, asteroids))  # Expected output: False

    # Test Case 3: Single asteroid that can be destroyed
    mass = 10
    asteroids = [5]
    print(canDestroyAllAsteroids(mass, asteroids))  # Expected output: True

    # Test Case 4: Single asteroid that cannot be destroyed
    mass = 1
    asteroids = [2]
    print(canDestroyAllAsteroids(mass, asteroids))  # Expected output: False

    # Test Case 5: No asteroids to destroy
    mass = 100
    asteroids = []
    print(canDestroyAllAsteroids(mass, asteroids))  # Expected output: True

"""
Time Complexity Analysis:
- Sorting the asteroids array takes O(n log n), where n is the length of the array.
- Iterating through the asteroids array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The sorting operation uses O(n) space in the worst case for the sorting algorithm.
- No additional data structures are used, so the space complexity is O(1) (excluding input storage).

Overall space complexity: O(n) (due to sorting).

Topic: Greedy Algorithm
"""