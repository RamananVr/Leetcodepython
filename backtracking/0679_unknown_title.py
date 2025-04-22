"""
LeetCode Problem #679: 24 Game

Problem Statement:
You are given an array of four integers `cards`. Each integer represents a card value. You need to determine whether you can use the four cards to get the value 24 by performing any of the following operations any number of times:

1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)

You can use each card only once and must use all four cards. The division operation may result in a floating-point number. You cannot use integer division. For example, 8 / 3 = 2.6666... is valid, but 8 // 3 = 2 is not.

Return `True` if you can achieve the value 24, otherwise return `False`.

Constraints:
- `cards.length == 4`
- `1 <= cards[i] <= 9`

Example:
Input: cards = [8, 1, 6, 6]
Output: True
Explanation: One possible way to achieve 24 is: (8 - (6 / (1 - 6))) = 24.

Input: cards = [1, 3, 4, 6]
Output: True
Explanation: One possible way to achieve 24 is: (6 / (1 - (3 / 4))) = 24.

Input: cards = [1, 1, 1, 1]
Output: False
"""

from itertools import permutations

def judgePoint24(cards):
    """
    Determines if the given cards can be used to achieve the value 24 using arithmetic operations.
    
    :param cards: List[int] - A list of four integers representing card values.
    :return: bool - True if 24 can be achieved, False otherwise.
    """
    def helper(nums):
        # Base case: if there's only one number left, check if it's close to 24
        if len(nums) == 1:
            return abs(nums[0] - 24) < 1e-6
        
        # Try all pairs of numbers and all operations
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    # Remaining numbers after removing nums[i] and nums[j]
                    remaining = [nums[k] for k in range(len(nums)) if k != i and k != j]
                    
                    # Try all possible results of combining nums[i] and nums[j]
                    for op in ('+', '-', '*', '/'):
                        if op == '+':
                            remaining.append(nums[i] + nums[j])
                        elif op == '-':
                            remaining.append(nums[i] - nums[j])
                        elif op == '*':
                            remaining.append(nums[i] * nums[j])
                        elif op == '/' and nums[j] != 0:  # Avoid division by zero
                            remaining.append(nums[i] / nums[j])
                        else:
                            continue
                        
                        # Recursively check if we can achieve 24 with the new set of numbers
                        if helper(remaining):
                            return True
                        
                        # Backtrack: remove the last appended number
                        remaining.pop()
        
        return False
    
    # Try all permutations of the cards
    for perm in permutations(cards):
        if helper(list(perm)):
            return True
    
    return False

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cards = [8, 1, 6, 6]
    print(judgePoint24(cards))  # Output: True

    # Test Case 2
    cards = [1, 3, 4, 6]
    print(judgePoint24(cards))  # Output: True

    # Test Case 3
    cards = [1, 1, 1, 1]
    print(judgePoint24(cards))  # Output: False

    # Test Case 4
    cards = [4, 4, 4, 4]
    print(judgePoint24(cards))  # Output: False

    # Test Case 5
    cards = [7, 2, 1, 10]
    print(judgePoint24(cards))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm tries all permutations of the cards (4! = 24 permutations).
- For each permutation, it recursively tries all pairs of numbers and all operations.
- The recursion depth is at most 4 (since there are 4 cards), and at each level, there are O(n^2) pairs to consider.
- Thus, the time complexity is approximately O(4! * n^2 * recursion_depth) = O(24 * 16) = O(384), which is constant for the given constraints.

Space Complexity:
- The space complexity is O(recursion_depth), which is O(4) due to the recursive calls.
- Additionally, we store intermediate results in a list, but this is bounded by the number of cards (4).
- Thus, the space complexity is O(4), which is constant.

Topic: Backtracking
"""