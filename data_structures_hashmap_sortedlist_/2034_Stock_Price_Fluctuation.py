"""
LeetCode Problem #2034: Stock Price Fluctuation

Problem Statement:
You are given a stream of records about a stock price's history. Each record contains a timestamp and the corresponding price. 
Unfortunately, due to the volatile market, the records do not come in order. Even worse, some records may be incorrect. 
Another record with the same timestamp may appear later with a different price. 

Design a system that supports the following operations:

1. `update(timestamp: int, price: int)`: Updates the price of the stock at the given timestamp. If a record with the same timestamp 
   previously existed, the previous price will be overridden.
2. `current() -> int`: Returns the latest price of the stock.
3. `maximum() -> int`: Returns the maximum price of the stock.
4. `minimum() -> int`: Returns the minimum price of the stock.

Constraints:
- `1 <= timestamp, price <= 10^9`
- At most `10^5` calls will be made to `update`, `current`, `maximum`, and `minimum`.

"""

from sortedcontainers import SortedList

class StockPrice:
    def __init__(self):
        # Dictionary to store the latest price for each timestamp
        self.timestamp_price = {}
        # SortedList to maintain all prices for efficient min/max operations
        self.prices = SortedList()
        # Variable to track the latest timestamp
        self.latest_timestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        # If the timestamp already exists, remove the old price from the sorted list
        if timestamp in self.timestamp_price:
            old_price = self.timestamp_price[timestamp]
            self.prices.remove(old_price)
        
        # Update the timestamp with the new price
        self.timestamp_price[timestamp] = price
        self.prices.add(price)
        
        # Update the latest timestamp if necessary
        self.latest_timestamp = max(self.latest_timestamp, timestamp)

    def current(self) -> int:
        # Return the price at the latest timestamp
        return self.timestamp_price[self.latest_timestamp]

    def maximum(self) -> int:
        # Return the maximum price (last element in the sorted list)
        return self.prices[-1]

    def minimum(self) -> int:
        # Return the minimum price (first element in the sorted list)
        return self.prices[0]


# Example Test Cases
if __name__ == "__main__":
    sp = StockPrice()
    
    # Test Case 1: Basic operations
    sp.update(1, 10)
    sp.update(2, 5)
    assert sp.current() == 5  # Latest price is 5
    assert sp.maximum() == 10  # Maximum price is 10
    assert sp.minimum() == 5  # Minimum price is 5
    
    # Test Case 2: Overriding a timestamp
    sp.update(1, 3)  # Update timestamp 1 with a new price
    assert sp.current() == 5  # Latest price is still 5
    assert sp.maximum() == 5  # Maximum price is now 5
    assert sp.minimum() == 3  # Minimum price is now 3
    
    # Test Case 3: Adding new timestamps
    sp.update(3, 15)
    assert sp.current() == 15  # Latest price is 15
    assert sp.maximum() == 15  # Maximum price is 15
    assert sp.minimum() == 3  # Minimum price is still 3
    
    print("All test cases passed!")

"""
Time and Space Complexity Analysis:

1. `update(timestamp, price)`:
   - Time Complexity: O(log N), where N is the number of prices in the SortedList. 
     Adding/removing an element in a SortedList takes O(log N).
   - Space Complexity: O(N), where N is the number of unique timestamps stored in the dictionary and SortedList.

2. `current()`:
   - Time Complexity: O(1), as it simply retrieves the value from the dictionary.
   - Space Complexity: O(1).

3. `maximum()` and `minimum()`:
   - Time Complexity: O(1), as the maximum and minimum values are directly accessible from the SortedList.
   - Space Complexity: O(1).

Overall:
- Time Complexity: O(log N) for `update`, O(1) for `current`, `maximum`, and `minimum`.
- Space Complexity: O(N), where N is the number of unique timestamps.

Topic: Data Structures (HashMap, SortedList)
"""