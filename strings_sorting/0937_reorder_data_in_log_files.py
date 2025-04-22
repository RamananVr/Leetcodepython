"""
LeetCode Question #937: Reorder Data in Log Files

Problem Statement:
You are given an array of logs. Each log is a space-delimited string of words, where the first word is an identifier.

There are two types of logs:
1. Letter-logs: All words (except the identifier) consist of lowercase English letters.
2. Digit-logs: All words (except the identifier) consist of digits.

Reorder the logs so that:
1. The letter-logs come before all digit-logs.
2. The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
3. The digit-logs should remain in the same order as they appear in the input.

Return the final order of the logs.

Example:
Input: logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
Output: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

Constraints:
- 1 <= logs.length <= 100
- 3 <= logs[i].length <= 100
- logs[i] consists of a lowercase English letter, a digit, and a space.
- The identifier is guaranteed to be unique for each log.
"""

# Solution
from typing import List

def reorderLogFiles(logs: List[str]) -> List[str]:
    # Separate logs into letter-logs and digit-logs
    letter_logs = []
    digit_logs = []
    
    for log in logs:
        identifier, rest = log.split(" ", 1)
        if rest[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append((rest, identifier))
    
    # Sort letter-logs by content, and then by identifier
    letter_logs.sort(key=lambda x: (x[0], x[1]))
    
    # Combine sorted letter-logs and original digit-logs
    return [f"{identifier} {content}" for content, identifier in letter_logs] + digit_logs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
    print(reorderLogFiles(logs1))  # Expected: ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"]

    # Test Case 2
    logs2 = ["let1 abc def", "let2 abc def", "dig1 123 456", "dig2 789 101"]
    print(reorderLogFiles(logs2))  # Expected: ["let1 abc def", "let2 abc def", "dig1 123 456", "dig2 789 101"]

    # Test Case 3
    logs3 = ["dig1 8 1 5 1", "dig2 3 6", "let1 art can"]
    print(reorderLogFiles(logs3))  # Expected: ["let1 art can", "dig1 8 1 5 1", "dig2 3 6"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting each log into identifier and content takes O(L), where L is the average length of a log.
- Sorting the letter-logs takes O(M * log(M)), where M is the number of letter-logs.
- Combining the results takes O(N), where N is the total number of logs.
Overall, the time complexity is O(N * log(M) + L), where N is the total number of logs and L is the average length of a log.

Space Complexity:
- The space complexity is O(N) for storing the letter-logs and digit-logs separately.
- Sorting the letter-logs also requires O(M) space for intermediate storage.
Overall, the space complexity is O(N).
"""

# Topic: Strings, Sorting