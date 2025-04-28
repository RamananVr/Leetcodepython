"""
LeetCode Problem #2335: Minimum Amount of Time to Fill Cups

Problem Statement:
You have a water dispenser that can dispense water into three different types of cups: cold, warm, and hot. 
Every second, you can fill exactly one unit of water into any one of the cups. You are given a 0-indexed integer 
array `amount` of length 3 where:

- `amount[0]` is the number of units of water needed to fill the cold cup,
- `amount[1]` is the number of units of water needed to fill the warm cup, and
- `amount[2]` is the number of units of water needed to fill the hot cup.

Return the minimum number of seconds needed to fill up all the cups.

Constraints:
- `amount.length == 3`
- `0 <= amount[i] <= 100`

Example:
Input: amount = [1, 4, 2]
Output: 4
Explanation: One way to fill the cups is:
- At the 1st second, fill the warm cup. (amount = [1, 3, 2])
- At the 2nd second, fill the warm cup. (amount = [1, 2, 2])
- At the 3rd second, fill the cold and hot cups simultaneously. (amount = [0, 1, 1])
- At the 4th second, fill the warm cup. (amount = [0, 0, 0])

Input: amount = [5, 4, 4]
Output: 7
Explanation: One way to fill the cups is:
- At each second, fill two of the cups with the most water remaining.
"""

# Clean and Correct Python Solution
from typing import List

def fillCups(amount: List[int]) -> int:
    # Sort the array in descending order
    amount.sort(reverse=True)
    
    seconds = 0
    while amount[0] > 0:
        # Always try to fill the two cups with the most water
        if amount[1] > 0:
            amount[0] -= 1
            amount[1] -= 1
        else:
            # If only one cup has water, fill it
            amount[0] -= 1
        # Increment the seconds
        seconds += 1
        # Re-sort the array to maintain descending order
        amount.sort(reverse=True)
    
    return seconds

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    amount1 = [1, 4, 2]
    print(fillCups(amount1))  # Output: 4

    # Test Case 2
    amount2 = [5, 4, 4]
    print(fillCups(amount2))  # Output: 7

    # Test Case 3
    amount3 = [0, 0, 0]
    print(fillCups(amount3))  # Output: 0

    # Test Case 4
    amount4 = [2, 2, 2]
    print(fillCups(amount4))  # Output: 3

    # Test Case 5
    amount5 = [10, 0, 0]
    print(fillCups(amount5))  # Output: 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until all elements in the `amount` array are reduced to 0.
- In each iteration, we sort the array, which takes O(3 * log(3)) = O(1) since the array size is fixed at 3.
- Therefore, the time complexity is O(max(amount)).

Space Complexity:
- The algorithm uses a constant amount of extra space, so the space complexity is O(1).

Topic: Greedy Algorithm
"""