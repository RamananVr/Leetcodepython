"""
LeetCode Problem #319: Bulb Switcher

Problem Statement:
There are `n` bulbs that are initially off. You first turn on all the bulbs. Then, you turn off every second bulb. 
On the third round, you toggle every third bulb (turning on if it's off or turning off if it's on). 
For the `i-th` round, you toggle every `i-th` bulb. For the `n-th` round, you only toggle the last bulb. 
Return the number of bulbs that are on after `n` rounds.

Example 1:
Input: n = 3
Output: 1
Explanation:
At first, the three bulbs are [off, off, off].
After the first round, the three bulbs are [on, on, on].
After the second round, the three bulbs are [on, off, on].
After the third round, the three bulbs are [on, off, off].
So you should return 1 because there is only one bulb that is on.

Example 2:
Input: n = 0
Output: 0

Example 3:
Input: n = 1
Output: 1

Constraints:
- 0 <= n <= 10^9
"""

def bulbSwitch(n: int) -> int:
    """
    The number of bulbs that remain on after n rounds is equal to the number of perfect squares <= n.
    This is because only perfect square numbers have an odd number of divisors, which means they will
    remain toggled on.
    """
    return int(n**0.5)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}, Output: {bulbSwitch(n)}")  # Expected Output: 1

    # Test Case 2
    n = 0
    print(f"Input: n = {n}, Output: {bulbSwitch(n)}")  # Expected Output: 0

    # Test Case 3
    n = 1
    print(f"Input: n = {n}, Output: {bulbSwitch(n)}")  # Expected Output: 1

    # Test Case 4
    n = 10
    print(f"Input: n = {n}, Output: {bulbSwitch(n)}")  # Expected Output: 3

    # Test Case 5
    n = 25
    print(f"Input: n = {n}, Output: {bulbSwitch(n)}")  # Expected Output: 5

"""
Time Complexity Analysis:
- The solution involves calculating the square root of `n`, which is an O(1) operation.
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of space, so the space complexity is O(1).

Topic: Math
"""