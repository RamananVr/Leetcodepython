"""
LeetCode Question #1921: Eliminate Maximum Number of Monsters

Problem Statement:
You are playing a video game where you are defending your city from a group of n monsters. 
You are given a 0-indexed integer array dist of size n, where dist[i] is the distance between 
the i-th monster and the city, and a 0-indexed integer array speed of size n, where speed[i] 
is the speed of the i-th monster (in distance per minute).

The monsters start moving toward the city at the same time. You have a weapon that can eliminate 
one monster per minute. Return the maximum number of monsters that you can eliminate before any 
monster reaches the city.

Example 1:
Input: dist = [1,3,4], speed = [1,1,1]
Output: 3
Explanation:
- At minute 1, the first monster is eliminated. The remaining monsters are 2 minutes and 3 minutes away.
- At minute 2, the second monster is eliminated. The remaining monster is 1 minute away.
- At minute 3, the third monster is eliminated.

Example 2:
Input: dist = [1,1,2,3], speed = [1,1,1,1]
Output: 1
Explanation:
- At minute 1, the first monster is eliminated. The remaining monsters are 0, 1, and 2 minutes away.
Thus, you can only eliminate 1 monster before one reaches the city.

Example 3:
Input: dist = [3,2,4], speed = [5,3,2]
Output: 1
Explanation:
- At minute 1, the first monster is eliminated. The remaining monsters are -2 and 2 minutes away.
Thus, you can only eliminate 1 monster before one reaches the city.

Constraints:
- n == dist.length == speed.length
- 1 <= n <= 10^5
- 1 <= dist[i], speed[i] <= 10^5
"""

# Python Solution
from typing import List

def eliminateMaximum(dist: List[int], speed: List[int]) -> int:
    # Calculate the time each monster takes to reach the city
    time_to_reach = [dist[i] / speed[i] for i in range(len(dist))]
    # Sort the times in ascending order
    time_to_reach.sort()
    
    # Eliminate monsters one by one
    eliminated = 0
    for minute, time in enumerate(time_to_reach):
        if minute >= time:  # If the monster reaches the city before we can eliminate it
            break
        eliminated += 1
    
    return eliminated

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    dist1 = [1, 3, 4]
    speed1 = [1, 1, 1]
    print(eliminateMaximum(dist1, speed1))  # Output: 3

    # Test Case 2
    dist2 = [1, 1, 2, 3]
    speed2 = [1, 1, 1, 1]
    print(eliminateMaximum(dist2, speed2))  # Output: 1

    # Test Case 3
    dist3 = [3, 2, 4]
    speed3 = [5, 3, 2]
    print(eliminateMaximum(dist3, speed3))  # Output: 1

    # Additional Test Case
    dist4 = [5, 10, 15]
    speed4 = [1, 2, 3]
    print(eliminateMaximum(dist4, speed4))  # Output: 3

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the time each monster takes to reach the city: O(n)
- Sorting the times: O(n log n)
- Iterating through the sorted times: O(n)
Overall: O(n log n)

Space Complexity:
- The `time_to_reach` list requires O(n) space.
Overall: O(n)

Topic: Arrays, Sorting
"""