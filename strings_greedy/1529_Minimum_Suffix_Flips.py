"""
LeetCode Problem #1529: Minimum Suffix Flips

Problem Statement:
You are given a binary string `target` of length `n`. You have another binary string `current` of the same length, 
initially set to all '0's. You want to make `current` equal to `target`.

In one operation, you can pick any index `i` (1-based) and flip all the bits from index `i` to the end of the string. 
Flipping means changing '0' to '1' and '1' to '0'.

Return the minimum number of operations needed to make `current` equal to `target`.

Constraints:
- `1 <= target.length <= 10^5`
- `target[i]` is either `'0'` or `'1'`.

Example:
Input: target = "10111"
Output: 3
Explanation: Initially, current = "00000".
- Flip from index 1: current = "11111".
- Flip from index 2: current = "10000".
- Flip from index 5: current = "10111".
"""

# Python Solution
def minFlips(target: str) -> int:
    flips = 0
    current_state = '0'  # Initially, all bits in `current` are '0'
    
    for bit in target:
        if bit != current_state:
            flips += 1
            current_state = bit  # Update the current state to match the target bit
    
    return flips

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    target = "10111"
    print(minFlips(target))  # Output: 3

    # Test Case 2
    target = "101"
    print(minFlips(target))  # Output: 3

    # Test Case 3
    target = "00000"
    print(minFlips(target))  # Output: 0

    # Test Case 4
    target = "11111"
    print(minFlips(target))  # Output: 1

    # Test Case 5
    target = "010101"
    print(minFlips(target))  # Output: 6

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution iterates through the `target` string once, so the time complexity is O(n), 
  where `n` is the length of the `target` string.

Space Complexity:
- The solution uses a constant amount of extra space (for variables like `flips` and `current_state`), 
  so the space complexity is O(1).

Topic: Strings, Greedy
"""