"""
LeetCode Question #2682: Find the Losers of the Circular Game

Problem Statement:
There are n friends that are playing a game. The friends are sitting in a circle and are numbered from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:
1. Start at the 1st friend.
2. Count the next k friends in the clockwise direction including the friend you are currently at. The counting wraps around the circle and may count some friends more than once.
3. The last friend you counted leaves the game.
4. If there is still more than one friend in the game, go back to step 2 starting from the friend immediately clockwise of the friend who just left and continue the game.
5. Else, the last friend in the game is the winner.

Given the number of friends, n, and an integer k, return an array of integers representing the friends that are lost at each turn, in the order they lost.

Examples:
Example 1:
Input: n = 5, k = 2
Output: [2,4,1,5]
Explanation: The game goes as follows:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the game. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4. 
5) Friend 4 leaves the game. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1. 
7) Friend 1 leaves the game. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the game. Winner is friend 3.

Example 2:
Input: n = 6, k = 5
Output: [5,4,6,2,3]
Explanation: The friends leave in the order: 5, 4, 6, 2, 3.

Constraints:
- 2 <= n <= 50
- 1 <= k <= 50
"""

from typing import List

def circularGameLosers(n: int, k: int) -> List[int]:
    """
    Simulate the circular game using array simulation.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    friends = list(range(1, n + 1))  # Friends numbered 1 to n
    losers = []
    current = 0  # Start at friend 1 (index 0)
    
    while len(friends) > 1:
        # Count k friends clockwise and remove the last one
        current = (current + k - 1) % len(friends)
        loser = friends.pop(current)
        losers.append(loser)
        
        # Adjust current position if we removed an element before current
        if current >= len(friends):
            current = 0
    
    return losers

def circularGameLosersOptimized(n: int, k: int) -> List[int]:
    """
    Optimized simulation with better position tracking.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    remaining = list(range(1, n + 1))
    losers = []
    pos = 0
    
    while len(remaining) > 1:
        # Move k-1 steps from current position
        pos = (pos + k - 1) % len(remaining)
        
        # Remove the friend at this position
        losers.append(remaining.pop(pos))
        
        # If we removed the last element, wrap to beginning
        if pos == len(remaining):
            pos = 0
    
    return losers

def circularGameLosersJosephus(n: int, k: int) -> List[int]:
    """
    Using Josephus problem pattern with step-by-step elimination.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    friends = list(range(1, n + 1))
    result = []
    start_idx = 0
    
    for _ in range(n - 1):
        # Calculate the index of the friend to eliminate
        eliminate_idx = (start_idx + k - 1) % len(friends)
        
        # Remove the friend and add to result
        eliminated = friends.pop(eliminate_idx)
        result.append(eliminated)
        
        # Update start index for next round
        if eliminate_idx < len(friends):
            start_idx = eliminate_idx
        else:
            start_idx = 0
    
    return result

def circularGameLosersVerbose(n: int, k: int) -> List[int]:
    """
    Verbose version with detailed tracking for understanding.
    
    Time Complexity: O(n^2)
    Space Complexity: O(n)
    """
    friends = list(range(1, n + 1))
    losers = []
    current_pos = 0
    
    print(f"Starting game with {n} friends, k={k}")
    print(f"Initial friends: {friends}")
    
    while len(friends) > 1:
        print(f"\nRound {len(losers) + 1}:")
        print(f"Current position: {current_pos} (friend {friends[current_pos]})")
        
        # Count k friends clockwise
        elimination_pos = (current_pos + k - 1) % len(friends)
        eliminated_friend = friends[elimination_pos]
        
        print(f"Counting {k} friends clockwise from position {current_pos}")
        print(f"Eliminating friend {eliminated_friend} at position {elimination_pos}")
        
        # Remove the eliminated friend
        friends.pop(elimination_pos)
        losers.append(eliminated_friend)
        
        print(f"Remaining friends: {friends}")
        
        # Update current position
        if elimination_pos < len(friends):
            current_pos = elimination_pos
        else:
            current_pos = 0
        
        if friends:
            print(f"Next starting position: {current_pos} (friend {friends[current_pos]})")
    
    print(f"\nWinner: {friends[0] if friends else 'None'}")
    return losers

# Test Cases
if __name__ == "__main__":
    test_cases = [
        (5, 2, [2, 4, 1, 5]),
        (6, 5, [5, 4, 6, 2, 3]),
        (3, 1, [1, 2]),
        (4, 3, [3, 2, 4]),
        (2, 1, [1]),
        (7, 3, [3, 6, 2, 7, 5, 1])
    ]
    
    print("Testing main approach:")
    for n, k, expected in test_cases:
        result = circularGameLosers(n, k)
        print(f"circularGameLosers({n}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting optimized approach:")
    for n, k, expected in test_cases:
        result = circularGameLosersOptimized(n, k)
        print(f"circularGameLosersOptimized({n}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    print("\nTesting Josephus approach:")
    for n, k, expected in test_cases:
        result = circularGameLosersJosephus(n, k)
        print(f"circularGameLosersJosephus({n}, {k}) = {result}, expected = {expected}, {'✓' if result == expected else '✗'}")
    
    # Verbose test for understanding
    print("\nVerbose example (n=5, k=2):")
    circularGameLosersVerbose(5, 2)

"""
Time and Space Complexity Analysis:

Main Approach (circularGameLosers):
Time Complexity: O(n^2) - For each of n-1 eliminations, we may need to shift elements in the list
Space Complexity: O(n) - Storing the list of remaining friends

Optimized Approach:
Time Complexity: O(n^2) - Same as main approach, list operations dominate
Space Complexity: O(n) - List of remaining friends

Josephus Approach:
Time Complexity: O(n^2) - Similar elimination pattern
Space Complexity: O(n) - List storage

Key Insights:
1. This is a variant of the Josephus problem
2. Circular indexing using modulo operation is crucial
3. Position tracking after elimination needs careful handling
4. The game continues until only one friend remains
5. Array simulation is straightforward but not the most efficient

Optimization Notes:
- Could use a circular linked list for O(n*k) time complexity
- For large k, we could optimize the counting step
- The current approach is suitable for the given constraints

Topic: Arrays, Simulation, Josephus Problem, Circular Data Structures
"""
