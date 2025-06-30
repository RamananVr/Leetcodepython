"""
2796. Repeat String

Problem Statement:
Given a string s, return a new string where each character in s is repeated according to its 
numeric value. If a character is not a digit, it should appear exactly once in the result.

The characters should appear in the same order as they appear in the original string.

Constraints:
- 1 <= s.length <= 100
- s consists of lowercase English letters and digits.

Test Cases:
1. Input: s = "a3b2c1"
   Output: "aaabbbc"
   
2. Input: s = "a12bc4d"
   Output: "aaaaaaaaaaaabbcccccd"
"""

def repeatString(s: str) -> str:
    """
    Repeat each character according to the digit that follows it.
    
    Algorithm:
    1. Iterate through the string
    2. For each character, check if next character is a digit
    3. If yes, repeat current character that many times
    4. If no, include character once
    
    Time Complexity: O(n * k) where k is average repeat count
    Space Complexity: O(n * k) for result string
    """
    result = []
    i = 0
    
    while i < len(s):
        char = s[i]
        
        # Check if current character is a digit
        if char.isdigit():
            i += 1
            continue
        
        # Check if next character is a digit
        if i + 1 < len(s) and s[i + 1].isdigit():
            repeat_count = int(s[i + 1])
            result.append(char * repeat_count)
            i += 2  # Skip both character and digit
        else:
            result.append(char)
            i += 1
    
    return ''.join(result)

def repeatStringOptimized(s: str) -> str:
    """
    Optimized version with single pass and list building.
    
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    result = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            i += 1
            continue
        
        char = s[i]
        repeat_count = 1
        
        # Look for following digits
        if i + 1 < len(s) and s[i + 1].isdigit():
            repeat_count = int(s[i + 1])
            i += 1  # Skip the digit
        
        # Add repeated character
        for _ in range(repeat_count):
            result.append(char)
        
        i += 1
    
    return ''.join(result)

def repeatStringWithMultipleDigits(s: str) -> str:
    """
    Handle multiple consecutive digits as a single number.
    
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    result = []
    i = 0
    
    while i < len(s):
        if s[i].isdigit():
            i += 1
            continue
        
        char = s[i]
        i += 1
        
        # Collect all consecutive digits
        num_str = ""
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        # Determine repeat count
        repeat_count = int(num_str) if num_str else 1
        
        # Add repeated character
        result.append(char * repeat_count)
    
    return ''.join(result)

def repeatStringRegex(s: str) -> str:
    """
    Using regular expressions to find character-digit patterns.
    
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    import re
    
    result = []
    
    # Find all character followed by optional digits
    pattern = r'([a-z])(\d*)'
    matches = re.findall(pattern, s)
    
    for char, digit_str in matches:
        repeat_count = int(digit_str) if digit_str else 1
        result.append(char * repeat_count)
    
    return ''.join(result)

def repeatStringIterative(s: str) -> str:
    """
    Simple iterative approach building result character by character.
    
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    result = ""
    i = 0
    
    while i < len(s):
        char = s[i]
        
        if char.isdigit():
            i += 1
            continue
        
        # Look ahead for digit
        repeat_count = 1
        if i + 1 < len(s) and s[i + 1].isdigit():
            repeat_count = int(s[i + 1])
            i += 1  # Skip digit
        
        # Repeat character
        result += char * repeat_count
        i += 1
    
    return result

def repeatStringWithValidation(s: str) -> str:
    """
    Version with input validation and edge case handling.
    
    Time Complexity: O(n * k)
    Space Complexity: O(n * k)
    """
    if not s:
        return ""
    
    result = []
    i = 0
    
    while i < len(s):
        char = s[i]
        
        if char.isdigit():
            i += 1
            continue
        
        if not char.islower():
            raise ValueError(f"Invalid character: {char}")
        
        repeat_count = 1
        if i + 1 < len(s) and s[i + 1].isdigit():
            digit = s[i + 1]
            repeat_count = int(digit)
            if repeat_count == 0:
                # Skip character if repeat count is 0
                i += 2
                continue
            i += 1
        
        result.append(char * repeat_count)
        i += 1
    
    return ''.join(result)

# Test cases
def test_repeat_string():
    # Test case 1
    s1 = "a3b2c1"
    result1 = repeatString(s1)
    print(f"Test 1 - Input: {s1}, Expected: aaabbbc, Got: {result1}")
    
    # Test case 2
    s2 = "a12bc4d"
    result2 = repeatStringWithMultipleDigits(s2)
    print(f"Test 2 - Input: {s2}, Expected: aaaaaaaaaaaabbcccccd, Got: {result2}")
    
    # Test case 3: No digits
    s3 = "abcd"
    result3 = repeatString(s3)
    print(f"Test 3 - Input: {s3}, Expected: abcd, Got: {result3}")
    
    # Test case 4: Only digits (should be ignored)
    s4 = "123"
    result4 = repeatString(s4)
    print(f"Test 4 - Input: {s4}, Expected: '', Got: '{result4}'")
    
    # Test case 5: Zero repeat
    s5 = "a0b2c"
    result5 = repeatStringWithValidation(s5)
    print(f"Test 5 - Input: {s5}, Expected: bbcc, Got: {result5}")

def test_all_solutions():
    test_input = "a3b2c1"
    
    result1 = repeatString(test_input)
    result2 = repeatStringOptimized(test_input)
    result3 = repeatStringIterative(test_input)
    result4 = repeatStringRegex(test_input)
    
    print(f"Original: {result1}")
    print(f"Optimized: {result2}")
    print(f"Iterative: {result3}")
    print(f"Regex: {result4}")
    print(f"All match: {result1 == result2 == result3 == result4}")

def test_edge_cases():
    # Empty string
    print(f"Empty string: '{repeatString('')}'")
    
    # Single character
    print(f"Single char 'a': '{repeatString('a')}'")
    
    # Single digit
    print(f"Single digit '5': '{repeatString('5')}'")
    
    # Character with large digit
    print(f"Large repeat 'a9': '{repeatString('a9')}'")

if __name__ == "__main__":
    test_repeat_string()
    print()
    test_all_solutions()
    print()
    test_edge_cases()

"""
Topic Classification: Strings, Simulation

Key Insights:
1. Need to distinguish between character-digit pairs and standalone digits
2. Digits should be treated as repeat counts, not characters to include
3. Can handle multi-digit numbers for larger repeat counts
4. Edge cases include zero repeats and no digits

Complexity Analysis:
- Time Complexity: O(n * k) where n is string length and k is average repeat count
- Space Complexity: O(n * k) for the resulting string
"""
