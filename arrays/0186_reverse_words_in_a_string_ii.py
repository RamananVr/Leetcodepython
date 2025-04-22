"""
LeetCode Question #186: Reverse Words in a String II

Problem Statement:
Given a character array `s`, reverse the order of the words. A word is defined as a sequence of non-space characters. 
The words in `s` will be separated by a single space. Your task is to modify the input array in-place.

Example:
Input: s = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
Output: ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

Constraints:
- The input string does not contain leading or trailing spaces.
- The words are always separated by a single space.
- The input string contains only printable ASCII characters.

You must solve the problem in-place, without allocating extra space for another array.
"""

def reverseWords(s):
    """
    Reverse the words in the input character array in-place.

    :param s: List[str] - The input character array
    :return: None - The input array is modified in-place
    """
    def reverse(start, end):
        """Helper function to reverse a portion of the array."""
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    # Step 1: Reverse the entire array
    reverse(0, len(s) - 1)

    # Step 2: Reverse each word in the array
    start = 0
    for i in range(len(s)):
        if s[i] == ' ' or i == len(s) - 1:
            end = i - 1 if s[i] == ' ' else i
            reverse(start, end)
            start = i + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = ['t', 'h', 'e', ' ', 's', 'k', 'y', ' ', 'i', 's', ' ', 'b', 'l', 'u', 'e']
    reverseWords(s1)
    print(s1)  # Expected Output: ['b', 'l', 'u', 'e', ' ', 'i', 's', ' ', 's', 'k', 'y', ' ', 't', 'h', 'e']

    # Test Case 2
    s2 = ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    reverseWords(s2)
    print(s2)  # Expected Output: ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'e', 'l', 'l', 'o']

    # Test Case 3
    s3 = ['a', ' ', 'b', ' ', 'c']
    reverseWords(s3)
    print(s3)  # Expected Output: ['c', ' ', 'b', ' ', 'a']

"""
Time and Space Complexity Analysis:

Time Complexity:
- Reversing the entire array takes O(n), where n is the length of the array.
- Reversing each word takes O(n) in total since every character is visited once.
- Overall time complexity: O(n).

Space Complexity:
- The algorithm operates in-place, so no additional space is used.
- Overall space complexity: O(1).

Topic: Arrays
"""