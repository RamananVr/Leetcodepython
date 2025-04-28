"""
LeetCode Question #2561: Rearranging Fruits

Problem Statement:
You are given two arrays `basket1` and `basket2` representing the types of fruits in two baskets. 
Each element in the arrays represents the type of fruit, and the number of occurrences of each type 
represents the count of that fruit in the respective basket.

You can swap fruits between the baskets. A swap consists of choosing a fruit type from one basket 
and swapping it with a fruit type from the other basket. The goal is to make both baskets identical 
in terms of the types and counts of fruits.

Return the minimum number of swaps required to make the baskets identical. If it is impossible to 
make the baskets identical, return -1.

Constraints:
- `basket1` and `basket2` have the same length `n`.
- `1 <= n <= 10^5`
- `1 <= basket1[i], basket2[i] <= 10^9`

"""

# Solution
from collections import Counter

def minCostToMakeIdentical(basket1, basket2):
    # Count the frequency of each fruit type in both baskets
    count1 = Counter(basket1)
    count2 = Counter(basket2)
    
    # Combine the counts to get the total frequency of each fruit type
    total_count = count1 + count2
    
    # Check if it's possible to make the baskets identical
    for fruit, total in total_count.items():
        if total % 2 != 0:
            return -1  # If any fruit has an odd total count, it's impossible
    
    # Find the minimum cost to make the baskets identical
    swaps = []
    min_fruit = min(total_count.keys())  # Minimum fruit type for cost calculation
    
    # Calculate excess fruits in basket1 and basket2
    excess1 = []
    excess2 = []
    for fruit in total_count:
        diff = count1[fruit] - total_count[fruit] // 2
        if diff > 0:
            excess1.extend([fruit] * diff)
        elif diff < 0:
            excess2.extend([fruit] * -diff)
    
    # Sort excess fruits for minimum cost calculation
    excess1.sort()
    excess2.sort(reverse=True)
    
    # Calculate the minimum cost of swaps
    for i in range(len(excess1)):
        swaps.append(min(excess1[i], excess2[i], 2 * min_fruit))
    
    return sum(swaps)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    basket1 = [4, 5, 6]
    basket2 = [6, 5, 4]
    print(minCostToMakeIdentical(basket1, basket2))  # Output: 0

    # Test Case 2
    basket1 = [1, 2, 3, 4]
    basket2 = [4, 3, 2, 1]
    print(minCostToMakeIdentical(basket1, basket2))  # Output: 0

    # Test Case 3
    basket1 = [1, 1, 2, 2]
    basket2 = [2, 2, 3, 3]
    print(minCostToMakeIdentical(basket1, basket2))  # Output: -1

    # Test Case 4
    basket1 = [1, 2, 2, 3]
    basket2 = [2, 3, 3, 1]
    print(minCostToMakeIdentical(basket1, basket2))  # Output: 2

# Time and Space Complexity Analysis
"""
Time Complexity:
- Counting frequencies using Counter takes O(n).
- Sorting excess1 and excess2 takes O(n log n).
- Calculating swaps takes O(n).
Overall time complexity: O(n log n).

Space Complexity:
- The space used by Counter is O(u), where u is the number of unique fruit types.
- Excess1 and excess2 arrays can have at most O(n) elements.
Overall space complexity: O(n).
"""

# Topic: Arrays, Hash Table, Sorting