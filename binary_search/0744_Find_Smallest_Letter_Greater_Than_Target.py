"""
LeetCode Problem #744: Find Smallest Letter Greater Than Target

Problem Statement:
You are given an array of characters `letters` that is sorted in non-decreasing order, and a character `target`. 
There are at least two different characters in `letters`.

Return the smallest character in the array that is strictly greater than `target`.

Note:
- The letters wrap around. For example, if `target == 'z'` and `letters == ['a', 'b'],` the answer is `'a'`.

Constraints:
- 2 <= letters.length <= 10^4
- letters[i] is a lowercase English letter.
- `target` is a lowercase English letter.

Example:
Input: letters = ["c", "f", "j"], target = "a"
Output: "c"

Input: letters = ["c", "f", "j"], target = "c"
Output: "f"

Input: letters = ["c", "f", "j"], target = "d"
Output: "f"
"""

# Solution
def nextGreatestLetter(letters, target):
    """
    Finds the smallest letter in the sorted array `letters` that is strictly greater than `target`.

    :param letters: List[str] - A sorted list of lowercase English letters.
    :param target: str - A lowercase English letter.
    :return: str - The smallest letter greater than `target`.
    """
    # Binary search approach
    left, right = 0, len(letters) - 1
    while left <= right:
        mid = (left + right) // 2
        if letters[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    # If no letter is strictly greater than target, wrap around to the first letter
    return letters[left % len(letters)]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    letters = ["c", "f", "j"]
    target = "a"
    print(nextGreatestLetter(letters, target))  # Output: "c"

    # Test Case 2
    letters = ["c", "f", "j"]
    target = "c"
    print(nextGreatestLetter(letters, target))  # Output: "f"

    # Test Case 3
    letters = ["c", "f", "j"]
    target = "d"
    print(nextGreatestLetter(letters, target))  # Output: "f"

    # Test Case 4
    letters = ["a", "b"]
    target = "z"
    print(nextGreatestLetter(letters, target))  # Output: "a"

    # Test Case 5
    letters = ["e", "e", "e", "k", "q", "q"]
    target = "e"
    print(nextGreatestLetter(letters, target))  # Output: "k"

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses binary search, which operates in O(log n) time, where n is the length of the `letters` array.

Space Complexity:
- The solution uses O(1) additional space since no extra data structures are used.

Topic: Binary Search
"""