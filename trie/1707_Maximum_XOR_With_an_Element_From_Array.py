"""
LeetCode Problem #1707: Maximum XOR With an Element From Array

Problem Statement:
You are given an array `nums` consisting of non-negative integers. You are also given a `queries` array, where `queries[i] = [xi, mi]`.

The answer to the `i-th` query is the maximum bitwise XOR value of `xi` that can be obtained by XORing `xi` with any element of `nums` such that the element is less than or equal to `mi`. In other words, the answer is `max(nums[j] XOR xi)` for all `j` such that `nums[j] <= mi`. If all elements in `nums` are greater than `mi`, then the answer is `-1`.

Return an array `answer` where `answer.length == queries.length` and `answer[i]` is the answer to the `i-th` query.

Constraints:
- `1 <= nums.length, queries.length <= 10^5`
- `0 <= nums[j], xi, mi <= 10^9`

"""

from typing import List

class Solution:
    def maximizeXor(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        # Sort nums for efficient range queries
        nums.sort()
        
        # Add indices to queries for result placement after sorting
        queries = [(x, m, i) for i, (x, m) in enumerate(queries)]
        queries.sort(key=lambda q: q[1])  # Sort queries by mi
        
        # Trie node definition
        class TrieNode:
            def __init__(self):
                self.children = {}
        
        # Trie root
        root = TrieNode()
        
        # Function to insert a number into the Trie
        def insert(num):
            node = root
            for i in range(31, -1, -1):  # 32-bit integers
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
        
        # Function to find the maximum XOR for a given number
        def find_max_xor(num):
            node = root
            if not node.children:  # If Trie is empty
                return -1
            max_xor = 0
            for i in range(31, -1, -1):  # 32-bit integers
                bit = (num >> i) & 1
                # Try to take the opposite bit for maximizing XOR
                toggled_bit = 1 - bit
                if toggled_bit in node.children:
                    max_xor = (max_xor << 1) | 1
                    node = node.children[toggled_bit]
                else:
                    max_xor = (max_xor << 1)
                    node = node.children[bit]
            return max_xor
        
        # Process queries
        result = [-1] * len(queries)
        idx = 0  # Pointer for nums
        for x, m, original_index in queries:
            # Insert all nums <= m into the Trie
            while idx < len(nums) and nums[idx] <= m:
                insert(nums[idx])
                idx += 1
            # Find the maximum XOR for the current query
            result[original_index] = find_max_xor(x)
        
        return result

# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    nums = [0, 1, 2, 3, 4]
    queries = [[3, 1], [1, 3], [5, 6]]
    print(sol.maximizeXor(nums, queries))  # Output: [3, 3, 7]
    
    # Test Case 2
    nums = [5, 2, 4, 6, 6, 3]
    queries = [[12, 4], [8, 1], [6, 3]]
    print(sol.maximizeXor(nums, queries))  # Output: [15, -1, 5]

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Sorting `nums`: O(n log n), where n is the length of `nums`.
   - Sorting `queries`: O(q log q), where q is the length of `queries`.
   - Inserting elements into the Trie: O(n * 32) = O(32n) = O(n), as each number has at most 32 bits.
   - Processing each query: O(q * 32) = O(32q) = O(q).
   - Total: O(n log n + q log q + n + q) = O((n + q) log(n + q)).

2. Space Complexity:
   - Trie storage: O(n * 32) = O(32n) = O(n), as each number has at most 32 bits.
   - Result array: O(q).
   - Total: O(n + q).

Topic: Trie
"""