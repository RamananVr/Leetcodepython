"""
LeetCode Problem #2363: Merge Similar Items

Problem Statement:
You are given two 2D integer arrays, `items1` and `items2`, representing items, where each `items[i] = [value, weight]` 
represents the value and weight of the `i-th` item. 

- Merge the two arrays such that for each unique value in either array, the resulting array contains a pair `[value, weight]` 
  where `weight` is the sum of weights of all items with that value.
- Return the merged array sorted by value.

Example:
Input: items1 = [[1, 1], [4, 5], [3, 8]], items2 = [[3, 1], [1, 5]]
Output: [[1, 6], [3, 9], [4, 5]]

Constraints:
- 1 <= items1.length, items2.length <= 1000
- 1 <= value, weight <= 1000
"""

# Solution
from collections import defaultdict

def mergeSimilarItems(items1, items2):
    """
    Merge two lists of items by summing weights for items with the same value.
    
    Args:
    items1 (List[List[int]]): First list of items, where each item is [value, weight].
    items2 (List[List[int]]): Second list of items, where each item is [value, weight].
    
    Returns:
    List[List[int]]: Merged list of items sorted by value.
    """
    weight_map = defaultdict(int)
    
    # Add weights from items1
    for value, weight in items1:
        weight_map[value] += weight
    
    # Add weights from items2
    for value, weight in items2:
        weight_map[value] += weight
    
    # Convert the dictionary to a sorted list of [value, weight]
    return sorted([[value, weight] for value, weight in weight_map.items()])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    items1 = [[1, 1], [4, 5], [3, 8]]
    items2 = [[3, 1], [1, 5]]
    print(mergeSimilarItems(items1, items2))  # Output: [[1, 6], [3, 9], [4, 5]]

    # Test Case 2
    items1 = [[5, 3], [2, 7]]
    items2 = [[5, 2], [2, 1], [3, 4]]
    print(mergeSimilarItems(items1, items2))  # Output: [[2, 8], [3, 4], [5, 5]]

    # Test Case 3
    items1 = [[1, 10]]
    items2 = [[1, 5], [2, 3]]
    print(mergeSimilarItems(items1, items2))  # Output: [[1, 15], [2, 3]]

    # Test Case 4
    items1 = []
    items2 = [[1, 2], [3, 4]]
    print(mergeSimilarItems(items1, items2))  # Output: [[1, 2], [3, 4]]

    # Test Case 5
    items1 = [[1, 1], [2, 2], [3, 3]]
    items2 = [[4, 4], [5, 5]]
    print(mergeSimilarItems(items1, items2))  # Output: [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5]]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Iterating through items1 and items2 takes O(n + m), where n is the length of items1 and m is the length of items2.
- Sorting the resulting list takes O(k log k), where k is the number of unique values in the merged dictionary.
- Overall time complexity: O(n + m + k log k).

Space Complexity:
- The `weight_map` dictionary stores up to k unique values, where k is the number of unique values in items1 and items2.
- The output list also contains k items.
- Overall space complexity: O(k).
"""

# Topic: Arrays, Hash Map