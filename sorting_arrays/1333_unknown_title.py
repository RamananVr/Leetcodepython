"""
LeetCode Problem #1333: Filter Restaurants by Vegan-Friendly, Price and Distance

Problem Statement:
Given the array `restaurants` where `restaurants[i] = [idi, ratingi, veganFriendlyi, pricei, distancei]`. 
You have to filter the restaurants using three filters.

The veganFriendly filter will be either 0 or 1 (where 0 means you can include any restaurant, and 1 means you should only include restaurants with veganFriendlyi set to 1). 
In addition, you have the filters `maxPrice` and `maxDistance` which are the maximum value for price and distance of a restaurant you are willing to consider respectively.

Return the array of restaurant IDs after filtering, ordered by rating from highest to lowest. 
For restaurants with the same rating, order them by ID from highest to lowest. 
For simplicity, the ID of a restaurant is guaranteed to be unique.

Constraints:
- 1 <= restaurants.length <= 10^4
- restaurants[i].length == 5
- 1 <= idi, ratingi, pricei, distancei <= 10^5
- 0 <= veganFriendlyi <= 1
- 1 <= maxPrice, maxDistance <= 10^5
- The IDs of restaurants are distinct.

Example:
Input: restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]], veganFriendly = 1, maxPrice = 50, maxDistance = 10
Output: [3,1,5]
Explanation: 
The restaurants are filtered as follows:
- Restaurants with ID 2 and 4 are excluded because they are not vegan-friendly.
- Restaurants with ID 1, 3, and 5 are included because they are vegan-friendly and their price and distance are within the respective limits.
- After sorting, restaurant ID 3 has the highest rating, followed by ID 1, and then ID 5.

Topic: Sorting, Arrays
"""

from typing import List

def filterRestaurants(restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
    # Filter restaurants based on the given conditions
    filtered = [
        restaurant for restaurant in restaurants
        if (veganFriendly == 0 or restaurant[2] == 1) and
           restaurant[3] <= maxPrice and
           restaurant[4] <= maxDistance
    ]
    
    # Sort by rating (descending), then by ID (descending)
    filtered.sort(key=lambda x: (-x[1], -x[0]))
    
    # Extract and return the IDs of the filtered restaurants
    return [restaurant[0] for restaurant in filtered]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    restaurants = [
        [1, 4, 1, 40, 10],
        [2, 8, 0, 50, 5],
        [3, 8, 1, 30, 4],
        [4, 10, 0, 10, 3],
        [5, 1, 1, 15, 1]
    ]
    veganFriendly = 1
    maxPrice = 50
    maxDistance = 10
    print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))  # Output: [3, 1, 5]

    # Test Case 2
    restaurants = [
        [1, 5, 1, 20, 5],
        [2, 3, 0, 30, 10],
        [3, 4, 1, 10, 2]
    ]
    veganFriendly = 0
    maxPrice = 25
    maxDistance = 5
    print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))  # Output: [1, 3]

    # Test Case 3
    restaurants = [
        [1, 5, 1, 20, 5],
        [2, 3, 0, 30, 10],
        [3, 4, 1, 10, 2]
    ]
    veganFriendly = 1
    maxPrice = 15
    maxDistance = 3
    print(filterRestaurants(restaurants, veganFriendly, maxPrice, maxDistance))  # Output: [3]

"""
Time Complexity:
- Filtering the restaurants takes O(n), where n is the number of restaurants.
- Sorting the filtered restaurants takes O(m log m), where m is the number of filtered restaurants.
- Extracting the IDs takes O(m).
- Overall time complexity: O(n + m log m).

Space Complexity:
- The space complexity is O(m) for storing the filtered restaurants.
- Overall space complexity: O(m), where m is the number of filtered restaurants.
"""