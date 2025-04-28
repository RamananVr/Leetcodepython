"""
LeetCode Problem #2844: Minimum Operations to Make a Special Number

Problem Statement:
You are given a string `num` representing a non-negative integer. A special number is a number that is divisible by 25. 
In one operation, you can remove one digit from the string `num`. The goal is to determine the minimum number of operations 
required to make the number represented by `num` a special number. If it is impossible to make `num` a special number, return -1.

Constraints:
- `1 <= num.length <= 100`
- `num` consists of digits ('0'-'9') only.
"""

# Solution
def minimumOperations(num: str) -> int:
    """
    Finds the minimum number of operations required to make the number represented by `num` divisible by 25.
    
    Args:
    num (str): A string representing a non-negative integer.
    
    Returns:
    int: Minimum number of operations required, or -1 if impossible.
    """
    n = len(num)
    min_operations = float('inf')
    
    # Check for pairs that make the number divisible by 25
    for target in ['00', '25', '50', '75']:
        j = len(target) - 1
        operations = 0
        for i in range(n - 1, -1, -1):
            if num[i] == target[j]:
                j -= 1
                if j < 0:
                    break
            else:
                operations += 1
        if j < 0:
            min_operations = min(min_operations, operations)
    
    return min_operations if min_operations != float('inf') else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Already divisible by 25
    print(minimumOperations("100"))  # Output: 0
    
    # Test Case 2: Remove digits to make divisible by 25
    print(minimumOperations("205"))  # Output: 1
    
    # Test Case 3: Impossible to make divisible by 25
    print(minimumOperations("1"))    # Output: -1
    
    # Test Case 4: Remove multiple digits
    print(minimumOperations("750"))  # Output: 0
    
    # Test Case 5: Remove digits to form "25"
    print(minimumOperations("12345"))  # Output: 2

"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates over the string `num` for each of the four target pairs ('00', '25', '50', '75').
- For each target pair, we perform a reverse traversal of the string `num`, which takes O(n) time.
- Since there are 4 target pairs, the total time complexity is O(4 * n) = O(n), where n is the length of the string `num`.

Space Complexity:
- The algorithm uses a constant amount of extra space for variables and does not use any additional data structures.
- Therefore, the space complexity is O(1).

Topic: Strings
"""