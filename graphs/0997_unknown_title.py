"""
LeetCode Problem #997: Find the Town Judge

Problem Statement:
In a town, there are `n` people labeled from 1 to `n`. There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:
1. The town judge trusts nobody.
2. Everybody (except for the town judge) trusts the town judge.
3. There is exactly one person that satisfies properties 1 and 2.

You are given an array `trust` where `trust[i] = [a, b]` represents that the person labeled `a` trusts the person labeled `b`.

Return the label of the town judge if the town judge exists and can be identified, or return -1 otherwise.

Constraints:
- 1 <= n <= 1000
- 0 <= trust.length <= 10^4
- trust[i].length == 2
- 1 <= a, b <= n
- a != b

"""

def findJudge(n: int, trust: list[list[int]]) -> int:
    # If there's only one person and no trust relationships, they are the judge.
    if n == 1 and not trust:
        return 1

    # Create two arrays to track trust counts.
    trust_counts = [0] * (n + 1)
    trusted_by_counts = [0] * (n + 1)

    # Process the trust relationships.
    for a, b in trust:
        trust_counts[a] += 1  # a trusts someone
        trusted_by_counts[b] += 1  # b is trusted by someone

    # Check for the town judge.
    for i in range(1, n + 1):
        if trust_counts[i] == 0 and trusted_by_counts[i] == n - 1:
            return i

    return -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Basic case with a clear judge
    n1 = 3
    trust1 = [[1, 3], [2, 3]]
    print(findJudge(n1, trust1))  # Expected Output: 3

    # Test Case 2: No judge exists
    n2 = 3
    trust2 = [[1, 3], [2, 3], [3, 1]]
    print(findJudge(n2, trust2))  # Expected Output: -1

    # Test Case 3: Single person in the town
    n3 = 1
    trust3 = []
    print(findJudge(n3, trust3))  # Expected Output: 1

    # Test Case 4: Larger case with a judge
    n4 = 4
    trust4 = [[1, 3], [1, 4], [2, 3], [2, 4], [4, 3]]
    print(findJudge(n4, trust4))  # Expected Output: 3

    # Test Case 5: No trust relationships, multiple people
    n5 = 2
    trust5 = []
    print(findJudge(n5, trust5))  # Expected Output: -1

"""
Time and Space Complexity Analysis:

Time Complexity:
- Processing the `trust` array takes O(E), where E is the length of the `trust` array.
- Checking the potential judge takes O(n), where n is the number of people.
- Overall time complexity: O(E + n).

Space Complexity:
- We use two arrays of size n+1 to track trust counts and trusted-by counts.
- Space complexity: O(n).

Topic: Graphs
"""