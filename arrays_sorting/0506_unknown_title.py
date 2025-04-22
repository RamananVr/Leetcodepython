"""
LeetCode Problem #506: Relative Ranks

Problem Statement:
You are given an integer array `score` of size `n`, where `score[i]` is the score of the ith athlete in a competition. 
All the scores are guaranteed to be unique.

The athletes are ranked according to their scores, where the 1st place athlete has the highest score, the 2nd place 
athlete has the 2nd highest score, and so on. The ranking is represented by:

- "Gold Medal" for the 1st place,
- "Silver Medal" for the 2nd place,
- "Bronze Medal" for the 3rd place,
- A string of their numeric rank (e.g., "4", "5", etc.) for the 4th place and beyond.

Return an array `result` where `result[i]` is the rank of the ith athlete.

Constraints:
- 1 <= score.length <= 10^4
- 0 <= score[i] <= 10^6
- All the values in `score` are unique.
"""

def findRelativeRanks(score):
    """
    Function to determine the relative ranks of athletes based on their scores.

    :param score: List[int] - List of scores of athletes
    :return: List[str] - List of ranks corresponding to the scores
    """
    # Step 1: Sort the scores in descending order and keep track of the original indices
    sorted_scores = sorted(enumerate(score), key=lambda x: -x[1])
    
    # Step 2: Create a result array to store the ranks
    result = [""] * len(score)
    
    # Step 3: Assign ranks based on the sorted order
    for rank, (index, _) in enumerate(sorted_scores):
        if rank == 0:
            result[index] = "Gold Medal"
        elif rank == 1:
            result[index] = "Silver Medal"
        elif rank == 2:
            result[index] = "Bronze Medal"
        else:
            result[index] = str(rank + 1)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    score1 = [5, 4, 3, 2, 1]
    print(findRelativeRanks(score1))  # Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]

    # Test Case 2
    score2 = [10, 3, 8, 9, 4]
    print(findRelativeRanks(score2))  # Output: ["Gold Medal", "5", "Bronze Medal", "Silver Medal", "4"]

    # Test Case 3
    score3 = [100]
    print(findRelativeRanks(score3))  # Output: ["Gold Medal"]

    # Test Case 4
    score4 = [1, 2, 3, 4, 5]
    print(findRelativeRanks(score4))  # Output: ["5", "4", "Bronze Medal", "Silver Medal", "Gold Medal"]

"""
Time Complexity Analysis:
- Sorting the scores takes O(n log n), where n is the length of the `score` array.
- Assigning ranks to the athletes takes O(n).
- Overall time complexity: O(n log n).

Space Complexity Analysis:
- The space required for the `sorted_scores` list is O(n).
- The space required for the `result` list is O(n).
- Overall space complexity: O(n).

Topic: Arrays, Sorting
"""