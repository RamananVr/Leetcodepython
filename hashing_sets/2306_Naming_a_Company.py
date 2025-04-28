"""
LeetCode Problem #2306: Naming a Company

Problem Statement:
You are given an array of strings `ideas` that represents a list of names to be used in the naming of a company. 
The process of naming a company involves choosing two distinct names from the list (idea1 and idea2) and swapping 
the first letters of the two names.

If both of the new names are not found in the original list, then the pair (idea1, idea2) is a valid name pair.

For example, if `ideas = ["coffee", "donuts", "time", "toffee"]`, the name pair ("coffee", "donuts") is valid 
because their swapped names "doffee" and "conuts" are not found in the original list. However, the pair 
("donuts", "time") is not valid because the name "tonuts" is found in the original list.

Return the total number of valid name pairs that can be formed.

Constraints:
- 2 <= ideas.length <= 5 * 10^4
- 1 <= ideas[i].length <= 10
- ideas[i] consists of lowercase English letters.
- All the strings in ideas are unique.
"""

# Solution
from collections import defaultdict

def distinctNames(ideas):
    """
    Calculate the total number of valid name pairs that can be formed by swapping the first letters of the names.

    :param ideas: List[str] - List of unique company name ideas.
    :return: int - Total number of valid name pairs.
    """
    # Group ideas by their first letter
    groups = defaultdict(set)
    for idea in ideas:
        first_letter = idea[0]
        groups[first_letter].add(idea[1:])
    
    # Calculate valid pairs
    valid_pairs = 0
    letters = list(groups.keys())
    for i in range(len(letters)):
        for j in range(i + 1, len(letters)):
            group1 = groups[letters[i]]
            group2 = groups[letters[j]]
            
            # Count common suffixes
            common_suffixes = len(group1 & group2)
            
            # Calculate valid pairs between these two groups
            valid_pairs += (len(group1) - common_suffixes) * (len(group2) - common_suffixes) * 2
    
    return valid_pairs

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    ideas1 = ["coffee", "donuts", "time", "toffee"]
    print(distinctNames(ideas1))  # Expected Output: 6

    # Test Case 2
    ideas2 = ["apple", "banana", "cherry", "date"]
    print(distinctNames(ideas2))  # Expected Output: 12

    # Test Case 3
    ideas3 = ["a", "b", "c", "d"]
    print(distinctNames(ideas3))  # Expected Output: 0

    # Test Case 4
    ideas4 = ["ab", "cd", "ef", "gh"]
    print(distinctNames(ideas4))  # Expected Output: 12

"""
Time and Space Complexity Analysis:

Time Complexity:
- Grouping ideas by their first letter takes O(n), where n is the length of the `ideas` list.
- Comparing groups involves iterating over pairs of groups. If there are k unique first letters, 
  this involves O(k^2) comparisons. Within each comparison, finding the intersection of two sets 
  takes O(min(len(group1), len(group2))). In the worst case, each group could contain up to n/k elements.
- Overall, the complexity is approximately O(n + k^2 * (n/k)) = O(n + kn), where k is the number of unique first letters.

Space Complexity:
- The `groups` dictionary stores the suffixes for each first letter. In the worst case, this requires O(n) space.
- Additional space is used for intermediate calculations, but it is negligible compared to the `groups` dictionary.
- Overall space complexity is O(n).

Topic: Hashing, Sets
"""