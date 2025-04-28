"""
LeetCode Question #1750: Minimum Length of String After Deleting Similar Ends

Problem Statement:
Given a string `s`, consisting only of characters 'a', 'b', and 'c', you can perform the following operation any number of times:
- Choose a non-empty prefix and a non-empty suffix of the string that consist of the same character and delete them.

Return the minimum length of the string that can be achieved after performing the above operation any number of times.

Example:
Input: s = "cabaabac"
Output: 0
Explanation: Remove the prefix "c" and suffix "c", then remove the prefix "a" and suffix "a", then remove the prefix "b" and suffix "b".

Input: s = "aabccabba"
Output: 3
Explanation: Remove the prefix "a" and suffix "a", then remove the prefix "a" and suffix "a", leaving "bccab".

Constraints:
- 1 <= s.length <= 10^5
- s consists of only characters 'a', 'b', and 'c'.
"""

# Python Solution
def minimumLength(s: str) -> int:
    left, right = 0, len(s) - 1
    
    while left < right and s[left] == s[right]:
        char = s[left]
        while left <= right and s[left] == char:
            left += 1
        while left <= right and s[right] == char:
            right -= 1
    
    return right - left + 1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cabaabac"
    print(minimumLength(s1))  # Output: 0

    # Test Case 2
    s2 = "aabccabba"
    print(minimumLength(s2))  # Output: 3

    # Test Case 3
    s3 = "abc"
    print(minimumLength(s3))  # Output: 3

    # Test Case 4
    s4 = "aaaa"
    print(minimumLength(s4))  # Output: 0

    # Test Case 5
    s5 = "abccba"
    print(minimumLength(s5))  # Output: 0

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses two pointers (`left` and `right`) to traverse the string. In the worst case, each pointer moves across the entire string once.
- Therefore, the time complexity is O(n), where n is the length of the string.

Space Complexity:
- The algorithm uses a constant amount of extra space (no additional data structures are used).
- Therefore, the space complexity is O(1).

Topic: Two Pointers
"""