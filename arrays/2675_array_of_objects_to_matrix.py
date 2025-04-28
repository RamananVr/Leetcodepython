"""
LeetCode Question #2675: Array of Objects to Matrix

Problem Statement:
You are given an array of objects `arr`, where each object represents a row in a matrix, and a list of strings `keys`, where each string represents a column in the matrix.

Return a 2D array `matrix` where `matrix[i][j]` is the value of `keys[j]` in the `i-th` object of `arr`. If `keys[j]` does not exist in the `i-th` object, you should use an empty string `""` instead.

Example:
Input: 
arr = [{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}, {"a": 6, "c": 7}]
keys = ["a", "b", "c"]

Output:
[[1, 2, ""], [3, 4, 5], [6, "", 7]]

Constraints:
- `arr` is an array of objects.
- `keys` is a list of strings.
- Each object in `arr` contains string keys and arbitrary values.
"""

# Python Solution
def array_of_objects_to_matrix(arr, keys):
    """
    Converts an array of objects into a matrix based on the given keys.

    :param arr: List[Dict[str, Any]] - Array of objects
    :param keys: List[str] - List of keys representing matrix columns
    :return: List[List[Any]] - Resulting matrix
    """
    matrix = []
    for obj in arr:
        row = [obj.get(key, "") for key in keys]
        matrix.append(row)
    return matrix

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    arr1 = [{"a": 1, "b": 2}, {"a": 3, "b": 4, "c": 5}, {"a": 6, "c": 7}]
    keys1 = ["a", "b", "c"]
    print(array_of_objects_to_matrix(arr1, keys1))  # Expected: [[1, 2, ""], [3, 4, 5], [6, "", 7]]

    # Test Case 2
    arr2 = [{"x": 10, "y": 20}, {"x": 30}, {"y": 40, "z": 50}]
    keys2 = ["x", "y", "z"]
    print(array_of_objects_to_matrix(arr2, keys2))  # Expected: [[10, 20, ""], [30, "", ""], ["", 40, 50]]

    # Test Case 3
    arr3 = [{"name": "Alice", "age": 25}, {"name": "Bob"}, {"age": 30}]
    keys3 = ["name", "age", "city"]
    print(array_of_objects_to_matrix(arr3, keys3))  # Expected: [["Alice", 25, ""], ["Bob", "", ""], ["", 30, ""]]

    # Test Case 4
    arr4 = []
    keys4 = ["a", "b", "c"]
    print(array_of_objects_to_matrix(arr4, keys4))  # Expected: []

# Time and Space Complexity Analysis
"""
Time Complexity:
- For each object in `arr`, we iterate over the `keys` list to construct a row.
- Let `n` be the number of objects in `arr` and `m` be the number of keys in `keys`.
- The time complexity is O(n * m), as we perform a constant-time operation for each key in each object.

Space Complexity:
- The space complexity is O(n * m) for the resulting matrix, as we store `n` rows, each with `m` elements.
- Additional space is used for the intermediate `row` list during computation, but this is negligible compared to the matrix size.
"""

# Topic: Arrays