"""
LeetCode Problem #1279: Traffic Light Controlled Intersection

Problem Statement:
There is an intersection of two roads. First road is road A which goes from North to South. 
Second road is road B which goes from West to East.

There is a traffic light located on each road before the intersection. A traffic light can 
either be green or red.

- Green means cars can cross the intersection in both directions of the road.
- Red means cars in both directions cannot cross the intersection and must wait until the 
  light turns green.

The traffic lights cannot be green on both roads at the same time. That means when the 
light is green on road A, it is red on road B and vice versa.

Initially, the traffic light is green on road A and red on road B. When the light is green 
on one road, all cars can cross the intersection in both directions until the light turns 
red.

When a car arrives at the intersection, it must wait until the traffic light turns green 
on its road and both roads are clear to cross the intersection. A car can cross the 
intersection in 1 second.

You are given an array `cars` of `n` elements where `cars[i] = (arrTime[i], road[i])`:
- `arrTime[i]` is the arrival time of the ith car at the intersection.
- `road[i]` is the road that the ith car travels on and is either 'A' or 'B'.

The cars are sorted by their arrival time. Return an array `result` where `result[i]` is 
the time at which the ith car will pass through the intersection.

Constraints:
- 1 <= cars.length <= 10^4
- 0 <= arrTime[i] <= 10^6
- arrTime is non-decreasing.
- road[i] is either 'A' or 'B'.

"""

from collections import deque

def getCrossingTimes(cars):
    """
    Function to calculate the crossing times of cars at the intersection.

    Args:
    cars (List[Tuple[int, str]]): List of tuples where each tuple contains the arrival time
                                  and the road ('A' or 'B') of a car.

    Returns:
    List[int]: List of times at which each car crosses the intersection.
    """
    # Initialize variables
    result = [0] * len(cars)
    queue_A = deque()  # Queue for cars on road A
    queue_B = deque()  # Queue for cars on road B
    current_time = 0
    green_light = 'A'  # Initially, road A has the green light

    # Process each car
    for i, (arrTime, road) in enumerate(cars):
        # Add car to the appropriate queue
        if road == 'A':
            queue_A.append((i, arrTime))
        else:
            queue_B.append((i, arrTime))

        # Process cars in the queues
        while queue_A or queue_B:
            # If both queues are empty, break
            if not queue_A and not queue_B:
                break

            # Determine the next car to process
            if green_light == 'A' and queue_A:
                car_index, car_arrival = queue_A.popleft()
                result[car_index] = max(current_time, car_arrival)
                current_time = result[car_index] + 1
            elif green_light == 'B' and queue_B:
                car_index, car_arrival = queue_B.popleft()
                result[car_index] = max(current_time, car_arrival)
                current_time = result[car_index] + 1
            else:
                # Switch the green light
                green_light = 'B' if green_light == 'A' else 'A'

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cars = [(0, 'A'), (1, 'B'), (2, 'A'), (3, 'B')]
    print(getCrossingTimes(cars))  # Expected Output: [0, 1, 2, 3]

    # Test Case 2
    cars = [(0, 'A'), (0, 'B'), (1, 'A'), (1, 'B')]
    print(getCrossingTimes(cars))  # Expected Output: [0, 1, 2, 3]

    # Test Case 3
    cars = [(0, 'A'), (1, 'A'), (2, 'B'), (3, 'B')]
    print(getCrossingTimes(cars))  # Expected Output: [0, 1, 2, 3]

"""
Time Complexity:
- O(n): We iterate through the list of cars once and process each car in constant time.

Space Complexity:
- O(n): We use two queues to store cars waiting on road A and road B, which in the worst 
        case can store all cars.

Topic: Simulation, Queue
"""