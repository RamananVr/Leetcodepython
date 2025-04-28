"""
LeetCode Problem #2094: Finding 3-Digit Even Numbers

Problem Statement:
You are given an integer array `digits`, where each element is a digit (0-9). You need to find all the unique 3-digit even numbers that can be formed using the digits in the array. Each digit from the array can only be used once in each number.

Return the sorted array of all unique 3-digit even numbers.

Constraints:
1. 3 <= digits.length <= 100
2. 0 <= digits[i] <= 9

Example:
Input: digits = [2, 1, 3, 0]
Output: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]
Explanation: All the possible 3-digit even numbers are:
102, 120, 130, 132, 210, 230, 302, 310, 312, 320. Notice that there are no repeated numbers or leading zeros.

Input: digits = [2, 2, 8, 8, 2]
Output: [222, 228, 282, 288, 822, 828, 882]
Explanation: The same digit can be used only once in each number. In this case, the valid numbers are 222, 228, 282, 288, 822, 828, and 882.

Input: digits = [3, 7, 5]
Output: []
Explanation: No even numbers can be formed since there are no even digits.
"""

from itertools import permutations

def findEvenNumbers(digits):
    """
    Finds all unique 3-digit even numbers that can be formed using the digits in the array.

    :param digits: List[int] - List of digits (0-9)
    :return: List[int] - Sorted list of unique 3-digit even numbers
    """
    # Use a set to store unique 3-digit even numbers
    result = set()

    # Generate all permutations of length 3
    for perm in permutations(digits, 3):
        # Form the number from the permutation
        num = perm[0] * 100 + perm[1] * 10 + perm[2]

        # Check if the number is a valid 3-digit even number
        if perm[0] != 0 and num % 2 == 0:
            result.add(num)

    # Return the sorted list of unique numbers
    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    digits1 = [2, 1, 3, 0]
    print(findEvenNumbers(digits1))  # Output: [102, 120, 130, 132, 210, 230, 302, 310, 312, 320]

    # Test Case 2
    digits2 = [2, 2, 8, 8, 2]
    print(findEvenNumbers(digits2))  # Output: [222, 228, 282, 288, 822, 828, 882]

    # Test Case 3
    digits3 = [3, 7, 5]
    print(findEvenNumbers(digits3))  # Output: []

    # Test Case 4
    digits4 = [0, 0, 2, 8]
    print(findEvenNumbers(digits4))  # Output: [200, 208, 280, 800, 808]

    # Test Case 5
    digits5 = [1, 4, 6, 0]
    print(findEvenNumbers(digits5))  # Output: [104, 106, 140, 146, 160, 164, 401, 406, 410, 416, 460, 461, 601, 604, 610, 614, 640, 641]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Generating all permutations of length 3 from the digits array takes O(n^3) time, where n is the length of the digits array.
   - Checking each permutation for validity and adding it to the set takes O(1) per permutation.
   - Sorting the final result takes O(k log k), where k is the number of valid 3-digit even numbers.
   - Overall time complexity: O(n^3 + k log k).

2. Space Complexity:
   - The space required for storing the set of unique numbers is O(k), where k is the number of valid 3-digit even numbers.
   - The space required for generating permutations is O(n).
   - Overall space complexity: O(n + k).

Topic: Arrays, Permutations
"""