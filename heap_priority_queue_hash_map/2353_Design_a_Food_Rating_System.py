"""
LeetCode Problem #2353: Design a Food Rating System

Problem Statement:
You are tasked with designing a food rating system. This system will allow users to rate foods and retrieve the highest-rated food for a specific cuisine. Implement the `FoodRatings` class:

- `FoodRatings` initializes with:
  - `foods`: A list of strings where `foods[i]` is the name of the i-th food.
  - `cuisines`: A list of strings where `cuisines[i]` is the cuisine of the i-th food.
  - `ratings`: A list of integers where `ratings[i]` is the initial rating of the i-th food.

- Methods:
  1. `changeRating(food: str, newRating: int) -> None`:
     - Updates the rating of the specified food to `newRating`.

  2. `highestRated(cuisine: str) -> str`:
     - Returns the name of the food with the highest rating for the given cuisine.
     - If there is a tie, return the lexicographically smallest name.

Constraints:
- `1 <= len(foods) <= 10^5`
- `len(foods) == len(cuisines) == len(ratings)`
- `1 <= len(foods[i]), len(cuisines[i]) <= 10`
- `foods[i]`, `cuisines[i]` consist of lowercase English letters.
- `1 <= ratings[i] <= 10^8`
- All `foods[i]` are distinct.
- At most `2 * 10^4` calls will be made to `changeRating` and `highestRated`.

"""

from collections import defaultdict
import heapq

class FoodRatings:
    def __init__(self, foods: list[str], cuisines: list[str], ratings: list[int]):
        # Map food to its cuisine and rating
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        
        # Map cuisine to a max-heap of (-rating, food) tuples
        self.cuisine_to_heap = defaultdict(list)
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            heapq.heappush(self.cuisine_to_heap[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        # Update the food's rating
        cuisine = self.food_to_cuisine[food]
        self.food_to_rating[food] = newRating
        
        # Push the updated rating into the heap
        heapq.heappush(self.cuisine_to_heap[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        # Get the max-heap for the cuisine
        heap = self.cuisine_to_heap[cuisine]
        
        # Remove invalid entries from the top of the heap
        while heap:
            rating, food = heap[0]
            if -rating == self.food_to_rating[food]:
                return food
            heapq.heappop(heap)

# Example Test Cases
if __name__ == "__main__":
    # Initialize the system
    foods = ["burger", "sushi", "pizza"]
    cuisines = ["american", "japanese", "italian"]
    ratings = [5, 8, 7]
    food_ratings = FoodRatings(foods, cuisines, ratings)

    # Test highestRated
    print(food_ratings.highestRated("japanese"))  # Output: "sushi"
    print(food_ratings.highestRated("italian"))   # Output: "pizza"

    # Test changeRating
    food_ratings.changeRating("pizza", 10)
    print(food_ratings.highestRated("italian"))   # Output: "pizza"

    food_ratings.changeRating("sushi", 5)
    print(food_ratings.highestRated("japanese"))  # Output: "sushi"

"""
Time Complexity:
- Initialization: O(n * log(n)), where n is the number of foods. Each food is pushed into a heap, which takes O(log(n)).
- changeRating: O(log(n)), where n is the number of foods in the cuisine's heap.
- highestRated: O(log(n)) amortized, as invalid entries are removed from the heap.

Space Complexity:
- O(n), where n is the number of foods. This accounts for the mappings and heaps.

Topic: Heap (Priority Queue), Hash Map
"""