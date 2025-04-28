"""
LeetCode Problem #1344: Angle Between Hands of a Clock

Problem Statement:
Given two numbers, `hour` and `minutes`, return the smaller angle (in degrees) formed between the hour and the minute hand.

Constraints:
1. 1 <= hour <= 12
2. 0 <= minutes <= 59
3. Answers within 10^-5 of the actual value will be accepted as correct.

Example:
Input: hour = 12, minutes = 30
Output: 165

Input: hour = 3, minutes = 15
Output: 7.5

Input: hour = 4, minutes = 50
Output: 155

Note:
- The hour hand moves as the minutes pass. For example, at 12:30, the hour hand is not exactly at 12 but slightly past it.
- The minute hand moves 6 degrees per minute (360 degrees / 60 minutes).
- The hour hand moves 0.5 degrees per minute (30 degrees per hour / 60 minutes).
"""

def angleClock(hour: int, minutes: int) -> float:
    """
    Calculate the smaller angle between the hour and minute hands of a clock.

    :param hour: int - The current hour (1 to 12).
    :param minutes: int - The current minutes (0 to 59).
    :return: float - The smaller angle between the two hands in degrees.
    """
    # Calculate the positions of the hour and minute hands in degrees
    minute_angle = minutes * 6  # Each minute represents 6 degrees
    hour_angle = (hour % 12) * 30 + (minutes * 0.5)  # Each hour represents 30 degrees, plus the effect of minutes

    # Calculate the absolute difference between the two angles
    angle = abs(hour_angle - minute_angle)

    # Return the smaller angle (either `angle` or `360 - angle`)
    return min(angle, 360 - angle)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    hour = 12
    minutes = 30
    print(f"Input: hour = {hour}, minutes = {minutes} -> Output: {angleClock(hour, minutes)}")  # Expected: 165

    # Test Case 2
    hour = 3
    minutes = 15
    print(f"Input: hour = {hour}, minutes = {minutes} -> Output: {angleClock(hour, minutes)}")  # Expected: 7.5

    # Test Case 3
    hour = 4
    minutes = 50
    print(f"Input: hour = {hour}, minutes = {minutes} -> Output: {angleClock(hour, minutes)}")  # Expected: 155

    # Test Case 4
    hour = 6
    minutes = 0
    print(f"Input: hour = {hour}, minutes = {minutes} -> Output: {angleClock(hour, minutes)}")  # Expected: 180

    # Test Case 5
    hour = 1
    minutes = 57
    print(f"Input: hour = {hour}, minutes = {minutes} -> Output: {angleClock(hour, minutes)}")  # Expected: 76.5

"""
Time Complexity Analysis:
- Calculating the angles for the hour and minute hands involves constant time operations.
- The absolute difference and minimum calculation are also constant time operations.
- Therefore, the overall time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of extra space for variables.
- Therefore, the overall space complexity is O(1).

Topic: Math
"""