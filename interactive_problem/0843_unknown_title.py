"""
LeetCode Problem #843: Guess the Word

Problem Statement:
This is an interactive problem.

You are given an array of unique strings `wordlist` where `wordlist[i]` is 6 letters long, and one of these strings is the secret word.

You want to guess the secret word by interacting with the `Master` API:
- `master.guess(word)`:
  - Returns an integer `match` representing the number of exact matches (letter and position) between `word` and the secret word.
  - If `word` is not the secret word, you can continue guessing.

There is a limit of 10 guesses. You can assume that the secret word exists in `wordlist`.

Constraints:
- `wordlist` contains unique strings.
- Each string in `wordlist` is 6 letters long.
- The secret word is guaranteed to be in `wordlist`.

Your goal is to implement the function `findSecretWord(wordlist: List[str], master: Master) -> None` to find the secret word within 10 guesses.

"""

from typing import List

class Master:
    def guess(self, word: str) -> int:
        """
        Simulates the Master API. This method is provided by the problem and should not be implemented by the user.
        """
        pass

def findSecretWord(wordlist: List[str], master: Master) -> None:
    """
    Function to find the secret word using the Master API.
    """
    def match_count(word1: str, word2: str) -> int:
        """
        Helper function to calculate the number of matching characters at the same positions between two words.
        """
        return sum(c1 == c2 for c1, c2 in zip(word1, word2))

    for _ in range(10):  # Limit of 10 guesses
        # Choose the word with the minimum maximum overlap with other words
        # This helps reduce the search space efficiently
        count = {word: sum(match_count(word, other) == 0 for other in wordlist) for word in wordlist}
        guess_word = min(wordlist, key=lambda w: count[w])
        
        match = master.guess(guess_word)
        if match == 6:  # Found the secret word
            return
        
        # Filter the wordlist to only include words with the same match count
        wordlist = [word for word in wordlist if match_count(guess_word, word) == match]

# Example Test Cases
class MockMaster(Master):
    def __init__(self, secret: str):
        self.secret = secret
        self.guess_count = 0

    def guess(self, word: str) -> int:
        self.guess_count += 1
        return sum(c1 == c2 for c1, c2 in zip(word, self.secret))

if __name__ == "__main__":
    # Test Case 1
    wordlist = ["acckzz", "ccbazz", "eiowzz", "abcczz"]
    secret = "acckzz"
    master = MockMaster(secret)
    findSecretWord(wordlist, master)
    print(f"Guesses made: {master.guess_count}")  # Expected: <= 10

    # Test Case 2
    wordlist = ["hamada", "khaled", "nasser", "ahmeda", "hamada"]
    secret = "hamada"
    master = MockMaster(secret)
    findSecretWord(wordlist, master)
    print(f"Guesses made: {master.guess_count}")  # Expected: <= 10

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm performs up to 10 guesses.
- For each guess, it calculates the match count for all pairs of words in the wordlist.
- Let `n` be the number of words in the wordlist and `m` be the length of each word (6 in this problem).
- Calculating match_count for two words takes O(m) time.
- Filtering the wordlist takes O(n * m) time.
- Overall, the time complexity is O(10 * n * m), which simplifies to O(n * m).

Space Complexity:
- The algorithm uses a dictionary to store the count of overlaps, which takes O(n) space.
- The filtered wordlist also takes O(n) space.
- Overall, the space complexity is O(n).

Topic: Interactive Problem
"""