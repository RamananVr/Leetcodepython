"""
LeetCode Problem #1715: Count Apples and Oranges

Problem Statement:
You are given a list of integers `fruits` where each integer represents a type of fruit. 
You are also given an integer `k`. You want to pick exactly `k` fruits such that the 
number of distinct types of fruits in your selection is maximized. Return the maximum 
number of distinct fruit types you can pick.

Constraints:
- 1 <= len(fruits) <= 10^5
- 1 <= fruits[i] <= 10^5
- 1 <= k <= len(fruits)
"""

from collections import Counter

def maxDistinctFruits(fruits, k):
    """
    Function to calculate the maximum number of distinct fruit types
    that can be picked from the given list of fruits with exactly k picks.

    :param fruits: List[int] - List of integers representing fruit types.
    :param k: int - Number of fruits to pick.
    :return: int - Maximum number of distinct fruit types.
    """
    # Frequency map of all fruits
    freq = Counter(fruits)
    
    # Sort fruit types by their frequency in descending order
    sorted_fruits = sorted(freq.items(), key=lambda x: -x[1])
    
    # Initialize variables
    distinct_count = 0
    remaining_k = k
    
    # Iterate through the sorted fruit types
    for fruit, count in sorted_fruits:
        if remaining_k == 0:
            break
        # Pick as many fruits of this type as possible
        if count <= remaining_k:
            distinct_count += 1
            remaining_k -= count
        else:
            # If we can't pick all fruits of this type, we can still pick some
            distinct_count += 1
            remaining_k = 0
    
    return distinct_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    fruits = [1, 2, 3, 4, 5]
    k = 3
    print(maxDistinctFruits(fruits, k))  # Expected Output: 3

    # Test Case 2
    fruits = [1, 1, 2, 2, 3, 3, 4, 4]
    k = 4
    print(maxDistinctFruits(fruits, k))  # Expected Output: 2

    # Test Case 3
    fruits = [1, 1, 1, 1, 1]
    k = 2
    print(maxDistinctFruits(fruits, k))  # Expected Output: 1

    # Test Case 4
    fruits = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    k = 5
    print(maxDistinctFruits(fruits, k))  # Expected Output: 3

    # Test Case 5
    fruits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 10
    print(maxDistinctFruits(fruits, k))  # Expected Output: 10

"""
Time Complexity Analysis:
- Constructing the frequency map using Counter takes O(n), where n is the length of the `fruits` list.
- Sorting the frequency map takes O(m log m), where m is the number of unique fruit types.
- Iterating through the sorted fruit types takes O(m).
Thus, the overall time complexity is O(n + m log m).

Space Complexity Analysis:
- The space complexity is O(m), where m is the number of unique fruit types, due to the frequency map.

Topic: Arrays, Hash Map, Sorting
"""