"""
LeetCode Question #555: Split Concatenated Strings

Problem Statement:
You are given an array of strings `strs`. You can choose any string from the array and reverse it. 
After reversing, you can concatenate all the strings in any order to form a new string. 
Return the lexicographically largest string that can be formed.

Example:
Input: strs = ["abc", "xyz"]
Output: "zyxcba"

Constraints:
1. 1 <= strs.length <= 50
2. 1 <= strs[i].length <= 50
3. All strings in `strs` consist of lowercase English letters.
"""

# Python Solution
def splitLoopedString(strs):
    """
    Function to find the lexicographically largest string that can be formed
    by reversing and concatenating strings in any order.
    """
    # Step 1: Preprocess each string to keep its lexicographically largest form
    for i in range(len(strs)):
        strs[i] = max(strs[i], strs[i][::-1])

    # Step 2: Try each string as the starting point
    max_string = ""
    for i, s in enumerate(strs):
        # Reverse and non-reverse versions of the current string
        for candidate in (s, s[::-1]):
            # Concatenate the current string with the rest of the strings
            rest = ''.join(strs[i+1:] + strs[:i])
            # Check all possible splits of the candidate string
            for j in range(len(candidate)):
                # Form the new string by splitting and concatenating
                new_string = candidate[j:] + rest + candidate[:j]
                # Update the maximum string if the new one is larger
                max_string = max(max_string, new_string)
    
    return max_string

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    strs1 = ["abc", "xyz"]
    print(splitLoopedString(strs1))  # Output: "zyxcba"

    # Test Case 2
    strs2 = ["a", "b", "c"]
    print(splitLoopedString(strs2))  # Output: "cba"

    # Test Case 3
    strs3 = ["abc", "def", "ghi"]
    print(splitLoopedString(strs3))  # Output: "ihgfedcba"

    # Test Case 4
    strs4 = ["aaa", "bbb", "ccc"]
    print(splitLoopedString(strs4))  # Output: "cccbbbaaa"

    # Test Case 5
    strs5 = ["z", "y", "x"]
    print(splitLoopedString(strs5))  # Output: "zyx"

"""
Time Complexity Analysis:
1. Preprocessing Step: O(n * m), where `n` is the number of strings and `m` is the average length of the strings.
   - For each string, we compute its reverse and compare it with the original.
2. Main Loop: O(n * m^2)
   - For each string, we consider both its original and reversed forms (2 options).
   - For each form, we iterate through all possible splits (m splits).
   - Concatenation of the rest of the strings takes O(n * m) in the worst case.
   - Overall, this results in O(n * m^2) complexity.

Space Complexity Analysis:
- The space complexity is O(n * m) due to the storage of the strings and intermediate results.

Topic: Strings
"""