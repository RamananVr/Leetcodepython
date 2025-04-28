"""
LeetCode Question #1208: Get Equal Substrings Within Budget

Problem Statement:
You are given two strings `s` and `t` of the same length and an integer `maxCost`.

You want to change `s` to `t`. Changing the i-th character of `s` to i-th character of `t` costs 
|s[i] - t[i]| (i.e., the absolute difference between the ASCII values of the characters).

You can choose any substring of `s` and change it to the corresponding substring of `t`. 
Return the maximum length of a substring of `s` that can be changed to be the same as the corresponding substring of `t` with a cost less than or equal to `maxCost`.

If there is no substring that satisfies the condition, return 0.

Example 1:
Input: s = "abcd", t = "bcdf", maxCost = 3
Output: 3
Explanation: "abc" -> "bcd". The cost is 3, so the maximum length is 3.

Example 2:
Input: s = "abcd", t = "cdef", maxCost = 3
Output: 1
Explanation: Each character in "abcd" costs 2 to change to the corresponding character in "cdef". The maximum length is 1.

Example 3:
Input: s = "abcd", t = "acde", maxCost = 0
Output: 1
Explanation: You cannot make any changes, so the maximum length is 1.

Constraints:
- `1 <= s.length <= 10^5`
- `t.length == s.length`
- `0 <= maxCost <= 10^6`
- `s` and `t` consist of only lowercase English letters.
"""

# Python Solution
def equalSubstring(s: str, t: str, maxCost: int) -> int:
    # Calculate the cost array
    cost = [abs(ord(s[i]) - ord(t[i])) for i in range(len(s))]
    
    # Sliding window approach
    start = 0
    current_cost = 0
    max_length = 0
    
    for end in range(len(s)):
        current_cost += cost[end]
        
        # Shrink the window if the cost exceeds maxCost
        while current_cost > maxCost:
            current_cost -= cost[start]
            start += 1
        
        # Update the maximum length
        max_length = max(max_length, end - start + 1)
    
    return max_length

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, t1, maxCost1 = "abcd", "bcdf", 3
    print(equalSubstring(s1, t1, maxCost1))  # Output: 3

    # Test Case 2
    s2, t2, maxCost2 = "abcd", "cdef", 3
    print(equalSubstring(s2, t2, maxCost2))  # Output: 1

    # Test Case 3
    s3, t3, maxCost3 = "abcd", "acde", 0
    print(equalSubstring(s3, t3, maxCost3))  # Output: 1

    # Test Case 4
    s4, t4, maxCost4 = "krrgw", "zjxss", 19
    print(equalSubstring(s4, t4, maxCost4))  # Output: 2

    # Test Case 5
    s5, t5, maxCost5 = "abcd", "abcd", 0
    print(equalSubstring(s5, t5, maxCost5))  # Output: 4

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the cost array takes O(n), where n is the length of the strings.
- The sliding window approach iterates through the string once, which is O(n).
- Overall time complexity: O(n).

Space Complexity:
- The cost array takes O(n) space.
- Other variables use O(1) space.
- Overall space complexity: O(n).
"""

# Topic: Sliding Window