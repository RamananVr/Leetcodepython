"""
LeetCode Problem #1652: Defuse the Bomb

Problem Statement:
You have a bomb to defuse, and your time is running out! Your task is to find the code of the bomb.

The code is represented by a list of integers `code` and a key `k`.

To decrypt the code:
- If `k > 0`, replace the `i-th` number in the code with the sum of the next `k` numbers.
- If `k < 0`, replace the `i-th` number in the code with the sum of the previous `k` numbers.
- If `k == 0`, replace the `i-th` number with `0`.

Since the code is circular, the next element after the last element is the first element, and the previous element before the first element is the last element.

Given the circular list `code` and an integer `k`, return the decrypted code as a list of integers.

Example:
Input: code = [5, 7, 1, 4], k = 3
Output: [12, 10, 16, 13]

Constraints:
- `1 <= code.length <= 100`
- `1 <= code[i] <= 100`
- `-100 <= k <= 100`
"""

# Python Solution
def decrypt(code, k):
    n = len(code)
    if k == 0:
        return [0] * n
    
    result = [0] * n
    extended_code = code * 2  # Extend the array to handle circular indexing
    
    if k > 0:
        for i in range(n):
            result[i] = sum(extended_code[i + 1:i + 1 + k])
    else:  # k < 0
        for i in range(n):
            result[i] = sum(extended_code[i + n + k:i + n])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    code = [5, 7, 1, 4]
    k = 3
    print(decrypt(code, k))  # Output: [12, 10, 16, 13]

    # Test Case 2
    code = [5, 7, 1, 4]
    k = 0
    print(decrypt(code, k))  # Output: [0, 0, 0, 0]

    # Test Case 3
    code = [2, 4, 9, 3]
    k = -2
    print(decrypt(code, k))  # Output: [12, 5, 6, 13]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Extending the array takes O(n).
- Calculating the sum for each element involves iterating over `k` elements, and this is done for all `n` elements.
- Overall, the time complexity is O(n * |k|), where |k| is the absolute value of k.

Space Complexity:
- The extended array takes O(2n) space.
- The result array takes O(n) space.
- Overall, the space complexity is O(n).
"""

# Topic: Arrays