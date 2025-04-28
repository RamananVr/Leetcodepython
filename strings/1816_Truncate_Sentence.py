"""
LeetCode Problem #1816: Truncate Sentence

Problem Statement:
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. 
Each of the words consists of only uppercase and lowercase English letters (no punctuation).

You are given a sentence `s` and an integer `k`. You need to truncate `s` such that it contains only 
the first `k` words. Return the truncated sentence.

Example 1:
Input: s = "Hello how are you Contestant", k = 4
Output: "Hello how are you"
Explanation: The first 4 words of the sentence are "Hello", "how", "are", and "you".

Example 2:
Input: s = "What is the solution to this problem", k = 4
Output: "What is the solution"
Explanation: The first 4 words of the sentence are "What", "is", "the", and "solution".

Example 3:
Input: s = "chopper is not a tanuki", k = 5
Output: "chopper is not a tanuki"

Constraints:
- 1 <= s.length <= 500
- k is in the range [1, the number of words in s].
- s consists of only lowercase and uppercase English letters and spaces.
- The words in s are separated by a single space.
- There are no leading or trailing spaces.

"""

# Clean and Correct Python Solution
def truncateSentence(s: str, k: int) -> str:
    """
    Truncates the sentence `s` to contain only the first `k` words.

    :param s: A string representing the sentence.
    :param k: An integer representing the number of words to keep.
    :return: A string containing the first `k` words of the sentence.
    """
    # Split the sentence into words and join the first k words with a space
    return " ".join(s.split()[:k])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "Hello how are you Contestant"
    k1 = 4
    print(truncateSentence(s1, k1))  # Expected Output: "Hello how are you"

    # Test Case 2
    s2 = "What is the solution to this problem"
    k2 = 4
    print(truncateSentence(s2, k2))  # Expected Output: "What is the solution"

    # Test Case 3
    s3 = "chopper is not a tanuki"
    k3 = 5
    print(truncateSentence(s3, k3))  # Expected Output: "chopper is not a tanuki"

    # Test Case 4 (Edge Case: Single Word)
    s4 = "word"
    k4 = 1
    print(truncateSentence(s4, k4))  # Expected Output: "word"

    # Test Case 5 (Edge Case: All Words)
    s5 = "a b c d e"
    k5 = 5
    print(truncateSentence(s5, k5))  # Expected Output: "a b c d e"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the string `s` into words using `split()` takes O(n), where n is the length of the string.
- Slicing the list of words to get the first `k` words takes O(k).
- Joining the `k` words back into a string using `join()` takes O(m), where m is the total length of the first `k` words.
- Overall, the time complexity is O(n + m), which simplifies to O(n) since m <= n.

Space Complexity:
- The `split()` operation creates a list of words, which takes O(n) space.
- The slicing operation creates a new list of the first `k` words, which takes O(k) space.
- The `join()` operation creates a new string, which takes O(m) space.
- Overall, the space complexity is O(n + k + m), which simplifies to O(n) since k and m are both <= n.
"""

# Topic: Strings