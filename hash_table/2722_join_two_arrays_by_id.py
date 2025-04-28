"""
LeetCode Question #2722: Join Two Arrays by ID

Problem Statement:
You are given two arrays, `arr1` and `arr2`, where each array contains objects. Each object has two properties:
- `id`: an integer representing the unique identifier of the object.
- `value`: an integer representing the value associated with the object.

Write a function `join_arrays_by_id(arr1, arr2)` that joins the two arrays based on their `id` property. The result should be an array of objects, where each object contains:
- `id`: the unique identifier.
- `value1`: the value from `arr1` corresponding to the `id` (or `None` if the `id` is not present in `arr1`).
- `value2`: the value from `arr2` corresponding to the `id` (or `None` if the `id` is not present in `arr2`).

The resulting array should be sorted by `id` in ascending order.

Example:
Input:
    arr1 = [{"id": 1, "value": 10}, {"id": 2, "value": 20}, {"id": 3, "value": 30}]
    arr2 = [{"id": 2, "value": 200}, {"id": 3, "value": 300}, {"id": 4, "value": 400}]
Output:
    [
        {"id": 1, "value1": 10, "value2": None},
        {"id": 2, "value1": 20, "value2": 200},
        {"id": 3, "value1": 30, "value2": 300},
        {"id": 4, "value1": None, "value2": 400}
    ]
"""

# Solution
def join_arrays_by_id(arr1, arr2):
    # Create dictionaries for quick lookup of values by id
    dict1 = {item["id"]: item["value"] for item in arr1}
    dict2 = {item["id"]: item["value"] for item in arr2}
    
    # Get all unique ids from both arrays
    all_ids = sorted(set(dict1.keys()).union(dict2.keys()))
    
    # Build the result array
    result = []
    for id in all_ids:
        result.append({
            "id": id,
            "value1": dict1.get(id, None),
            "value2": dict2.get(id, None)
        })
    
    return result

# Example Test Cases
if __name__ == "__main__":
    arr1 = [{"id": 1, "value": 10}, {"id": 2, "value": 20}, {"id": 3, "value": 30}]
    arr2 = [{"id": 2, "value": 200}, {"id": 3, "value": 300}, {"id": 4, "value": 400}]
    
    # Test Case 1
    print(join_arrays_by_id(arr1, arr2))
    # Expected Output:
    # [
    #     {"id": 1, "value1": 10, "value2": None},
    #     {"id": 2, "value1": 20, "value2": 200},
    #     {"id": 3, "value1": 30, "value2": 300},
    #     {"id": 4, "value1": None, "value2": 400}
    # ]

    # Test Case 2
    arr1 = [{"id": 5, "value": 50}]
    arr2 = [{"id": 6, "value": 60}]
    print(join_arrays_by_id(arr1, arr2))
    # Expected Output:
    # [
    #     {"id": 5, "value1": 50, "value2": None},
    #     {"id": 6, "value1": None, "value2": 60}
    # ]

    # Test Case 3
    arr1 = []
    arr2 = [{"id": 1, "value": 100}]
    print(join_arrays_by_id(arr1, arr2))
    # Expected Output:
    # [
    #     {"id": 1, "value1": None, "value2": 100}
    # ]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Constructing `dict1` and `dict2` takes O(n1 + n2), where n1 is the length of `arr1` and n2 is the length of `arr2`.
- Finding all unique ids and sorting them takes O(k log k), where k is the number of unique ids.
- Building the result array takes O(k), where k is the number of unique ids.

Overall time complexity: O(n1 + n2 + k log k).

Space Complexity:
- The dictionaries `dict1` and `dict2` take O(n1 + n2) space.
- The result array takes O(k) space.

Overall space complexity: O(n1 + n2 + k).

Topic: Hash Table
"""