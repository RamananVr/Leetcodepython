"""
LeetCode Problem #332: Reconstruct Itinerary

Problem Statement:
You are given a list of airline tickets where tickets[i] = [from_i, to_i] represent the departure and the arrival airports of one flight. Reconstruct the itinerary in order and return it. All of the tickets belong to a man who departs from "JFK". Thus, the itinerary must begin with "JFK".

If there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order when read as a single string. For example, the itinerary ["JFK", "ATL", "JFK", "SFO"] has a smaller lexical order than ["JFK", "SFO", "JFK", "ATL"].

You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

Constraints:
- 1 <= tickets.length <= 300
- tickets[i].length == 2
- from_i.length == 3
- to_i.length == 3
- from_i and to_i consist of uppercase English letters.
- from_i != to_i
"""

from collections import defaultdict
import heapq

def findItinerary(tickets):
    """
    Reconstructs the itinerary using all tickets exactly once, starting from "JFK".
    
    :param tickets: List[List[str]] - List of tickets where each ticket is [from, to].
    :return: List[str] - The reconstructed itinerary in lexical order.
    """
    # Build the graph using a min-heap for lexical order
    graph = defaultdict(list)
    for frm, to in tickets:
        heapq.heappush(graph[frm], to)
    
    result = []
    
    def dfs(airport):
        # Visit all destinations from the current airport in lexical order
        while graph[airport]:
            next_airport = heapq.heappop(graph[airport])
            dfs(next_airport)
        # Append the airport to the result in reverse order
        result.append(airport)
    
    # Start DFS from "JFK"
    dfs("JFK")
    return result[::-1]  # Reverse the result to get the correct order

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    tickets1 = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
    print(findItinerary(tickets1))  # Output: ["JFK", "MUC", "LHR", "SFO", "SJC"]

    # Test Case 2
    tickets2 = [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]
    print(findItinerary(tickets2))  # Output: ["JFK", "ATL", "JFK", "SFO", "ATL", "SFO"]

    # Test Case 3
    tickets3 = [["JFK", "KUL"], ["JFK", "NRT"], ["NRT", "JFK"]]
    print(findItinerary(tickets3))  # Output: ["JFK", "NRT", "JFK", "KUL"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the graph takes O(E * log(E)) time, where E is the number of tickets, because we use a min-heap to store destinations.
- The DFS traversal visits each edge once, so it takes O(E) time.
- Overall, the time complexity is O(E * log(E)).

Space Complexity:
- The graph uses O(V + E) space, where V is the number of unique airports and E is the number of tickets.
- The recursion stack in the worst case can go as deep as O(V).
- Overall, the space complexity is O(V + E).
"""

# Topic: Graphs