"""
LeetCode Problem #406: Queue Reconstruction by Height

Problem Statement:
You are given an array of people, `people`, where `people[i] = [hi, ki]`:
- `hi` is the height of the ith person.
- `ki` is the number of people in front of the ith person who have a height greater than or equal to `hi`.

Reconstruct and return the queue that is represented by the input array `people`. 
The returned queue should be formatted as an array `queue`, where `queue[j] = [hj, kj]` is the attributes of the jth person in the queue.

Example 1:
Input: people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
Output: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

Example 2:
Input: people = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
Output: [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]

Constraints:
- 1 <= people.length <= 2000
- 0 <= hi <= 10^6
- 0 <= ki < people.length
- It is guaranteed that the queue can be reconstructed.

"""

# Clean and Correct Python Solution
from typing import List

def reconstructQueue(people: List[List[int]]) -> List[List[int]]:
    # Sort the people array:
    # 1. By height in descending order (taller people first).
    # 2. By k-value in ascending order (if heights are the same).
    people.sort(key=lambda x: (-x[0], x[1]))
    
    # Initialize an empty list to reconstruct the queue.
    queue = []
    
    # Insert each person into the queue at the index specified by their k-value.
    for person in people:
        queue.insert(person[1], person)
    
    return queue

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    people1 = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print("Test Case 1 Output:", reconstructQueue(people1))  # Expected: [[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]]

    # Test Case 2
    people2 = [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]
    print("Test Case 2 Output:", reconstructQueue(people2))  # Expected: [[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]]

    # Test Case 3
    people3 = [[9, 0], [7, 0], [1, 9], [3, 0], [2, 7], [5, 3], [6, 0], [3, 4], [6, 2], [5, 2]]
    print("Test Case 3 Output:", reconstructQueue(people3))  # Expected: [[3, 0], [6, 0], [7, 0], [5, 2], [3, 4], [5, 3], [6, 2], [9, 0], [2, 7], [1, 9]]

# Time and Space Complexity Analysis
"""
Time Complexity:
1. Sorting the `people` array takes O(n log n), where n is the length of the array.
2. Inserting each person into the queue takes O(n) in the worst case (due to list insertion at a specific index).
   Since we do this for all n people, the total insertion cost is O(n^2).
Overall Time Complexity: O(n^2).

Space Complexity:
1. The space used by the `queue` list is O(n), where n is the number of people.
2. The sorting operation may use additional space depending on the sorting algorithm, but this is typically O(1) for in-place sorting.
Overall Space Complexity: O(n).
"""

# Topic: Arrays, Sorting, Greedy Algorithm