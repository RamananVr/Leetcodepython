"""
LeetCode Problem #1996: The Number of Weak Characters in the Game

Problem Statement:
You are playing a game that contains multiple characters, and each of the characters has two properties: attack and defense. 
You are given a 2D integer array properties where properties[i] = [attack_i, defense_i] represents the properties of the ith character in the game.

A character is said to be weak if any other character has both attack and defense levels strictly greater than this character's attack and defense levels. 
Return the number of weak characters.

Example:
Input: properties = [[5,5],[6,3],[3,6]]
Output: 0
Explanation: No character is weak because no other character has both attack and defense levels strictly greater than any character.

Input: properties = [[2,2],[3,3]]
Output: 1
Explanation: The first character is weak because the second character has both attack and defense levels strictly greater than the first character.

Input: properties = [[1,5],[10,4],[4,3]]
Output: 1
Explanation: The third character is weak because the second character has both attack and defense levels strictly greater than the third character.

Constraints:
- 2 <= properties.length <= 10^5
- properties[i].length == 2
- 1 <= attack_i, defense_i <= 10^5
"""

# Solution
def numberOfWeakCharacters(properties):
    """
    Function to calculate the number of weak characters in the game.

    :param properties: List[List[int]] - A list of [attack, defense] pairs for each character.
    :return: int - The number of weak characters.
    """
    # Sort properties by attack in descending order, and by defense in ascending order if attacks are equal
    properties.sort(key=lambda x: (-x[0], x[1]))
    
    max_defense = 0  # Tracks the maximum defense encountered so far
    weak_characters = 0  # Count of weak characters
    
    for _, defense in properties:
        # If the current character's defense is less than the max defense seen so far, it is weak
        if defense < max_defense:
            weak_characters += 1
        else:
            max_defense = defense  # Update max defense
    
    return weak_characters

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    properties1 = [[5,5],[6,3],[3,6]]
    print(numberOfWeakCharacters(properties1))  # Output: 0

    # Test Case 2
    properties2 = [[2,2],[3,3]]
    print(numberOfWeakCharacters(properties2))  # Output: 1

    # Test Case 3
    properties3 = [[1,5],[10,4],[4,3]]
    print(numberOfWeakCharacters(properties3))  # Output: 1

    # Additional Test Case
    properties4 = [[1,1],[2,1],[2,2],[1,2]]
    print(numberOfWeakCharacters(properties4))  # Output: 1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Sorting the properties array takes O(n log n), where n is the number of characters.
- Iterating through the sorted array takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- Sorting the array requires O(n) space in the worst case for the sorting algorithm.
- No additional data structures are used, so the space complexity is O(1) (excluding input storage).
- Overall space complexity: O(n).

Topic: Arrays, Sorting, Greedy
"""