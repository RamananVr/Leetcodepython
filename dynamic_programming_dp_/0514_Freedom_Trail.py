"""
LeetCode Problem #514: Freedom Trail

Problem Statement:
In the video game Fallout 4, the quest "Road to Freedom" requires players to reach a metal dial called the "Freedom Trail Ring," 
and use the dial to spell a specific keyword in order to open the door.

Given a string ring, which represents the code engraved on the outer ring and another string key, which represents the keyword 
that needs to be spelled, you need to find the minimum number of steps to spell all the characters in the keyword.

Initially, the first character of the ring is aligned at the "12:00" direction. You need to spell all the characters in the 
string key one by one by rotating the ring clockwise or anticlockwise to make each character of the string key appear at the 
"12:00" direction and then pressing the center button.

At the stage of rotating the ring to spell the key character key[i]:
1. You can rotate the ring clockwise or anticlockwise one place, which counts as 1 step. The final goal is to align one of the 
   ring's characters with the "12:00" direction.
2. Once the character is aligned, you need to press the center button to spell this character, which also counts as 1 step.

Given the strings ring and key, return the minimum number of steps in order to spell the key.

Constraints:
- 1 <= ring.length, key.length <= 100
- ring and key consist of only lowercase English letters.
- It is guaranteed that key can always be spelled by rotating the ring.
"""

# Solution
from collections import defaultdict
from functools import lru_cache

def findRotateSteps(ring: str, key: str) -> int:
    # Preprocess the ring to store the indices of each character
    char_to_indices = defaultdict(list)
    for i, char in enumerate(ring):
        char_to_indices[char].append(i)
    
    n = len(ring)
    
    @lru_cache(None)
    def dfs(ring_pos, key_index):
        # Base case: if we've spelled the entire key
        if key_index == len(key):
            return 0
        
        # Get the current character in the key we need to spell
        target_char = key[key_index]
        min_steps = float('inf')
        
        # Try aligning the ring to each occurrence of the target character
        for target_pos in char_to_indices[target_char]:
            # Calculate the distance to rotate to the target position
            clockwise_steps = abs(target_pos - ring_pos)
            anticlockwise_steps = n - clockwise_steps
            rotation_steps = min(clockwise_steps, anticlockwise_steps)
            
            # Recurse to the next character in the key
            steps = rotation_steps + 1 + dfs(target_pos, key_index + 1)  # +1 for pressing the button
            min_steps = min(min_steps, steps)
        
        return min_steps
    
    # Start the recursion from the initial position (12:00) and the first character of the key
    return dfs(0, 0)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ring = "godding"
    key = "gd"
    print(findRotateSteps(ring, key))  # Expected Output: 4

    # Test Case 2
    ring = "abcde"
    key = "ade"
    print(findRotateSteps(ring, key))  # Expected Output: 6

    # Test Case 3
    ring = "caotmcaataijjxi"
    key = "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx"
    print(findRotateSteps(ring, key))  # Expected Output: 137

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let n = len(ring) and m = len(key).
- For each character in the key (m iterations), we may need to consider all positions of the ring (n iterations).
- Each recursive call involves calculating distances and making recursive calls, which is O(n).
- Using memoization, the total number of unique states is O(n * m).
- Thus, the time complexity is O(n * m).

Space Complexity:
- The space complexity is O(n * m) for the memoization cache.
- Additionally, the recursion stack can go up to O(m) depth.
- Thus, the total space complexity is O(n * m).
"""

# Topic: Dynamic Programming (DP)