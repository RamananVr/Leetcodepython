"""
LeetCode Problem #683: K Empty Slots

Problem Statement:
You have `n` bulbs in a row numbered from 1 to `n`. Initially, all the bulbs are turned off. 
On the `i-th` day, you will turn on the bulb at position `bulbs[i]`. A bulb is called "empty slot" 
if there are exactly `k` bulbs between it and another turned-on bulb, and all bulbs in between are turned off.

Given an array `bulbs` where `bulbs[i]` represents the position of the bulb turned on on the `i-th` day, 
and an integer `k`, return the earliest day that there exists two turned-on bulbs with exactly `k` bulbs 
between them. If no such day exists, return `-1`.

Example:
Input: bulbs = [1, 3, 2], k = 1
Output: 2
Explanation:
On the first day: bulbs[1] = 1 -> [1, 0, 0]
On the second day: bulbs[2] = 3 -> [1, 0, 1]
On the third day: bulbs[3] = 2 -> [1, 1, 1]
The earliest day there exists two turned-on bulbs with exactly one empty slot between them is day 2.

Constraints:
- `n == bulbs.length`
- `1 <= n <= 2 * 10^4`
- `1 <= bulbs[i] <= n`
- `bulbs` is a permutation of numbers from `1` to `n`.
- `0 <= k < n - 1`
"""

# Solution
def kEmptySlots(bulbs, k):
    """
    Finds the earliest day there exists two turned-on bulbs with exactly k bulbs between them.

    :param bulbs: List[int] - The order in which bulbs are turned on.
    :param k: int - The number of empty slots between two turned-on bulbs.
    :return: int - The earliest day or -1 if no such day exists.
    """
    n = len(bulbs)
    days = [0] * n  # days[i] represents the day the bulb at position i+1 is turned on
    
    # Fill the days array
    for day, bulb in enumerate(bulbs):
        days[bulb - 1] = day + 1
    
    # Sliding window approach
    left, right = 0, k + 1
    res = float('inf')
    
    while right < n:
        valid = True
        for i in range(left + 1, right):
            if days[i] < max(days[left], days[right]):
                valid = False
                break
        
        if valid:
            res = min(res, max(days[left], days[right]))
        
        left += 1
        right += 1
    
    return res if res != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bulbs = [1, 3, 2]
    k = 1
    print(kEmptySlots(bulbs, k))  # Output: 2

    # Test Case 2
    bulbs = [6, 5, 8, 9, 7, 1, 10, 2, 3, 4]
    k = 2
    print(kEmptySlots(bulbs, k))  # Output: 8

    # Test Case 3
    bulbs = [1, 2, 3]
    k = 1
    print(kEmptySlots(bulbs, k))  # Output: -1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the bulbs array once to construct the `days` array, which takes O(n).
- The sliding window approach iterates through the bulbs array with a window of size k+1, which takes O(n).
- Overall time complexity: O(n).

Space Complexity:
- The `days` array requires O(n) space.
- No additional space is used apart from a few variables.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Sliding Window