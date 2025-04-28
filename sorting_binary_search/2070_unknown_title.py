"""
LeetCode Problem #2070: Most Beautiful Item for Each Query

Problem Statement:
You are given a 2D integer array `items` where `items[i] = [price_i, beauty_i]` denotes the price and beauty of an item, respectively.

You are also given a 1D integer array `queries` where `queries[j]` denotes the maximum price of an item you can afford.

For each query `queries[j]`, find the maximum beauty of an item you can afford with a price less than or equal to `queries[j]`. If no such item exists, the answer for that query is 0.

Return an array `answer` of the same length as `queries` where `answer[j]` is the answer to the `j`-th query.

Constraints:
- `1 <= items.length, queries.length <= 10^5`
- `items[i].length == 2`
- `1 <= price_i, beauty_i, queries[j] <= 10^9`

Example:
Input: items = [[1, 2], [3, 4], [2, 3]], queries = [2, 3, 1]
Output: [3, 4, 2]
Explanation:
- For queries[0] = 2, you can afford items with prices [1, 2]. The maximum beauty is 3.
- For queries[1] = 3, you can afford items with prices [1, 2, 3]. The maximum beauty is 4.
- For queries[2] = 1, you can only afford the item with price 1. The maximum beauty is 2.

Topic: Sorting, Binary Search
"""

from typing import List
import bisect

def maximumBeauty(items: List[List[int]], queries: List[int]) -> List[int]:
    # Step 1: Sort items by price, and for equal prices, by beauty in descending order
    items.sort()
    
    # Step 2: Precompute the maximum beauty for each price
    max_beauty = 0
    processed_items = []
    for price, beauty in items:
        max_beauty = max(max_beauty, beauty)
        processed_items.append((price, max_beauty))
    
    # Step 3: Answer each query using binary search
    result = []
    for query in queries:
        # Find the largest price <= query using binary search
        idx = bisect.bisect_right(processed_items, (query, float('inf'))) - 1
        if idx >= 0:
            result.append(processed_items[idx][1])
        else:
            result.append(0)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    items = [[1, 2], [3, 4], [2, 3]]
    queries = [2, 3, 1]
    print(maximumBeauty(items, queries))  # Output: [3, 4, 2]

    # Test Case 2
    items = [[10, 100], [5, 50], [7, 70]]
    queries = [5, 10, 7]
    print(maximumBeauty(items, queries))  # Output: [50, 100, 70]

    # Test Case 3
    items = [[1, 1], [2, 2], [3, 3]]
    queries = [1, 2, 3, 4]
    print(maximumBeauty(items, queries))  # Output: [1, 2, 3, 3]

    # Test Case 4
    items = [[1, 10], [2, 20], [3, 30]]
    queries = [0, 1, 2, 3]
    print(maximumBeauty(items, queries))  # Output: [0, 10, 20, 30]

"""
Time Complexity:
- Sorting the items: O(n log n), where n is the number of items.
- Processing the items to compute max beauty: O(n).
- Answering each query using binary search: O(m log n), where m is the number of queries.
Overall: O(n log n + m log n)

Space Complexity:
- The space used for storing the processed items: O(n).
- Overall: O(n)
"""