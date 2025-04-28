"""
LeetCode Problem #2274: Maximum Consecutive Floors Without Special Floors

Problem Statement:
Alice manages a building with `n` floors numbered from `1` to `n`. She has decided to designate some floors as "special floors". 
A floor is special if it is listed in the array `special`. You are given two integers `bottom` and `top`, which denote the range 
of floors Alice is considering, and an integer array `special`, where `special[i]` represents a special floor.

Return the maximum number of consecutive floors without any special floors.

Example:
Input: bottom = 2, top = 9, special = [4, 6]
Output: 3
Explanation: The special floors are 4 and 6, so the floors without special floors are:
- Floors 2, 3 (2 consecutive floors)
- Floors 5 (1 consecutive floor)
- Floors 7, 8, 9 (3 consecutive floors)
The maximum number of consecutive floors is 3.

Constraints:
- 1 <= special.length <= 10^5
- 1 <= bottom <= special[i] <= top <= 10^9
- All the values of `special` are distinct.
"""

# Python Solution
def maxConsecutive(bottom: int, top: int, special: list[int]) -> int:
    """
    This function calculates the maximum number of consecutive floors without any special floors.
    """
    # Sort the special floors
    special.sort()
    
    # Initialize the maximum gap
    max_gap = 0
    
    # Check the gap before the first special floor
    max_gap = max(max_gap, special[0] - bottom)
    
    # Check the gaps between consecutive special floors
    for i in range(1, len(special)):
        max_gap = max(max_gap, special[i] - special[i - 1] - 1)
    
    # Check the gap after the last special floor
    max_gap = max(max_gap, top - special[-1])
    
    return max_gap

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    bottom = 2
    top = 9
    special = [4, 6]
    print(maxConsecutive(bottom, top, special))  # Output: 3

    # Test Case 2
    bottom = 1
    top = 10
    special = [2, 4, 6, 8]
    print(maxConsecutive(bottom, top, special))  # Output: 2

    # Test Case 3
    bottom = 5
    top = 15
    special = [7, 10, 12]
    print(maxConsecutive(bottom, top, special))  # Output: 4

    # Test Case 4
    bottom = 1
    top = 100
    special = [50]
    print(maxConsecutive(bottom, top, special))  # Output: 49

    # Test Case 5
    bottom = 1
    top = 1
    special = [1]
    print(maxConsecutive(bottom, top, special))  # Output: 0

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the `special` array takes O(k * log(k)), where k is the length of the `special` array.
- Iterating through the sorted `special` array to calculate gaps takes O(k).
- Overall time complexity: O(k * log(k)).

Space Complexity:
- The sorting operation is in-place, so no additional space is used apart from the input.
- Overall space complexity: O(1) (excluding input storage).
"""

# Topic: Arrays, Sorting