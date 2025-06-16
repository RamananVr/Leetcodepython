"""
LeetCode Problem 2745: Construct the Longest New String

You are given three integers x, y, and z.

You have x strings equal to "AA", y strings equal to "BB", and z strings equal to "AB".

You want to choose some (possibly all or none) of these strings and concatenate them in some order 
to form a new string. This new string must not contain "AAA" or "BBB" as a substring.

Return the maximum possible length of such a string.

Example 1:
Input: x = 2, y = 1, z = 1
Output: 8
Explanation: We can concatenate the strings "AA" + "AB" + "BB" + "AA" to get "AABBBAA".
- "AA" appears at indices 0-1 and 6-7.
- "AB" appears at index 2-3.
- "BB" appears at index 4-5.
- "AAA" does not appear as a substring.
- "BBB" does not appear as a substring.
Length is 8.

Example 2:
Input: x = 5, y = 1, z = 2
Output: 12
Explanation: We can concatenate "AA" + "AB" + "BB" + "AB" + "AA" + "AA" to get "AABBABAAAA".
However, we need to be careful about "AAA". One valid arrangement is "ABAA" + "BBAB" + "AA" + "AA".
Actually, optimal might be "AA" + "AB" + "BB" + "AB" + "AA" + "AA" = "AABBBABAAAA" (length 11).
Let me recalculate: "AB" + "AA" + "BB" + "AB" + "AA" + "AA" = "ABAABBABAAAA" (length 12).

Example 3:
Input: x = 3, y = 2, z = 2
Output: 14
Explanation: We can use all strings. One possible arrangement: 
"AB" + "AA" + "BB" + "AB" + "AA" + "BB" + "AA" = "ABAABBABAABBAA" (length 14).

Constraints:
- 1 <= x, y, z <= 50
"""

from functools import lru_cache


def longestString(x: int, y: int, z: int) -> int:
    """
    Find the maximum length string using x "AA", y "BB", and z "AB" pieces.
    
    Key insights:
    1. "AB" pieces can be placed anywhere and don't create "AAA" or "BBB"
    2. We need to carefully place "AA" and "BB" pieces to avoid consecutive same letters
    3. The pattern depends on the relationship between x and y
    
    Args:
        x: Number of "AA" strings
        y: Number of "BB" strings  
        z: Number of "AB" strings
        
    Returns:
        Maximum possible length of valid string
        
    Time Complexity: O(1) - mathematical solution
    Space Complexity: O(1)
    """
    # Each piece contributes 2 characters
    # All "AB" pieces can always be used
    total_ab = z * 2
    
    # For "AA" and "BB" pieces, we need to be more careful
    if x == y:
        # Equal counts: can use all pieces
        # Pattern like: AA-BB-AA-BB... or BB-AA-BB-AA...
        total_aa_bb = (x + y) * 2
    elif abs(x - y) == 1:
        # Difference of 1: can use all pieces
        # The extra piece can be placed at start or end
        total_aa_bb = (x + y) * 2
    else:
        # Larger difference: limited by the smaller count
        # Can use all of smaller + (smaller + 1) of larger
        min_count = min(x, y)
        total_aa_bb = (min_count * 2 + min_count + 1) * 2
    
    return total_ab + total_aa_bb


def longestStringDP(x: int, y: int, z: int) -> int:
    """
    Dynamic programming solution with memoization.
    
    State: (remaining_x, remaining_y, remaining_z, last_char)
    last_char: 'A' or 'B' representing the last character of current string
    
    Args:
        x: Number of "AA" strings
        y: Number of "BB" strings
        z: Number of "AB" strings
        
    Returns:
        Maximum possible length of valid string
        
    Time Complexity: O(x * y * z)
    Space Complexity: O(x * y * z)
    """
    @lru_cache(maxsize=None)
    def dp(rem_x: int, rem_y: int, rem_z: int, last_char: str) -> int:
        """
        Return maximum length starting from current state.
        
        Args:
            rem_x: Remaining "AA" pieces
            rem_y: Remaining "BB" pieces  
            rem_z: Remaining "AB" pieces
            last_char: Last character of current string ('A', 'B', or '')
            
        Returns:
            Maximum additional length possible
        """
        if rem_x == 0 and rem_y == 0 and rem_z == 0:
            return 0
        
        max_len = 0
        
        # Try using "AA" piece
        if rem_x > 0 and last_char != 'A':
            max_len = max(max_len, 2 + dp(rem_x - 1, rem_y, rem_z, 'A'))
        
        # Try using "BB" piece  
        if rem_y > 0 and last_char != 'B':
            max_len = max(max_len, 2 + dp(rem_x, rem_y - 1, rem_z, 'B'))
        
        # Try using "AB" piece
        if rem_z > 0:
            max_len = max(max_len, 2 + dp(rem_x, rem_y, rem_z - 1, 'B'))
        
        return max_len
    
    # Try starting with each type of piece
    result = 0
    
    # Start with "AA"
    if x > 0:
        result = max(result, 2 + dp(x - 1, y, z, 'A'))
    
    # Start with "BB"
    if y > 0:
        result = max(result, 2 + dp(x, y - 1, z, 'B'))
    
    # Start with "AB"
    if z > 0:
        result = max(result, 2 + dp(x, y, z - 1, 'B'))
    
    return result


def longestStringGreedy(x: int, y: int, z: int) -> int:
    """
    Greedy approach: try to balance "AA" and "BB" usage.
    
    Args:
        x: Number of "AA" strings
        y: Number of "BB" strings
        z: Number of "AB" strings
        
    Returns:
        Maximum possible length of valid string
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # All "AB" pieces can always be used
    result = z * 2
    
    # For "AA" and "BB", we need to alternate them
    # Maximum we can place is limited by the constraint that
    # we cannot have three consecutive same characters
    
    if x == 0 or y == 0:
        # If one type is missing, we can only use one piece of the other
        result += min(1, max(x, y)) * 2
    else:
        # Both types available
        # We can use min(x, y) pairs plus potentially one extra
        min_pairs = min(x, y)
        max_count = max(x, y)
        
        if max_count <= min_pairs + 1:
            # Can use all pieces
            result += (x + y) * 2
        else:
            # Limited by alternating constraint
            result += (min_pairs * 2 + min_pairs + 1) * 2
    
    return result


def longestStringMath(x: int, y: int, z: int) -> int:
    """
    Mathematical solution based on pattern analysis.
    
    Args:
        x: Number of "AA" strings
        y: Number of "BB" strings
        z: Number of "AB" strings
        
    Returns:
        Maximum possible length of valid string
        
    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    # All AB pieces contribute 2z to the length
    # For AA and BB pieces:
    # - If |x - y| <= 1: can use all pieces (x + y) * 2
    # - If |x - y| > 1: can use 2 * min(x, y) + 2 pieces
    
    ab_contribution = z * 2
    
    if abs(x - y) <= 1:
        aa_bb_contribution = (x + y) * 2
    else:
        aa_bb_contribution = 2 * min(x, y) * 2 + 2
    
    return ab_contribution + aa_bb_contribution


# Test cases
def test_longestString():
    """Test the longestString function with various inputs."""
    
    test_cases = [
        {
            "x": 2, "y": 1, "z": 1,
            "expected": 8,
            "description": "Example 1: balanced case"
        },
        {
            "x": 5, "y": 1, "z": 2,
            "expected": 12,
            "description": "Example 2: unbalanced with more AA"
        },
        {
            "x": 3, "y": 2, "z": 2,
            "expected": 14,
            "description": "Example 3: can use all pieces"
        },
        {
            "x": 0, "y": 0, "z": 1,
            "expected": 2,
            "description": "Only AB pieces"
        },
        {
            "x": 1, "y": 0, "z": 0,
            "expected": 2,
            "description": "Only AA pieces"
        },
        {
            "x": 0, "y": 1, "z": 0,
            "expected": 2,
            "description": "Only BB pieces"
        },
        {
            "x": 1, "y": 1, "z": 0,
            "expected": 4,
            "description": "Equal AA and BB, no AB"
        },
        {
            "x": 10, "y": 1, "z": 0,
            "expected": 4,
            "description": "Highly unbalanced"
        },
        {
            "x": 1, "y": 4, "z": 5,
            "expected": 16,
            "description": "More AB pieces"
        }
    ]
    
    for i, test in enumerate(test_cases):
        x, y, z = test["x"], test["y"], test["z"]
        expected = test["expected"]
        
        # Test main solution
        result1 = longestString(x, y, z)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Input: x = {x}, y = {y}, z = {z}")
        print(f"  Expected: {expected}")
        print(f"  Mathematical approach: {result1}")
        
        # Test DP solution
        result2 = longestStringDP(x, y, z)
        print(f"  DP approach: {result2}")
        
        # Test greedy solution
        result3 = longestStringGreedy(x, y, z)
        print(f"  Greedy approach: {result3}")
        
        # Test math solution
        result4 = longestStringMath(x, y, z)
        print(f"  Math approach: {result4}")
        
        # Verify results
        assert result1 == expected, f"Mathematical approach failed for test {i+1}"
        assert result2 == expected, f"DP approach failed for test {i+1}"
        assert result3 == expected, f"Greedy approach failed for test {i+1}"
        assert result4 == expected, f"Math approach failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_longestString()

"""
Complexity Analysis:

1. Mathematical Approach (longestString):
   - Time Complexity: O(1) - constant time calculation
   - Space Complexity: O(1) - only using constant extra space

2. DP Approach (longestStringDP):
   - Time Complexity: O(x * y * z) - states in memoization table
   - Space Complexity: O(x * y * z) - memoization table size

3. Greedy Approach (longestStringGreedy):
   - Time Complexity: O(1) - constant time operations
   - Space Complexity: O(1) - only using constant extra space

4. Math Approach (longestStringMath):
   - Time Complexity: O(1) - mathematical formula
   - Space Complexity: O(1) - constant space

Key Insights:
- All "AB" pieces can always be used (contribute 2z to length)
- "AA" and "BB" pieces must be alternated to avoid "AAA" or "BBB"
- If |x - y| ≤ 1, all "AA" and "BB" pieces can be used
- If |x - y| > 1, we're limited to 2*min(x,y) + 2 total "AA"/"BB" pieces
- The optimal solution follows a mathematical pattern

Constraints Analysis:
- Cannot have "AAA" substring: no three consecutive A's
- Cannot have "BBB" substring: no three consecutive B's
- "AB" pieces are safe and can be placed anywhere

Topics: Dynamic Programming, Greedy Algorithms, String Manipulation, Mathematical Analysis
"""
