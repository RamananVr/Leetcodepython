"""
LeetCode Question #2007: Find Original Array From Doubled Array

Problem Statement:
An integer array `changed` is called a doubled array if it can be formed by taking an integer array `original` and appending twice the value of every element in `original`, in any order. 

Given an array `changed`, return the original array `original`. If `changed` cannot be a doubled array, return an empty array.

Example 1:
Input: changed = [1,3,4,2,6,8]
Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]. 
The resulting doubled array would be [1,3,4,2,6,8], which can be reordered to [1,3,4,2,6,8].

Example 2:
Input: changed = [6,3,0,1]
Output: []
Explanation: changed is not a doubled array.

Example 3:
Input: changed = [1]
Output: []
Explanation: changed cannot be a doubled array.

Constraints:
- 1 <= changed.length <= 10^5
- 0 <= changed[i] <= 10^5
"""

# Python Solution
from collections import Counter

def findOriginalArray(changed):
    if len(changed) % 2 != 0:
        return []
    
    changed.sort()
    count = Counter(changed)
    original = []
    
    for num in changed:
        if count[num] == 0:
            continue
        if count[num * 2] == 0:
            return []
        original.append(num)
        count[num] -= 1
        count[num * 2] -= 1
    
    return original

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    changed = [1, 3, 4, 2, 6, 8]
    print(findOriginalArray(changed))  # Output: [1, 3, 4]

    # Test Case 2
    changed = [6, 3, 0, 1]
    print(findOriginalArray(changed))  # Output: []

    # Test Case 3
    changed = [1]
    print(findOriginalArray(changed))  # Output: []

    # Test Case 4
    changed = [0, 0, 0, 0]
    print(findOriginalArray(changed))  # Output: [0, 0]

    # Test Case 5
    changed = [2, 4, 1, 8, 3, 6]
    print(findOriginalArray(changed))  # Output: [1, 3, 4]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the array takes O(n log n), where n is the length of the `changed` array.
- Iterating through the array and updating the Counter takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The Counter object uses O(n) space to store the frequency of elements.
- The `original` array uses O(n/2) space in the worst case (half the size of `changed`).
- Overall space complexity: O(n).

Topic: Arrays, Hash Table, Sorting
"""