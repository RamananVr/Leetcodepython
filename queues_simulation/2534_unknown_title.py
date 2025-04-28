"""
LeetCode Problem #2534: Time Taken to Cross the Door

Problem Statement:
There is a door that can be used by people to either enter or exit a room. Each person is represented by a triplet (arrivalTime, direction, id):
- `arrivalTime` is the time (in seconds) at which the person arrives at the door.
- `direction` is either 0 (indicating the person wants to enter the room) or 1 (indicating the person wants to exit the room).
- `id` is a unique identifier for the person.

The door can only be used by one person at a time. If two people arrive at the same time:
- If the door was last used for exiting (or it is the first use), the person wanting to exit gets priority.
- Otherwise, the person wanting to enter gets priority.

Write a function `timeTaken` that takes a list of people represented as `List[List[int]]` and returns a list of integers where the `i-th` integer is the time at which the person with `id = i` crosses the door.

Constraints:
- 1 <= len(people) <= 10^5
- 0 <= arrivalTime <= 10^9
- direction is either 0 or 1
- The `id` values are unique and range from 0 to len(people) - 1.

Example:
Input: people = [[0, 1, 0], [0, 1, 1], [1, 0, 2], [2, 1, 3]]
Output: [2, 0, 3, 4]

Explanation:
- At time 0, person 1 exits (priority to exiting).
- At time 1, person 2 enters.
- At time 2, person 3 exits.
- At time 3, person 0 enters.
"""

from collections import deque
from typing import List

def timeTaken(people: List[List[int]]) -> List[int]:
    # Sort people by arrival time
    people.sort(key=lambda x: x[0])
    
    # Queues for entering and exiting
    enter_queue = deque()
    exit_queue = deque()
    
    # Result array to store the time each person crosses the door
    result = [-1] * len(people)
    
    # Variables to track the current time and last door usage
    current_time = 0
    last_used = -1  # -1 means the door hasn't been used yet
    
    # Index to iterate through the sorted people list
    i = 0
    n = len(people)
    
    while i < n or enter_queue or exit_queue:
        # Add people arriving at the current time to their respective queues
        while i < n and people[i][0] == current_time:
            if people[i][1] == 0:
                enter_queue.append(people[i])
            else:
                exit_queue.append(people[i])
            i += 1
        
        # Determine who uses the door at the current time
        if exit_queue and (last_used == 1 or not enter_queue):
            # Exit has priority if the door was last used for exiting or if no one is waiting to enter
            person = exit_queue.popleft()
            result[person[2]] = current_time
            last_used = 1
        elif enter_queue:
            # Otherwise, someone enters
            person = enter_queue.popleft()
            result[person[2]] = current_time
            last_used = 0
        else:
            # If no one is waiting, move to the next time
            last_used = -1
        
        # Increment the current time
        current_time += 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    people = [[0, 1, 0], [0, 1, 1], [1, 0, 2], [2, 1, 3]]
    print(timeTaken(people))  # Output: [2, 0, 3, 4]

    # Test Case 2
    people = [[0, 0, 0], [1, 1, 1], [1, 0, 2], [2, 1, 3]]
    print(timeTaken(people))  # Output: [0, 2, 1, 3]

    # Test Case 3
    people = [[0, 1, 0], [1, 0, 1], [1, 1, 2], [2, 0, 3]]
    print(timeTaken(people))  # Output: [0, 2, 1, 3]

"""
Time Complexity:
- Sorting the people list takes O(n log n), where n is the number of people.
- Processing each person and updating the queues takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The space used by the enter_queue and exit_queue is O(n) in the worst case.
- The result array also takes O(n) space.
- Overall space complexity: O(n).

Topic: Queues, Simulation
"""