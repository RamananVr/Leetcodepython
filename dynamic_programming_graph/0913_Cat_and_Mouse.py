"""
LeetCode Problem #913: Cat and Mouse

Problem Statement:
A game is played by a cat and a mouse named Cat and Mouse. The game is played on a graph with n nodes. 
Each node is uniquely numbered from 0 to n - 1. The graph is given as follows: graph[a] is a list of all nodes b 
such that there is an edge between nodes a and b.

Mouse starts at node 1 and Cat starts at node 2. Node 0 is the "hole" where the mouse can escape. 
During each turn, Mouse moves first, then Cat moves, and they continue taking turns. 
NOTE: Mouse cannot move to the same node as Cat, and Cat cannot move to the "hole" (node 0).

The game ends if:
1. Mouse reaches the hole (node 0), and the mouse wins.
2. Cat catches the mouse, and the cat wins.
3. The game will continue forever if both players keep moving without winning.

You are given a graph, and you need to determine the outcome of the game if both players play optimally:
- If the mouse wins, return 1.
- If the cat wins, return 2.
- If the game continues forever, return 0.

Constraints:
- 3 <= graph.length <= 50
- 1 <= graph[i].length < graph.length
- 0 <= graph[i][j] < graph.length
- graph[i] is a list of distinct nodes.
- The graph is connected.

"""

from collections import deque

def catMouseGame(graph):
    n = len(graph)
    DRAW, MOUSE_WIN, CAT_WIN = 0, 1, 2

    # dp[mouse][cat][turn] represents the result of the game when:
    # - mouse is at `mouse`
    # - cat is at `cat`
    # - it's `turn`'s turn (0 for mouse, 1 for cat)
    dp = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]

    # Base cases
    for i in range(n):
        dp[0][i][0] = dp[0][i][1] = MOUSE_WIN  # Mouse wins if it reaches the hole
        dp[i][i][0] = dp[i][i][1] = CAT_WIN    # Cat wins if it catches the mouse

    # Reverse BFS to determine the outcome of all states
    queue = deque()
    for i in range(n):
        for t in range(2):
            queue.append((0, i, t, MOUSE_WIN))  # Mouse wins if it reaches the hole
            queue.append((i, i, t, CAT_WIN))    # Cat wins if it catches the mouse

    while queue:
        mouse, cat, turn, result = queue.popleft()
        dp[mouse][cat][turn] = result

        if turn == 0:  # Mouse's turn
            for prev_mouse in graph[mouse]:
                if dp[prev_mouse][cat][1] == DRAW:  # Cat's turn next
                    if result == MOUSE_WIN:
                        dp[prev_mouse][cat][1] = MOUSE_WIN
                        queue.append((prev_mouse, cat, 1, MOUSE_WIN))
                    elif all(dp[next_mouse][cat][1] == CAT_WIN for next_mouse in graph[prev_mouse]):
                        dp[prev_mouse][cat][1] = CAT_WIN
                        queue.append((prev_mouse, cat, 1, CAT_WIN))
        else:  # Cat's turn
            for prev_cat in graph[cat]:
                if prev_cat == 0:  # Cat cannot move to the hole
                    continue
                if dp[mouse][prev_cat][0] == DRAW:  # Mouse's turn next
                    if result == CAT_WIN:
                        dp[mouse][prev_cat][0] = CAT_WIN
                        queue.append((mouse, prev_cat, 0, CAT_WIN))
                    elif all(dp[mouse][next_cat][0] == MOUSE_WIN for next_cat in graph[prev_cat] if next_cat != 0):
                        dp[mouse][prev_cat][0] = MOUSE_WIN
                        queue.append((mouse, prev_cat, 0, MOUSE_WIN))

    return dp[1][2][0]

# Example Test Cases
if __name__ == "__main__":
    graph1 = [[2,5],[3],[0,4,5],[1,4,5],[2,3],[0,2,3]]
    graph2 = [[1,3],[0],[3],[0,2]]

    print(catMouseGame(graph1))  # Output: 0 (Game continues forever)
    print(catMouseGame(graph2))  # Output: 1 (Mouse wins)

"""
Time and Space Complexity Analysis:

Time Complexity:
- The number of states in the game is O(n^2 * 2), where n is the number of nodes in the graph.
- Each state is processed once, and for each state, we iterate over the neighbors of the mouse and cat.
- Therefore, the time complexity is O(n^3) in the worst case.

Space Complexity:
- The space complexity is O(n^2 * 2) for the dp table and O(n^2 * 2) for the queue.
- Therefore, the space complexity is O(n^2).

Topic: Dynamic Programming, Graph
"""