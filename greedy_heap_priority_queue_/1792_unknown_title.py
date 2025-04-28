"""
LeetCode Problem #1792: Maximum Average Pass Ratio

Problem Statement:
There is a school that has classes. Each class has a certain number of students and a certain number of students who have already passed the class. 
You are given an array classes, where classes[i] = [passi, totali]. You are also given an integer extraStudents. You can assign the extraStudents 
to any class in such a way that the average pass ratio across all the classes is maximized.

The pass ratio of a class is defined as passi / totali. The average pass ratio is the sum of pass ratios of all the classes divided by the number of classes.

Return the maximum possible average pass ratio after assigning the extraStudents optimally.

Constraints:
- 1 <= classes.length <= 10^5
- classes[i].length == 2
- 1 <= passi <= totali <= 10^5
- 1 <= extraStudents <= 10^5
- The input is generated such that the answer will be within 10^-5 of the actual answer.

"""

import heapq

def maxAverageRatio(classes, extraStudents):
    """
    Calculate the maximum average pass ratio after assigning extra students optimally.

    :param classes: List[List[int]] - A list of classes where each class is represented as [passi, totali].
    :param extraStudents: int - The number of extra students to assign.
    :return: float - The maximum possible average pass ratio.
    """
    # Define a function to calculate the gain in pass ratio by adding one student
    def gain(passi, totali):
        return (passi + 1) / (totali + 1) - passi / totali

    # Create a max-heap based on the gain of adding one student
    max_heap = [(-gain(passi, totali), passi, totali) for passi, totali in classes]
    heapq.heapify(max_heap)

    # Assign extra students to maximize the average pass ratio
    for _ in range(extraStudents):
        g, passi, totali = heapq.heappop(max_heap)
        passi += 1
        totali += 1
        heapq.heappush(max_heap, (-gain(passi, totali), passi, totali))

    # Calculate the final average pass ratio
    total_ratio = sum(passi / totali for _, passi, totali in max_heap)
    return total_ratio / len(classes)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    classes1 = [[1, 2], [3, 5], [2, 2]]
    extraStudents1 = 2
    print(maxAverageRatio(classes1, extraStudents1))  # Expected Output: 0.78333

    # Test Case 2
    classes2 = [[2, 4], [3, 9], [4, 5], [2, 10]]
    extraStudents2 = 4
    print(maxAverageRatio(classes2, extraStudents2))  # Expected Output: 0.53485

    # Test Case 3
    classes3 = [[5, 10], [2, 3], [1, 2]]
    extraStudents3 = 3
    print(maxAverageRatio(classes3, extraStudents3))  # Expected Output: 0.76667

"""
Time and Space Complexity Analysis:

Time Complexity:
- Building the initial heap takes O(n), where n is the number of classes.
- Each heap operation (pop and push) takes O(log n).
- We perform heap operations for each of the extraStudents, so the total time complexity is O(extraStudents * log n).

Space Complexity:
- The heap stores n elements, so the space complexity is O(n).

Topic: Greedy, Heap (Priority Queue)
"""