"""
LeetCode Question #294: Flip Game II

Problem Statement:
You are playing the following Flip Game with your friend: Given a string that contains only these two characters: '+' and '-', you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move, and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:
Input: s = "++++"
Output: True
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".

Constraints:
- The input string `s` will only contain '+' and '-'.
- The length of `s` will be at most 60.
"""

def canWin(s: str) -> bool:
    """
    Determines if the starting player can guarantee a win in the Flip Game II.
    
    :param s: A string containing only '+' and '-'.
    :return: True if the starting player can guarantee a win, False otherwise.
    """
    def can_win_recursive(s, memo):
        if s in memo:
            return memo[s]
        
        for i in range(len(s) - 1):
            if s[i:i+2] == "++":
                # Try flipping "++" to "--" and check if the opponent loses
                next_state = s[:i] + "--" + s[i+2:]
                if not can_win_recursive(next_state, memo):
                    memo[s] = True
                    return True
        
        memo[s] = False
        return False
    
    return can_win_recursive(s, {})

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "++++"
    print(canWin(s1))  # Output: True

    # Test Case 2
    s2 = "+-++-+"
    print(canWin(s2))  # Output: False

    # Test Case 3
    s3 = "++--++"
    print(canWin(s3))  # Output: True

    # Test Case 4
    s4 = "++"
    print(canWin(s4))  # Output: True

    # Test Case 5
    s5 = "--"
    print(canWin(s5))  # Output: False

"""
Time and Space Complexity Analysis:

Time Complexity:
- The recursive function explores all possible states of the string `s`.
- The number of states is bounded by the length of the string `s`, and each state can be represented uniquely.
- In the worst case, there are O(2^n) states, where `n` is the length of the string.
- Memoization ensures that each state is computed only once, reducing redundant calculations.

Space Complexity:
- The space complexity is dominated by the memoization dictionary, which stores the results for each state.
- The maximum number of states stored in the dictionary is O(2^n).
- Additionally, the recursion stack can go up to O(n) in depth.

Overall:
- Time Complexity: O(2^n)
- Space Complexity: O(2^n)

Topic: Backtracking
"""