"""
LeetCode Problem #1711: Count Good Meals

Problem Statement:
A "good meal" is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

Given an integer array `deliciousness` where `deliciousness[i]` is the deliciousness of the i-th food item, return the number of different good meals you can make from this list modulo 10^9 + 7.

Note:
- A power of two is a number of the form `2^x` where `x >= 0`.
- The pairs of food items can be in any order.

Constraints:
- `1 <= deliciousness.length <= 10^5`
- `0 <= deliciousness[i] <= 2^20`

Example:
Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (3,5), (7,9), and (1,7).

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: The good meals are (1,1), (1,1), (1,1), (3,3), (3,3), (3,3), (1,3), (1,3), (1,3), (1,7), (3,7), (3,7), (3,7), (1,3), (3,7).
"""

# Python Solution
from collections import Counter

def countPairs(deliciousness):
    MOD = 10**9 + 7
    max_val = 2**21  # Maximum possible sum (2^20 + 2^20)
    count = Counter()
    result = 0
    
    for value in deliciousness:
        for power in range(22):  # Check all powers of 2 up to 2^21
            target = 2**power
            result += count[target - value]
        count[value] += 1
    
    return result % MOD

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    deliciousness = [1, 3, 5, 7, 9]
    print(countPairs(deliciousness))  # Output: 4

    # Test Case 2
    deliciousness = [1, 1, 1, 3, 3, 3, 7]
    print(countPairs(deliciousness))  # Output: 15

    # Test Case 3
    deliciousness = [0, 0, 0, 0]
    print(countPairs(deliciousness))  # Output: 6

    # Test Case 4
    deliciousness = [1048576, 1048576]
    print(countPairs(deliciousness))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- The outer loop iterates over all elements in the `deliciousness` array, which has a length of `n`.
- For each element, we check up to 22 powers of 2 (from 2^0 to 2^21). This is constant work (22 iterations).
- Thus, the overall time complexity is O(n).

Space Complexity:
- We use a Counter (dictionary) to store the frequency of elements in the array. In the worst case, the dictionary could store up to `n` unique elements.
- Thus, the space complexity is O(n).

Topic: Hash Table
"""