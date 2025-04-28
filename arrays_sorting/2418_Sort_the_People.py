"""
LeetCode Problem #2418: Sort the People

Problem Statement:
You are given an array of strings `names` and an array of positive integers `heights`, both of length `n`.

For each index `i`, `names[i]` and `heights[i]` denote the name and height of the `i-th` person.

Return `names` sorted in descending order by the people's heights.

Example 1:
Input: names = ["Mary", "John", "Emma"], heights = [180, 165, 170]
Output: ["Mary", "Emma", "John"]
Explanation: Mary is the tallest, followed by Emma and John.

Example 2:
Input: names = ["Alice", "Bob", "Bob"], heights = [155, 185, 150]
Output: ["Bob", "Alice", "Bob"]
Explanation: The Bob with height 185 comes first, followed by Alice and the Bob with height 150.

Constraints:
- `n == names.length == heights.length`
- `1 <= n <= 10^3`
- `1 <= names[i].length <= 20`
- `1 <= heights[i] <= 10^5`
- `names[i]` consists of lower and upper case English letters.
- All the values of `heights` are distinct.
"""

# Clean and Correct Python Solution
def sortPeople(names, heights):
    # Combine names and heights into a list of tuples, then sort by height in descending order
    sorted_people = sorted(zip(heights, names), reverse=True)
    # Extract the names from the sorted list of tuples
    return [name for _, name in sorted_people]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    names1 = ["Mary", "John", "Emma"]
    heights1 = [180, 165, 170]
    print(sortPeople(names1, heights1))  # Output: ["Mary", "Emma", "John"]

    # Test Case 2
    names2 = ["Alice", "Bob", "Bob"]
    heights2 = [155, 185, 150]
    print(sortPeople(names2, heights2))  # Output: ["Bob", "Alice", "Bob"]

    # Test Case 3
    names3 = ["Charlie", "David", "Eve"]
    heights3 = [160, 190, 170]
    print(sortPeople(names3, heights3))  # Output: ["David", "Eve", "Charlie"]

    # Test Case 4
    names4 = ["Zoe"]
    heights4 = [200]
    print(sortPeople(names4, heights4))  # Output: ["Zoe"]

    # Test Case 5
    names5 = ["Anna", "Bella", "Cara"]
    heights5 = [150, 150, 150]
    print(sortPeople(names5, heights5))  # Output: ["Anna", "Bella", "Cara"]  # Note: Heights are distinct per constraints.

# Time and Space Complexity Analysis
"""
Time Complexity:
- Combining `names` and `heights` into a list of tuples takes O(n).
- Sorting the list of tuples takes O(n log n), where n is the length of the input arrays.
- Extracting the names from the sorted list takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The combined list of tuples requires O(n) space.
- The output list of names also requires O(n) space.
- Overall space complexity: O(n).
"""

# Topic: Arrays, Sorting