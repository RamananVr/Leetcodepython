"""
LeetCode Question #2517: Maximum Tastiness of Candy Basket

Problem Statement:
You are given an array of positive integers `price` where `price[i]` represents the price of the ith candy. 
You are also given a positive integer `k`.

The tastiness of a candy basket is defined as the minimum absolute difference of the prices of any two candies 
in the basket. You want to select `k` candies such that the tastiness of the basket is maximized.

Return the maximum tastiness of the candy basket.

Example 1:
Input: price = [13, 5, 1, 8, 21], k = 3
Output: 8
Explanation: Choose candies with prices [13, 5, 21]. The tastiness of the basket is min(|13 - 5|, |13 - 21|, |5 - 21|) = 8.

Example 2:
Input: price = [1, 3, 1], k = 2
Output: 2
Explanation: Choose candies with prices [1, 3]. The tastiness of the basket is min(|1 - 3|) = 2.

Example 3:
Input: price = [7, 7, 7, 7], k = 2
Output: 0
Explanation: Choose candies with prices [7, 7]. The tastiness of the basket is min(|7 - 7|) = 0.

Constraints:
- 2 <= k <= price.length <= 10^4
- 1 <= price[i] <= 10^9
"""

# Solution
def maximumTastiness(price, k):
    def can_form_basket_with_tastiness(mid):
        # Try to form a basket with tastiness >= mid
        count = 1  # Start with the first candy
        prev = price[0]
        for i in range(1, len(price)):
            if price[i] - prev >= mid:
                count += 1
                prev = price[i]
            if count >= k:
                return True
        return False

    # Sort the prices to enable binary search
    price.sort()

    # Binary search for the maximum tastiness
    left, right = 0, price[-1] - price[0]
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if can_form_basket_with_tastiness(mid):
            result = mid  # Update result and try for a larger tastiness
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    price1 = [13, 5, 1, 8, 21]
    k1 = 3
    print(maximumTastiness(price1, k1))  # Output: 8

    # Test Case 2
    price2 = [1, 3, 1]
    k2 = 2
    print(maximumTastiness(price2, k2))  # Output: 2

    # Test Case 3
    price3 = [7, 7, 7, 7]
    k3 = 2
    print(maximumTastiness(price3, k3))  # Output: 0

    # Test Case 4
    price4 = [1, 10, 20, 30, 40]
    k4 = 4
    print(maximumTastiness(price4, k4))  # Output: 10

    # Test Case 5
    price5 = [1, 2, 3, 4, 5]
    k5 = 3
    print(maximumTastiness(price5, k5))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the `price` array.
- Binary search runs for O(log(max_diff)), where max_diff is the difference between the largest and smallest price.
- For each binary search iteration, we iterate through the array to check if a basket can be formed, which takes O(n).
- Overall complexity: O(n log n + n log(max_diff)) ≈ O(n log n).

Space Complexity:
- The space complexity is O(1) since we are not using any additional data structures apart from variables.

Topic: Binary Search
"""