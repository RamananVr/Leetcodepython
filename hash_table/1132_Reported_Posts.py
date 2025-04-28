"""
LeetCode Problem #1132: Reported Posts

Problem Statement:
You are given a list of posts and a list of reports. Each report is a tuple (a, b) where user `a` reports post `b`. 
A post is considered "reported" if it has been reported by at least `k` unique users. Your task is to return a list 
of all posts that are reported.

Write a function `reported_posts(posts: List[int], reports: List[Tuple[int, int]], k: int) -> List[int]` that takes:
- `posts`: A list of integers representing post IDs.
- `reports`: A list of tuples where each tuple (a, b) represents that user `a` reported post `b`.
- `k`: An integer threshold for the number of unique reports required for a post to be considered "reported".

The function should return a list of post IDs that are reported, sorted in ascending order.

Constraints:
- 1 <= len(posts) <= 10^4
- 1 <= len(reports) <= 10^5
- 1 <= k <= 10^3
- Each post ID in `posts` is unique.
- Each report (a, b) is unique.

Example:
Input:
posts = [1, 2, 3, 4]
reports = [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]
k = 2

Output:
[2, 3]

Explanation:
- Post 2 is reported by users 1, 2, and 3 (3 unique reports, >= k).
- Post 3 is reported by users 1 and 2 (2 unique reports, >= k).
- Post 4 is not reported by any user.
- Post 1 is not reported by any user.
"""

from typing import List, Tuple
from collections import defaultdict

def reported_posts(posts: List[int], reports: List[Tuple[int, int]], k: int) -> List[int]:
    # Dictionary to store unique reporters for each post
    post_reports = defaultdict(set)
    
    # Process each report
    for user, post in reports:
        post_reports[post].add(user)
    
    # Find posts with at least k unique reports
    result = [post for post in posts if len(post_reports[post]) >= k]
    
    # Return the result sorted in ascending order
    return sorted(result)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    posts = [1, 2, 3, 4]
    reports = [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3)]
    k = 2
    print(reported_posts(posts, reports, k))  # Output: [2, 3]

    # Test Case 2
    posts = [1, 2, 3]
    reports = [(1, 1), (2, 1), (3, 1), (1, 2)]
    k = 3
    print(reported_posts(posts, reports, k))  # Output: [1]

    # Test Case 3
    posts = [1, 2, 3, 4, 5]
    reports = [(1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]
    k = 5
    print(reported_posts(posts, reports, k))  # Output: [5]

    # Test Case 4
    posts = [1, 2, 3]
    reports = []
    k = 1
    print(reported_posts(posts, reports, k))  # Output: []

    # Test Case 5
    posts = [1, 2, 3, 4]
    reports = [(1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
    k = 3
    print(reported_posts(posts, reports, k))  # Output: [2, 3]

"""
Time Complexity Analysis:
- Processing the reports: O(len(reports)), as we iterate through the list of reports.
- Checking the number of unique reporters for each post: O(len(posts)), as we iterate through the list of posts.
- Sorting the result: O(len(result) * log(len(result))), where `result` is the list of reported posts.
Overall: O(len(reports) + len(posts) + len(result) * log(len(result)))

Space Complexity Analysis:
- The `post_reports` dictionary stores sets of unique reporters for each post. In the worst case, this requires O(len(reports)) space.
- The result list requires O(len(posts)) space in the worst case.
Overall: O(len(reports) + len(posts))

Topic: Hash Table
"""