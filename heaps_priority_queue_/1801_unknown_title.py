"""
LeetCode Problem #1801: Number of Orders in the Backlog

Problem Statement:
You are given a 2D integer array `orders`, where each `orders[i] = [price, amount, orderType]` denotes that `amount` orders have been placed of type `orderType` at the price `price`.
- `orderType` is 0 for a buy order, and 1 for a sell order.

There is a backlog that consists of orders that have not been executed. The backlog is initially empty. When an order is placed, the following happens:
1. If the order is a buy order, you look at the sell orders in the backlog. If the price of any sell order is less than or equal to the price of the buy order, they will match and execute. Each time you match a buy order with a sell order, the amount of both orders decreases by the minimum of the amounts. If the sell order's amount becomes 0, remove it from the backlog. Stop processing the buy order if it becomes 0.
2. If the order is a sell order, you look at the buy orders in the backlog. If the price of any buy order is greater than or equal to the price of the sell order, they will match and execute. Each time you match a sell order with a buy order, the amount of both orders decreases by the minimum of the amounts. If the buy order's amount becomes 0, remove it from the backlog. Stop processing the sell order if it becomes 0.
3. Any remaining buy or sell order that could not be matched is added to the backlog.

Return the total number of orders in the backlog after processing all the orders. Since the answer can be large, return it modulo 10^9 + 7.

Constraints:
- `1 <= orders.length <= 10^5`
- `orders[i].length == 3`
- `1 <= price, amount <= 10^9`
- `orderType` is 0 or 1.

"""

import heapq

def getNumberOfBacklogOrders(orders):
    MOD = 10**9 + 7
    buy_heap = []  # Max-heap for buy orders (invert prices to simulate max-heap)
    sell_heap = []  # Min-heap for sell orders

    for price, amount, orderType in orders:
        if orderType == 0:  # Buy order
            while amount > 0 and sell_heap and sell_heap[0][0] <= price:
                sell_price, sell_amount = heapq.heappop(sell_heap)
                matched_amount = min(amount, sell_amount)
                amount -= matched_amount
                sell_amount -= matched_amount
                if sell_amount > 0:
                    heapq.heappush(sell_heap, (sell_price, sell_amount))
            if amount > 0:
                heapq.heappush(buy_heap, (-price, amount))
        else:  # Sell order
            while amount > 0 and buy_heap and -buy_heap[0][0] >= price:
                buy_price, buy_amount = heapq.heappop(buy_heap)
                matched_amount = min(amount, buy_amount)
                amount -= matched_amount
                buy_amount -= matched_amount
                if buy_amount > 0:
                    heapq.heappush(buy_heap, (buy_price, buy_amount))
            if amount > 0:
                heapq.heappush(sell_heap, (price, amount))

    total_orders = sum(amount for _, amount in buy_heap) + sum(amount for _, amount in sell_heap)
    return total_orders % MOD


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    orders1 = [[10, 5, 0], [15, 2, 1], [25, 1, 1], [30, 4, 0]]
    print(getNumberOfBacklogOrders(orders1))  # Expected Output: 6

    # Test Case 2
    orders2 = [[7, 1000000000, 1], [15, 3, 0], [5, 999999997, 0], [5, 1, 1]]
    print(getNumberOfBacklogOrders(orders2))  # Expected Output: 999999984

    # Test Case 3
    orders3 = [[1, 1, 0], [2, 1, 1], [3, 1, 0], [4, 1, 1]]
    print(getNumberOfBacklogOrders(orders3))  # Expected Output: 0


"""
Time Complexity:
- Processing each order involves matching it with orders in the opposite heap. In the worst case, this involves popping and pushing elements in a heap, which takes O(log N) time per operation.
- Since there are at most O(N) orders, the overall time complexity is O(N log N), where N is the number of orders.

Space Complexity:
- The space complexity is O(N) due to the storage of orders in the buy and sell heaps.

Topic: Heaps (Priority Queue)
"""