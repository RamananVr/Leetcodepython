"""
LeetCode Problem #1357: Apply Discount Every n Orders

Problem Statement:
Design a system that applies discounts to customers' orders based on their order count. 
A customer starts with a counter `0`. Every time they place an order, the counter increments by `1`. 
When the counter reaches `n`, the customer gets a discount of `discount` percent on their total bill. 
The counter resets to `0` after applying the discount.

Implement the `Cashier` class:
- `Cashier(int n, int discount, int[] products, int[] prices)`:
  Initializes the object with:
  - `n`: The number of orders required to apply the discount.
  - `discount`: The percentage discount to apply.
  - `products`: A list of product IDs.
  - `prices`: A list of prices corresponding to the product IDs.

- `float getBill(int[] product, int[] amount)`:
  - Takes a list of product IDs and their respective quantities.
  - Returns the total bill after applying the discount (if applicable).

Constraints:
- 1 <= n <= 1000
- 0 <= discount <= 100
- 1 <= products.length <= 200
- prices.length == products.length
- 1 <= products[i] <= 200
- 1 <= prices[i] <= 1000
- 1 <= product.length <= products.length
- amount.length == product.length
- 1 <= product[i] <= 200
- 1 <= amount[i] <= 1000
- At most 1000 calls will be made to `getBill`.

"""

class Cashier:
    def __init__(self, n: int, discount: int, products: list[int], prices: list[int]):
        """
        Initializes the Cashier object with the given parameters.
        """
        self.n = n
        self.discount = discount
        self.counter = 0
        self.product_prices = {product: price for product, price in zip(products, prices)}

    def getBill(self, product: list[int], amount: list[int]) -> float:
        """
        Calculates the total bill for the given products and their quantities.
        Applies a discount if the counter reaches `n`.
        """
        # Increment the counter for each order
        self.counter += 1

        # Calculate the total bill without discount
        total = sum(self.product_prices[prod] * amt for prod, amt in zip(product, amount))

        # Apply discount if the counter reaches `n`
        if self.counter == self.n:
            total *= (1 - self.discount / 100)
            self.counter = 0  # Reset the counter

        return total


# Example Test Cases
if __name__ == "__main__":
    # Initialize the Cashier object
    cashier = Cashier(3, 50, [1, 2, 3, 4, 5], [100, 200, 300, 400, 500])

    # Test Case 1: First order (no discount)
    print(cashier.getBill([1, 2], [1, 2]))  # Expected: 500 (100*1 + 200*2)

    # Test Case 2: Second order (no discount)
    print(cashier.getBill([3, 5], [1, 1]))  # Expected: 800 (300*1 + 500*1)

    # Test Case 3: Third order (discount applied)
    print(cashier.getBill([1, 4], [2, 1]))  # Expected: 700 (100*2 + 400*1 = 600, then 50% discount)

    # Test Case 4: Fourth order (no discount, counter reset)
    print(cashier.getBill([2, 3], [1, 1]))  # Expected: 500 (200*1 + 300*1)


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - `__init__`: O(m), where `m` is the number of products, to create the `product_prices` dictionary.
   - `getBill`: O(k), where `k` is the number of products in the current order, to calculate the total bill.

   Overall, the time complexity for each `getBill` call is O(k).

2. Space Complexity:
   - The `product_prices` dictionary requires O(m) space, where `m` is the number of products.
   - No additional space is used in `getBill` apart from a few variables.

   Overall, the space complexity is O(m).

Topic: Hash Table, Simulation
"""