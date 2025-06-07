"""
LeetCode Question #2660: Determine the Winner of a Bowling Game

Problem Statement:
You are given two 0-indexed integer arrays player1 and player2, that represent the number of pins that player 1 and player 2 hit in a bowling game, respectively.

The bowling game consists of n turns, and the score of each player in the ith turn is:
- 2 * player[i] if the player hit 10 pins in any of the previous two turns.
- player[i] otherwise.

The score of the player is the sum of their scores in all n turns.

Return:
- 1 if the score of player 1 is more than the score of player 2,
- 2 if the score of player 2 is more than the score of player 1, and
- 0 if the scores of player 1 and player 2 are equal.

Examples:
Example 1:
Input: player1 = [4,10,7,9], player2 = [6,5,2,3]
Output: 1
Explanation: The score of player1 is 4 + 10 + 2*7 + 2*9 = 46.
The score of player2 is 6 + 5 + 2 + 3 = 16.
Score of player1 > score of player2, so, player1 wins and we return 1.

Example 2:
Input: player1 = [3,5,7,6], player2 = [8,10,10,2]
Output: 2
Explanation: The score of player1 is 3 + 5 + 7 + 6 = 21.
The score of player2 is 8 + 10 + 2*10 + 2*2 = 42.
Score of player2 > score of player1, so, player2 wins and we return 2.

Example 3:
Input: player1 = [2,3], player2 = [4,1]
Output: 0
Explanation: The score of player1 is 2 + 3 = 5.
The score of player2 is 4 + 1 = 5.
The scores are equal, so we return 0.

Constraints:
- n == player1.length == player2.length
- 1 <= n <= 1000
- 0 <= player1[i], player2[i] <= 10
"""

from typing import List

def isWinner(player1: List[int], player2: List[int]) -> int:
    """
    Determine the winner of the bowling game.
    
    Rules:
    - Score is doubled if player hit 10 pins in any of the previous two turns
    - Return 1 if player1 wins, 2 if player2 wins, 0 if tie
    """
    def calculate_score(player):
        """Calculate total score for a player."""
        score = 0
        n = len(player)
        
        for i in range(n):
            multiplier = 1
            
            # Check if player hit 10 in previous turn
            if i > 0 and player[i-1] == 10:
                multiplier = 2
            # Check if player hit 10 two turns ago
            elif i > 1 and player[i-2] == 10:
                multiplier = 2
            
            score += multiplier * player[i]
        
        return score
    
    score1 = calculate_score(player1)
    score2 = calculate_score(player2)
    
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

def isWinnerOptimized(player1: List[int], player2: List[int]) -> int:
    """
    Optimized version with single pass calculation.
    """
    score1 = score2 = 0
    n = len(player1)
    
    for i in range(n):
        # Calculate multiplier for player1
        multiplier1 = 1
        if (i > 0 and player1[i-1] == 10) or (i > 1 and player1[i-2] == 10):
            multiplier1 = 2
        score1 += multiplier1 * player1[i]
        
        # Calculate multiplier for player2
        multiplier2 = 1
        if (i > 0 and player2[i-1] == 10) or (i > 1 and player2[i-2] == 10):
            multiplier2 = 2
        score2 += multiplier2 * player2[i]
    
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

def isWinnerVerbose(player1: List[int], player2: List[int]) -> int:
    """
    Verbose version for better understanding and debugging.
    """
    def calculate_score_verbose(player, player_name):
        """Calculate score with detailed breakdown."""
        score = 0
        n = len(player)
        breakdown = []
        
        for i in range(n):
            base_score = player[i]
            multiplier = 1
            reason = "normal"
            
            # Check for 10 in previous turn
            if i > 0 and player[i-1] == 10:
                multiplier = 2
                reason = f"10 in turn {i-1}"
            # Check for 10 two turns ago
            elif i > 1 and player[i-2] == 10:
                multiplier = 2
                reason = f"10 in turn {i-2}"
            
            turn_score = multiplier * base_score
            score += turn_score
            
            breakdown.append(f"Turn {i}: {base_score} x {multiplier} = {turn_score} ({reason})")
        
        print(f"{player_name} breakdown:")
        for line in breakdown:
            print(f"  {line}")
        print(f"  Total: {score}\n")
        
        return score
    
    score1 = calculate_score_verbose(player1, "Player 1")
    score2 = calculate_score_verbose(player2, "Player 2")
    
    if score1 > score2:
        return 1
    elif score2 > score1:
        return 2
    else:
        return 0

def isWinnerAlternative(player1: List[int], player2: List[int]) -> int:
    """
    Alternative implementation using boolean flags.
    """
    def get_player_score(pins):
        """Calculate player score using boolean flags."""
        total = 0
        strike_bonus_1 = False  # Strike in previous turn
        strike_bonus_2 = False  # Strike two turns ago
        
        for pin in pins:
            # Calculate current turn score
            if strike_bonus_1 or strike_bonus_2:
                total += 2 * pin
            else:
                total += pin
            
            # Update strike bonus flags
            strike_bonus_2 = strike_bonus_1
            strike_bonus_1 = (pin == 10)
        
        return total
    
    score1 = get_player_score(player1)
    score2 = get_player_score(player2)
    
    return 1 if score1 > score2 else (2 if score2 > score1 else 0)

# Test Cases
if __name__ == "__main__":
    test_cases = [
        ([4, 10, 7, 9], [6, 5, 2, 3], 1),
        ([3, 5, 7, 6], [8, 10, 10, 2], 2),
        ([2, 3], [4, 1], 0),
        ([10, 10, 10], [5, 5, 5], 1),
        ([1, 1, 1, 10, 10, 10, 1], [1, 1, 1, 1, 1, 1, 1], 1),
        ([10], [10], 0),
        ([5, 6], [7, 4], 0)
    ]
    
    print("Testing main approach:")
    for player1, player2, expected in test_cases:
        result = isWinner(player1, player2)
        print(f"isWinner({player1}, {player2}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for player1, player2, expected in test_cases:
        result = isWinnerOptimized(player1, player2)
        print(f"isWinnerOptimized({player1}, {player2}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting alternative approach:")
    for player1, player2, expected in test_cases:
        result = isWinnerAlternative(player1, player2)
        print(f"isWinnerAlternative({player1}, {player2}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Detailed breakdown for first test case
    print("\nDetailed breakdown for test case 1:")
    isWinnerVerbose([4, 10, 7, 9], [6, 5, 2, 3])

"""
Time and Space Complexity Analysis:

All Approaches:
Time Complexity: O(n) - single pass through both arrays
Space Complexity: O(1) - only using constant extra space

Main Approach:
- Clear separation of concerns with helper function
- Easy to understand and debug

Optimized Approach:
- Single pass through arrays
- Slightly more efficient as it avoids function calls

Alternative Approach:
- Uses boolean flags to track strike bonuses
- Different perspective on the same problem

Key Insights:
1. A strike (10 pins) affects the next two turns
2. Need to check both previous turn and two turns ago
3. Score calculation is straightforward once bonus conditions are identified

Rules Summary:
- Normal turn: score = pins hit
- Bonus turn: score = 2 * pins hit (if 10 hit in previous 1 or 2 turns)

Topic: Arrays, Simulation, Game Logic, State Tracking
"""
