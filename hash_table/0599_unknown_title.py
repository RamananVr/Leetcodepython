"""
LeetCode Problem #599: Minimum Index Sum of Two Lists

Problem Statement:
Given two arrays `list1` and `list2`, find the common strings with the least index sum. 
A string's index sum is defined as the sum of its indices in `list1` and `list2`. 
If there is a tie, return all the strings with the minimum index sum in a list. 
The result can be returned in any order.

Example:
Input: list1 = ["Shogun", "Tapioca", "Burger", "Pizza"], list2 = ["Pizza", "Burger", "Shogun"]
Output: ["Shogun"]
Explanation: The common strings are "Shogun", "Burger", and "Pizza". The index sum of "Shogun" is 0 + 2 = 2. 
The index sum of "Burger" is 2 + 1 = 3. The index sum of "Pizza" is 3 + 0 = 3. 
The minimum index sum is 2, so the result is ["Shogun"].

Constraints:
- 1 <= list1.length, list2.length <= 1000
- 1 <= list1[i].length, list2[i].length <= 30
- list1[i] and list2[i] consist of English letters and are unique.
"""

def findRestaurant(list1, list2):
    """
    Finds the common strings with the least index sum between two lists.

    Args:
    list1 (List[str]): First list of strings.
    list2 (List[str]): Second list of strings.

    Returns:
    List[str]: List of strings with the minimum index sum.
    """
    # Create a dictionary to store the indices of elements in list1
    index_map = {word: idx for idx, word in enumerate(list1)}
    
    # Initialize variables to track the minimum index sum and the result
    min_index_sum = float('inf')
    result = []
    
    # Iterate through list2 and calculate index sums for common strings
    for idx2, word in enumerate(list2):
        if word in index_map:
            index_sum = idx2 + index_map[word]
            if index_sum < min_index_sum:
                min_index_sum = index_sum
                result = [word]
            elif index_sum == min_index_sum:
                result.append(word)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    list1 = ["Shogun", "Tapioca", "Burger", "Pizza"]
    list2 = ["Pizza", "Burger", "Shogun"]
    print(findRestaurant(list1, list2))  # Output: ["Shogun"]

    # Test Case 2
    list1 = ["Shogun", "Tapioca", "Burger", "Pizza"]
    list2 = ["Burger", "Pizza", "Shogun"]
    print(findRestaurant(list1, list2))  # Output: ["Shogun"]

    # Test Case 3
    list1 = ["Shogun", "Tapioca", "Burger", "Pizza"]
    list2 = ["Tapioca", "Burger", "Pizza"]
    print(findRestaurant(list1, list2))  # Output: ["Tapioca"]

    # Test Case 4
    list1 = ["a", "b", "c"]
    list2 = ["c", "b", "a"]
    print(findRestaurant(list1, list2))  # Output: ["a", "b", "c"]

"""
Time and Space Complexity Analysis:

Time Complexity:
- Constructing the `index_map` dictionary takes O(n), where n is the length of `list1`.
- Iterating through `list2` takes O(m), where m is the length of `list2`.
- Checking if a word exists in `index_map` and calculating the index sum are O(1) operations.
- Overall, the time complexity is O(n + m).

Space Complexity:
- The `index_map` dictionary requires O(n) space, where n is the length of `list1`.
- The `result` list requires O(k) space, where k is the number of common strings with the minimum index sum.
- Overall, the space complexity is O(n + k).

Topic: Hash Table
"""