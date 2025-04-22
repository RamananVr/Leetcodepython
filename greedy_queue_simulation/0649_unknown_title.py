"""
LeetCode Problem #649: Dota2 Senate

Problem Statement:
In the world of Dota2, there are two parties: the Radiant and the Dire. The Dota2 senate consists of senators coming from two parties. Now the senate wants to make a decision about a change in the Dota2 game. The voting for this change is a round-based procedure. In each round, each senator can exercise one of the two rights:

1. Ban one senator's right: A senator can make another senator lose all their rights in this and all the following rounds.
2. Announce the victory: If this senator found the senators who still have rights to vote are all from the same party, he can announce the victory and decide on the change in the game.

Given a string `senate` representing each senator's party belonging. The character 'R' and 'D' represent the Radiant party and the Dire party. Then if there are `n` senators, the size of the given string will be `n`.

The round-based procedure starts from the first senator to the last senator in the given order. This procedure will last until the end of voting. All the senators who have lost their rights will be skipped during the procedure.

Suppose every senator is smart enough and will play the best strategy for their own party. Predict which party will finally announce the victory and change the Dota2 game. The output should be "Radiant" or "Dire".

Constraints:
- `n == len(senate)`
- `1 <= n <= 10^4`
- `senate[i]` is either 'R' or 'D'.

"""

from collections import deque

def predictPartyVictory(senate: str) -> str:
    # Queues to store the indices of Radiant and Dire senators
    radiant_queue = deque()
    dire_queue = deque()
    
    # Populate the queues with the indices of the senators
    for i, s in enumerate(senate):
        if s == 'R':
            radiant_queue.append(i)
        else:
            dire_queue.append(i)
    
    # Total number of senators
    n = len(senate)
    
    # Simulate the rounds
    while radiant_queue and dire_queue:
        # Get the front senators from both queues
        radiant_index = radiant_queue.popleft()
        dire_index = dire_queue.popleft()
        
        # The senator with the smaller index bans the other
        if radiant_index < dire_index:
            # Radiant senator bans Dire senator and gets back in the queue
            radiant_queue.append(radiant_index + n)
        else:
            # Dire senator bans Radiant senator and gets back in the queue
            dire_queue.append(dire_index + n)
    
    # If Radiant queue is not empty, Radiant wins; otherwise, Dire wins
    return "Radiant" if radiant_queue else "Dire"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    senate = "RD"
    print(predictPartyVictory(senate))  # Output: "Radiant"

    # Test Case 2
    senate = "RDD"
    print(predictPartyVictory(senate))  # Output: "Dire"

    # Test Case 3
    senate = "RRDDD"
    print(predictPartyVictory(senate))  # Output: "Dire"

    # Test Case 4
    senate = "RDRDR"
    print(predictPartyVictory(senate))  # Output: "Radiant"

"""
Time Complexity Analysis:
- Let `n` be the length of the input string `senate`.
- Each senator is added back to the queue at most once after being processed, so the total number of operations is proportional to `2n`.
- Each operation (popping from the queue and appending back) takes O(1).
- Therefore, the time complexity is O(n).

Space Complexity Analysis:
- We use two queues to store the indices of Radiant and Dire senators.
- In the worst case, both queues together store all `n` indices.
- Therefore, the space complexity is O(n).

Topic: Greedy, Queue, Simulation
"""