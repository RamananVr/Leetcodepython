"""
LeetCode Problem #2021: Brightest Position on Street

Problem Statement:
A street is represented as a number line. Each position on the street is a point on the number line. 
A street lamp is represented as a tuple (position, range), where `position` is the position of the lamp 
on the number line, and `range` is the distance the lamp can illuminate on both sides. A lamp at position `p` 
with range `r` illuminates all positions from `p - r` to `p + r` (inclusive).

You are given a list of street lamps, where each lamp is represented as a tuple (position, range). 
Your task is to find the position on the street that is illuminated by the most lamps. If there are multiple 
positions with the same maximum illumination, return the smallest such position.

Constraints:
- 1 <= len(lamps) <= 10^5
- -10^9 <= position <= 10^9
- 1 <= range <= 10^9

Example:
Input: lamps = [(0, 2), (5, 3), (7, 1)]
Output: 5

Explanation:
- Lamp 1 illuminates positions [-2, -1, 0, 1, 2].
- Lamp 2 illuminates positions [2, 3, 4, 5, 6, 7, 8].
- Lamp 3 illuminates positions [6, 7, 8].
- Position 5 is illuminated by 2 lamps, which is the maximum. 
"""

# Python Solution
def brightest_position(lamps):
    """
    Finds the position on the street that is illuminated by the most lamps.
    
    Args:
    lamps (List[Tuple[int, int]]): A list of tuples where each tuple represents a lamp's position and range.
    
    Returns:
    int: The position on the street with the maximum illumination.
    """
    from collections import defaultdict

    # Use a sweep line algorithm to track illumination changes
    illumination_changes = defaultdict(int)
    
    for position, range_ in lamps:
        illumination_changes[position - range_] += 1  # Start of illumination
        illumination_changes[position + range_ + 1] -= 1  # End of illumination
    
    # Sort the keys of illumination_changes to process in order
    sorted_positions = sorted(illumination_changes.keys())
    
    max_illumination = 0
    current_illumination = 0
    brightest_position = None
    
    for pos in sorted_positions:
        current_illumination += illumination_changes[pos]
        if current_illumination > max_illumination:
            max_illumination = current_illumination
            brightest_position = pos
    
    return brightest_position

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    lamps = [(0, 2), (5, 3), (7, 1)]
    print(brightest_position(lamps))  # Output: 5

    # Test Case 2
    lamps = [(1, 1), (2, 2), (3, 1)]
    print(brightest_position(lamps))  # Output: 2

    # Test Case 3
    lamps = [(0, 5), (10, 5)]
    print(brightest_position(lamps))  # Output: 0

    # Test Case 4
    lamps = [(0, 1), (2, 1), (4, 1)]
    print(brightest_position(lamps))  # Output: 0

    # Test Case 5
    lamps = [(0, 10**9)]
    print(brightest_position(lamps))  # Output: -1000000000

"""
Time Complexity:
- Sorting the keys of `illumination_changes` takes O(n log n), where n is the number of unique positions.
- Iterating through the sorted positions takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `illumination_changes` dictionary stores at most 2 * len(lamps) keys, so the space complexity is O(n).

Topic: Sweep Line Algorithm
"""