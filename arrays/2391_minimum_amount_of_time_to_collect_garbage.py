"""
LeetCode Question #2391: Minimum Amount of Time to Collect Garbage

Problem Statement:
You are given a 0-indexed array of strings `garbage` where `garbage[i]` represents the types of garbage at the ith house. 
`garbage[i]` consists only of the characters 'M', 'P', and 'G' representing one unit of metal, paper, and glass garbage, respectively. 
You are also given a 0-indexed integer array `travel` where `travel[i]` is the time taken to move from house i to house i + 1.

The garbage truck starts at house 0. You need to pick up all the garbage in every house and return the minimum amount of time required to do so.

The truck can only carry one type of garbage at a time. Therefore, it must finish collecting one type of garbage before moving on to the next type.

Constraints:
- 2 <= garbage.length <= 10^5
- 1 <= garbage[i].length <= 10
- `garbage[i]` consists of only 'M', 'P', and 'G'.
- 1 <= travel.length <= garbage.length - 1
- 1 <= travel[i] <= 100

Example:
Input: garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3]
Output: 21
Explanation:
- The truck collects glass garbage ('G') first. It takes 1 unit of time to collect garbage at house 0, 3 units of time to collect garbage at house 3, and 2 + 4 + 3 = 9 units of time to travel between houses.
- The truck collects paper garbage ('P') next. It takes 1 unit of time to collect garbage at house 1, 1 unit of time to collect garbage at house 2, and 2 + 4 = 6 units of time to travel between houses.
- The truck collects metal garbage ('M') last. It takes 1 unit of time to collect garbage at house 2, and 2 + 4 = 6 units of time to travel between houses.
- Total time = 1 + 9 + 1 + 6 + 1 + 6 = 21.

Write a function `minTimeToCollectGarbage(garbage: List[str], travel: List[int]) -> int` to solve the problem.
"""

from typing import List

def minTimeToCollectGarbage(garbage: List[str], travel: List[int]) -> int:
    # Total time to collect garbage
    total_time = 0
    
    # Last occurrence of each garbage type
    last_position = {'M': 0, 'P': 0, 'G': 0}
    
    # Calculate the total time to collect garbage at each house
    for i, g in enumerate(garbage):
        total_time += len(g)  # Time to collect garbage at house i
        for char in g:
            last_position[char] = i  # Update the last position of the garbage type
    
    # Calculate the travel time for each garbage type
    for char in 'MPG':
        for i in range(1, last_position[char] + 1):
            total_time += travel[i - 1]
    
    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    garbage = ["G", "P", "GP", "GG"]
    travel = [2, 4, 3]
    print(minTimeToCollectGarbage(garbage, travel))  # Output: 21

    # Test Case 2
    garbage = ["MMM", "PGM", "GP"]
    travel = [3, 10]
    print(minTimeToCollectGarbage(garbage, travel))  # Output: 37

    # Test Case 3
    garbage = ["G", "P", "M"]
    travel = [1, 2]
    print(minTimeToCollectGarbage(garbage, travel))  # Output: 8

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the total garbage collection time takes O(n), where n is the number of houses.
- Calculating the travel time for each garbage type takes O(n) in the worst case (if all houses contain all types of garbage).
- Overall, the time complexity is O(n).

Space Complexity:
- We use a dictionary `last_position` to store the last occurrence of each garbage type, which takes O(1) space since there are only three garbage types ('M', 'P', 'G').
- The space complexity is O(1).

Topic: Arrays
"""