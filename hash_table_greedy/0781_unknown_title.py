"""
LeetCode Problem #781: Rabbits in Forest

Problem Statement:
In a forest, each rabbit has some color. Some rabbits tell you how many other rabbits have the same color as them. 
Those answers are placed in an array. Return the minimum number of rabbits that could be in the forest.

Example:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
- The two rabbits that answered "1" could both be of one color, say red.
- The rabbit that answered "2" could be of a different color, say green.
- The minimum number of rabbits is 5: 2 (red) + 3 (green).

Constraints:
- 1 <= answers.length <= 1000
- 0 <= answers[i] < 1000
"""

def numRabbits(answers):
    """
    Calculate the minimum number of rabbits in the forest based on their answers.

    :param answers: List[int] - List of answers from rabbits
    :return: int - Minimum number of rabbits in the forest
    """
    from collections import Counter

    count = Counter(answers)
    total_rabbits = 0

    for answer, frequency in count.items():
        group_size = answer + 1
        groups = (frequency + group_size - 1) // group_size  # Ceiling division
        total_rabbits += groups * group_size

    return total_rabbits

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    answers = [1, 1, 2]
    print(numRabbits(answers))  # Output: 5

    # Test Case 2
    answers = [10, 10, 10]
    print(numRabbits(answers))  # Output: 11

    # Test Case 3
    answers = []
    print(numRabbits(answers))  # Output: 0

    # Test Case 4
    answers = [0, 0, 1, 1, 1]
    print(numRabbits(answers))  # Output: 6

    # Test Case 5
    answers = [3, 3, 3, 3]
    print(numRabbits(answers))  # Output: 4

"""
Time Complexity:
- Let n be the length of the `answers` array.
- Counting the frequency of elements using `Counter` takes O(n).
- Iterating through the unique answers and performing calculations takes O(k), where k is the number of unique answers.
- Overall time complexity: O(n + k).

Space Complexity:
- The `Counter` object stores up to k unique answers, where k <= n.
- Space complexity: O(k).

Topic: Hash Table, Greedy
"""