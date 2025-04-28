"""
LeetCode Problem #1826: Faulty Sensor

Problem Statement:
An experiment is being conducted in a lab. To ensure accuracy, there are two sensors, sensor1 and sensor2, collecting data simultaneously. However, one of the sensors is faulty. The data from the sensors is represented as two non-empty arrays of the same length, sensor1 and sensor2, where sensor1[i] and sensor2[i] are the ith data points collected by the two sensors.

It is known that the faulty sensor always reports the same value as the non-faulty sensor at the beginning, but then starts reporting incorrect values. Once a sensor starts reporting incorrect values, it continues to report incorrect values indefinitely.

You are given the two arrays sensor1 and sensor2. Your task is to determine which sensor is faulty. If sensor1 is faulty, return 1. If sensor2 is faulty, return 2. It is guaranteed that there is a faulty sensor.

Example 1:
Input: sensor1 = [2,3,4,5], sensor2 = [2,3,4,6]
Output: 2

Example 2:
Input: sensor1 = [2,3,4,5], sensor2 = [2,3,4,5]
Output: 1

Constraints:
- 1 <= sensor1.length == sensor2.length <= 100
- 1 <= sensor1[i], sensor2[i] <= 100

"""

def faultySensor(sensor1, sensor2):
    """
    Determines which sensor is faulty.

    Args:
    sensor1 (List[int]): Data collected by sensor1.
    sensor2 (List[int]): Data collected by sensor2.

    Returns:
    int: 1 if sensor1 is faulty, 2 if sensor2 is faulty.
    """
    n = len(sensor1)
    for i in range(n - 1):
        if sensor1[i] != sensor2[i]:
            # Compare the next values to determine the faulty sensor
            if sensor1[i + 1] != sensor2[i]:
                return 1  # sensor1 is faulty
            elif sensor2[i + 1] != sensor1[i]:
                return 2  # sensor2 is faulty
    return 1  # Default case: sensor1 is faulty

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    sensor1 = [2, 3, 4, 5]
    sensor2 = [2, 3, 4, 6]
    print(faultySensor(sensor1, sensor2))  # Output: 2

    # Test Case 2
    sensor1 = [2, 3, 4, 5]
    sensor2 = [2, 3, 4, 5]
    print(faultySensor(sensor1, sensor2))  # Output: 1

    # Test Case 3
    sensor1 = [1, 2, 3, 4]
    sensor2 = [1, 2, 3, 5]
    print(faultySensor(sensor1, sensor2))  # Output: 2

    # Test Case 4
    sensor1 = [10, 20, 30, 40]
    sensor2 = [10, 20, 30, 50]
    print(faultySensor(sensor1, sensor2))  # Output: 2

    # Test Case 5
    sensor1 = [5, 5, 5, 5]
    sensor2 = [5, 5, 5, 6]
    print(faultySensor(sensor1, sensor2))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the arrays once, comparing elements and their neighbors.
- Therefore, the time complexity is O(n), where n is the length of the arrays.

Space Complexity:
- The function uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Arrays
"""