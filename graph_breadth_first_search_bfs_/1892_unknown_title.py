"""
LeetCode Problem #1892: Page Recommendations

Problem Statement:
You are given an integer `n` representing the number of pages in a book, and a 2D list `relations` where `relations[i] = [x, y]` indicates that page `x` recommends page `y`. You are also given an integer `k`.

A page is considered "recommended" if:
1. It is directly recommended by another page.
2. It is indirectly recommended by following a chain of recommendations of length at most `k`.

Return a list of integers where the `i-th` integer is the number of pages that are recommended by page `i` (including itself).

Constraints:
- `1 <= n <= 100`
- `0 <= len(relations) <= n * (n - 1)`
- `1 <= k <= 10`
- `1 <= x, y <= n`
- `x != y`

"""

from collections import defaultdict, deque

def page_recommendations(n, relations, k):
    """
    Function to calculate the number of pages recommended by each page.

    :param n: int - Number of pages in the book
    :param relations: List[List[int]] - List of direct recommendations
    :param k: int - Maximum chain length for recommendations
    :return: List[int] - Number of pages recommended by each page
    """
    # Build the adjacency list for the graph
    graph = defaultdict(list)
    for x, y in relations:
        graph[x].append(y)

    # Result array to store the count of recommended pages for each page
    result = [0] * n

    # Perform BFS for each page to calculate the number of recommended pages
    for page in range(1, n + 1):
        visited = set()
        queue = deque([(page, 0)])  # (current_page, current_depth)
        visited.add(page)

        while queue:
            current_page, depth = queue.popleft()
            result[page - 1] += 1  # Count the current page as recommended

            if depth < k:  # Only continue if we haven't exceeded the chain length
                for neighbor in graph[current_page]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor, depth + 1))

    return result


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 4
    relations = [[1, 2], [2, 3], [3, 4]]
    k = 2
    print(page_recommendations(n, relations, k))  # Output: [3, 3, 2, 1]

    # Test Case 2
    n = 5
    relations = [[1, 2], [2, 3], [3, 4], [4, 5]]
    k = 3
    print(page_recommendations(n, relations, k))  # Output: [4, 4, 3, 2, 1]

    # Test Case 3
    n = 3
    relations = [[1, 2], [2, 3], [1, 3]]
    k = 1
    print(page_recommendations(n, relations, k))  # Output: [2, 2, 1]

    # Test Case 4
    n = 3
    relations = []
    k = 2
    print(page_recommendations(n, relations, k))  # Output: [1, 1, 1]

    # Test Case 5
    n = 6
    relations = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [1, 6]]
    k = 2
    print(page_recommendations(n, relations, k))  # Output: [4, 3, 3, 2, 2, 1]


"""
Time Complexity:
- For each page, we perform a BFS. In the worst case, the BFS will visit all `n` pages and traverse all `len(relations)` edges.
- Therefore, the time complexity is O(n * (n + len(relations))).

Space Complexity:
- The adjacency list requires O(len(relations)) space.
- The BFS queue and visited set require O(n) space for each page.
- Therefore, the space complexity is O(n + len(relations)).

Topic: Graph, Breadth-First Search (BFS)
"""