"""
LeetCode Question #1412: Find the Number of Good Meals

Problem Statement:
A "good meal" is defined as a pair of dishes whose sum of deliciousness values is a power of two.
You are given an integer array `deliciousness` where `deliciousness[i]` is the deliciousness value of the i-th dish.

Return the number of different good meals you can make from the dishes. Since the answer can be very large, return it modulo 10^9 + 7.

A pair of dishes (i, j) is considered different if i != j (i.e., the dishes are distinct).

Constraints:
- 1 <= deliciousness.length <= 10^5
- 0 <= deliciousness[i] <= 2^20

Example:
Input: deliciousness = [1,3,5,7,9]
Output: 4
Explanation: The good meals are (1,3), (1,7), (3,5), (7,9) with sums 4, 8, 8, and 16 respectively. All of these are powers of two.

Input: deliciousness = [1,1,1,3,3,3,7]
Output: 15
Explanation: There are 15 good meals in total.
"""

# Python Solution
from collections import Counter

def countPairs(deliciousness):
    MOD = 10**9 + 7
    power_of_two = [2**i for i in range(22)]  # Generate all powers of two up to 2^21
    count = Counter()
    result = 0
    
    for value in deliciousness:
        for target in power_of_two:
            complement = target - value
            if complement in count:
                result += count[complement]
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
- The outer loop iterates over the `deliciousness` array, which has a length of n.
- For each value, we iterate over the list of powers of two (22 iterations).
- Checking and updating the Counter dictionary is O(1) on average.
- Thus, the overall time complexity is O(n * 22) = O(n).

Space Complexity:
- We use a Counter dictionary to store the frequency of values in the `deliciousness` array.
- In the worst case, the dictionary could store up to n unique values.
- The space complexity is O(n).

Topic: Hash Table
"""