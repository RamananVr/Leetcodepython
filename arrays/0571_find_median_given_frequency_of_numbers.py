"""
LeetCode Question #571: Find Median Given Frequency of Numbers

Problem Statement:
A frequency table is a list of numbers paired with their frequencies, such as [(1, 2), (2, 3), (3, 1)].
The frequency table represents the numbers and how many times they appear. For example, the table above
represents the numbers [1, 1, 2, 2, 2, 3].

Your task is to find the median of the numbers represented by the frequency table. The median is the middle
value in an ordered list of numbers. If the list has an even number of elements, the median is the average
of the two middle values.

Write a function `findMedian(freqTable: List[Tuple[int, int]]) -> float` that takes a frequency table as input
and returns the median of the numbers.

Constraints:
- The frequency table is guaranteed to represent at least one number.
- The numbers in the frequency table are distinct and sorted in ascending order.
- The frequencies are positive integers.

Example:
Input: freqTable = [(1, 2), (2, 3), (3, 1)]
Output: 2.0
Explanation: The numbers represented are [1, 1, 2, 2, 2, 3]. The median is 2.

Input: freqTable = [(1, 1), (2, 1), (3, 1), (4, 1)]
Output: 2.5
Explanation: The numbers represented are [1, 2, 3, 4]. The median is (2 + 3) / 2 = 2.5.
"""

from typing import List, Tuple

def findMedian(freqTable: List[Tuple[int, int]]) -> float:
    # Step 1: Calculate the total number of elements
    total_count = sum(freq for _, freq in freqTable)
    
    # Step 2: Determine the position(s) of the median
    if total_count % 2 == 1:
        median_pos = total_count // 2 + 1  # 1-based index for odd total
    else:
        median_pos = (total_count // 2, total_count // 2 + 1)  # 1-based indices for even total
    
    # Step 3: Traverse the frequency table to find the median
    current_count = 0
    median_values = []
    
    for num, freq in freqTable:
        current_count += freq
        if isinstance(median_pos, int):  # Odd total case
            if current_count >= median_pos:
                return float(num)
        else:  # Even total case
            if current_count >= median_pos[0] and len(median_values) == 0:
                median_values.append(num)
            if current_count >= median_pos[1]:
                median_values.append(num)
                return sum(median_values) / 2.0

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    freqTable1 = [(1, 2), (2, 3), (3, 1)]
    print(findMedian(freqTable1))  # Output: 2.0

    # Test Case 2
    freqTable2 = [(1, 1), (2, 1), (3, 1), (4, 1)]
    print(findMedian(freqTable2))  # Output: 2.5

    # Test Case 3
    freqTable3 = [(1, 5)]
    print(findMedian(freqTable3))  # Output: 1.0

    # Test Case 4
    freqTable4 = [(1, 1), (2, 2), (3, 2), (4, 1)]
    print(findMedian(freqTable4))  # Output: 2.5

"""
Time and Space Complexity Analysis:

Time Complexity:
- Calculating the total count takes O(n), where n is the number of entries in the frequency table.
- Traversing the frequency table to find the median takes O(n) in the worst case.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm uses a constant amount of extra space (no additional data structures are created).
- Overall space complexity: O(1).

Topic: Arrays
"""