"""
LeetCode Problem #358: Rearrange String k Distance Apart

Problem Statement:
Given a string `s` and an integer `k`, rearrange the string such that the same characters are at least distance `k` from each other. 
If it is not possible to rearrange the string, return an empty string "".

Example 1:
Input: s = "aabbcc", k = 3
Output: "abcabc"
Explanation: The same letters are at least distance 3 from each other.

Example 2:
Input: s = "aaabc", k = 3
Output: ""
Explanation: It is not possible to rearrange the string.

Example 3:
Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.

Constraints:
- `1 <= s.length <= 10^4`
- `s` consists of only lowercase English letters.
- `0 <= k <= s.length`
"""

from collections import Counter, deque
import heapq

def rearrangeString(s: str, k: int) -> str:
    if k == 0:
        return s  # No rearrangement needed if k == 0

    # Step 1: Count the frequency of each character
    char_count = Counter(s)

    # Step 2: Use a max heap to store characters by their frequency
    max_heap = [(-freq, char) for char, freq in char_count.items()]
    heapq.heapify(max_heap)

    # Step 3: Use a queue to keep track of characters that are cooling down
    queue = deque()
    result = []

    while max_heap or queue:
        if max_heap:
            # Pop the most frequent character
            freq, char = heapq.heappop(max_heap)
            result.append(char)
            # Decrease the frequency and add it to the cooldown queue
            queue.append((char, freq + 1))  # Increment freq since it's negative

        # If the queue has k elements, we can re-add the oldest character back to the heap
        if len(queue) >= k:
            cooled_char, cooled_freq = queue.popleft()
            if cooled_freq < 0:  # Only re-add if there's remaining frequency
                heapq.heappush(max_heap, (cooled_freq, cooled_char))

    # If the result length matches the input string, we successfully rearranged it
    return "".join(result) if len(result) == len(s) else ""

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1, k1 = "aabbcc", 3
    print(rearrangeString(s1, k1))  # Output: "abcabc"

    # Test Case 2
    s2, k2 = "aaabc", 3
    print(rearrangeString(s2, k2))  # Output: ""

    # Test Case 3
    s3, k3 = "aaadbbcc", 2
    print(rearrangeString(s3, k3))  # Output: "abacabcd"

    # Test Case 4 (Edge Case: k = 0)
    s4, k4 = "aabbcc", 0
    print(rearrangeString(s4, k4))  # Output: "aabbcc"

    # Test Case 5 (Edge Case: Single character string)
    s5, k5 = "a", 1
    print(rearrangeString(s5, k5))  # Output: "a"

"""
Time Complexity:
- Building the frequency counter: O(n), where n is the length of the string `s`.
- Heap operations (push and pop): O(n log c), where c is the number of unique characters in `s`.
- Overall: O(n log c).

Space Complexity:
- The heap and queue can store up to O(c) elements, where c is the number of unique characters.
- The result string takes O(n) space.
- Overall: O(n + c).

Topic: Greedy, Heap (Priority Queue)
"""