"""
LeetCode Question #2292: Products With Minimum Ratings

Problem Statement:
You are given a 2D integer array `products` where `products[i] = [rating_i, price_i]` represents the rating and price of the i-th product. 
You are also given an integer `min_rating`.

A product is considered valid if its rating is greater than or equal to `min_rating`. Return the price of the product with the minimum price among all valid products. 
If there are multiple products with the same minimum price, return the one with the highest rating. If no valid product exists, return -1.

Example:
Input: products = [[4, 100], [3, 200], [5, 100], [2, 300]], min_rating = 4
Output: 100
Explanation: The valid products are [4, 100] and [5, 100]. Both have the same price, but [5, 100] has a higher rating.

Constraints:
- 1 <= products.length <= 10^4
- 1 <= rating_i, price_i <= 10^5
- 1 <= min_rating <= 10^5
"""

# Python Solution
from typing import List

def minimum_price_with_min_rating(products: List[List[int]], min_rating: int) -> int:
    # Initialize variables to track the minimum price and the highest rating for ties
    min_price = float('inf')
    max_rating = -1

    for rating, price in products:
        if rating >= min_rating:
            # Check if this product has a lower price or resolves a tie with a higher rating
            if price < min_price or (price == min_price and rating > max_rating):
                min_price = price
                max_rating = rating

    # If no valid product was found, return -1
    return min_price if min_price != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    products = [[4, 100], [3, 200], [5, 100], [2, 300]]
    min_rating = 4
    print(minimum_price_with_min_rating(products, min_rating))  # Output: 100

    # Test Case 2
    products = [[1, 50], [2, 60], [3, 70]]
    min_rating = 4
    print(minimum_price_with_min_rating(products, min_rating))  # Output: -1

    # Test Case 3
    products = [[5, 300], [5, 200], [4, 200], [3, 100]]
    min_rating = 4
    print(minimum_price_with_min_rating(products, min_rating))  # Output: 200

    # Test Case 4
    products = [[4, 100], [4, 100], [4, 100]]
    min_rating = 4
    print(minimum_price_with_min_rating(products, min_rating))  # Output: 100

    # Test Case 5
    products = [[10, 500], [9, 400], [8, 300], [7, 200]]
    min_rating = 8
    print(minimum_price_with_min_rating(products, min_rating))  # Output: 300

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `products` list once, performing constant-time operations for each product.
- Let n = len(products). The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables (min_price and max_rating).
- The space complexity is O(1).
"""

# Topic: Arrays