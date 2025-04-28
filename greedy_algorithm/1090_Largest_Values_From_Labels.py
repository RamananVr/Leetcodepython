"""
LeetCode Problem #1090: Largest Values From Labels

Problem Statement:
We have a set of items: the i-th item has value `values[i]` and label `labels[i]`.
We choose a subset `S` of these items, such that:
    - |S| <= num_wanted (the subset size is at most `num_wanted`), and
    - There are at most `use_limit` items with the same label in `S`.

Return the largest possible sum of the subset `S`.

Constraints:
- `values.length == labels.length`
- `1 <= values.length <= 2 * 10^4`
- `0 <= values[i], labels[i] <= 2 * 10^4`
- `1 <= num_wanted, use_limit <= values.length`
"""

from collections import defaultdict

def largestValsFromLabels(values, labels, num_wanted, use_limit):
    """
    Finds the largest possible sum of a subset of items, adhering to the constraints.
    
    :param values: List[int] - The values of the items.
    :param labels: List[int] - The labels of the items.
    :param num_wanted: int - The maximum number of items in the subset.
    :param use_limit: int - The maximum number of items with the same label in the subset.
    :return: int - The largest possible sum of the subset.
    """
    # Combine values and labels into a list of tuples and sort by value in descending order
    items = sorted(zip(values, labels), key=lambda x: -x[0])
    
    label_count = defaultdict(int)  # To track the count of items per label
    total_sum = 0
    count = 0  # To track the total number of items in the subset
    
    for value, label in items:
        if count >= num_wanted:  # Stop if we've reached the maximum number of items
            break
        if label_count[label] < use_limit:  # Check if we can add another item with this label
            total_sum += value
            label_count[label] += 1
            count += 1
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    values = [5, 4, 3, 2, 1]
    labels = [1, 1, 2, 2, 3]
    num_wanted = 3
    use_limit = 1
    print(largestValsFromLabels(values, labels, num_wanted, use_limit))  # Output: 9

    # Test Case 2
    values = [5, 4, 3, 2, 1]
    labels = [1, 3, 3, 3, 2]
    num_wanted = 3
    use_limit = 2
    print(largestValsFromLabels(values, labels, num_wanted, use_limit))  # Output: 12

    # Test Case 3
    values = [9, 8, 8, 7, 6]
    labels = [0, 0, 0, 1, 1]
    num_wanted = 3
    use_limit = 1
    print(largestValsFromLabels(values, labels, num_wanted, use_limit))  # Output: 16

    # Test Case 4
    values = [9, 8, 8, 7, 6]
    labels = [0, 0, 0, 1, 1]
    num_wanted = 3
    use_limit = 2
    print(largestValsFromLabels(values, labels, num_wanted, use_limit))  # Output: 24

"""
Time Complexity:
- Sorting the items takes O(n log n), where n is the length of the `values` list.
- Iterating through the sorted list takes O(n).
- Overall time complexity: O(n log n).

Space Complexity:
- The `label_count` dictionary requires O(k) space, where k is the number of unique labels.
- The sorted list of items requires O(n) space.
- Overall space complexity: O(n + k).

Topic: Greedy Algorithm
"""