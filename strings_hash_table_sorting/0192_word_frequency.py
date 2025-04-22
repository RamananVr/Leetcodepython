"""
LeetCode Question #192: Word Frequency

Problem Statement:
Write a bash script to calculate the frequency of each word in a text file `words.txt`.

- The `words.txt` file contains words separated by one or more spaces.
- For each word, output its frequency in descending order. If two words have the same frequency, then the word with the lexicographical order comes first.
- Each word must appear in a new line in the format: `word count`.

Example:
Assume that `words.txt` has the following content:
```
the day is sunny the the
the sunny is is
```

Your script should output the following, sorted by descending frequency:
```
the 4
is 3
sunny 2
day 1
```

Note:
- Do not use any extra libraries like `awk` or `sed`.
- The output should be case-sensitive (e.g., "The" and "the" are different words).

Since this is a bash problem, we will provide a Python solution that mimics the behavior of the bash script for educational purposes.
"""

# Python Solution
from collections import Counter

def word_frequency(file_path):
    """
    Reads a file and calculates the frequency of each word, then returns the result
    sorted by descending frequency and lexicographical order for ties.

    :param file_path: Path to the input file containing words
    :return: List of tuples with word and its frequency
    """
    with open(file_path, 'r') as file:
        # Read all lines and split into words
        words = file.read().split()
    
    # Count the frequency of each word
    word_count = Counter(words)
    
    # Sort by frequency (descending) and then by word (lexicographical order)
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    return sorted_word_count

# Example Test Cases
if __name__ == "__main__":
    # Create a sample file for testing
    sample_file = "words.txt"
    with open(sample_file, "w") as f:
        f.write("the day is sunny the the\n")
        f.write("the sunny is is\n")
    
    # Call the function and print the result
    result = word_frequency(sample_file)
    for word, count in result:
        print(f"{word} {count}")

"""
Expected Output:
the 4
is 3
sunny 2
day 1
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Reading the file: O(n), where n is the total number of characters in the file.
- Splitting into words: O(n), where n is the total number of characters in the file.
- Counting word frequencies: O(m), where m is the total number of words.
- Sorting the word frequencies: O(k log k), where k is the number of unique words.

Overall Time Complexity: O(n + k log k), where n is the total number of characters in the file and k is the number of unique words.

Space Complexity:
- Storing the words in memory: O(m), where m is the total number of words.
- Storing the word frequency dictionary: O(k), where k is the number of unique words.

Overall Space Complexity: O(m + k).
"""

# Topic: Strings, Hash Table, Sorting