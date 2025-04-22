"""
LeetCode Problem #770: Basic Calculator IV

Problem Statement:
Given an expression such as "e + 8 - a + 5" and an evaluation map such as {"e": 1}, return a list of terms representing the simplified expression, sorted lexicographically.

- The expression consists of integers, variables, and the operations '+', '-', '*', and parentheses '(' and ')'.
- The evaluation map gives the values of variables (e.g., {"e": 1} means e = 1).
- The result should be a list of terms in lexicographical order, where each term is represented as a string. For example, "2*a*b*c" should be represented as "2*a*b*c".
- Terms with a coefficient of 0 should not be included.
- The result should not contain any spaces.

Constraints:
1. The length of the expression will not exceed 1000.
2. The evaluation map will have at most 1000 keys.
3. The keys in the evaluation map are strings of lowercase letters.
4. The values in the evaluation map are integers.
5. The expression contains only lowercase letters, digits, '+', '-', '*', '(', ')', and spaces.
6. The answer is guaranteed to fit within a 32-bit integer.

Example:
Input: expression = "e + 8 - a + 5", evalvars = ["e"], evalints = [1]
Output: ["-1*a", "14"]

Input: expression = "e - 8 + temperature - pressure", evalvars = ["e", "temperature"], evalints = [1, 12]
Output: ["-1*pressure", "5"]

Input: expression = "(e + 8) * (e - 8)", evalvars = [], evalints = []
Output: ["1*e*e", "-64"]

Input: expression = "7 - 7", evalvars = [], evalints = []
Output: []

Input: expression = "a * b * c + b * a * c * 4", evalvars = [], evalints = []
Output: ["5*a*b*c"]

Input: expression = "((a - b) * (b - c) + (c - a))", evalvars = [], evalints = []
Output: ["-1*a*b", "1*a*c", "1*b*c", "-1*a", "1*b", "-1*c"]

"""

from collections import Counter
from typing import List

class Solution:
    def basicCalculatorIV(self, expression: str, evalvars: List[str], evalints: List[int]) -> List[str]:
        # Map variables to their values
        evalmap = dict(zip(evalvars, evalints))
        
        def combine(c1, c2, sign=1):
            for k, v in c2.items():
                c1[k] += sign * v
            return c1

        def multiply(c1, c2):
            c = Counter()
            for k1, v1 in c1.items():
                for k2, v2 in c2.items():
                    nk = tuple(sorted(k1 + k2))
                    c[nk] += v1 * v2
            return c

        def parse(expression):
            stack = []
            c = Counter()
            sign = 1
            i = 0
            while i < len(expression):
                if expression[i] == ' ':
                    i += 1
                elif expression[i] == '+':
                    sign = 1
                    i += 1
                elif expression[i] == '-':
                    sign = -1
                    i += 1
                elif expression[i] == '(':
                    stack.append((c, sign))
                    c = Counter()
                    sign = 1
                    i += 1
                elif expression[i] == ')':
                    prev_c, prev_sign = stack.pop()
                    c = combine(prev_c, c, prev_sign)
                    i += 1
                elif expression[i].isalnum():
                    j = i
                    while i < len(expression) and expression[i].isalnum():
                        i += 1
                    token = expression[j:i]
                    if token.isdigit():
                        combine(c, Counter({(): sign * int(token)}))
                    else:
                        if token in evalmap:
                            combine(c, Counter({(): sign * evalmap[token]}))
                        else:
                            combine(c, Counter({(token,): sign}))
                elif expression[i] == '*':
                    c2 = Counter()
                    i += 1
                    while i < len(expression) and expression[i] == ' ':
                        i += 1
                    if expression[i].isalnum():
                        j = i
                        while i < len(expression) and expression[i].isalnum():
                            i += 1
                        token = expression[j:i]
                        if token.isdigit():
                            c2 = Counter({(): int(token)})
                        else:
                            if token in evalmap:
                                c2 = Counter({(): evalmap[token]})
                            else:
                                c2 = Counter({(token,): 1})
                    elif expression[i] == '(':
                        bal = 0
                        j = i
                        while i < len(expression):
                            if expression[i] == '(':
                                bal += 1
                            elif expression[i] == ')':
                                bal -= 1
                                if bal == 0:
                                    break
                            i += 1
                        c2 = parse(expression[j:i+1])
                        i += 1
                    c = multiply(c, c2)
            return c

        c = parse(expression)
        result = []
        for k, v in sorted(c.items(), key=lambda x: (-len(x[0]), x[0])):
            if v:
                result.append(f"{v}" + "".join(f"*{x}" for x in k))
        return result


# Example Test Cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test Case 1
    expression = "e + 8 - a + 5"
    evalvars = ["e"]
    evalints = [1]
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: ["-1*a", "14"]

    # Test Case 2
    expression = "e - 8 + temperature - pressure"
    evalvars = ["e", "temperature"]
    evalints = [1, 12]
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: ["-1*pressure", "5"]

    # Test Case 3
    expression = "(e + 8) * (e - 8)"
    evalvars = []
    evalints = []
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: ["1*e*e", "-64"]

    # Test Case 4
    expression = "7 - 7"
    evalvars = []
    evalints = []
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: []

    # Test Case 5
    expression = "a * b * c + b * a * c * 4"
    evalvars = []
    evalints = []
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: ["5*a*b*c"]

    # Test Case 6
    expression = "((a - b) * (b - c) + (c - a))"
    evalvars = []
    evalints = []
    print(sol.basicCalculatorIV(expression, evalvars, evalints))  # Output: ["-1*a*b", "1*a*c", "1*b*c", "-1*a", "1*b", "-1*c"]

"""
Time Complexity:
- Parsing the expression and evaluating it involves traversing the string and performing operations on terms. 
- Let n be the length of the expression and m be the number of unique terms. The complexity is O(n * m).

Space Complexity:
- The space complexity is O(m), where m is the number of unique terms in the expression.

Topic: String Parsing, HashMap, Counter
"""