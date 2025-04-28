"""
LeetCode Problem #187: Repeated DNA Sequences

Problem Statement:
The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'. 
For example, "ACGAATTCCG" is a DNA sequence. When studying DNA, it is useful to identify repeated 
sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once 
in a DNA molecule.

You may return the answer in any order.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'A', 'C', 'G', or 'T'.

Example 1:
Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC", "CCCCCAAAAA"]

Example 2:
Input: s = "AAAAAAAAAAAAA"
Output: ["AAAAAAAAAA"]
"""

def findRepeatedDnaSequences(s: str) -> list[str]:
    """
    Finds all 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

    :param s: A string representing the DNA sequence.
    :return: A list of repeated 10-letter-long sequences.
    """
    if len(s) < 10:
        return []

    seen = set()
    repeated = set()

    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if substring in seen:
            repeated.add(substring)
        else:
            seen.add(substring)

    return list(repeated)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(findRepeatedDnaSequences(s1))  # Output: ["AAAAACCCCC", "CCCCCAAAAA"]

    # Test Case 2
    s2 = "AAAAAAAAAAAAA"
    print(findRepeatedDnaSequences(s2))  # Output: ["AAAAAAAAAA"]

    # Test Case 3
    s3 = "ACGTACGTACGT"
    print(findRepeatedDnaSequences(s3))  # Output: []

    # Test Case 4
    s4 = "A"
    print(findRepeatedDnaSequences(s4))  # Output: []

    # Test Case 5
    s5 = "AAAAAAAAAAAACCCCCCCCCCC"
    print(findRepeatedDnaSequences(s5))  # Output: ["AAAAAAAAAA", "CCCCCCCCCC"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The loop iterates through the string `s` with a sliding window of size 10.
- For a string of length `n`, the loop runs `n - 9` times.
- Each substring operation and set operation (add or check) is O(1) on average.
- Therefore, the overall time complexity is O(n).

Space Complexity:
- The `seen` set stores all unique 10-letter substrings, and the `repeated` set stores the repeated ones.
- In the worst case, the space complexity is O(n) for storing substrings in the sets.
- Thus, the space complexity is O(n).

Topic: Hashing
"""