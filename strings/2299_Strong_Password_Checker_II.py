"""
LeetCode Problem #2299: Strong Password Checker II

Problem Statement:
A password is considered strong if the following conditions are all met:
1. It has at least 8 characters.
2. It contains at least one lowercase letter.
3. It contains at least one uppercase letter.
4. It contains at least one digit.
5. It contains at least one special character. The special characters are: "!@#$%^&*()-+".
6. It does not contain two of the same character in adjacent positions (e.g., "aa" is weak, but "ab" is strong).

Given a string password, return true if it is a strong password. Otherwise, return false.

Constraints:
- 1 <= password.length <= 100
- password consists of letters, digits, and special characters: "!@#$%^&*()-+".
"""

# Solution
def strongPasswordCheckerII(password: str) -> bool:
    # Check if the password has at least 8 characters
    if len(password) < 8:
        return False
    
    # Initialize flags for each condition
    has_lower = has_upper = has_digit = has_special = False
    special_characters = set("!@#$%^&*()-+")
    
    # Iterate through the password to check conditions
    for i in range(len(password)):
        char = password[i]
        
        # Check for lowercase letter
        if char.islower():
            has_lower = True
        
        # Check for uppercase letter
        if char.isupper():
            has_upper = True
        
        # Check for digit
        if char.isdigit():
            has_digit = True
        
        # Check for special character
        if char in special_characters:
            has_special = True
        
        # Check for adjacent duplicate characters
        if i > 0 and password[i] == password[i - 1]:
            return False
    
    # Return true if all conditions are met
    return has_lower and has_upper and has_digit and has_special

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Strong password
    password1 = "Aa1!aa1!"
    print(strongPasswordCheckerII(password1))  # Expected: True

    # Test Case 2: Too short
    password2 = "Aa1!"
    print(strongPasswordCheckerII(password2))  # Expected: False

    # Test Case 3: Missing special character
    password3 = "Aa1aa1aa"
    print(strongPasswordCheckerII(password3))  # Expected: False

    # Test Case 4: Adjacent duplicate characters
    password4 = "Aa1!!aa1"
    print(strongPasswordCheckerII(password4))  # Expected: False

    # Test Case 5: Missing uppercase letter
    password5 = "aa1!aa1!"
    print(strongPasswordCheckerII(password5))  # Expected: False

    # Test Case 6: Missing lowercase letter
    password6 = "AA1!AA1!"
    print(strongPasswordCheckerII(password6))  # Expected: False

    # Test Case 7: Missing digit
    password7 = "Aa!Aa!Aa!"
    print(strongPasswordCheckerII(password7))  # Expected: False

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the password string once, performing constant-time checks for each character.
- Therefore, the time complexity is O(n), where n is the length of the password.

Space Complexity:
- The function uses a set to store special characters, which is a constant size.
- No additional space is used proportional to the input size.
- Therefore, the space complexity is O(1).
"""

# Topic: Strings