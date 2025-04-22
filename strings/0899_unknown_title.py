"""
LeetCode Problem #899: Orderly Queue

Problem Statement:
You are given a string `s` and an integer `k`. You can choose one of the first `k` letters of `s` and append it to the end of the string.

Return the lexicographically smallest string that can be obtained after applying the above operation any number of times.

Constraints:
- `1 <= k <= s.length <= 1000`
- `s` consists of lowercase English letters.

Explanation:
- If `k == 1`, the only operation you can perform is rotating the string. Thus, you need to find the smallest rotation of the string.
- If `k > 1`, you can rearrange the string in any order. Therefore, the lexicographically smallest string is simply the sorted version of `s`.
"""

def orderlyQueue(s: str, k: int) -> str:
    """
    Returns the lexicographically smallest string after applying the operation any number of times.

    :param s: Input string consisting of lowercase English letters.
    :param k: Integer representing the number of letters you can choose from the start of the string.
    :return: Lexicographically smallest string.
    """
    if k == 1:
        # Generate all rotations of the string and return the smallest one
        return min(s[i:] + s[:i] for i in range(len(s)))
    else:
        # If k > 1, we can sort the string to get the smallest lexicographical order
        return ''.join(sorted(s))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: k == 1, smallest rotation
    s1, k1 = "cba", 1
    print(orderlyQueue(s1, k1))  # Output: "acb"

    # Test Case 2: k > 1, sorted string
    s2, k2 = "cba", 2
    print(orderlyQueue(s2, k2))  # Output: "abc"

    # Test Case 3: Larger string with k == 1
    s3, k3 = "baaca", 1
    print(orderlyQueue(s3, k3))  # Output: "aacab"

    # Test Case 4: Larger string with k > 1
    s4, k4 = "baaca", 3
    print(orderlyQueue(s4, k4))  # Output: "aaabc"

    # Test Case 5: Already sorted string
    s5, k5 = "abc", 2
    print(orderlyQueue(s5, k5))  # Output: "abc"

"""
Time and Space Complexity Analysis:

1. When k == 1:
   - Time Complexity: O(n^2), where n is the length of the string. This is because we generate n rotations, each taking O(n) time to compute.
   - Space Complexity: O(n), for storing the rotations.

2. When k > 1:
   - Time Complexity: O(n log n), where n is the length of the string. This is due to the sorting operation.
   - Space Complexity: O(n), for storing the sorted string.

Topic: Strings
"""