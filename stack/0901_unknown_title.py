"""
LeetCode Problem #901: Online Stock Span

Problem Statement:
Design an algorithm that collects daily price quotes for some stock and returns the span of that stock's price for the current day.

The span of the stock's price today is defined as the maximum number of consecutive days (starting from today and going backward) for which the price of the stock was less than or equal to today's price.

For example, if the prices of the stock over the last 7 days were [100, 80, 60, 70, 60, 75, 85], then the stock spans are [1, 1, 1, 2, 1, 4, 6].

Implement the StockSpanner class:
- `StockSpanner()` Initializes the object of the class.
- `next(int price)` Returns the span of the stock's price for the current day.

Constraints:
- 1 <= price <= 10^5
- At most 10^4 calls will be made to `next`.
"""

# Solution
class StockSpanner:
    def __init__(self):
        # Stack to store pairs of (price, span)
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        # While the stack is not empty and the top price is less than or equal to the current price
        while self.stack and self.stack[-1][0] <= price:
            # Add the span of the top element to the current span
            span += self.stack.pop()[1]
        # Push the current price and its span onto the stack
        self.stack.append((price, span))
        return span

# Example Test Cases
if __name__ == "__main__":
    spanner = StockSpanner()
    print(spanner.next(100))  # Output: 1
    print(spanner.next(80))   # Output: 1
    print(spanner.next(60))   # Output: 1
    print(spanner.next(70))   # Output: 2
    print(spanner.next(60))   # Output: 1
    print(spanner.next(75))   # Output: 4
    print(spanner.next(85))   # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- Each call to `next` involves popping elements from the stack. Each price is pushed and popped from the stack exactly once.
- Therefore, the amortized time complexity for each call to `next` is O(1).

Space Complexity:
- The stack stores pairs of (price, span). In the worst case, all prices are strictly decreasing, and the stack will contain all prices.
- Therefore, the space complexity is O(n), where n is the number of calls to `next`.

Topic: Stack
"""