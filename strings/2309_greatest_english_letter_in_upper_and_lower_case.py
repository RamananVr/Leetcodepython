"""
LeetCode Question #2309: Greatest English Letter in Upper and Lower Case

Problem Statement:
Given a string `s` of English letters (both uppercase and lowercase), return the greatest English letter which exists in both uppercase and lowercase in `s`. 
The returned letter should be in uppercase. If no such letter exists, return an empty string.

Example:
Input: s = "lEeTcOdE"
Output: "E"
Explanation: The letter 'E' exists in both uppercase ('E') and lowercase ('e').

Input: s = "aA"
Output: "A"
Explanation: The letter 'A' exists in both uppercase ('A') and lowercase ('a').

Input: s = "abc"
Output: ""
Explanation: No letter exists in both uppercase and lowercase.

Constraints:
- 1 <= s.length <= 1000
- s consists of lowercase and uppercase English letters.
"""

# Python Solution
def greatest_letter(s: str) -> str:
    # Create sets for uppercase and lowercase letters in the string
    uppercase_set = set()
    lowercase_set = set()
    
    # Populate the sets
    for char in s:
        if char.isupper():
            uppercase_set.add(char)
        elif char.islower():
            lowercase_set.add(char)
    
    # Find the greatest letter that exists in both sets
    result = ""
    for char in uppercase_set:
        if char.lower() in lowercase_set:
            result = max(result, char)
    
    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "lEeTcOdE"
    print(greatest_letter(s1))  # Output: "E"

    # Test Case 2
    s2 = "aA"
    print(greatest_letter(s2))  # Output: "A"

    # Test Case 3
    s3 = "abc"
    print(greatest_letter(s3))  # Output: ""

    # Test Case 4
    s4 = "AbCdEfGhIjK"
    print(greatest_letter(s4))  # Output: "K"

    # Test Case 5
    s5 = "zZyYxX"
    print(greatest_letter(s5))  # Output: "Z"


# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the string `s` once to populate the sets, which takes O(n) time, where n is the length of the string.
- Then, it iterates through the uppercase set to find the greatest letter, which takes O(26) time (constant, as there are at most 26 uppercase letters).
- Overall, the time complexity is O(n).

Space Complexity:
- Two sets are used to store the uppercase and lowercase letters, which can each contain at most 26 elements.
- Therefore, the space complexity is O(1) (constant space usage).

Overall Complexity:
Time: O(n)
Space: O(1)
"""

# Topic: Strings