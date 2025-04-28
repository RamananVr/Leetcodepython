"""
LeetCode Problem #564: Find the Closest Palindrome

Problem Statement:
Given a string `n` representing an integer, return the closest integer (not including itself), 
which is a palindrome. If there is a tie, return the smaller one.

The closest is defined as the absolute difference minimized between two integers.

Constraints:
- `n` is a positive integer represented as a string.
- 1 <= n.length <= 18
- `n` does not have leading zeros except for the number "0" itself.

Example 1:
Input: n = "123"
Output: "121"

Example 2:
Input: n = "1"
Output: "0"

Example 3:
Input: n = "99"
Output: "101"
"""

def nearest_palindromic(n: str) -> str:
    """
    Finds the closest palindrome to the given number n.
    """
    length = len(n)
    num = int(n)
    
    # Edge case for single-digit numbers
    if num <= 10:
        return str(num - 1)
    if num == 11:
        return "9"
    
    # Generate candidates
    candidates = set()
    
    # Case 1: Palindrome by mirroring the first half
    prefix = int(n[:(length + 1) // 2])
    for diff in [-1, 0, 1]:
        new_prefix = str(prefix + diff)
        if length % 2 == 0:
            candidate = int(new_prefix + new_prefix[::-1])
        else:
            candidate = int(new_prefix + new_prefix[-2::-1])
        candidates.add(candidate)
    
    # Case 2: Edge cases for numbers like 100...001 or 999...999
    candidates.add(10**(length - 1) - 1)  # Smallest number with one less digit
    candidates.add(10**length + 1)       # Smallest number with one more digit
    
    # Remove the original number itself
    candidates.discard(num)
    
    # Find the closest palindrome
    closest = None
    min_diff = float('inf')
    for candidate in candidates:
        diff = abs(candidate - num)
        if diff < min_diff or (diff == min_diff and candidate < closest):
            closest = candidate
            min_diff = diff
    
    return str(closest)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = "123"
    print(nearest_palindromic(n))  # Output: "121"

    # Test Case 2
    n = "1"
    print(nearest_palindromic(n))  # Output: "0"

    # Test Case 3
    n = "99"
    print(nearest_palindromic(n))  # Output: "101"

    # Test Case 4
    n = "808"
    print(nearest_palindromic(n))  # Output: "818"

    # Test Case 5
    n = "1000"
    print(nearest_palindromic(n))  # Output: "999"

"""
Time Complexity:
- Let `L` be the length of the input string `n`.
- Generating candidates involves mirroring the first half of the string, which is O(L).
- Comparing the candidates involves a constant number of comparisons (at most 5 candidates), so this is O(1).
- Overall time complexity: O(L).

Space Complexity:
- The space used is primarily for storing the candidates, which is O(1) since the number of candidates is constant.
- Overall space complexity: O(1).

Topic: Strings, Math
"""