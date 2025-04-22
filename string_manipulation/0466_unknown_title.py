"""
LeetCode Problem #466: Count The Repetitions

Problem Statement:
We define str = [s, n] as the string formed by concatenating s exactly n times.
For example, str = ["abc", 3] = "abcabcabc".

On the other hand, we define that string s2 can be obtained from string s1 if we can remove some characters from s1 such that the remaining characters of s1 form s2.

For example, s2 = "abc" can be obtained from s1 = "abdbec" based on the following sequence: "abdbec" -> "abdec" -> "abc".

Given two strings s1 and s2 and two integers n1 and n2, return the maximum integer m such that [s2, m] can be obtained from [s1, n1].

Constraints:
- 1 <= s1.length, s2.length <= 100
- s1 and s2 consist of lowercase English letters.
- 1 <= n1, n2 <= 10^6
"""

def getMaxRepetitions(s1: str, n1: int, s2: str, n2: int) -> int:
    if not set(s2).issubset(set(s1)):
        return 0

    s1_count, s2_count = 0, 0
    index_map = {}
    s2_index = 0

    while s1_count < n1:
        s1_count += 1
        for char in s1:
            if char == s2[s2_index]:
                s2_index += 1
                if s2_index == len(s2):
                    s2_index = 0
                    s2_count += 1

        if s2_index in index_map:
            prev_s1_count, prev_s2_count = index_map[s2_index]
            cycle_s1_count = s1_count - prev_s1_count
            cycle_s2_count = s2_count - prev_s2_count

            remaining_s1_count = n1 - s1_count
            cycles = remaining_s1_count // cycle_s1_count

            s1_count += cycles * cycle_s1_count
            s2_count += cycles * cycle_s2_count
        else:
            index_map[s2_index] = (s1_count, s2_count)

    return s2_count // n2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "acb"
    n1 = 4
    s2 = "ab"
    n2 = 2
    print(getMaxRepetitions(s1, n1, s2, n2))  # Output: 2

    # Test Case 2
    s1 = "abc"
    n1 = 3
    s2 = "abc"
    n2 = 1
    print(getMaxRepetitions(s1, n1, s2, n2))  # Output: 3

    # Test Case 3
    s1 = "abc"
    n1 = 1
    s2 = "d"
    n2 = 1
    print(getMaxRepetitions(s1, n1, s2, n2))  # Output: 0

    # Test Case 4
    s1 = "aaa"
    n1 = 3
    s2 = "aa"
    n2 = 1
    print(getMaxRepetitions(s1, n1, s2, n2))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through `s1` up to `n1` times. Within each iteration, it processes each character of `s1`.
- If a cycle is detected, the remaining iterations are skipped, reducing the effective number of iterations.
- In the worst case, the time complexity is O(n1 * len(s1)).

Space Complexity:
- The space complexity is O(len(s2)) due to the `index_map` dictionary, which stores at most `len(s2)` entries.

Primary Topic: String Manipulation
"""