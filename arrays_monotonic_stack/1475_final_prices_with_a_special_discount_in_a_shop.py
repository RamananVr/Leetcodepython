"""
LeetCode Question #1475: Final Prices With a Special Discount in a Shop

Problem Statement:
------------------
You are given an integer array `prices` where `prices[i]` is the price of the ith item in a shop.

There is a special discount for items in the shop. If you buy the ith item, then you will receive a discount 
equivalent to the price of the next item that is less than or equal to the price of the ith item. 
Otherwise, you will not receive any discount at all.

Return an array where the ith element is the final price you will pay for the ith item of the shop, 
considering the special discount.

Example 1:
----------
Input: prices = [8, 4, 6, 2, 3]
Output: [4, 2, 4, 2, 3]
Explanation:
- For item 0, the price is 8. The next item with a price <= 8 is item 1, which costs 4. So, the final price is 8 - 4 = 4.
- For item 1, the price is 4. The next item with a price <= 4 is item 3, which costs 2. So, the final price is 4 - 2 = 2.
- For item 2, the price is 6. The next item with a price <= 6 is item 3, which costs 2. So, the final price is 6 - 2 = 4.
- For item 3, the price is 2. There are no items after it with a price <= 2, so the final price is 2.
- For item 4, the price is 3. There are no items after it with a price <= 3, so the final price is 3.

Example 2:
----------
Input: prices = [1, 2, 3, 4, 5]
Output: [1, 2, 3, 4, 5]
Explanation: In this case, no item has a discount.

Example 3:
----------
Input: prices = [10, 1, 1, 6]
Output: [9, 0, 1, 6]

Constraints:
------------
- 1 <= prices.length <= 500
- 1 <= prices[i] <= 10^3
"""

# Python Solution
def finalPrices(prices):
    """
    This function calculates the final prices of items after applying the special discount.

    :param prices: List[int] - List of item prices
    :return: List[int] - List of final prices after discounts
    """
    n = len(prices)
    result = prices[:]  # Copy the original prices to modify
    stack = []  # Monotonic stack to keep track of indices

    for i in range(n):
        # While the stack is not empty and the current price is less than or equal to the price at the top of the stack
        while stack and prices[i] <= prices[stack[-1]]:
            index = stack.pop()
            result[index] -= prices[i]  # Apply the discount
        stack.append(i)  # Push the current index onto the stack

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    prices1 = [8, 4, 6, 2, 3]
    print(finalPrices(prices1))  # Output: [4, 2, 4, 2, 3]

    # Test Case 2
    prices2 = [1, 2, 3, 4, 5]
    print(finalPrices(prices2))  # Output: [1, 2, 3, 4, 5]

    # Test Case 3
    prices3 = [10, 1, 1, 6]
    print(finalPrices(prices3))  # Output: [9, 0, 1, 6]

    # Test Case 4
    prices4 = [5, 5, 5, 5]
    print(finalPrices(prices4))  # Output: [0, 0, 0, 5]

    # Test Case 5
    prices5 = [7]
    print(finalPrices(prices5))  # Output: [7]

"""
Time and Space Complexity Analysis:
------------------------------------
Time Complexity:
- The algorithm iterates through the `prices` array once, and each index is pushed and popped from the stack at most once.
- Therefore, the time complexity is O(n), where n is the length of the `prices` array.

Space Complexity:
- The space complexity is O(n) due to the stack used to store indices.

Topic: Arrays, Monotonic Stack
"""