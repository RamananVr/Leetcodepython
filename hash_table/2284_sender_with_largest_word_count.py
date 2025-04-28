"""
LeetCode Question #2284: Sender With Largest Word Count

Problem Statement:
You have a chat log of `n` messages. Each message is represented as a string `message[i]` and was sent by a user `sender[i]`.

A word is defined as a sequence of non-space characters. A sender's word count is the total number of words sent by the sender. Note that a sender may send multiple messages.

Return the sender with the largest word count. If there is a tie, return the sender with the lexicographically largest name.

Example:
Input: messages = ["Hello userTwo", "Hi userThree", "Wonderful day userTwo"], senders = ["userOne", "userTwo", "userThree"]
Output: "userTwo"

Constraints:
- `n == len(messages) == len(senders)`
- `1 <= n <= 10^4`
- `1 <= len(messages[i]) <= 100`
- `1 <= len(senders[i]) <= 10`
- `messages[i]` consists of uppercase and lowercase English letters and spaces.
- `senders[i]` consists of uppercase and lowercase English letters only.
"""

# Python Solution
from collections import defaultdict

def largestWordCount(messages, senders):
    # Dictionary to store word count for each sender
    word_count = defaultdict(int)
    
    # Calculate word count for each sender
    for message, sender in zip(messages, senders):
        word_count[sender] += len(message.split())
    
    # Find the sender with the largest word count
    max_sender = max(word_count.keys(), key=lambda sender: (word_count[sender], sender))
    
    return max_sender

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    messages1 = ["Hello userTwo", "Hi userThree", "Wonderful day userTwo"]
    senders1 = ["userOne", "userTwo", "userThree"]
    print(largestWordCount(messages1, senders1))  # Output: "userTwo"

    # Test Case 2
    messages2 = ["How are you", "I am fine", "Thank you"]
    senders2 = ["Alice", "Bob", "Alice"]
    print(largestWordCount(messages2, senders2))  # Output: "Alice"

    # Test Case 3
    messages3 = ["Hi", "Hello", "Hey"]
    senders3 = ["Charlie", "Charlie", "Charlie"]
    print(largestWordCount(messages3, senders3))  # Output: "Charlie"

    # Test Case 4
    messages4 = ["Hi there", "Hello world", "Good morning"]
    senders4 = ["Zoe", "Alice", "Zoe"]
    print(largestWordCount(messages4, senders4))  # Output: "Zoe"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting each message into words takes O(m), where m is the total number of characters across all messages.
- Iterating through the `messages` and `senders` arrays takes O(n), where n is the number of messages.
- Finding the sender with the maximum word count takes O(k), where k is the number of unique senders.
- Overall time complexity: O(m + n + k).

Space Complexity:
- The `word_count` dictionary stores word counts for up to k unique senders, which takes O(k) space.
- Overall space complexity: O(k).
"""

# Topic: Hash Table