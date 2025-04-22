"""
LeetCode Problem #433: Minimum Genetic Mutation

Problem Statement:
A gene string can be represented by an 8-character long string, where each character is one of 'A', 'C', 'G', or 'T'. 
Suppose we need to investigate a mutation from a start gene string to an end gene string where one mutation is defined 
as one single character changed in the gene string.

- For example, "AACCGGTT" -> "AACCGGTA" is one mutation.

There is also a gene bank that records all the valid gene mutations. A gene must be in the bank to make it a valid gene string.

Given the two gene strings `start` and `end`, and a list of gene strings `bank`, return the minimum number of mutations 
needed to mutate from `start` to `end`. If there is no such mutation, return -1.

Note:
- The starting point is assumed to be valid, but it might not be included in the bank.
- If the end string is not in the bank, return -1.

Constraints:
- `start.length == 8`
- `end.length == 8`
- `0 <= bank.length <= 10^3`
- `bank[i].length == 8`
- `start`, `end`, and `bank[i]` consist of only the characters ['A', 'C', 'G', 'T'].

"""

from collections import deque

def minMutation(start: str, end: str, bank: list[str]) -> int:
    if end not in bank:
        return -1

    # Helper function to check if two gene strings differ by exactly one character
    def is_one_mutation_away(gene1, gene2):
        diff_count = 0
        for c1, c2 in zip(gene1, gene2):
            if c1 != c2:
                diff_count += 1
                if diff_count > 1:
                    return False
        return diff_count == 1

    # BFS setup
    bank_set = set(bank)  # Use a set for O(1) lookups
    queue = deque([(start, 0)])  # (current_gene, mutation_count)
    visited = set()

    while queue:
        current_gene, mutations = queue.popleft()

        if current_gene == end:
            return mutations

        for gene in list(bank_set):
            if is_one_mutation_away(current_gene, gene) and gene not in visited:
                visited.add(gene)
                queue.append((gene, mutations + 1))

    return -1


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    start = "AACCGGTT"
    end = "AACCGGTA"
    bank = ["AACCGGTA"]
    print(minMutation(start, end, bank))  # Output: 1

    # Test Case 2
    start = "AACCGGTT"
    end = "AAACGGTA"
    bank = ["AACCGGTA", "AACCGCTA", "AAACGGTA"]
    print(minMutation(start, end, bank))  # Output: 2

    # Test Case 3
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC", "AACCCCCC"]
    print(minMutation(start, end, bank))  # Output: 3

    # Test Case 4
    start = "AAAAACCC"
    end = "AACCCCCC"
    bank = ["AAAACCCC", "AAACCCCC"]
    print(minMutation(start, end, bank))  # Output: -1


"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `n` be the length of the bank (number of gene strings in the bank).
- Let `m` be the length of each gene string (fixed at 8 in this problem).
- For each gene in the bank, we check if it is one mutation away from the current gene. This takes O(m) time.
- In the worst case, we process all `n` genes in the bank, and for each gene, we perform the mutation check.
- BFS ensures that each gene is processed at most once, so the overall time complexity is O(n * m).

Space Complexity:
- The space required for the queue is O(n) in the worst case, where all genes are added to the queue.
- The space required for the visited set is O(n).
- The space required for the bank set is O(n).
- Overall space complexity is O(n).

Topic: Breadth-First Search (BFS)
"""