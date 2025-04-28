"""
LeetCode Problem #2347: Best Poker Hand

Problem Statement:
You are given an integer array `ranks` and a character array `suits`. The `ranks[i]` and `suits[i]` represent the rank and suit of the ith card, respectively.

The following are the types of poker hands you can make from the cards:
1. "Flush": Five cards of the same suit.
2. "Three of a Kind": Three cards of the same rank.
3. "Pair": Two cards of the same rank.
4. "High Card": Any single card.

Return a string representing the best type of poker hand you can make with the given cards.

Note:
- The input arrays will always have five cards.
- The ranks array contains integers from 1 to 13.
- The suits array contains characters from 'a' to 'd'.

Example:
Input: ranks = [13, 2, 3, 5, 9], suits = ['a', 'a', 'a', 'a', 'a']
Output: "Flush"

Input: ranks = [4, 4, 2, 4, 5], suits = ['d', 'a', 'a', 'b', 'c']
Output: "Three of a Kind"

Input: ranks = [10, 10, 2, 3, 4], suits = ['a', 'b', 'c', 'd', 'a']
Output: "Pair"
"""

# Solution
def bestHand(ranks, suits):
    # Check for Flush
    if len(set(suits)) == 1:
        return "Flush"
    
    # Count occurrences of each rank
    rank_count = {}
    for rank in ranks:
        rank_count[rank] = rank_count.get(rank, 0) + 1
    
    # Check for Three of a Kind or Pair
    max_count = max(rank_count.values())
    if max_count >= 3:
        return "Three of a Kind"
    elif max_count == 2:
        return "Pair"
    
    # Default case: High Card
    return "High Card"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Flush
    ranks1 = [13, 2, 3, 5, 9]
    suits1 = ['a', 'a', 'a', 'a', 'a']
    print(bestHand(ranks1, suits1))  # Output: "Flush"

    # Test Case 2: Three of a Kind
    ranks2 = [4, 4, 2, 4, 5]
    suits2 = ['d', 'a', 'a', 'b', 'c']
    print(bestHand(ranks2, suits2))  # Output: "Three of a Kind"

    # Test Case 3: Pair
    ranks3 = [10, 10, 2, 3, 4]
    suits3 = ['a', 'b', 'c', 'd', 'a']
    print(bestHand(ranks3, suits3))  # Output: "Pair"

    # Test Case 4: High Card
    ranks4 = [1, 2, 3, 4, 5]
    suits4 = ['a', 'b', 'c', 'd', 'a']
    print(bestHand(ranks4, suits4))  # Output: "High Card"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Checking for Flush: O(5) -> Constant time since we only check the suits array.
- Counting occurrences of ranks: O(5) -> We iterate through the ranks array once.
- Finding the maximum count: O(1) -> The rank_count dictionary will have at most 13 keys (ranks from 1 to 13).
Overall: O(5) -> Constant time.

Space Complexity:
- rank_count dictionary: At most 13 keys (one for each rank).
Overall: O(1) -> Constant space.
"""

# Topic: Arrays, Hash Table