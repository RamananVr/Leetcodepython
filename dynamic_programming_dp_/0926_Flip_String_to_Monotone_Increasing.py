"""
LeetCode Problem #926: Flip String to Monotone Increasing

Problem Statement:
A binary string is monotone increasing if it consists of some number of `0`s (possibly none), 
followed by some number of `1`s (also possibly none). You are given a binary string `s`. 
You can flip `s[i]` (changing it from `0` to `1` or from `1` to `0`) as many times as you want.

Return the minimum number of flips to make `s` monotone increasing.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either '0' or '1'.
"""

def minFlipsMonoIncr(s: str) -> int:
    """
    This function calculates the minimum number of flips required to make the binary string `s` monotone increasing.
    """
    # Count the total number of 1s in the string
    total_ones = sum(1 for char in s if char == '1')
    
    # Initialize variables
    flips = 0  # Number of flips needed to make the string monotone increasing
    min_flips = len(s)  # Start with a large value for the minimum flips
    
    for char in s:
        # Update the minimum flips at each position
        min_flips = min(min_flips, flips + total_ones)
        
        # Update flips and total_ones based on the current character
        if char == '0':
            flips += 1  # Flip 0 to 1
        else:
            total_ones -= 1  # Reduce the count of 1s to the right
    
    # Final update for the minimum flips
    min_flips = min(min_flips, flips + total_ones)
    
    return min_flips

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "00110"
    print(minFlipsMonoIncr(s1))  # Expected Output: 1

    # Test Case 2
    s2 = "010110"
    print(minFlipsMonoIncr(s2))  # Expected Output: 2

    # Test Case 3
    s3 = "00011000"
    print(minFlipsMonoIncr(s3))  # Expected Output: 2

    # Test Case 4
    s4 = "11111"
    print(minFlipsMonoIncr(s4))  # Expected Output: 0

    # Test Case 5
    s5 = "00000"
    print(minFlipsMonoIncr(s5))  # Expected Output: 0

"""
Time Complexity Analysis:
- Calculating the total number of 1s in the string takes O(n), where n is the length of the string.
- The loop iterates through the string once, performing constant-time operations for each character. This also takes O(n).
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The algorithm uses a constant amount of extra space (variables like `total_ones`, `flips`, and `min_flips`).
- Hence, the space complexity is O(1).

Topic: Dynamic Programming (DP)
"""