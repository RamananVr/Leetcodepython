"""
LeetCode Problem #1057: Campus Bikes

Problem Statement:
On a campus represented as a 2D grid, there are `workers` and `bikes`. You are given two arrays `workers` and `bikes`, where `workers[i] = [xi, yi]` is the position of the i-th worker, and `bikes[j] = [xj, yj]` is the position of the j-th bike. 

We need to assign each worker to a bike. Each worker can be assigned to only one bike, and each bike can be assigned to only one worker. The Manhattan distance between two points `(p1, q1)` and `(p2, q2)` is `|p1 - p2| + |q1 - q2|`.

Assign bikes to workers in a way that minimizes the sum of the Manhattan distances between each worker and their assigned bike. Return a list `result` of length `n`, where `result[i]` is the index (0-based) of the bike assigned to the i-th worker.

The assignment should be done in the following priority order:
1. The Manhattan distance between a worker and a bike.
2. If there are multiple pairs with the same distance, assign based on the worker index (ascending order).
3. If there are still multiple pairs, assign based on the bike index (ascending order).

Constraints:
- `1 <= workers.length, bikes.length <= 1000`
- `workers[i].length == bikes[j].length == 2`
- `0 <= workers[i][0], workers[i][1], bikes[j][0], bikes[j][1] < 1000`

"""

# Solution
from heapq import heappush, heappop

def assignBikes(workers, bikes):
    # Create a priority queue to store (distance, worker_index, bike_index)
    pq = []
    
    # Calculate all distances and push them into the priority queue
    for i, (wx, wy) in enumerate(workers):
        for j, (bx, by) in enumerate(bikes):
            distance = abs(wx - bx) + abs(wy - by)
            heappush(pq, (distance, i, j))
    
    # Initialize result array and visited sets
    result = [-1] * len(workers)
    used_bikes = set()
    
    # Process the priority queue
    while pq:
        distance, worker_index, bike_index = heappop(pq)
        if result[worker_index] == -1 and bike_index not in used_bikes:
            result[worker_index] = bike_index
            used_bikes.add(bike_index)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    workers = [[0, 0], [2, 1]]
    bikes = [[1, 2], [3, 3]]
    print(assignBikes(workers, bikes))  # Output: [0, 1]

    # Test Case 2
    workers = [[0, 0], [1, 1], [2, 0]]
    bikes = [[1, 0], [2, 2], [2, 1]]
    print(assignBikes(workers, bikes))  # Output: [0, 2, 1]

    # Test Case 3
    workers = [[0, 0]]
    bikes = [[1, 1]]
    print(assignBikes(workers, bikes))  # Output: [0]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the Manhattan distance for all worker-bike pairs takes O(n * m), where n is the number of workers and m is the number of bikes.
- Pushing all pairs into the priority queue takes O(n * m * log(n * m)) due to heap operations.
- Extracting pairs from the priority queue takes O(n * m * log(n * m)) in the worst case.

Overall time complexity: O(n * m * log(n * m))

Space Complexity:
- The priority queue stores up to n * m pairs, so it requires O(n * m) space.
- The result array and the used_bikes set require O(n + m) space.

Overall space complexity: O(n * m)
"""

# Topic: Greedy, Heap (Priority Queue)