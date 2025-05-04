"""
LeetCode Problem #2138: Divide a String Into Groups of Size k

Problem Statement:
You are given a string `s` of lowercase English letters and an integer `k`. 
You need to divide the string into groups of size `k`. The last group may be 
smaller than `k` if there are not enough characters left in the string. 

If a group is smaller than `k`, you should pad it with the character `'x'` to 
make its size equal to `k`.

Return a list of strings denoting the groups formed.

Example 1:
Input: s = "abcdefghi", k = 3
Output: ["abc", "def", "ghi"]
Explanation: The string is divided into groups of size 3.

Example 2:
Input: s = "abcdefghij", k = 3
Output: ["abc", "def", "ghi", "jxx"]
Explanation: The string is divided into groups of size 3. The last group "j" 
is padded with "xx" to make its size equal to 3.

Constraints:
- `1 <= s.length <= 100`
- `1 <= k <= 100`
- `s` consists of lowercase English letters only.
"""

# Python Solution
def divideString(s: str, k: int) -> list[str]:
    result = []
    n = len(s)
    
    # Iterate through the string in steps of k
    for i in range(0, n, k):
        group = s[i:i+k]
        # If the group is smaller than k, pad it with 'x'
        if len(group) < k:
            group += 'x' * (k - len(group))
        result.append(group)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abcdefghi"
    k1 = 3
    print(divideString(s1, k1))  # Output: ["abc", "def", "ghi"]

    # Test Case 2
    s2 = "abcdefghij"
    k2 = 3
    print(divideString(s2, k2))  # Output: ["abc", "def", "ghi", "jxx"]

    # Test Case 3
    s3 = "a"
    k3 = 2
    print(divideString(s3, k3))  # Output: ["ax"]

    # Test Case 4
    s4 = "xyz"
    k4 = 5
    print(divideString(s4, k4))  # Output: ["xyzxx"]

    # Test Case 5
    s5 = "hello"
    k5 = 1
    print(divideString(s5, k5))  # Output: ["h", "e", "l", "l", "o"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string in steps of size `k`. 
  In the worst case, it processes all `n` characters of the string.
- Therefore, the time complexity is O(n), where `n` is the length of the string `s`.

Space Complexity:
- The function creates a list to store the resulting groups. 
  In the worst case, the list will contain approximately `n/k` groups, 
  each of size `k`. This results in a total space usage of O(n).
- Therefore, the space complexity is O(n).
"""

# Topic: Strings