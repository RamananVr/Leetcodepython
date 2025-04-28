"""
LeetCode Problem #475: Heaters

Problem Statement:
Winter is coming! During the contest, your first job is to design a standard heater with a fixed warm radius to warm all the houses.

Every house can be warmed, as long as the house is within the heater's warm radius range. 

Given the positions of houses and heaters on a horizontal line, return the minimum radius standard of heaters so that all houses can be covered.

The input will be two integer arrays `houses` and `heaters`, where `houses[i]` represents the position of the ith house, and `heaters[j]` represents the position of the jth heater. Both arrays are non-empty, and each position is a non-negative integer.

Constraints:
- 1 <= houses.length, heaters.length <= 10^4
- 0 <= houses[i], heaters[j] <= 10^9

Example:
Input: houses = [1,2,3], heaters = [2]
Output: 1
Explanation: The only heater is placed at position 2, and the radius of 1 is sufficient to cover all houses.

Input: houses = [1,2,3,4], heaters = [1,4]
Output: 1
Explanation: Each heater covers two houses.

Input: houses = [1,5], heaters = [2]
Output: 3
Explanation: The heater at position 2 needs a radius of 3 to cover both houses.

Follow up:
Could you solve this problem in O(n log n) time complexity?
"""

from typing import List

def findRadius(houses: List[int], heaters: List[int]) -> int:
    """
    Finds the minimum radius of heaters required to cover all houses.
    """
    # Sort both houses and heaters
    houses.sort()
    heaters.sort()
    
    # Function to find the closest heater for a given house
    def find_closest_heater(house):
        left, right = 0, len(heaters) - 1
        while left <= right:
            mid = (left + right) // 2
            if heaters[mid] < house:
                left = mid + 1
            else:
                right = mid - 1
        # Calculate distances to the closest heaters
        dist1 = abs(house - heaters[right]) if right >= 0 else float('inf')
        dist2 = abs(house - heaters[left]) if left < len(heaters) else float('inf')
        return min(dist1, dist2)
    
    # Find the maximum radius required for all houses
    max_radius = 0
    for house in houses:
        max_radius = max(max_radius, find_closest_heater(house))
    
    return max_radius

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    houses = [1, 2, 3]
    heaters = [2]
    print(findRadius(houses, heaters))  # Output: 1

    # Test Case 2
    houses = [1, 2, 3, 4]
    heaters = [1, 4]
    print(findRadius(houses, heaters))  # Output: 1

    # Test Case 3
    houses = [1, 5]
    heaters = [2]
    print(findRadius(houses, heaters))  # Output: 3

    # Test Case 4
    houses = [1, 2, 3, 5, 15]
    heaters = [2, 30]
    print(findRadius(houses, heaters))  # Output: 13

"""
Time Complexity:
- Sorting the houses and heaters takes O(n log n + m log m), where n is the number of houses and m is the number of heaters.
- For each house, we perform a binary search on the heaters array, which takes O(log m). Since there are n houses, this step takes O(n log m).
- Overall time complexity: O(n log n + m log m + n log m).

Space Complexity:
- The space complexity is O(1) additional space, as we are not using any extra data structures apart from variables.

Topic: Arrays, Binary Search
"""