"""
LeetCode Problem #1487: Making File Names Unique

Problem Statement:
Given an array of strings `names` of size `n`, you will create `n` new strings such that:
- If a string `names[i]` is not present in the new list, you can add it directly.
- Otherwise, if a string `names[i]` is already present, you need to append a suffix `"(k)"` to it, where `k` is the smallest positive integer such that the resulting name is not present in the new list.

Return an array of strings `result` where `result[i]` is the new name you assigned to `names[i]`.

Example:
Input: names = ["pes", "fifa", "gta", "pes(2019)", "pes"]
Output: ["pes", "fifa", "gta", "pes(2019)", "pes(1)"]

Constraints:
- 1 <= names.length <= 5 * 10^4
- 1 <= names[i].length <= 20
- names[i] consists of lowercase English letters, digits, and/or round brackets.
"""

# Solution
def getFolderNames(names):
    """
    Generate unique folder names by appending suffixes when necessary.

    :param names: List[str] - List of folder names
    :return: List[str] - List of unique folder names
    """
    name_map = {}  # Dictionary to track the next available suffix for each name
    result = []    # List to store the final unique names

    for name in names:
        if name not in name_map:
            # If the name is not in the map, add it directly
            result.append(name)
            name_map[name] = 1  # Initialize the suffix counter for this name
        else:
            # If the name is already in the map, find the next available suffix
            suffix = name_map[name]
            while f"{name}({suffix})" in name_map:
                suffix += 1
            unique_name = f"{name}({suffix})"
            result.append(unique_name)
            name_map[name] = suffix + 1  # Update the suffix counter for the original name
            name_map[unique_name] = 1   # Initialize the suffix counter for the new unique name

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    names1 = ["pes", "fifa", "gta", "pes(2019)", "pes"]
    print(getFolderNames(names1))  # Output: ["pes", "fifa", "gta", "pes(2019)", "pes(1)"]

    # Test Case 2
    names2 = ["gta", "gta", "gta", "gta"]
    print(getFolderNames(names2))  # Output: ["gta", "gta(1)", "gta(2)", "gta(3)"]

    # Test Case 3
    names3 = ["doc", "doc", "image", "doc(1)", "doc"]
    print(getFolderNames(names3))  # Output: ["doc", "doc(1)", "image", "doc(1)(1)", "doc(2)"]

    # Test Case 4
    names4 = ["a", "a", "a", "a", "a"]
    print(getFolderNames(names4))  # Output: ["a", "a(1)", "a(2)", "a(3)", "a(4)"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each name in the input list, we may need to check for the next available suffix.
- In the worst case, this involves checking up to `k` suffixes, where `k` is the smallest integer such that the name with suffix `"(k)"` is unique.
- Since we use a dictionary for lookups, each check is O(1).
- Therefore, the overall time complexity is O(n), where `n` is the number of names.

Space Complexity:
- We use a dictionary to store the names and their suffix counters.
- In the worst case, the dictionary will store all unique names and their suffixes, which is proportional to the size of the input list.
- Therefore, the space complexity is O(n).
"""

# Topic: Hash Table