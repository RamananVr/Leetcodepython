"""
LeetCode Problem #1286: Iterator for Combination

Problem Statement:
Design the CombinationIterator class:
- CombinationIterator(string characters, int combinationLength) Initializes the object with a string characters of sorted distinct lowercase English letters and a number combinationLength as arguments.
- next() Returns the next combination of length combinationLength in lexicographical order.
- hasNext() Returns true if and only if there is a next combination that can be returned.

Constraints:
- 1 <= combinationLength <= characters.length <= 15
- All the characters of characters are unique.
- At most 10^4 calls will be made to next and hasNext.
- It's guaranteed that all calls of the function next are valid.

Example:
Input:
    ["CombinationIterator", "next", "hasNext", "next", "hasNext", "next", "hasNext"]
    [["abc", 2], [], [], [], [], [], []]
Output:
    [null, "ab", true, "ac", true, "bc", false]
Explanation:
    CombinationIterator itr = new CombinationIterator("abc", 2);
    itr.next();    // return "ab"
    itr.hasNext(); // return True
    itr.next();    // return "ac"
    itr.hasNext(); // return True
    itr.next();    // return "bc"
    itr.hasNext(); // return False
"""

from itertools import combinations

class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        """
        Initializes the iterator with the given characters and combination length.
        """
        self.combinations = list(combinations(characters, combinationLength))
        self.index = 0

    def next(self) -> str:
        """
        Returns the next combination in lexicographical order.
        """
        result = ''.join(self.combinations[self.index])
        self.index += 1
        return result

    def hasNext(self) -> bool:
        """
        Returns True if there are more combinations to return, otherwise False.
        """
        return self.index < len(self.combinations)


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    itr = CombinationIterator("abc", 2)
    print(itr.next())    # Output: "ab"
    print(itr.hasNext()) # Output: True
    print(itr.next())    # Output: "ac"
    print(itr.hasNext()) # Output: True
    print(itr.next())    # Output: "bc"
    print(itr.hasNext()) # Output: False

    # Test Case 2
    itr2 = CombinationIterator("abcd", 3)
    print(itr2.next())    # Output: "abc"
    print(itr2.hasNext()) # Output: True
    print(itr2.next())    # Output: "abd"
    print(itr2.hasNext()) # Output: True
    print(itr2.next())    # Output: "acd"
    print(itr2.hasNext()) # Output: True
    print(itr2.next())    # Output: "bcd"
    print(itr2.hasNext()) # Output: False

"""
Time Complexity Analysis:
- Initialization (__init__): O(C(n, k)), where n is the length of the characters string and k is the combinationLength. This is the cost of generating all combinations.
- next(): O(k), where k is the combinationLength, as we join the characters to form the string.
- hasNext(): O(1), as it simply compares the current index with the length of the combinations list.

Space Complexity Analysis:
- Space complexity is O(C(n, k)), where C(n, k) is the number of combinations, as we store all combinations in memory.

Topic: Iterators, Combinatorics
"""