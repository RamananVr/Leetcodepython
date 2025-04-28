"""
LeetCode Problem #1830: Minimum Number of Operations to Make String Sorted

Problem Statement:
You are given a string `s` (0-indexed) consisting of only lowercase English letters. 
In one operation, you can choose any index `i` in the string, then remove the character at index `i` and insert it at the end of the string.

Return the minimum number of such operations required to make `s` sorted in lexicographical order.

Constraints:
- 1 <= s.length <= 3000
- `s` consists of lowercase English letters.
"""

from math import factorial
from collections import Counter

def makeStringSorted(s: str) -> int:
    MOD = 10**9 + 7
    
    # Precompute factorials up to the length of the string
    max_len = len(s)
    fact = [1] * (max_len + 1)
    for i in range(2, max_len + 1):
        fact[i] = fact[i - 1] * i % MOD
    
    # Helper function to calculate modular inverse
    def mod_inverse(x):
        return pow(x, MOD - 2, MOD)
    
    # Count frequency of each character
    freq = Counter(s)
    result = 0
    
    for i, char in enumerate(s):
        # Count characters smaller than the current character
        for smaller_char in range(ord('a'), ord(char)):
            if freq[chr(smaller_char)] > 0:
                # Calculate permutations if we move a smaller character to the front
                freq[chr(smaller_char)] -= 1
                perm = fact[len(s) - i - 1]
                for count in freq.values():
                    perm = perm * mod_inverse(fact[count]) % MOD
                result = (result + perm) % MOD
                freq[chr(smaller_char)] += 1
        
        # Update frequency of the current character
        freq[char] -= 1
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "cba"
    print(makeStringSorted(s1))  # Expected Output: 5

    # Test Case 2
    s2 = "aabb"
    print(makeStringSorted(s2))  # Expected Output: 2

    # Test Case 3
    s3 = "leetcode"
    print(makeStringSorted(s3))  # Expected Output: 3991

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm involves iterating through the string `s` (O(n)) and for each character, calculating permutations based on the frequency of characters (O(26) for lowercase English letters).
- Precomputing factorials takes O(n).
- Overall complexity is O(n * 26) = O(n).

Space Complexity:
- The space used for storing factorials is O(n).
- The frequency counter uses O(26) space for lowercase English letters.
- Overall space complexity is O(n).

Topic: String Manipulation, Permutations, Modular Arithmetic
"""