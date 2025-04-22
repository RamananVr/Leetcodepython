"""
LeetCode Question #842: Split Array into Fibonacci Sequence

Problem Statement:
You are given a string `num` that contains only digits. You need to split `num` into a Fibonacci-like sequence, 
where each number is a positive integer and the sequence satisfies the property that:
    - `F[i] + F[i+1] = F[i+2]` for all `i >= 0`.

Return any Fibonacci-like sequence split from `num`, or return an empty list if it is impossible to split `num`.

Notes:
- A sequence is Fibonacci-like if it has at least three numbers.
- Numbers in the sequence must not have leading zeros, except for the number 0 itself.
- Numbers in the sequence must fit within a 32-bit signed integer (i.e., -2^31 <= num <= 2^31 - 1).

Example 1:
Input: num = "112358"
Output: [1, 1, 2, 3, 5, 8]

Example 2:
Input: num = "123456579"
Output: [123, 456, 579]

Constraints:
- 1 <= num.length <= 30
- num consists of digits only.
"""

# Python Solution
def splitIntoFibonacci(num: str) -> list:
    def is_valid_fib_sequence(seq):
        """Helper function to check if the sequence satisfies Fibonacci property."""
        return len(seq) >= 3 and seq[-1] == seq[-2] + seq[-3]

    def backtrack(index, path):
        """Backtracking function to find the Fibonacci sequence."""
        if index == len(num) and len(path) >= 3:
            return path
        for i in range(index, len(num)):
            # Avoid numbers with leading zeros
            if num[index] == '0' and i > index:
                break
            # Parse the current number
            curr = int(num[index:i + 1])
            # Check if the number exceeds the 32-bit signed integer limit
            if curr > 2**31 - 1:
                break
            # If the path has at least two numbers, check the Fibonacci property
            if len(path) >= 2 and curr != path[-1] + path[-2]:
                continue
            # Add the current number to the path and recurse
            path.append(curr)
            result = backtrack(i + 1, path)
            if result:
                return result
            # Backtrack by removing the last number
            path.pop()
        return []

    return backtrack(0, [])

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "112358"
    print(splitIntoFibonacci(num1))  # Output: [1, 1, 2, 3, 5, 8]

    # Test Case 2
    num2 = "123456579"
    print(splitIntoFibonacci(num2))  # Output: [123, 456, 579]

    # Test Case 3
    num3 = "0000"
    print(splitIntoFibonacci(num3))  # Output: [0, 0, 0]

    # Test Case 4
    num4 = "1101111"
    print(splitIntoFibonacci(num4))  # Output: [11, 0, 11, 11]

    # Test Case 5
    num5 = "0123"
    print(splitIntoFibonacci(num5))  # Output: [] (Leading zero invalid)

# Time and Space Complexity Analysis
"""
Time Complexity:
- The backtracking approach explores all possible splits of the string `num`.
- For a string of length `n`, there are O(n^2) possible splits (since we can choose two indices to split the string).
- For each split, we perform constant-time checks and recursive calls.
- Therefore, the overall time complexity is O(n^2).

Space Complexity:
- The space complexity is determined by the recursion stack and the `path` list.
- In the worst case, the recursion stack and `path` list can grow to O(n).
- Therefore, the space complexity is O(n).
"""

# Topic: Backtracking