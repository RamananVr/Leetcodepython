"""
LeetCode Problem #2591: Distribute Money to Maximum Children

Problem Statement:
You are given an integer `money` denoting the total amount of money you have and an integer `children` denoting the number of children you want to distribute the money to.

You need to distribute the money according to the following rules:
1. Each child must receive at least 1 unit of money.
2. No child can receive exactly 4 units of money.
3. You need to maximize the number of children who receive exactly 8 units of money.

Return the maximum number of children who can receive exactly 8 units of money. If it is impossible to distribute the money according to the rules, return -1.

Constraints:
- 1 <= money <= 10^9
- 1 <= children <= 10^5
"""

def max_children_with_8_units(money: int, children: int) -> int:
    # Step 1: Check if it's possible to distribute money
    if money < children:  # Each child must get at least 1 unit
        return -1

    # Step 2: Distribute the money
    money -= children  # Give each child 1 unit initially
    max_eights = min(money // 7, children)  # Maximize children with 8 units
    money -= max_eights * 7  # Deduct the money used for 8-unit children
    remaining_children = children - max_eights

    # Step 3: Handle remaining money and children
    if remaining_children == 0 and money > 0:
        return max_eights - 1  # If extra money remains, reduce one 8-unit child
    if remaining_children == 1 and money == 3:
        return max_eights - 1  # Avoid a child getting exactly 4 units
    return max_eights

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case
    print(max_children_with_8_units(20, 3))  # Expected output: 1

    # Test Case 2: Not enough money
    print(max_children_with_8_units(5, 10))  # Expected output: -1

    # Test Case 3: All children can get 8 units
    print(max_children_with_8_units(56, 7))  # Expected output: 7

    # Test Case 4: Extra money left over
    print(max_children_with_8_units(23, 3))  # Expected output: 2

    # Test Case 5: Edge case with exactly 4 units
    print(max_children_with_8_units(11, 2))  # Expected output: 0

"""
Time Complexity Analysis:
- The solution involves basic arithmetic operations and comparisons, which are O(1).
- Therefore, the time complexity is O(1).

Space Complexity Analysis:
- The solution uses a constant amount of extra space for variables.
- Therefore, the space complexity is O(1).

Topic: Greedy
"""