"""
LeetCode Problem #2298: Minimum Amount of Time to Collect Garbage

Problem Statement:
You are given a 0-indexed array of strings `garbage` where `garbage[i]` represents the types of garbage at the ith house. 
`garbage[i]` consists only of the characters 'M', 'P', and 'G' representing one unit of metal, paper, and glass garbage, respectively. 
Picking up one unit of any type of garbage takes 1 minute.

You are also given a 0-indexed integer array `travel` where `travel[i]` is the number of minutes needed to travel between the 
ith house and the (i + 1)th house.

There are three garbage trucks in the city, each responsible for picking up one type of garbage. Each garbage truck starts at house 0. 
You need to pick up all the garbage at every house and return the minimum number of minutes needed to pick up all the garbage.

Constraints:
- `2 <= garbage.length <= 10^5`
- `garbage[i].length <= 10`
- `1 <= travel.length == garbage.length - 1 <= 10^5`
- `travel[i]` is a positive integer
- `garbage[i]` consists of only the letters 'M', 'P', and 'G'.

Example:
Input: garbage = ["G", "P", "GP", "GG"], travel = [2, 4, 3]
Output: 21
Explanation:
- The metal truck takes 8 minutes to pick up all the metal garbage.
- The paper truck takes 7 minutes to pick up all the paper garbage.
- The glass truck takes 6 minutes to pick up all the glass garbage.
- Total time = 8 + 7 + 6 = 21 minutes.

Your task is to implement a function that calculates the minimum time required to collect all the garbage.
"""

def minTimeToCollectGarbage(garbage, travel):
    # Total time to collect garbage
    total_time = 0
    
    # Last seen indices for each type of garbage
    last_seen = {'M': 0, 'P': 0, 'G': 0}
    
    # Calculate the total garbage collection time
    for i, g in enumerate(garbage):
        # Add the time to pick up garbage at the current house
        total_time += len(g)
        
        # Update the last seen index for each type of garbage
        for char in g:
            last_seen[char] = i
    
    # Add the travel time for each garbage type
    for char in 'MPG':
        for i in range(1, last_seen[char] + 1):
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
    garbage = ["P", "P", "P", "P"]
    travel = [1, 1, 1]
    print(minTimeToCollectGarbage(garbage, travel))  # Output: 7

    # Test Case 4
    garbage = ["G", "M", "P"]
    travel = [5, 5]
    print(minTimeToCollectGarbage(garbage, travel))  # Output: 15

"""
Time Complexity:
- Let n = len(garbage) and m = sum(len(garbage[i]) for all i).
- Iterating through the garbage array takes O(n).
- Calculating the total garbage collection time involves iterating through each character in garbage, which takes O(m).
- Adding the travel time for each garbage type takes O(n).
- Overall time complexity: O(n + m).

Space Complexity:
- The space used is O(1) since we only use a fixed amount of extra space for variables.

Topic: Arrays
"""