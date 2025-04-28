"""
LeetCode Problem #1732: Find the Highest Altitude

Problem Statement:
There is a biker going on a road trip. The road trip consists of `n + 1` points at different altitudes. 
The biker starts his trip on point 0 with altitude equal to 0.

You are given an integer array `gain` of length `n` where `gain[i]` is the net gain in altitude between 
points `i` and `i + 1` for all (0 <= i < n). Return the highest altitude of a point.

Example 1:
Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0, -5, -4, 1, 1, -6]. The highest is 1.

Example 2:
Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0, -4, -7, -9, -10, -6, -3, -1]. The highest is 0.

Constraints:
- n == gain.length
- 1 <= n <= 100
- -100 <= gain[i] <= 100
"""

# Python Solution
def largestAltitude(gain):
    """
    Function to find the highest altitude during the trip.

    :param gain: List[int] - List of net altitude gains between consecutive points.
    :return: int - The highest altitude reached.
    """
    current_altitude = 0
    max_altitude = 0

    for g in gain:
        current_altitude += g
        max_altitude = max(max_altitude, current_altitude)

    return max_altitude

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    gain1 = [-5, 1, 5, 0, -7]
    print("Test Case 1 Output:", largestAltitude(gain1))  # Expected Output: 1

    # Test Case 2
    gain2 = [-4, -3, -2, -1, 4, 3, 2]
    print("Test Case 2 Output:", largestAltitude(gain2))  # Expected Output: 0

    # Test Case 3
    gain3 = [1, 2, 3, 4, 5]
    print("Test Case 3 Output:", largestAltitude(gain3))  # Expected Output: 15

    # Test Case 4
    gain4 = [-1, -2, -3, -4, -5]
    print("Test Case 4 Output:", largestAltitude(gain4))  # Expected Output: 0

    # Test Case 5
    gain5 = [0, 0, 0, 0]
    print("Test Case 5 Output:", largestAltitude(gain5))  # Expected Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `gain` list once, performing O(1) operations for each element.
- Therefore, the time complexity is O(n), where n is the length of the `gain` list.

Space Complexity:
- The function uses a constant amount of extra space for variables `current_altitude` and `max_altitude`.
- Therefore, the space complexity is O(1).
"""

# Topic: Arrays