"""
LeetCode Problem #2159: Order Two Strings to Make Equal

Problem Statement:
You are given two strings s1 and s2, both of the same length. A string swap is an operation where you choose two indices i and j (0-indexed) in a string and swap the characters at s1[i] and s1[j]. Return true if it is possible to make s1 equal to s2 by performing at most one string swap on s1, or false otherwise.

Constraints:
- s1.length == s2.length
- 1 <= s1.length <= 100
- s1 and s2 consist of only lowercase English letters.
"""

def areAlmostEqual(s1: str, s2: str) -> bool:
    """
    Determines if two strings can be made equal by performing at most one swap on s1.

    :param s1: First string
    :param s2: Second string
    :return: True if s1 can be made equal to s2 with at most one swap, False otherwise
    """
    # If the strings are already equal, no swap is needed
    if s1 == s2:
        return True

    # Find the indices where the characters differ
    diff_indices = [i for i in range(len(s1)) if s1[i] != s2[i]]

    # If there are exactly two differences, check if swapping them makes the strings equal
    if len(diff_indices) == 2:
        i, j = diff_indices
        return s1[i] == s2[j] and s1[j] == s2[i]

    # If there are not exactly two differences, it's not possible to make the strings equal with one swap
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Strings are already equal
    print(areAlmostEqual("bank", "bank"))  # Expected: True

    # Test Case 2: One swap can make the strings equal
    print(areAlmostEqual("bank", "kanb"))  # Expected: True

    # Test Case 3: More than one swap needed
    print(areAlmostEqual("attack", "defend"))  # Expected: False

    # Test Case 4: Strings differ in only one character
    print(areAlmostEqual("abcd", "abcf"))  # Expected: False

    # Test Case 5: Strings differ in exactly two characters but swapping doesn't help
    print(areAlmostEqual("abcd", "abdc"))  # Expected: True

"""
Time Complexity Analysis:
- Let n be the length of the strings s1 and s2.
- The algorithm iterates through the strings once to find the differing indices, which takes O(n) time.
- The comparison and swap check are O(1) operations.
- Overall time complexity: O(n).

Space Complexity Analysis:
- The algorithm uses a list to store the differing indices, which in the worst case can store up to n indices.
- Overall space complexity: O(n).

Topic: Strings
"""