"""
LeetCode Problem #691: Stickers to Spell Word

Problem Statement:
We are given a collection of `stickers`. Each sticker is a string that consists of lowercase English letters. 
We are also given a target string `target`. You want to form the target string using the stickers you have. 
You can use each sticker as many times as you want, but you cannot reorder the letters in any sticker.

Return the minimum number of stickers that you need to spell out the target. If the target cannot be spelled out, return -1.

Example 1:
Input: stickers = ["with", "example", "science"], target = "thehat"
Output: 3
Explanation: We can use 2 "with" stickers and 1 "example" sticker.

Example 2:
Input: stickers = ["notice", "possible"], target = "basicbasic"
Output: -1
Explanation: We cannot form the target "basicbasic" from the given stickers.

Constraints:
- 1 <= stickers.length <= 50
- 1 <= stickers[i].length <= 10
- 1 <= target.length <= 15
- stickers[i] and target consist of lowercase English letters.
"""

from collections import Counter
from functools import lru_cache

def minStickers(stickers, target):
    """
    Function to calculate the minimum number of stickers required to form the target string.
    
    :param stickers: List[str] - List of stickers available.
    :param target: str - Target string to form.
    :return: int - Minimum number of stickers required, or -1 if impossible.
    """
    # Preprocess stickers into a list of Counters for efficient frequency comparison
    sticker_counts = [Counter(sticker) for sticker in stickers]
    
    # Cache the results of subproblems using lru_cache
    @lru_cache(None)
    def dfs(remaining):
        # Base case: if no characters are left in the target, return 0 stickers
        if not remaining:
            return 0
        
        # Count the frequency of characters in the remaining target
        remaining_count = Counter(remaining)
        
        # Try using each sticker to reduce the remaining target
        min_stickers = float('inf')
        for sticker in sticker_counts:
            # If the sticker does not contain any useful characters, skip it
            if sticker[remaining[0]] == 0:
                continue
            
            # Create a new remaining target after using the sticker
            new_remaining = ''.join(
                [char * max(0, remaining_count[char] - sticker[char]) for char in remaining_count]
            )
            
            # Recursively calculate the number of stickers needed for the new remaining target
            result = dfs(new_remaining)
            if result != -1:
                min_stickers = min(min_stickers, 1 + result)
        
        # If no sticker can reduce the target, return -1
        return min_stickers if min_stickers != float('inf') else -1
    
    # Start the recursive process with the full target
    return dfs(target)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    stickers = ["with", "example", "science"]
    target = "thehat"
    print(minStickers(stickers, target))  # Output: 3

    # Test Case 2
    stickers = ["notice", "possible"]
    target = "basicbasic"
    print(minStickers(stickers, target))  # Output: -1

    # Test Case 3
    stickers = ["a", "b", "c"]
    target = "abc"
    print(minStickers(stickers, target))  # Output: 3

    # Test Case 4
    stickers = ["ab", "bc", "cd"]
    target = "abcd"
    print(minStickers(stickers, target))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the number of stickers and `m` be the length of the target string.
- The number of unique subproblems is bounded by the number of possible subsets of the target string, which is O(2^m).
- For each subproblem, we iterate through all stickers (O(n)) and calculate the new remaining target (O(m)).
- Thus, the overall time complexity is O(n * m * 2^m).

Space Complexity:
- The space complexity is dominated by the memoization cache, which stores results for O(2^m) subproblems.
- Each subproblem requires O(m) space to store the remaining target string.
- Thus, the space complexity is O(m * 2^m).

Topic: Dynamic Programming
"""