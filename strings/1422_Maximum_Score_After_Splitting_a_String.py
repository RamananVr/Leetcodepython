"""
LeetCode Problem #1422: Maximum Score After Splitting a String

Problem Statement:
Given a string `s` of zeros and ones, you can split the string into two non-empty substrings 
(left and right) where the left substring contains the first `i` characters of the string 
and the right substring contains the remaining characters. 

The score after splitting the string is the number of zeros in the left substring plus the 
number of ones in the right substring.

Return the maximum score you can achieve after splitting the string.

Constraints:
- 2 <= s.length <= 500
- The string `s` consists of characters '0' and '1' only.
"""

def maxScore(s: str) -> int:
    """
    Function to calculate the maximum score after splitting the string.

    Args:
    s (str): The input binary string.

    Returns:
    int: The maximum score achievable.
    """
    # Initialize variables
    max_score = 0
    n = len(s)
    
    # Precompute the total number of ones in the string
    total_ones = s.count('1')
    
    # Initialize the count of zeros in the left substring
    left_zeros = 0
    # Initialize the count of ones in the right substring
    right_ones = total_ones
    
    # Iterate through the string, stopping before the last character
    for i in range(n - 1):
        if s[i] == '0':
            left_zeros += 1
        else:
            right_ones -= 1
        
        # Calculate the score for the current split
        current_score = left_zeros + right_ones
        # Update the maximum score
        max_score = max(max_score, current_score)
    
    return max_score

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "011101"
    print(maxScore(s1))  # Expected Output: 5

    # Test Case 2
    s2 = "00111"
    print(maxScore(s2))  # Expected Output: 5

    # Test Case 3
    s3 = "1111"
    print(maxScore(s3))  # Expected Output: 3

    # Test Case 4
    s4 = "0000"
    print(maxScore(s4))  # Expected Output: 3

    # Test Case 5
    s5 = "010101"
    print(maxScore(s5))  # Expected Output: 4

"""
Time and Space Complexity Analysis:

Time Complexity:
- The function iterates through the string once to count the total number of ones (O(n)).
- Then, it iterates through the string again to calculate the score for each split (O(n)).
- Overall time complexity: O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `max_score`, `left_zeros`, and `right_ones`.
- Overall space complexity: O(1).

Topic: Strings
"""