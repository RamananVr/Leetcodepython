"""
LeetCode Problem #556: Next Greater Element III

Problem Statement:
Given a positive integer `n`, find the smallest integer which has exactly the same digits existing in the integer `n` and is greater in value than `n`. If no such positive integer exists, return `-1`.

Note that the returned integer should fit in a 32-bit integer, if there is a valid result but it does not fit in a 32-bit integer, return `-1`.

Constraints:
- 1 <= n <= 2^31 - 1 (i.e., 2147483647)

Example 1:
Input: n = 12
Output: 21

Example 2:
Input: n = 21
Output: -1
"""

def nextGreaterElement(n: int) -> int:
    # Convert the number to a list of digits
    digits = list(str(n))
    length = len(digits)
    
    # Step 1: Find the first decreasing element from the right
    i = length - 2
    while i >= 0 and digits[i] >= digits[i + 1]:
        i -= 1
    
    # If no such element is found, return -1 (no greater permutation exists)
    if i == -1:
        return -1
    
    # Step 2: Find the smallest element larger than digits[i] to the right of it
    j = length - 1
    while digits[j] <= digits[i]:
        j -= 1
    
    # Step 3: Swap the two elements
    digits[i], digits[j] = digits[j], digits[i]
    
    # Step 4: Reverse the digits to the right of i to get the smallest permutation
    digits = digits[:i + 1] + digits[i + 1:][::-1]
    
    # Convert the list of digits back to an integer
    result = int("".join(digits))
    
    # Check if the result fits in a 32-bit integer
    return result if result <= 2**31 - 1 else -1

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    n1 = 12
    print(f"Input: {n1}, Output: {nextGreaterElement(n1)}")  # Expected Output: 21

    # Test Case 2
    n2 = 21
    print(f"Input: {n2}, Output: {nextGreaterElement(n2)}")  # Expected Output: -1

    # Test Case 3
    n3 = 1234
    print(f"Input: {n3}, Output: {nextGreaterElement(n3)}")  # Expected Output: 1243

    # Test Case 4
    n4 = 4321
    print(f"Input: {n4}, Output: {nextGreaterElement(n4)}")  # Expected Output: -1

    # Test Case 5
    n5 = 1999999999
    print(f"Input: {n5}, Output: {nextGreaterElement(n5)}")  # Expected Output: -1

"""
Time Complexity:
- The algorithm involves a single pass to find the first decreasing element (O(d), where d is the number of digits in n).
- Another pass is used to find the smallest element larger than the decreasing element (O(d)).
- Reversing the digits to the right of the decreasing element also takes O(d).
- Overall, the time complexity is O(d), where d is the number of digits in n.

Space Complexity:
- The algorithm uses O(d) space to store the digits of the number as a list.
- Thus, the space complexity is O(d).

Topic: Arrays, Permutations
"""