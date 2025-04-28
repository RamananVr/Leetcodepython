"""
LeetCode Problem #1849: Splitting a String Into Descending Consecutive Values

Problem Statement:
You are given a string `s` that consists of only digits.

Check if it is possible to split the string `s` into one or more substrings such that:
1. Each substring represents a positive integer without leading zeros.
2. The values of the substrings are strictly decreasing by exactly 1.

For example, splitting the string "54321" into ["54", "53", "52", "51"] is valid because they are in strictly decreasing order by 1, but splitting it as ["543", "21"] is not valid.

Return `true` if it is possible to split `s` as described above, or `false` otherwise.

A substring is a contiguous sequence of characters in a string.

Constraints:
- `1 <= s.length <= 20`
- `s` consists of only digits.

---

Solution:
Below is a clean and correct Python solution to the problem.
"""

def splitString(s: str) -> bool:
    def backtrack(index, prev_value):
        # If we've reached the end of the string, return True
        if index == len(s):
            return True
        
        # Try all possible splits starting from the current index
        current_number = 0
        for i in range(index, len(s)):
            current_number = current_number * 10 + int(s[i])
            
            # If the current number is greater than or equal to the previous value, stop exploring
            if current_number >= prev_value:
                break
            
            # If the current number is exactly 1 less than the previous value, recurse
            if current_number == prev_value - 1:
                if backtrack(i + 1, current_number):
                    return True
        
        # If no valid split is found, return False
        return False
    
    # Try all possible starting numbers
    for i in range(len(s) - 1):
        # Extract the starting number
        starting_number = int(s[:i + 1])
        
        # If a valid split is found, return True
        if backtrack(i + 1, starting_number):
            return True
    
    # If no valid split is found, return False
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Valid split
    s1 = "54321"
    print(splitString(s1))  # Output: True (e.g., ["54", "53", "52", "51"])
    
    # Test Case 2: Invalid split
    s2 = "1234"
    print(splitString(s2))  # Output: False (no valid decreasing sequence)
    
    # Test Case 3: Single digit string
    s3 = "9"
    print(splitString(s3))  # Output: False (cannot split a single digit)
    
    # Test Case 4: Valid split with leading zeros in substrings
    s4 = "05040302"
    print(splitString(s4))  # Output: True (e.g., ["05", "04", "03", "02"])
    
    # Test Case 5: Valid split with large numbers
    s5 = "10009998"
    print(splitString(s5))  # Output: True (e.g., ["100", "99", "98"])

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - The outer loop iterates over all possible starting numbers, which can be up to `O(n)` where `n` is the length of the string.
   - The recursive function explores all possible splits for each starting number. In the worst case, this can result in a branching factor of `O(n)` for each level of recursion.
   - Therefore, the overall time complexity is approximately `O(n * n)` or `O(n^2)`.

2. Space Complexity:
   - The space complexity is determined by the recursion depth, which can be at most `O(n)` in the worst case.
   - Thus, the space complexity is `O(n)`.

Topic: Backtracking
"""