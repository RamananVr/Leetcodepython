"""
LeetCode Question #38: Count and Say

Problem Statement:
The "Count and Say" sequence is a sequence of digit strings defined by the recursive formula:

- countAndSay(1) = "1"
- countAndSay(n) is the string you get by reading the previous term (countAndSay(n-1)), describing the count of each group of consecutive digits in it.

To determine the next term, you count the number of digits (in groups) and say the digit. For example:
- The term "1" translates to "one 1" → "11".
- The term "11" translates to "two 1s" → "21".
- The term "21" translates to "one 2, then one 1" → "1211".

Given a positive integer n, return the nth term of the "Count and Say" sequence.

Constraints:
- 1 <= n <= 30
"""

def countAndSay(n: int) -> str:
    def next_sequence(s: str) -> str:
        result = []
        count = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                count += 1
            else:
                result.append(str(count) + s[i - 1])
                count = 1
        result.append(str(count) + s[-1])  # Add the last group
        return ''.join(result)
    
    sequence = "1"
    for _ in range(n - 1):
        sequence = next_sequence(sequence)
    return sequence

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: n = 1
    print(countAndSay(1))  # Expected Output: "1"

    # Test Case 2: n = 4
    print(countAndSay(4))  # Expected Output: "1211"

    # Test Case 3: n = 6
    print(countAndSay(6))  # Expected Output: "312211"

    # Test Case 4: n = 10
    print(countAndSay(10))  # Expected Output: "13211311123113112211"

"""
Topic: Strings
"""