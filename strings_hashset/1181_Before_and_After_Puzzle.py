"""
LeetCode Problem #1181: Before and After Puzzle

Problem Statement:
Given a list of phrases `phrases`, generate a list of "before and after puzzles". A "before and after puzzle" is a phrase formed by merging two phrases where the last word of the first phrase is the same as the first word of the second phrase.

Return the puzzles in sorted order without duplicates.

Example:
Input: phrases = ["writing code", "code rocks"]
Output: ["writing code rocks"]

Constraints:
1. 1 <= phrases.length <= 100
2. 1 <= phrases[i].length <= 100
3. phrases[i] consists of English letters and spaces.
4. There are no leading or trailing spaces in phrases[i].
5. All words in phrases[i] are separated by a single space.
"""

# Solution
def before_and_after_puzzles(phrases):
    """
    Generate a list of "before and after puzzles" from the given phrases.

    :param phrases: List[str] - List of phrases
    :return: List[str] - Sorted list of unique puzzles
    """
    puzzles = set()
    
    # Iterate through all pairs of phrases
    for i in range(len(phrases)):
        for j in range(len(phrases)):
            if i != j:
                # Split phrases into words
                first_phrase = phrases[i].split()
                second_phrase = phrases[j].split()
                
                # Check if the last word of the first phrase matches the first word of the second phrase
                if first_phrase[-1] == second_phrase[0]:
                    # Merge the two phrases
                    merged_phrase = " ".join(first_phrase + second_phrase[1:])
                    puzzles.add(merged_phrase)
    
    # Return sorted list of unique puzzles
    return sorted(puzzles)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    phrases = ["writing code", "code rocks"]
    print(before_and_after_puzzles(phrases))  # Output: ["writing code rocks"]

    # Test Case 2
    phrases = ["a quick brown fox", "fox jumps", "jumps over", "over the lazy dog"]
    print(before_and_after_puzzles(phrases))  
    # Output: ["a quick brown fox jumps", "fox jumps over", "jumps over the lazy dog"]

    # Test Case 3
    phrases = ["hello world", "world peace", "peace out"]
    print(before_and_after_puzzles(phrases))  
    # Output: ["hello world peace", "world peace out"]

    # Test Case 4
    phrases = ["abc def", "def ghi", "ghi abc"]
    print(before_and_after_puzzles(phrases))  
    # Output: ["abc def ghi", "def ghi abc", "ghi abc def"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting each phrase into words takes O(L), where L is the average length of a phrase.
- Comparing the last word of one phrase with the first word of another takes O(1).
- Iterating through all pairs of phrases takes O(N^2), where N is the number of phrases.
- Adding a merged phrase to the set takes O(L) in the worst case.
- Sorting the final list of puzzles takes O(P log P), where P is the number of unique puzzles.

Overall time complexity: O(N^2 * L + P log P)

Space Complexity:
- The set `puzzles` stores up to O(N^2) merged phrases, each of length O(L).
- The space required for splitting phrases into words is O(L) per phrase.

Overall space complexity: O(N^2 * L)
"""

# Topic: Strings, HashSet