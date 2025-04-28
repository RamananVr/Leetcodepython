"""
LeetCode Question #1229: Meeting Scheduler

Problem Statement:
Given the availability time slots arrays `slots1` and `slots2` of two people and a meeting duration `duration`, 
return the earliest time slot that works for both of them and is of duration `duration`.

If there is no common time slot that satisfies the condition, return an empty array.

The input arrays are sorted by the start time.

Example 1:
Input: slots1 = [[10, 50], [60, 120], [140, 210]], slots2 = [[0, 15], [60, 70]], duration = 8
Output: [60, 68]

Example 2:
Input: slots1 = [[10, 50]], slots2 = [[60, 120], [140, 210]], duration = 8
Output: []

Constraints:
- 1 <= slots1.length, slots2.length <= 10^4
- slots1[i].length, slots2[i].length == 2
- slots2[i][0] < slots2[i][1]
- 0 <= slots1[i][0], slots1[i][1] <= 10^9
- 1 <= duration <= 10^6
"""

# Python Solution
from typing import List

def minAvailableDuration(slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
    # Sort both slots by their start times
    slots1.sort()
    slots2.sort()
    
    # Use two pointers to iterate through both lists
    i, j = 0, 0
    while i < len(slots1) and j < len(slots2):
        # Find the intersection of the current slots
        start = max(slots1[i][0], slots2[j][0])
        end = min(slots1[i][1], slots2[j][1])
        
        # Check if the intersection is at least `duration` long
        if end - start >= duration:
            return [start, start + duration]
        
        # Move the pointer for the slot that ends earlier
        if slots1[i][1] < slots2[j][1]:
            i += 1
        else:
            j += 1
    
    # If no valid slot is found, return an empty array
    return []

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    slots1 = [[10, 50], [60, 120], [140, 210]]
    slots2 = [[0, 15], [60, 70]]
    duration = 8
    print(minAvailableDuration(slots1, slots2, duration))  # Output: [60, 68]

    # Test Case 2
    slots1 = [[10, 50]]
    slots2 = [[60, 120], [140, 210]]
    duration = 8
    print(minAvailableDuration(slots1, slots2, duration))  # Output: []

    # Test Case 3
    slots1 = [[10, 20], [30, 40]]
    slots2 = [[15, 25], [35, 45]]
    duration = 5
    print(minAvailableDuration(slots1, slots2, duration))  # Output: [15, 20]

    # Test Case 4
    slots1 = [[10, 15], [20, 25]]
    slots2 = [[12, 18], [22, 28]]
    duration = 3
    print(minAvailableDuration(slots1, slots2, duration))  # Output: [12, 15]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting both `slots1` and `slots2` takes O(n log n + m log m), where n and m are the lengths of the two lists.
- The two-pointer traversal takes O(n + m) since we iterate through both lists once.
- Overall time complexity: O(n log n + m log m).

Space Complexity:
- Sorting is done in-place, and no additional data structures are used.
- Space complexity: O(1).
"""

# Topic: Arrays, Two Pointers