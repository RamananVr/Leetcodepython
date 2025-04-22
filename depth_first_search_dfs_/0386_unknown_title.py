"""
LeetCode Problem #386: Lexicographical Numbers

Problem Statement:
Given an integer n, return 1 to n in lexicographical order.

In lexicographical order, strings are sorted as they are in a dictionary (alphabetical order). 
For example, "10" comes before "2" because "1" is smaller than "2" when comparing character by character.

You must write an algorithm to efficiently generate the lexicographical order for numbers from 1 to n.

Constraints:
- 1 <= n <= 10^5
"""

def lexicalOrder(n):
    """
    Generate numbers from 1 to n in lexicographical order.

    :param n: int, the upper limit of the range
    :return: List[int], numbers in lexicographical order
    """
    result = []
    
    def dfs(current):
        if current > n:
            return
        result.append(current)
        for i in range(10):
            next_num = current * 10 + i
            if next_num > n:
                break
            dfs(next_num)
    
    for i in range(1, 10):
        dfs(i)
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n = 13
    print(lexicalOrder(n))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]

    # Test Case 2
    n = 20
    print(lexicalOrder(n))  # Output: [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 3, 4, 5, 6, 7, 8, 9]

    # Test Case 3
    n = 5
    print(lexicalOrder(n))  # Output: [1, 2, 3, 4, 5]

"""
Time and Space Complexity Analysis:

Time Complexity:
The algorithm uses Depth-First Search (DFS) to traverse the numbers in lexicographical order. 
Each number is visited exactly once, and the total number of numbers is n. 
Thus, the time complexity is O(n).

Space Complexity:
The space complexity is determined by the recursion stack used in DFS. 
In the worst case, the depth of the recursion stack is proportional to the number of digits in n, which is O(log10(n)).
Additionally, the result list stores all n numbers, so the space complexity is O(n).

Overall Space Complexity: O(n + log10(n))

Topic: Depth-First Search (DFS)
"""