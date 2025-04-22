"""
LeetCode Problem #904: Fruit Into Baskets

Problem Statement:
You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array `fruits` where `fruits[i]` is the type of fruit the i-th tree produces.

You want to collect as much fruit as possible. However, the owner has some strict rules:
- You can only use two baskets, and each basket can only hold a single type of fruit.
- You can start collecting from any tree of your choice and stop collecting from any tree of your choice (including the start and the end of the row).
- Once you have started collecting fruit, you must pick exactly one fruit from every tree until you stop collecting.
- The baskets can only hold the two types of fruit you started collecting.

Given the integer array `fruits`, return the maximum number of fruits you can collect.

Constraints:
- `1 <= fruits.length <= 10^5`
- `0 <= fruits[i] < fruits.length`
"""

# Solution
def totalFruit(fruits):
    """
    Finds the maximum number of fruits that can be collected using two baskets.

    :param fruits: List[int] - List of integers representing the types of fruits.
    :return: int - Maximum number of fruits that can be collected.
    """
    max_fruits = 0
    left = 0
    fruit_count = {}

    for right in range(len(fruits)):
        fruit = fruits[right]
        fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

        while len(fruit_count) > 2:
            left_fruit = fruits[left]
            fruit_count[left_fruit] -= 1
            if fruit_count[left_fruit] == 0:
                del fruit_count[left_fruit]
            left += 1

        max_fruits = max(max_fruits, right - left + 1)

    return max_fruits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    fruits = [1, 2, 1]
    print(totalFruit(fruits))  # Expected Output: 3

    # Test Case 2
    fruits = [0, 1, 2, 2]
    print(totalFruit(fruits))  # Expected Output: 3

    # Test Case 3
    fruits = [1, 2, 3, 2, 2]
    print(totalFruit(fruits))  # Expected Output: 4

    # Test Case 4
    fruits = [3, 3, 3, 1, 2, 1, 1, 2, 3, 3, 4]
    print(totalFruit(fruits))  # Expected Output: 5

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through the `fruits` array once using the `right` pointer, and the `left` pointer also moves forward as needed.
- Each operation inside the loop (adding/removing from the dictionary) is O(1).
- Therefore, the overall time complexity is O(n), where n is the length of the `fruits` array.

Space Complexity:
- The space complexity is O(1) since the `fruit_count` dictionary will store at most 2 keys (representing the two types of fruits in the baskets).
"""

# Topic: Sliding Window, Arrays