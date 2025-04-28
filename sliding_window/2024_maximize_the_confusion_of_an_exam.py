"""
LeetCode Question #2024: Maximize the Confusion of an Exam

Problem Statement:
A teacher is giving a test to students, and the test has `n` questions. The teacher knows the correct answers to each question, and the students' answers are stored in a string `answerKey`, where `answerKey[i]` is either `'T'` (True) or `'F'` (False). The teacher wants to maximize the number of consecutive answers that are either all `'T'` or all `'F'` by changing at most `k` answers in the string.

Given a string `answerKey` and an integer `k`, return the maximum number of consecutive `'T'` or `'F'` answers that can be achieved by changing at most `k` answers.

Constraints:
- `n == len(answerKey)`
- `1 <= n <= 10^5`
- `answerKey[i]` is either `'T'` or `'F'`
- `0 <= k <= n`
"""

# Solution
def maxConsecutiveAnswers(answerKey: str, k: int) -> int:
    def maxConsecutiveChar(char: str) -> int:
        left = 0
        max_length = 0
        changes = 0

        for right in range(len(answerKey)):
            if answerKey[right] != char:
                changes += 1

            while changes > k:
                if answerKey[left] != char:
                    changes -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length

    return max(maxConsecutiveChar('T'), maxConsecutiveChar('F'))

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    answerKey = "TTFF"
    k = 2
    print(maxConsecutiveAnswers(answerKey, k))  # Output: 4

    # Test Case 2
    answerKey = "TFFT"
    k = 1
    print(maxConsecutiveAnswers(answerKey, k))  # Output: 3

    # Test Case 3
    answerKey = "TTFTTFTT"
    k = 1
    print(maxConsecutiveAnswers(answerKey, k))  # Output: 5

    # Test Case 4
    answerKey = "TFTFTFTF"
    k = 2
    print(maxConsecutiveAnswers(answerKey, k))  # Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function `maxConsecutiveChar` iterates through the string `answerKey` using a sliding window approach.
- Each character is processed at most twice (once when expanding the window and once when contracting it).
- Therefore, the time complexity for each call to `maxConsecutiveChar` is O(n), where `n` is the length of `answerKey`.
- Since we call `maxConsecutiveChar` twice (once for `'T'` and once for `'F'`), the overall time complexity is O(2n) = O(n).

Space Complexity:
- The function uses a constant amount of extra space (variables like `left`, `right`, `changes`, and `max_length`).
- Therefore, the space complexity is O(1).

Topic: Sliding Window
"""