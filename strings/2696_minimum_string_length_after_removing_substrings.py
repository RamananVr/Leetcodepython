"""
2696. Minimum String Length After Removing Substrings

PROBLEM STATEMENT:
You are given a string s consisting only of uppercase English letters.
You can apply some operations to this string where, in one operation, you can remove any 
occurrence of one of the substrings "AB" or "CD" from s.

Return the minimum possible length of the resulting string that you can obtain.
Note that the string becomes empty if you remove all characters from it.

EXAMPLES:
Example 1:
Input: s = "ABFCACDB"
Output: 2
Explanation: We can do the following operations:
- Remove the substring "AB" from "ABFCACDB", so s = "FCACDB".
- Remove the substring "CD" from "FCACDB", so s = "FCAB".
- Remove the substring "AB" from "FCAB", so s = "FC".
So the resulting length is 2.

Example 2:
Input: s = "ACBBD"
Output: 5
Explanation: We cannot remove any occurrence of "AB" or "CD" from "ACBBD".

CONSTRAINTS:
- 1 <= s.length <= 100
- s consists only of uppercase English letters.
"""

def min_length_after_removals(s):
    """
    Find minimum string length after removing all possible "AB" and "CD" substrings.
    
    Approach: Use a stack to simulate the removal process.
    When we see 'B' and the top of stack is 'A', we can remove "AB".
    When we see 'D' and the top of stack is 'C', we can remove "CD".
    Otherwise, push the character onto the stack.
    
    Args:
        s: String consisting of uppercase English letters
    
    Returns:
        Minimum possible length after all removals
    """
    stack = []
    
    for char in s:
        if stack and ((char == 'B' and stack[-1] == 'A') or 
                      (char == 'D' and stack[-1] == 'C')):
            # Remove the pair by popping from stack
            stack.pop()
        else:
            # Add character to stack
            stack.append(char)
    
    return len(stack)

def min_length_after_removals_iterative(s):
    """
    Alternative approach using iterative string replacement.
    
    Args:
        s: String consisting of uppercase English letters
    
    Returns:
        Minimum possible length after all removals
    """
    while "AB" in s or "CD" in s:
        s = s.replace("AB", "").replace("CD", "")
    
    return len(s)

def min_length_after_removals_recursive(s):
    """
    Recursive approach to remove substrings.
    
    Args:
        s: String consisting of uppercase English letters
    
    Returns:
        Minimum possible length after all removals
    """
    # Find first occurrence of "AB" or "CD"
    ab_pos = s.find("AB")
    cd_pos = s.find("CD")
    
    if ab_pos == -1 and cd_pos == -1:
        # No more removals possible
        return len(s)
    
    # Choose the earliest occurrence
    if ab_pos != -1 and (cd_pos == -1 or ab_pos < cd_pos):
        # Remove "AB"
        new_s = s[:ab_pos] + s[ab_pos + 2:]
        return min_length_after_removals_recursive(new_s)
    else:
        # Remove "CD"
        new_s = s[:cd_pos] + s[cd_pos + 2:]
        return min_length_after_removals_recursive(new_s)

def min_length_simulation(s):
    """
    Simulation approach that shows the step-by-step process.
    
    Args:
        s: String consisting of uppercase English letters
    
    Returns:
        Tuple of (final_length, steps_taken)
    """
    steps = []
    current = s
    
    while True:
        found_removal = False
        
        # Look for "AB"
        ab_pos = current.find("AB")
        if ab_pos != -1:
            current = current[:ab_pos] + current[ab_pos + 2:]
            steps.append(f"Remove AB: {current}")
            found_removal = True
            continue
        
        # Look for "CD"
        cd_pos = current.find("CD")
        if cd_pos != -1:
            current = current[:cd_pos] + current[cd_pos + 2:]
            steps.append(f"Remove CD: {current}")
            found_removal = True
            continue
        
        if not found_removal:
            break
    
    return len(current), steps

def test_min_length_after_removals():
    """Test the minimum string length implementation."""
    
    # Test 1: Example 1
    s1 = "ABFCACDB"
    assert min_length_after_removals(s1) == 2
    assert min_length_after_removals_iterative(s1) == 2
    assert min_length_after_removals_recursive(s1) == 2
    
    # Test 2: Example 2
    s2 = "ACBBD"
    assert min_length_after_removals(s2) == 5
    assert min_length_after_removals_iterative(s2) == 5
    assert min_length_after_removals_recursive(s2) == 5
    
    # Test 3: All removable
    s3 = "ABCD"
    assert min_length_after_removals(s3) == 0
    assert min_length_after_removals_iterative(s3) == 0
    assert min_length_after_removals_recursive(s3) == 0
    
    # Test 4: Nested removals
    s4 = "AABBCCDD"
    assert min_length_after_removals(s4) == 0
    
    # Test 5: Mixed case
    s5 = "ACDBABCD"
    result = min_length_after_removals(s5)
    assert result == 0  # Everything can be removed
    
    # Test 6: No removals possible
    s6 = "ADBC"
    assert min_length_after_removals(s6) == 4
    
    # Test 7: Single characters
    s7 = "A"
    assert min_length_after_removals(s7) == 1
    
    s8 = "B"
    assert min_length_after_removals(s8) == 1
    
    # Test 8: Empty string
    s9 = ""
    assert min_length_after_removals(s9) == 0
    
    # Test 9: Complex case with simulation
    s10 = "ABABCDCD"
    length, steps = min_length_simulation(s10)
    assert length == 0
    
    # Test 10: Overlapping patterns
    s11 = "AAABBBCCCDDDD"
    result = min_length_after_removals(s11)
    # A A A B B B C C C D D D D
    # A A AB -> A A
    # A A
    # No more AB or CD can be formed
    expected = 2  # A A remains
    assert result == expected
    
    # Test 11: Alternating pattern
    s12 = "ABABABCDCDCD"
    result = min_length_after_removals(s12)
    assert result == 0
    
    # Test 12: Check step-by-step for understanding
    s13 = "CABDABCD"
    length, steps = min_length_simulation(s13)
    print(f"Steps for {s13}:")
    for step in steps:
        print(f"  {step}")
    print(f"Final length: {length}")
    
    print("All test cases passed!")

def analyze_removal_patterns():
    """Analyze different removal patterns and their effects."""
    
    test_cases = [
        "ABFCACDB",
        "ACBBD", 
        "ABCD",
        "AABBCCDD",
        "CABDABCD",
        "ABABCDCD",
        "AABBBCCCDDDD"
    ]
    
    print("Analysis of removal patterns:")
    print("-" * 50)
    
    for s in test_cases:
        stack_result = min_length_after_removals(s)
        iterative_result = min_length_after_removals_iterative(s)
        recursive_result = min_length_after_removals_recursive(s)
        
        print(f"Input: {s}")
        print(f"  Stack approach: {stack_result}")
        print(f"  Iterative approach: {iterative_result}")
        print(f"  Recursive approach: {recursive_result}")
        
        _, steps = min_length_simulation(s)
        print(f"  Removal steps: {len(steps)}")
        print()

if __name__ == "__main__":
    test_min_length_after_removals()
    analyze_removal_patterns()

"""
COMPLEXITY ANALYSIS:
- Time Complexity: 
  - Stack approach: O(n) where n is string length
  - Iterative replacement: O(n²) in worst case due to string operations
  - Recursive: O(n²) due to string slicing and recursive calls
- Space Complexity: 
  - Stack approach: O(n) for the stack
  - Iterative: O(n) for string storage
  - Recursive: O(n) for recursion depth and string copies

TOPICS: Stack, String Manipulation, Greedy Algorithm, Simulation

KEY INSIGHTS:
1. Stack is the most efficient approach for this type of pattern matching
2. Greedy removal works because removing any valid pair doesn't prevent future removals
3. The order of removal doesn't matter for the final result
4. Stack naturally handles nested patterns like "AABB"
5. This problem is similar to matching parentheses but with specific character pairs
"""
