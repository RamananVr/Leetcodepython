"""
LeetCode Problem #2268: Minimum Number of Keypresses

Problem Statement:
You have a phone keyboard layout with 9 keys, each key can hold up to 3 letters. 
The letters are assigned to the keys in lexicographical order. For example:
Key 1: ['a', 'b', 'c']
Key 2: ['d', 'e', 'f']
Key 3: ['g', 'h', 'i']
...
Key 9: ['w', 'x', 'y', 'z'] (if there are fewer than 26 letters, the last key may have fewer letters).

To type a letter, you need to press the key corresponding to that letter. 
The number of keypresses required to type a letter depends on its position on the key:
- The first letter on a key requires 1 keypress.
- The second letter on a key requires 2 keypresses.
- The third letter on a key requires 3 keypresses.

Given a string `s` consisting of lowercase English letters, return the minimum number of keypresses required to type the string.

Constraints:
- 1 <= len(s) <= 10^5
- s consists of lowercase English letters.

Example:
Input: s = "apple"
Output: 10
Explanation:
- 'a' is on key 1 and requires 1 keypress.
- 'p' is on key 7 and requires 2 keypresses.
- 'p' is on key 7 and requires 2 keypresses.
- 'l' is on key 5 and requires 2 keypresses.
- 'e' is on key 2 and requires 3 keypresses.
Total = 1 + 2 + 2 + 2 + 3 = 10.
"""

from collections import Counter

def minimumKeypresses(s: str) -> int:
    # Count the frequency of each character in the string
    freq = Counter(s)
    
    # Sort characters by frequency in descending order
    # If two characters have the same frequency, their order doesn't matter
    sorted_freq = sorted(freq.values(), reverse=True)
    
    # Assign characters to keys and calculate the total keypresses
    total_keypresses = 0
    for i, count in enumerate(sorted_freq):
        # Determine the keypress cost based on the position in the sorted list
        keypress_cost = (i // 9) + 1
        total_keypresses += keypress_cost * count
    
    return total_keypresses

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "apple"
    print(f"Input: {s1} -> Output: {minimumKeypresses(s1)}")  # Expected: 10

    # Test Case 2
    s2 = "abcdefghijklmnopqrstuvwxyz"
    print(f"Input: {s2} -> Output: {minimumKeypresses(s2)}")  # Expected: 36

    # Test Case 3
    s3 = "aaaabbbbcccc"
    print(f"Input: {s3} -> Output: {minimumKeypresses(s3)}")  # Expected: 12

    # Test Case 4
    s4 = "a"
    print(f"Input: {s4} -> Output: {minimumKeypresses(s4)}")  # Expected: 1

    # Test Case 5
    s5 = "zzzzzzzzzz"
    print(f"Input: {s5} -> Output: {minimumKeypresses(s5)}")  # Expected: 10

"""
Time Complexity:
- Counting the frequency of characters takes O(n), where n is the length of the string.
- Sorting the frequencies takes O(26 * log(26)) = O(1) since there are at most 26 unique characters.
- Calculating the total keypresses takes O(26) = O(1).
Overall, the time complexity is O(n).

Space Complexity:
- The space required for the frequency counter is O(26) = O(1) since there are at most 26 unique characters.
- The sorted list of frequencies also takes O(26) = O(1) space.
Overall, the space complexity is O(1).

Topic: Greedy Algorithm
"""