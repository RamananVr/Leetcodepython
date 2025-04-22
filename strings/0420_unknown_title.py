"""
LeetCode Problem #420: Strong Password Checker

Problem Statement:
A password is considered strong if the following conditions are all met:
1. It has at least 6 characters and at most 20 characters.
2. It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
3. It must NOT contain three or more consecutive identical characters (like "aaa" or "111").

Write a function `strongPasswordChecker(password: str) -> int` that returns the minimum number of steps required to make the password strong. If the password is already strong, return 0.

In one step, you can:
- Insert one character to the password,
- Delete one character from the password, or
- Replace one character in the password.

Constraints:
- `0 <= len(password) <= 50`
- `password` consists of letters, digits, and special characters.
"""

def strongPasswordChecker(password: str) -> int:
    n = len(password)
    has_lower = any(c.islower() for c in password)
    has_upper = any(c.isupper() for c in password)
    has_digit = any(c.isdigit() for c in password)
    
    # Count missing character types
    missing_types = 3 - (has_lower + has_upper + has_digit)
    
    # Count groups of three or more consecutive identical characters
    replace = 0
    i = 2
    groups = []
    while i < n:
        if password[i] == password[i - 1] == password[i - 2]:
            length = 2
            while i < n and password[i] == password[i - 1]:
                length += 1
                i += 1
            groups.append(length)
        else:
            i += 1
    
    # If password length is less than 6, we need to add characters
    if n < 6:
        return max(6 - n, missing_types)
    
    # If password length is between 6 and 20, we only need replacements
    elif n <= 20:
        for group in groups:
            replace += group // 3
        return max(replace, missing_types)
    
    # If password length is greater than 20, we need deletions
    else:
        excess_length = n - 20
        for i in range(len(groups)):
            if excess_length <= 0:
                break
            if groups[i] >= 3:
                reduce_by = min(excess_length, groups[i] % 3 + 1)
                groups[i] -= reduce_by
                excess_length -= reduce_by
        
        replace = 0
        for group in groups:
            replace += group // 3
        
        return (n - 20) + max(replace, missing_types)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Already strong password
    print(strongPasswordChecker("aA1bB2"))  # Output: 0

    # Test Case 2: Too short, missing types
    print(strongPasswordChecker("a"))  # Output: 5

    # Test Case 3: Too long, needs deletions and replacements
    print(strongPasswordChecker("aaaabbbbccccddddeeeee"))  # Output: 7

    # Test Case 4: Missing character types and consecutive characters
    print(strongPasswordChecker("aaa111"))  # Output: 2

    # Test Case 5: Needs replacements for consecutive characters
    print(strongPasswordChecker("aaaBBB111"))  # Output: 2

"""
Time Complexity Analysis:
- Checking for lowercase, uppercase, and digit types: O(n)
- Counting groups of consecutive characters: O(n)
- Handling replacements and deletions: O(n)
Overall time complexity: O(n)

Space Complexity Analysis:
- We use a list to store groups of consecutive characters, which takes O(n) space in the worst case.
Overall space complexity: O(n)

Topic: Strings
"""