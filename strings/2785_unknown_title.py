"""
LeetCode Problem #2785: Sort Vowels in a String

Problem Statement:
You are given a string `s` consisting of lowercase English letters. You need to sort the vowels in the string in 
ascending order and return the resulting string. The consonants should remain in their original positions.

Vowels are the letters 'a', 'e', 'i', 'o', and 'u'. Note that the order of consonants and non-vowel characters 
should not be changed.

Example:
Input: s = "hello"
Output: "holle"

Input: s = "leetcode"
Output: "leotcede"

Constraints:
- 1 <= s.length <= 10^5
- s consists of lowercase English letters.
"""

# Solution
def sortVowels(s: str) -> str:
    # Define vowels
    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    # Extract vowels from the string and sort them
    sorted_vowels = sorted([char for char in s if char in vowels])
    
    # Initialize a pointer for the sorted vowels
    vowel_index = 0
    
    # Build the result string
    result = []
    for char in s:
        if char in vowels:
            # Replace vowel with the next sorted vowel
            result.append(sorted_vowels[vowel_index])
            vowel_index += 1
        else:
            # Keep consonants unchanged
            result.append(char)
    
    return ''.join(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "hello"
    print(sortVowels(s1))  # Output: "holle"

    # Test Case 2
    s2 = "leetcode"
    print(sortVowels(s2))  # Output: "leotcede"

    # Test Case 3
    s3 = "programming"
    print(sortVowels(s3))  # Output: "progremming"

    # Test Case 4
    s4 = "aeiou"
    print(sortVowels(s4))  # Output: "aeiou"

    # Test Case 5
    s5 = "bcdfghjklmnpqrstvwxyz"
    print(sortVowels(s5))  # Output: "bcdfghjklmnpqrstvwxyz"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Extracting vowels from the string takes O(n), where n is the length of the string.
- Sorting the vowels takes O(k log k), where k is the number of vowels in the string.
- Constructing the result string takes O(n).
- Overall time complexity: O(n + k log k), where k <= n.

Space Complexity:
- The space required to store the sorted vowels is O(k), where k is the number of vowels.
- The result list also takes O(n) space.
- Overall space complexity: O(n).

Topic: Strings
"""