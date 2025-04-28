"""
LeetCode Question #1096: Brace Expansion II

Problem Statement:
Under the grammar given below, strings can represent a set of words.

Grammar:
- `{}` represents a set of words.
- `,` represents union (e.g., `{a,b}` is the set containing "a" and "b").
- Concatenation represents joining words (e.g., `{a,b}{c,d}` is the set containing "ac", "ad", "bc", "bd").
- The input string is guaranteed to be valid.

Given an expression representing a set of words under the grammar, return the sorted list of words in the set.

Example:
Input: "{a,b}{c,{d,e}}"
Output: ["ac", "ad", "ae", "bc", "bd", "be"]

Constraints:
- 1 <= expression.length <= 50
- The input expression is guaranteed to be valid.
"""

# Solution
from typing import List

class Solution:
    def braceExpansionII(self, expression: str) -> List[str]:
        def parse(expr):
            stack = []
            current_set = set()
            current_concat = {""}
            
            i = 0
            while i < len(expr):
                char = expr[i]
                if char == '{':
                    # Start a new sub-expression
                    stack.append((current_set, current_concat))
                    current_set, current_concat = set(), {""}
                elif char == '}':
                    # End the current sub-expression
                    sub_set = current_set
                    current_set, current_concat = stack.pop()
                    current_concat = {x + y for x in current_concat for y in sub_set}
                elif char == ',':
                    # Union operation
                    current_set |= current_concat
                    current_concat = {""}
                else:
                    # Concatenation operation
                    j = i
                    while j < len(expr) and expr[j] not in ",{}":
                        j += 1
                    word = expr[i:j]
                    current_concat = {x + word for x in current_concat}
                    i = j - 1
                i += 1
            
            return current_set | current_concat
        
        return sorted(parse(expression))

# Example Test Cases
if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1
    expression1 = "{a,b}{c,{d,e}}"
    print(solution.braceExpansionII(expression1))  # Output: ["ac", "ad", "ae", "bc", "bd", "be"]
    
    # Test Case 2
    expression2 = "{{a,z},a{b,c},{ab,z}}"
    print(solution.braceExpansionII(expression2))  # Output: ["a", "ab", "ac", "z"]
    
    # Test Case 3
    expression3 = "{a,b,c}"
    print(solution.braceExpansionII(expression3))  # Output: ["a", "b", "c"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Parsing the expression involves iterating through the string, and for each union or concatenation operation, we may need to combine sets.
- Let n be the length of the expression and m be the maximum size of any intermediate set. The complexity is approximately O(n * m^2) due to set operations.

Space Complexity:
- The space complexity is O(m), where m is the size of the largest set generated during parsing.

Overall, the solution is efficient for the given constraints (expression length <= 50).

Topic: String Parsing, Backtracking
"""