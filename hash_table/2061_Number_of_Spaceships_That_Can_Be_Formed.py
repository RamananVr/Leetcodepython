"""
LeetCode Problem #2061: Number of Spaceships That Can Be Formed

Problem Statement:
You are given a list of strings `words` and a string `target`. Each string in `words` represents a spaceship part, 
and the string `target` represents the spaceship you want to form. A spaceship can be formed if you can use the 
characters from the strings in `words` to exactly match the characters in `target`. Each character in `words` can 
only be used once per spaceship, and you can use multiple strings from `words` to form the spaceship.

Return the maximum number of spaceships that can be formed.

Constraints:
- 1 <= len(words) <= 1000
- 1 <= len(words[i]) <= 100
- 1 <= len(target) <= 100
- `words[i]` and `target` consist of lowercase English letters only.
"""

from collections import Counter

def maxNumberOfSpaceships(words, target):
    """
    Calculate the maximum number of spaceships that can be formed using the given words.

    :param words: List[str] - List of strings representing spaceship parts.
    :param target: str - The target spaceship string.
    :return: int - Maximum number of spaceships that can be formed.
    """
    # Count the frequency of each character in the words list
    total_char_count = Counter()
    for word in words:
        total_char_count.update(word)
    
    # Count the frequency of each character in the target string
    target_char_count = Counter(target)
    
    # Calculate the maximum number of spaceships that can be formed
    max_spaceships = float('inf')
    for char, count in target_char_count.items():
        if char not in total_char_count:
            return 0  # If a required character is missing, no spaceship can be formed
        max_spaceships = min(max_spaceships, total_char_count[char] // count)
    
    return max_spaceships


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    words1 = ["abc", "aabc", "bc"]
    target1 = "abc"
    print(maxNumberOfSpaceships(words1, target1))  # Output: 2

    # Test Case 2
    words2 = ["ab", "bc", "ca"]
    target2 = "abc"
    print(maxNumberOfSpaceships(words2, target2))  # Output: 1

    # Test Case 3
    words3 = ["a", "b", "c", "d"]
    target3 = "abcd"
    print(maxNumberOfSpaceships(words3, target3))  # Output: 1

    # Test Case 4
    words4 = ["a", "b", "c"]
    target4 = "abcd"
    print(maxNumberOfSpaceships(words4, target4))  # Output: 0

    # Test Case 5
    words5 = ["abc", "abc", "abc"]
    target5 = "aaa"
    print(maxNumberOfSpaceships(words5, target5))  # Output: 1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Counting characters in `words` takes O(n * m), where `n` is the number of words and `m` is the average length of a word.
- Counting characters in `target` takes O(t), where `t` is the length of the target string.
- Iterating through the `target_char_count` dictionary takes O(t).
- Overall time complexity: O(n * m + t).

Space Complexity:
- The `total_char_count` and `target_char_count` dictionaries store character frequencies.
- The space complexity is O(u), where `u` is the number of unique characters in `words` and `target`.
- Overall space complexity: O(u).

Topic: Hash Table
"""