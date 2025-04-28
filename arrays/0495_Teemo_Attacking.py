"""
LeetCode Problem #495: Teemo Attacking

Problem Statement:
Our hero Teemo is attacking an enemy Ashe with poison attacks! When Teemo attacks Ashe, 
Ashe gets poisoned for a certain duration. If Teemo attacks again before the poison effect 
ends, the timer for the poison effect resets, and the poison effect will end duration seconds 
after the new attack.

You are given a non-decreasing integer array `timeSeries`, where `timeSeries[i]` denotes the 
time Teemo attacks Ashe, and an integer `duration` denoting the duration of the poison effect.

Return the total time that Ashe is poisoned.

Example 1:
Input: timeSeries = [1, 4], duration = 2
Output: 4
Explanation: Teemo's attacks on Ashe go as follows:
- At time 1, Ashe is poisoned for 2 seconds.
- At time 4, Ashe is poisoned for another 2 seconds.
Thus, the total time Ashe is poisoned is 2 + 2 = 4.

Example 2:
Input: timeSeries = [1, 2], duration = 2
Output: 3
Explanation: Teemo's attacks on Ashe go as follows:
- At time 1, Ashe is poisoned for 2 seconds.
- At time 2, the poison effect resets, and Ashe is poisoned for an additional 2 seconds.
Thus, the total time Ashe is poisoned is 1 (from time 1 to time 2) + 2 (from time 2 to time 4) = 3.

Constraints:
- 1 <= timeSeries.length <= 10^4
- 0 <= timeSeries[i], duration <= 10^7
- timeSeries is sorted in non-decreasing order.
"""

def findPoisonedDuration(timeSeries, duration):
    """
    Calculate the total time Ashe is poisoned.

    :param timeSeries: List[int] - Times when Teemo attacks.
    :param duration: int - Duration of poison effect.
    :return: int - Total time Ashe is poisoned.
    """
    if not timeSeries:
        return 0

    total_time = 0

    for i in range(len(timeSeries) - 1):
        # Add the minimum of the duration or the gap between consecutive attacks
        total_time += min(duration, timeSeries[i + 1] - timeSeries[i])

    # Add the duration for the last attack
    total_time += duration

    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    timeSeries1 = [1, 4]
    duration1 = 2
    print(findPoisonedDuration(timeSeries1, duration1))  # Output: 4

    # Test Case 2
    timeSeries2 = [1, 2]
    duration2 = 2
    print(findPoisonedDuration(timeSeries2, duration2))  # Output: 3

    # Test Case 3
    timeSeries3 = [1, 3, 5, 7]
    duration3 = 2
    print(findPoisonedDuration(timeSeries3, duration3))  # Output: 8

    # Test Case 4
    timeSeries4 = []
    duration4 = 5
    print(findPoisonedDuration(timeSeries4, duration4))  # Output: 0

    # Test Case 5
    timeSeries5 = [1, 2, 3, 4, 5]
    duration5 = 5
    print(findPoisonedDuration(timeSeries5, duration5))  # Output: 9

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the `timeSeries` array once, performing constant-time operations 
  for each element. Thus, the time complexity is O(n), where n is the length of the `timeSeries` array.

Space Complexity:
- The function uses a constant amount of extra space, regardless of the input size. 
  Thus, the space complexity is O(1).

Topic: Arrays
"""