"""
LeetCode Problem #1225: Reported Posts

Problem Statement:
In a social media platform, users can report posts that they find inappropriate. Each report is represented as a pair of integers [a, b], where `a` is the ID of the user who reported the post, and `b` is the ID of the post being reported. Given a list of reports and an integer `k`, return the IDs of the posts that have been reported at least `k` times.

Input:
- reports: List[List[int]] - A list of reports where each report is a pair [a, b].
- k: int - The minimum number of reports a post must have to be included in the result.

Output:
- List[int] - A list of post IDs that have been reported at least `k` times.

Constraints:
- 1 <= len(reports) <= 10^4
- 1 <= a, b <= 10^4
- 1 <= k <= 10^4
- Each report is unique (no duplicate reports).

Example:
Input: reports = [[1, 101], [2, 101], [3, 102], [4, 101], [5, 102]], k = 2
Output: [101, 102]

Explanation:
- Post 101 has been reported 3 times (by users 1, 2, and 4).
- Post 102 has been reported 2 times (by users 3 and 5).
- Both posts 101 and 102 have been reported at least 2 times, so they are included in the result.
"""

from collections import defaultdict
from typing import List

def reported_posts(reports: List[List[int]], k: int) -> List[int]:
    """
    Function to find post IDs that have been reported at least k times.

    Args:
    reports (List[List[int]]): A list of reports where each report is a pair [a, b].
    k (int): The minimum number of reports a post must have to be included in the result.

    Returns:
    List[int]: A list of post IDs that have been reported at least k times.
    """
    # Dictionary to count the number of reports for each post
    post_report_count = defaultdict(int)
    
    # Count the reports for each post
    for _, post_id in reports:
        post_report_count[post_id] += 1
    
    # Filter posts that have been reported at least k times
    result = [post_id for post_id, count in post_report_count.items() if count >= k]
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    reports = [[1, 101], [2, 101], [3, 102], [4, 101], [5, 102]]
    k = 2
    print(reported_posts(reports, k))  # Output: [101, 102]

    # Test Case 2
    reports = [[1, 201], [2, 202], [3, 201], [4, 202], [5, 203]]
    k = 2
    print(reported_posts(reports, k))  # Output: [201, 202]

    # Test Case 3
    reports = [[1, 301], [2, 302], [3, 303], [4, 304], [5, 305]]
    k = 1
    print(reported_posts(reports, k))  # Output: [301, 302, 303, 304, 305]

    # Test Case 4
    reports = [[1, 401], [2, 401], [3, 401], [4, 402], [5, 402]]
    k = 3
    print(reported_posts(reports, k))  # Output: [401]

    # Test Case 5
    reports = []
    k = 1
    print(reported_posts(reports, k))  # Output: []

"""
Time Complexity Analysis:
- Counting the reports for each post: O(n), where n is the number of reports.
- Filtering posts with at least k reports: O(m), where m is the number of unique posts.
- Overall time complexity: O(n + m).

Space Complexity Analysis:
- Space used by the dictionary to store report counts: O(m), where m is the number of unique posts.
- Overall space complexity: O(m).

Topic: Hash Table
"""