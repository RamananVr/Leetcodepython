"""
LeetCode Problem #481: Magical String

Problem Statement:
A magical string S consists of only '1' and '2' and obeys the following rules:
- The string is constructed by concatenating a sequence of groups of '1's and '2's.
- The number of '1's or '2's in each group is determined by the sequence itself.

The first few elements of the magical string S are: "1221121221221121122...".
The first group is "1", the second group is "22", the third group is "11", the fourth group is "2", and so on.
The groups alternate between '1' and '2', and the number of elements in each group is determined by the sequence itself.

Given an integer n, return the number of '1's in the first n elements of the magical string.

Example:
Input: n = 6
Output: 3
Explanation: The first 6 elements of the magical string are "122112". There are 3 '1's in it.

Constraints:
- 1 <= n <= 10^5
"""

def magicalString(n: int) -> int:
    if n == 0:
        return 0
    if n <= 3:
        return 1  # The first three elements are "122", which contains one '1'.

    # Initialize the magical string and pointers
    magical = [1, 2, 2]
    pointer = 2  # Points to the current group size in the magical string
    current_num = 1  # The next number to append (alternates between 1 and 2)

    # Generate the magical string until its length reaches n
    while len(magical) < n:
        group_size = magical[pointer]
        magical.extend([current_num] * group_size)
        current_num = 3 - current_num  # Toggle between 1 and 2
        pointer += 1

    # Count the number of '1's in the first n elements
    return magical[:n].count(1)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 6
    print(magicalString(n))  # Output: 3

    # Test Case 2
    n = 10
    print(magicalString(n))  # Output: 5

    # Test Case 3
    n = 1
    print(magicalString(n))  # Output: 1

    # Test Case 4
    n = 15
    print(magicalString(n))  # Output: 7

"""
Time and Space Complexity Analysis:

Time Complexity:
- The while loop runs until the length of the magical string reaches n.
- Each iteration appends a group of size determined by the magical string itself.
- In the worst case, the loop runs approximately O(n) times, and appending elements takes O(1) per operation.
- Thus, the overall time complexity is O(n).

Space Complexity:
- The magical string is stored in a list, which grows to size n.
- Thus, the space complexity is O(n).

Topic: String Construction
"""