"""
LeetCode Problem #2081: Sum of k-Mirror Numbers

Problem Statement:
A k-mirror number is a positive integer that reads the same both forward and backward in base-10 and in base-k.

Given three integers k, n, and m, return the sum of the first n k-mirror numbers that are less than or equal to m.

Constraints:
1 <= k <= 9
1 <= n <= 30
1 <= m <= 10^9
"""

def is_palindrome(s: str) -> bool:
    """Helper function to check if a string is a palindrome."""
    return s == s[::-1]

def is_k_mirror(num: int, k: int) -> bool:
    """Check if a number is a k-mirror number."""
    # Check if the number is a palindrome in base-10
    if not is_palindrome(str(num)):
        return False
    
    # Convert the number to base-k and check if it's a palindrome
    base_k_representation = []
    temp = num
    while temp > 0:
        base_k_representation.append(temp % k)
        temp //= k
    return is_palindrome(''.join(map(str, base_k_representation)))

def sum_of_k_mirror_numbers(k: int, n: int, m: int) -> int:
    """
    Find the sum of the first n k-mirror numbers that are less than or equal to m.
    """
    count = 0
    total_sum = 0
    num = 1
    
    while count < n:
        if num > m:
            break
        if is_k_mirror(num, k):
            total_sum += num
            count += 1
        num += 1
    
    return total_sum

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    k = 2
    n = 5
    m = 50
    print(sum_of_k_mirror_numbers(k, n, m))  # Expected Output: 25 (1, 3, 5, 7, 9 are the first 5 2-mirror numbers)

    # Test Case 2
    k = 3
    n = 3
    m = 100
    print(sum_of_k_mirror_numbers(k, n, m))  # Expected Output: 15 (1, 2, 4 are the first 3 3-mirror numbers)

    # Test Case 3
    k = 10
    n = 2
    m = 20
    print(sum_of_k_mirror_numbers(k, n, m))  # Expected Output: 3 (1, 2 are the first 2 10-mirror numbers)

"""
Time Complexity Analysis:
- Checking if a number is a palindrome in base-10 takes O(d), where d is the number of digits in the number.
- Converting a number to base-k takes O(log_k(num)).
- Checking if a number is a palindrome in base-k takes O(log_k(num)).
- For each number, the total cost is O(d + log_k(num)).
- In the worst case, we iterate through all numbers up to m, so the total complexity is O(m * (d + log_k(m))).

Space Complexity Analysis:
- The space complexity is O(log_k(num)) for storing the base-k representation of the number.

Topic: Palindromes, Number Theory
"""