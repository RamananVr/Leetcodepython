"""
LeetCode Problem #1405: Longest Happy String

Problem Statement:
A string is called happy if it does not have any of the strings 'aaa', 'bbb', or 'ccc' as a substring.
Given three integers a, b, and c, return the longest possible happy string. If there are multiple
longest happy strings, return any of them. If there is no such string, return an empty string.

a, b, and c represent the maximum number of occurrences of 'a', 'b', and 'c' respectively.

A happy string must be constructed by only using the characters 'a', 'b', and 'c', and it must not
contain 'aaa', 'bbb', or 'ccc' as a substring.

Constraints:
- 0 <= a, b, c <= 100
- a + b + c > 0
"""

import heapq

def longest_happy_string(a: int, b: int, c: int) -> str:
    # Create a max heap with the counts of 'a', 'b', and 'c'
    max_heap = []
    if a > 0:
        heapq.heappush(max_heap, (-a, 'a'))
    if b > 0:
        heapq.heappush(max_heap, (-b, 'b'))
    if c > 0:
        heapq.heappush(max_heap, (-c, 'c'))
    
    result = []
    
    while max_heap:
        # Pop the character with the highest remaining count
        count1, char1 = heapq.heappop(max_heap)
        if len(result) >= 2 and result[-1] == result[-2] == char1:
            # If adding this character would create three consecutive characters, try the next one
            if not max_heap:
                break  # No other characters to use, so we stop
            count2, char2 = heapq.heappop(max_heap)
            result.append(char2)
            count2 += 1  # Decrease the count of char2
            if count2 < 0:
                heapq.heappush(max_heap, (count2, char2))
            # Push char1 back into the heap
            heapq.heappush(max_heap, (count1, char1))
        else:
            # Otherwise, add char1 to the result
            result.append(char1)
            count1 += 1  # Decrease the count of char1
            if count1 < 0:
                heapq.heappush(max_heap, (count1, char1))
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    a, b, c = 1, 1, 7
    print(longest_happy_string(a, b, c))  # Expected output: "ccbccacc" or similar

    # Test Case 2
    a, b, c = 2, 2, 1
    print(longest_happy_string(a, b, c))  # Expected output: "aabbc" or similar

    # Test Case 3
    a, b, c = 7, 1, 0
    print(longest_happy_string(a, b, c))  # Expected output: "aabaa" or similar

    # Test Case 4
    a, b, c = 0, 0, 0
    print(longest_happy_string(a, b, c))  # Expected output: ""

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm uses a max heap to manage the counts of 'a', 'b', and 'c'. Each heap operation (push or pop)
  takes O(log k), where k is the size of the heap. Since there are at most 3 characters ('a', 'b', 'c'),
  k is constant (k = 3). Therefore, each heap operation is O(1).
- The while loop runs until all characters are used, which is O(a + b + c).
- Overall time complexity: O(a + b + c).

Space Complexity:
- The heap stores at most 3 elements, so the space used by the heap is O(1).
- The result string uses O(a + b + c) space.
- Overall space complexity: O(a + b + c).

Topic: Greedy, Heap (Priority Queue)
"""