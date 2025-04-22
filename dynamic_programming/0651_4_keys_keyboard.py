"""
LeetCode Question #651: 4 Keys Keyboard

Problem Statement:
Imagine you have a special keyboard with the following keys:
1. Key 'A': Prints one 'A' on the screen.
2. Key 'Ctrl-A': Selects all the text on the screen.
3. Key 'Ctrl-C': Copies all the selected text to the clipboard.
4. Key 'Ctrl-V': Pastes the text from the clipboard onto the screen, appending it after what is already on the screen.

You can only press the keys in the above order. Initially, your screen is empty, and you have nothing in your clipboard.

Given an integer `n`, which represents the number of key presses allowed, write a function to return the maximum number of 'A's you can print on the screen.

Constraints:
- 1 <= n <= 50

"""

# Python Solution
def maxA(n: int) -> int:
    """
    Dynamic Programming solution to find the maximum number of 'A's
    that can be printed with n key presses.
    """
    # dp[i] represents the maximum number of 'A's that can be printed with i key presses
    dp = [0] * (n + 1)
    
    for i in range(1, n + 1):
        # Press 'A' key
        dp[i] = dp[i - 1] + 1
        
        # Try all possible Ctrl-A, Ctrl-C, Ctrl-V sequences
        for j in range(2, i):
            # If we perform Ctrl-A, Ctrl-C at step j, and then Ctrl-V (i - j) times
            dp[i] = max(dp[i], dp[j - 2] * (i - j + 1))
    
    return dp[n]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}, Output: {maxA(n)}")  # Expected Output: 3
    
    # Test Case 2
    n = 7
    print(f"Input: n = {n}, Output: {maxA(n)}")  # Expected Output: 9
    
    # Test Case 3
    n = 10
    print(f"Input: n = {n}, Output: {maxA(n)}")  # Expected Output: 20
    
    # Test Case 4
    n = 15
    print(f"Input: n = {n}, Output: {maxA(n)}")  # Expected Output: 81

# Time and Space Complexity Analysis
"""
Time Complexity:
- The outer loop runs for n iterations.
- The inner loop runs for i iterations in the worst case.
- Therefore, the total time complexity is O(n^2).

Space Complexity:
- The space complexity is O(n) due to the dp array.

Overall Complexity: Time: O(n^2), Space: O(n)
"""

# Topic: Dynamic Programming