"""
LeetCode Problem #2118: Build the Lexicographically Largest Valid Sequence

Problem Statement:
You are given an integer `n` that represents the size of a sequence. You are tasked to construct a sequence of size `2 * n - 1` such that:
1. Each integer from 1 to n appears exactly twice in the sequence.
2. The distance between the two occurrences of the integer `i` is exactly `i` (i.e., there are `i` numbers between the two occurrences of `i`).
3. The sequence is lexicographically largest.

Return the lexicographically largest sequence. If there are multiple valid sequences, return any of them.

Constraints:
- 1 <= n <= 20
"""

from typing import List

def constructDistancedSequence(n: int) -> List[int]:
    def backtrack(index: int) -> bool:
        # If we have filled the entire sequence, return True
        if index == len(sequence):
            return True
        
        # If the current position is already filled, move to the next index
        if sequence[index] != 0:
            return backtrack(index + 1)
        
        # Try placing numbers from n to 1 (to ensure lexicographical order)
        for num in range(n, 0, -1):
            if used[num]:
                continue
            
            # If num == 1, it only occupies one position
            if num == 1:
                sequence[index] = num
                used[num] = True
                if backtrack(index + 1):
                    return True
                sequence[index] = 0
                used[num] = False
            else:
                # Check if we can place `num` at `index` and `index + num`
                if index + num < len(sequence) and sequence[index + num] == 0:
                    sequence[index] = sequence[index + num] = num
                    used[num] = True
                    if backtrack(index + 1):
                        return True
                    # Backtrack
                    sequence[index] = sequence[index + num] = 0
                    used[num] = False
        
        return False

    # Initialize the sequence and used array
    sequence = [0] * (2 * n - 1)
    used = [False] * (n + 1)
    
    # Start backtracking from index 0
    backtrack(0)
    return sequence

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(f"Input: n = {n}")
    print(f"Output: {constructDistancedSequence(n)}")
    # Expected Output: [3, 1, 2, 3, 2] or other valid sequences

    # Test Case 2
    n = 4
    print(f"Input: n = {n}")
    print(f"Output: {constructDistancedSequence(n)}")
    # Expected Output: [4, 1, 3, 1, 2, 4, 3, 2] or other valid sequences

    # Test Case 3
    n = 5
    print(f"Input: n = {n}")
    print(f"Output: {constructDistancedSequence(n)}")
    # Expected Output: [5, 1, 4, 1, 3, 5, 2, 4, 3, 2] or other valid sequences

"""
Time Complexity:
- The time complexity is O(n!), where n is the input size. This is because we are trying all permutations of numbers from 1 to n in the worst case.

Space Complexity:
- The space complexity is O(n), where n is the input size. This is due to the recursion stack and the `used` array.

Topic: Backtracking
"""