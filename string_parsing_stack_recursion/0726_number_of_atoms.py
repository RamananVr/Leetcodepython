"""
LeetCode Question #726: Number of Atoms

Problem Statement:
Given a string formula representing a chemical formula, return the count of each atom in the formula as a string in the following format:
- The count of each atom is written as the atom followed by its count. If the count is 1, it is omitted.
- The result should be sorted in lexicographical order of the atom names.

The formula string may contain:
- Parentheses `()`, which indicate a grouping of atoms.
- Numbers, which indicate the count of atoms or groups of atoms.
- Atom names, which consist of one uppercase letter followed by zero or more lowercase letters.

You may assume that the formula is always valid.

Constraints:
- 1 <= formula.length <= 1000
- formula consists of English letters, digits, '(', and ')'.
- formula is always valid.

Example:
Input: formula = "H2O"
Output: "H2O"

Input: formula = "Mg(OH)2"
Output: "H2MgO2"

Input: formula = "K4(ON(SO3)2)2"
Output: "K4N2O14S4"
"""

from collections import defaultdict
import re

def countOfAtoms(formula: str) -> str:
    def parse_formula(index):
        counts = defaultdict(int)
        while index < len(formula):
            if formula[index] == '(':
                # Parse the group inside parentheses
                sub_counts, index = parse_formula(index + 1)
                multiplier = 1
                # Check for multiplier after the closing parenthesis
                match = re.match(r'\d+', formula[index:])
                if match:
                    multiplier = int(match.group())
                    index += len(match.group())
                # Add the multiplied counts to the current counts
                for atom, count in sub_counts.items():
                    counts[atom] += count * multiplier
            elif formula[index] == ')':
                # End of a group
                return counts, index + 1
            else:
                # Parse an atom and its count
                match = re.match(r'([A-Z][a-z]*)(\d*)', formula[index:])
                atom = match.group(1)
                count = int(match.group(2)) if match.group(2) else 1
                counts[atom] += count
                index += len(match.group(0))
        return counts, index

    # Parse the entire formula
    atom_counts, _ = parse_formula(0)
    # Sort the atoms lexicographically and format the result
    result = ''.join(f"{atom}{(count if count > 1 else '')}" for atom, count in sorted(atom_counts.items()))
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    formula1 = "H2O"
    print(countOfAtoms(formula1))  # Output: "H2O"

    # Test Case 2
    formula2 = "Mg(OH)2"
    print(countOfAtoms(formula2))  # Output: "H2MgO2"

    # Test Case 3
    formula3 = "K4(ON(SO3)2)2"
    print(countOfAtoms(formula3))  # Output: "K4N2O14S4"

    # Test Case 4
    formula4 = "Be32"
    print(countOfAtoms(formula4))  # Output: "Be32"

# Time and Space Complexity Analysis
# Time Complexity:
# - Parsing the formula involves iterating through the string once, and for each atom or group, we perform constant-time operations.
# - Sorting the atoms at the end takes O(n log n), where n is the number of unique atoms.
# - Overall time complexity: O(m + n log n), where m is the length of the formula and n is the number of unique atoms.

# Space Complexity:
# - The space required for the counts dictionary is proportional to the number of unique atoms, O(n).
# - The recursion stack depth is proportional to the maximum nesting of parentheses, O(d), where d is the depth of the formula.
# - Overall space complexity: O(n + d).

# Topic: String Parsing, Stack, Recursion