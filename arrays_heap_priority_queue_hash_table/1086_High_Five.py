"""
LeetCode Problem #1086: High Five

Problem Statement:
Given a list of scores of different students, `items`, where `items[i] = [IDi, scorei]` represents one score from a student with ID `IDi`, calculate each student's top five average. Return the answer as an array of pairs result, where `result[j] = [IDj, topFiveAveragej]` represents the student ID `IDj` and their top five average. The result array should be sorted in ascending order by student ID.

A student's top five average is calculated as the integer part of the average of their top five scores. If a student has fewer than five scores, use all their scores to calculate the average.

Constraints:
1. `1 <= items.length <= 1000`
2. `items[i].length == 2`
3. `1 <= IDi <= 1000`
4. `0 <= scorei <= 100`
5. For each `IDi`, there will be at least one score.

Example:
Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation:
The student with ID = 1 has scores 91, 92, 60, 65, 87, and 100. Their top five scores are 100, 92, 91, 87, and 65, and their average is (100 + 92 + 91 + 87 + 65) // 5 = 87.
The student with ID = 2 has scores 93, 97, 77, 100, and 76. Their top five scores are 100, 97, 93, 77, and 76, and their average is (100 + 97 + 93 + 77 + 76) // 5 = 88.
"""

from collections import defaultdict
import heapq

def highFive(items):
    """
    Calculate the top five average for each student.

    :param items: List[List[int]] - A list of [student ID, score] pairs.
    :return: List[List[int]] - A list of [student ID, top five average] pairs sorted by student ID.
    """
    # Dictionary to store min-heaps for each student
    scores = defaultdict(list)

    # Iterate through the items and maintain a min-heap of size 5 for each student
    for student_id, score in items:
        heapq.heappush(scores[student_id], score)
        if len(scores[student_id]) > 5:
            heapq.heappop(scores[student_id])  # Remove the smallest score if heap size exceeds 5

    # Calculate the top five average for each student
    result = []
    for student_id in sorted(scores.keys()):
        top_five_average = sum(scores[student_id]) // len(scores[student_id])
        result.append([student_id, top_five_average])

    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    items1 = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
    print(highFive(items1))  # Expected Output: [[1,87],[2,88]]

    # Test Case 2
    items2 = [[1,100],[7,90],[1,95],[7,80],[1,80],[7,85],[1,70],[7,75],[1,60],[7,95]]
    print(highFive(items2))  # Expected Output: [[1,81],[7,85]]

    # Test Case 3
    items3 = [[1,50],[1,60],[1,70],[1,80],[1,90]]
    print(highFive(items3))  # Expected Output: [[1,70]]

    # Test Case 4
    items4 = [[1,100],[2,100],[3,100],[4,100],[5,100]]
    print(highFive(items4))  # Expected Output: [[1,100],[2,100],[3,100],[4,100],[5,100]]

"""
Time Complexity:
- Inserting into a heap of size 5 takes O(log 5) = O(1).
- For each of the `n` scores in the input, we perform a heap operation, so the total time complexity is O(n).
- Sorting the student IDs takes O(k log k), where `k` is the number of unique student IDs.
- Overall time complexity: O(n + k log k).

Space Complexity:
- We use a dictionary to store heaps for each student. In the worst case, we store up to 5 scores for each of the `k` students.
- Space complexity: O(k * 5) = O(k).

Topic: Arrays, Heap (Priority Queue), Hash Table
"""