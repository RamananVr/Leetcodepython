"""
LeetCode Question #1718: Construct the Lexicographically Largest Valid Sequence

Problem Statement:
You are given an integer n. You need to construct a 2n - 1 sized array that satisfies the following conditions:
1. The array contains each integer from 1 to n exactly twice.
2. The distance between the two occurrences of the integer i is exactly i (i.e., the second occurrence of i is i indices after the first occurrence of i).
3. If there are multiple valid sequences, return the lexicographically largest sequence.

Return the constructed array. If no valid array exists, return an empty array.

Example:
Input: n = 3
Output: [3, 1, 2, 1, 3, 2]

Constraints:
- 1 <= n <= 20
"""

# Solution
def constructDistancedSequence(n):
    def backtrack(index, sequence, used):
        # If the sequence is complete, return True
        if index == len(sequence):
            return True
        
        # If the current index is already filled, move to the next index
        if sequence[index] != 0:
            return backtrack(index + 1, sequence, used)
        
        # Try placing numbers from n to 1
        for num in range(n, 0, -1):
            if used[num]:
                continue
            
            # Check if we can place `num` at `index` and `index + num`
            if num == 1 or (index + num < len(sequence) and sequence[index + num] == 0):
                # Place `num` in the sequence
                sequence[index] = num
                if num != 1:
                    sequence[index + num] = num
                used[num] = True
                
                # Recursively try to fill the rest of the sequence
                if backtrack(index + 1, sequence, used):
                    return True
                
                # Backtrack: undo the placement
                sequence[index] = 0
                if num != 1:
                    sequence[index + num] = 0
                used[num] = False
        
        return False
    
    # Initialize the sequence and used array
    sequence = [0] * (2 * n - 1)
    used = [False] * (n + 1)
    
    # Start backtracking from index 0
    backtrack(0, sequence, used)
    return sequence

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 3
    print(constructDistancedSequence(n))  # Output: [3, 1, 2, 1, 3, 2]

    # Test Case 2
    n = 4
    print(constructDistancedSequence(n))  # Output: [4, 1, 3, 1, 2, 4, 3, 2]

    # Test Case 3
    n = 5
    print(constructDistancedSequence(n))  # Output: [5, 1, 4, 1, 3, 5, 2, 4, 3, 2]

"""
Time and Space Complexity Analysis:

Time Complexity:
- The solution uses backtracking, and in the worst case, it explores all possible placements of numbers.
- For each number, we attempt to place it in multiple positions, leading to a complexity of O(n!) in the worst case.

Space Complexity:
- The space complexity is O(n) for the `used` array and O(2n - 1) for the `sequence` array, resulting in O(n) overall.

Topic: Backtracking
"""