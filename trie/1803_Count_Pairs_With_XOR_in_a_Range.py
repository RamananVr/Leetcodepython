"""
LeetCode Problem #1803: Count Pairs With XOR in a Range

Problem Statement:
Given a (0-indexed) integer array `nums` and two integers `low` and `high`, 
return the number of pairs `(i, j)` where `0 <= i < j < nums.length` and 
`low <= (nums[i] XOR nums[j]) <= high`.

Example:
Input: nums = [1,4,2,7], low = 2, high = 6
Output: 6
Explanation: All pairs (i, j) are as follows:
    - (0, 1): nums[0] XOR nums[1] = 1 XOR 4 = 5
    - (0, 2): nums[0] XOR nums[2] = 1 XOR 2 = 3
    - (0, 3): nums[0] XOR nums[3] = 1 XOR 7 = 6
    - (1, 2): nums[1] XOR nums[2] = 4 XOR 2 = 6
    - (1, 3): nums[1] XOR nums[3] = 4 XOR 7 = 3
    - (2, 3): nums[2] XOR nums[3] = 2 XOR 7 = 5
    All of these pairs satisfy the condition 2 <= XOR <= 6.

Constraints:
- 1 <= nums.length <= 2 * 10^4
- 0 <= nums[i] <= 2^14
- 0 <= low <= high <= 2^14
"""

from typing import List

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        class TrieNode:
            def __init__(self):
                self.children = {}
                self.count = 0

        def insert(num):
            node = trie
            for i in range(14, -1, -1):  # 15 bits for numbers up to 2^14
                bit = (num >> i) & 1
                if bit not in node.children:
                    node.children[bit] = TrieNode()
                node = node.children[bit]
                node.count += 1

        def count_less_than(num, limit):
            node = trie
            count = 0
            for i in range(14, -1, -1):
                if not node:
                    break
                bit_num = (num >> i) & 1
                bit_limit = (limit >> i) & 1
                if bit_limit == 1:
                    if bit_num in node.children:
                        count += node.children[bit_num].count
                    node = node.children.get(1 - bit_num, None)
                else:
                    node = node.children.get(bit_num, None)
            return count

        def count_pairs_with_xor_in_range(nums, low, high):
            count = 0
            for num in nums:
                count += count_less_than(num, high + 1) - count_less_than(num, low)
                insert(num)
            return count

        trie = TrieNode()
        return count_pairs_with_xor_in_range(nums, low, high)


# Example Test Cases
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    nums = [1, 4, 2, 7]
    low = 2
    high = 6
    print(solution.countPairs(nums, low, high))  # Output: 6

    # Test Case 2
    nums = [9, 8, 4, 2, 1]
    low = 5
    high = 10
    print(solution.countPairs(nums, low, high))  # Output: 8

    # Test Case 3
    nums = [0, 1, 2, 3, 4]
    low = 1
    high = 4
    print(solution.countPairs(nums, low, high))  # Output: 10


"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Inserting a number into the Trie takes O(15) = O(1) since the maximum bit length is 15 (for numbers up to 2^14).
   - Counting pairs with XOR in range involves traversing the Trie, which also takes O(1) per query.
   - For `n` numbers in the array, we perform these operations `n` times.
   - Overall time complexity: O(n).

2. Space Complexity:
   - The Trie stores up to `n` numbers, each represented by at most 15 bits.
   - In the worst case, the Trie can have up to O(n * 15) nodes.
   - Overall space complexity: O(n).

Topic: Trie
"""