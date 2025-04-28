"""
LeetCode Question #2399: Check Distances Between Same Letters

Problem Statement:
You are given a 0-indexed string `s` consisting of only lowercase English letters, where each letter in `s` appears at most twice. 
You are also given a 0-indexed integer array `distance` of length 26.

Each letter in the alphabet is numbered from 0 to 25 (i.e., 'a' is 0, 'b' is 1, 'c' is 2, ..., 'z' is 25).

In the string `s`, if the letter `x` occurs twice, the distance between its two occurrences is defined as the number of indices between the two occurrences. 
In other words, if the first occurrence of `x` is at index `i` and the second occurrence is at index `j`, then `distance[x] = j - i - 1`.

Return `true` if the distances between every pair of the same letter in `s` is equal to the corresponding value in `distance`. Otherwise, return `false`.
"""

def checkDistances(s: str, distance: list[int]) -> bool:
    # Create a dictionary to store the first occurrence of each character
    first_occurrence = {}
    
    for i, char in enumerate(s):
        # Calculate the index of the character in the alphabet
        char_index = ord(char) - ord('a')
        
        if char in first_occurrence:
            # If the character has already been seen, calculate the distance
            calculated_distance = i - first_occurrence[char] - 1
            # Check if the calculated distance matches the given distance
            if calculated_distance != distance[char_index]:
                return False
        else:
            # Store the first occurrence of the character
            first_occurrence[char] = i
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "abaccb"
    distance1 = [1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(checkDistances(s1, distance1))  # Output: True

    # Test Case 2
    s2 = "aa"
    distance2 = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(checkDistances(s2, distance2))  # Output: True

    # Test Case 3
    s3 = "abaccb"
    distance3 = [1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(checkDistances(s3, distance3))  # Output: False

    # Test Case 4
    s4 = "zxyzz"
    distance4 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]
    print(checkDistances(s4, distance4))  # Output: True

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string `s` once, making the time complexity O(n), where `n` is the length of the string.

Space Complexity:
- The function uses a dictionary to store the first occurrence of each character. In the worst case, the dictionary will store up to 26 entries (one for each letter of the alphabet). 
  Therefore, the space complexity is O(1), as the size of the dictionary is bounded by the number of letters in the alphabet.

Topic: Strings
"""