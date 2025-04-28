"""
LeetCode Problem #1974: Minimum Time to Type Word Using Special Typewriter

Problem Statement:
There is a special typewriter with lowercase English letters 'a' to 'z' arranged in a circle. 
The typewriter has a pointer initially pointing to the character 'a'. 
You can perform one of the following operations at a time:

1. Move the pointer one character counterclockwise or clockwise for 1 second.
2. Type the character the pointer is currently on for 1 second.

Given a string `word`, return the minimum time required to type the string.

Example:
Input: word = "abc"
Output: 5
Explanation: 
- The pointer is initially on 'a'.
- Move to 'b' in 1 second, type 'b' in 1 second.
- Move to 'c' in 1 second, type 'c' in 1 second.
- Type 'a' in 1 second.
Total time = 5 seconds.

Constraints:
- 1 <= word.length <= 100
- word consists of lowercase English letters.
"""

# Clean, Correct Python Solution
def minTimeToType(word: str) -> int:
    # Initialize the pointer at 'a' and the total time to 0
    pointer = 'a'
    total_time = 0

    for char in word:
        # Calculate the clockwise and counterclockwise distances
        clockwise_distance = abs(ord(char) - ord(pointer))
        counterclockwise_distance = 26 - clockwise_distance

        # Add the minimum distance to the total time
        total_time += min(clockwise_distance, counterclockwise_distance)

        # Add 1 second for typing the character
        total_time += 1

        # Update the pointer to the current character
        pointer = char

    return total_time

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    word1 = "abc"
    print(f"Minimum time to type '{word1}': {minTimeToType(word1)}")  # Expected Output: 5

    # Test Case 2
    word2 = "bza"
    print(f"Minimum time to type '{word2}': {minTimeToType(word2)}")  # Expected Output: 7

    # Test Case 3
    word3 = "zjpc"
    print(f"Minimum time to type '{word3}': {minTimeToType(word3)}")  # Expected Output: 34

    # Test Case 4
    word4 = "a"
    print(f"Minimum time to type '{word4}': {minTimeToType(word4)}")  # Expected Output: 1

    # Test Case 5
    word5 = "azazaz"
    print(f"Minimum time to type '{word5}': {minTimeToType(word5)}")  # Expected Output: 18

# Time and Space Complexity Analysis
"""
Time Complexity:
- The algorithm iterates through each character in the input string `word`.
- For each character, it performs constant-time operations (calculating distances and updating variables).
- Therefore, the time complexity is O(n), where n is the length of the string `word`.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables like `pointer` and `total_time`.
- No additional data structures are used.
- Therefore, the space complexity is O(1).
"""

# Topic: Strings, Simulation