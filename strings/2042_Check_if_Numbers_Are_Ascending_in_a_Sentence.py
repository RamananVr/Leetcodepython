"""
LeetCode Problem #2042: Check if Numbers Are Ascending in a Sentence

Problem Statement:
A sentence is a list of tokens separated by a single space with no leading or trailing spaces. 
Every token is either a positive number consisting of digits 0-9 with no leading zeros, or a word 
consisting of lowercase English letters.

- For example, "a puppy has 2 eyes 4 legs" is a sentence with tokens ["a", "puppy", "has", "2", "eyes", "4", "legs"].

You are given a string `s` representing a sentence. You need to check if all the numbers in the 
sentence are strictly increasing from left to right (ignoring all words).

- For example, in the sentence "1 box has 3 blue 4 red 6 green and 12 yellow marbles", the numbers 
  are [1, 3, 4, 6, 12], which are strictly increasing.

Return `true` if so, or `false` otherwise.

Constraints:
1. 1 <= s.length <= 1000
2. s consists of lowercase English letters, spaces, and digits.
3. The tokens in s are separated by a single space.
4. There are at least two tokens in s.
"""

def areNumbersAscending(s: str) -> bool:
    """
    Function to check if all numbers in the sentence are strictly increasing.
    
    :param s: A string representing the sentence.
    :return: True if numbers are strictly increasing, False otherwise.
    """
    prev_num = -1  # Initialize the previous number to a very small value
    for token in s.split():
        if token.isdigit():  # Check if the token is a number
            current_num = int(token)
            if current_num <= prev_num:  # If the current number is not greater than the previous
                return False
            prev_num = current_num  # Update the previous number
    return True


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Numbers are strictly increasing
    s1 = "1 box has 3 blue 4 red 6 green and 12 yellow marbles"
    print(areNumbersAscending(s1))  # Expected: True

    # Test Case 2: Numbers are not strictly increasing
    s2 = "hello world 5 x 5"
    print(areNumbersAscending(s2))  # Expected: False

    # Test Case 3: No numbers in the sentence
    s3 = "this is a test sentence"
    print(areNumbersAscending(s3))  # Expected: True (no numbers means no violation)

    # Test Case 4: Single number in the sentence
    s4 = "there is only 1 number here"
    print(areNumbersAscending(s4))  # Expected: True

    # Test Case 5: Numbers are equal (not strictly increasing)
    s5 = "1 2 2 3"
    print(areNumbersAscending(s5))  # Expected: False

    # Test Case 6: Large numbers in the sentence
    s6 = "10 20 30 40 50"
    print(areNumbersAscending(s6))  # Expected: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the string into tokens takes O(n), where n is the length of the string.
- Iterating through the tokens and checking if they are digits also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The space required for splitting the string into tokens is O(n) in the worst case.
- No additional data structures are used, so the space complexity is O(n).

Topic: Strings
"""