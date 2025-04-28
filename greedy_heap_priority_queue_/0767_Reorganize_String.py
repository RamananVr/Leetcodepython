"""
LeetCode Problem #767: Reorganize String

Problem Statement:
Given a string `s`, rearrange the characters of `s` so that any two adjacent characters are not the same.

Return any possible rearrangement of `s` or return an empty string if no such arrangement is possible.

Constraints:
- 1 <= s.length <= 500
- `s` consists of lowercase English letters.

Example 1:
Input: s = "aab"
Output: "aba"

Example 2:
Input: s = "aaab"
Output: ""

Example 3:
Input: s = "aabb"
Output: "abab" or "baba" or other valid outputs
"""

from collections import Counter
import heapq

def reorganizeString(s: str) -> str:
    # Step 1: Count the frequency of each character
    char_count = Counter(s)
    
    # Step 2: Create a max heap based on character frequencies
    max_heap = [(-freq, char) for char, freq in char_count.items()]
    heapq.heapify(max_heap)
    
    # Step 3: Initialize variables to build the result
    prev_freq, prev_char = 0, ""
    result = []
    
    # Step 4: Process the heap
    while max_heap:
        freq, char = heapq.heappop(max_heap)
        result.append(char)
        
        # If the previous character still has remaining frequency, push it back into the heap
        if prev_freq < 0:
            heapq.heappush(max_heap, (prev_freq, prev_char))
        
        # Update prev_freq and prev_char for the next iteration
        prev_freq, prev_char = freq + 1, char  # Decrease frequency since we used one instance of `char`
    
    # Step 5: Check if the result is valid
    result_str = ''.join(result)
    for i in range(1, len(result_str)):
        if result_str[i] == result_str[i - 1]:
            return ""
    
    return result_str

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aab"
    print(reorganizeString(s1))  # Expected Output: "aba"

    # Test Case 2
    s2 = "aaab"
    print(reorganizeString(s2))  # Expected Output: ""

    # Test Case 3
    s3 = "aabb"
    print(reorganizeString(s3))  # Expected Output: "abab" or "baba" or other valid outputs

    # Test Case 4
    s4 = "vvvlo"
    print(reorganizeString(s4))  # Expected Output: "vlvov" or other valid outputs

    # Test Case 5
    s5 = "aaaaaabbbbcc"
    print(reorganizeString(s5))  # Expected Output: "" (not possible to reorganize)

"""
Time Complexity Analysis:
- Counting character frequencies takes O(n), where n is the length of the string `s`.
- Building the max heap takes O(k log k), where k is the number of unique characters in `s`.
- Processing the heap involves O(n log k) operations, as we process each character in the string and perform heap operations.
- Overall time complexity: O(n log k), where k <= 26 (since there are at most 26 lowercase English letters). In practice, this simplifies to O(n).

Space Complexity Analysis:
- The space required for the character frequency counter is O(k), where k is the number of unique characters.
- The max heap also requires O(k) space.
- The result list requires O(n) space.
- Overall space complexity: O(n + k), which simplifies to O(n) in practice.

Topic: Greedy, Heap (Priority Queue)
"""