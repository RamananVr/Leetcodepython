"""
LeetCode Problem #1653: Minimum Deletions to Make String Balanced

Problem Statement:
You are given a string `s` consisting only of characters 'a' and 'b'. You can delete any number of characters in the string.

A string is considered balanced if there are no two indices `i` and `j` such that `i < j` and `s[i] = 'b'` and `s[j] = 'a'`. In other words, all the 'b's in the string must appear before all the 'a's.

Return the minimum number of deletions needed to make the string balanced.

Constraints:
- 1 <= s.length <= 10^5
- s[i] is either 'a' or 'b'.
"""

def minimumDeletions(s: str) -> int:
    """
    This function calculates the minimum number of deletions required to make the string balanced.
    """
    # Count the total number of 'a' characters in the string
    total_a = s.count('a')
    
    # Initialize variables to track the minimum deletions and the count of 'a' and 'b' seen so far
    min_deletions = float('inf')
    count_a = 0
    count_b = 0
    
    for char in s:
        if char == 'a':
            # If the current character is 'a', we increment the count of 'a' seen so far
            count_a += 1
        else:
            # If the current character is 'b', we increment the count of 'b' seen so far
            count_b += 1
        
        # Calculate the deletions needed to make the string balanced at this point
        # Deletions = 'b's before this point + 'a's after this point
        deletions = count_b + (total_a - count_a)
        min_deletions = min(min_deletions, deletions)
    
    # Return the minimum deletions found
    return min_deletions

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    s1 = "aababbab"
    print(f"Minimum deletions for '{s1}': {minimumDeletions(s1)}")  # Expected output: 2

    # Test Case 2
    s2 = "bbaaaaabb"
    print(f"Minimum deletions for '{s2}': {minimumDeletions(s2)}")  # Expected output: 2

    # Test Case 3
    s3 = "ababab"
    print(f"Minimum deletions for '{s3}': {minimumDeletions(s3)}")  # Expected output: 3

    # Test Case 4
    s4 = "bbbb"
    print(f"Minimum deletions for '{s4}': {minimumDeletions(s4)}")  # Expected output: 0

    # Test Case 5
    s5 = "aaaa"
    print(f"Minimum deletions for '{s5}': {minimumDeletions(s5)}")  # Expected output: 0

"""
Time Complexity Analysis:
- The solution iterates through the string once to count the total number of 'a's (O(n)).
- Then, it iterates through the string again to calculate the minimum deletions (O(n)).
- Overall time complexity: O(n), where n is the length of the string.

Space Complexity Analysis:
- The solution uses a constant amount of extra space for variables like `total_a`, `count_a`, `count_b`, and `min_deletions`.
- Overall space complexity: O(1).

Topic: String, Prefix Sum
"""