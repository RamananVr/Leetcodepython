"""
LeetCode Problem #1946: Largest Number After Mutating Substring

Problem Statement:
You are given a string `num`, which represents a large integer, and an integer array `change` of length 10 where `change[i]` is the digit that digit `i` must be replaced with.

You may choose to mutate a single substring of `num`. To mutate a substring, replace each digit `num[i]` with the digit `change[num[i]]` for all indices `i` in the substring. The substring must be non-empty.

Your goal is to maximize the resulting number. Return a string representing the largest number possible after mutating (or choosing not to mutate) a single substring of `num`.

Example 1:
Input: num = "132", change = [9,8,5,0,3,6,4,2,6,8]
Output: "832"
Explanation: Replace the substring "1" with "8" and "3" with "5".

Example 2:
Input: num = "021", change = [9,4,3,5,7,2,1,9,0,6]
Output: "934"
Explanation: Replace the substring "021" with "934".

Example 3:
Input: num = "5", change = [1,4,7,5,3,2,5,6,9,4]
Output: "5"
Explanation: No mutation is done since it does not increase the number.

Constraints:
- 1 <= num.length <= 10^5
- num consists of only digits 0-9.
- change.length == 10
- 0 <= change[i] <= 9
"""

def maximumNumber(num: str, change: list[int]) -> str:
    """
    Function to find the largest number after mutating a substring of the input number.
    """
    num_list = list(num)  # Convert the string to a list for mutability
    mutated = False  # Flag to track if mutation has started

    for i in range(len(num_list)):
        original_digit = int(num_list[i])
        new_digit = change[original_digit]

        if new_digit > original_digit:
            # Start mutating
            num_list[i] = str(new_digit)
            mutated = True
        elif new_digit < original_digit and mutated:
            # Stop mutating once the mutation decreases the value
            break

    return ''.join(num_list)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    num1 = "132"
    change1 = [9, 8, 5, 0, 3, 6, 4, 2, 6, 8]
    print(maximumNumber(num1, change1))  # Output: "832"

    # Test Case 2
    num2 = "021"
    change2 = [9, 4, 3, 5, 7, 2, 1, 9, 0, 6]
    print(maximumNumber(num2, change2))  # Output: "934"

    # Test Case 3
    num3 = "5"
    change3 = [1, 4, 7, 5, 3, 2, 5, 6, 9, 4]
    print(maximumNumber(num3, change3))  # Output: "5"

    # Test Case 4
    num4 = "123456"
    change4 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(maximumNumber(num4, change4))  # Output: "123456"

    # Test Case 5
    num5 = "987654"
    change5 = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
    print(maximumNumber(num5, change5))  # Output: "987654"

"""
Time Complexity:
- O(n), where n is the length of the string `num`. We iterate through the string once.

Space Complexity:
- O(n), due to the conversion of the string `num` to a list for mutability.

Topic: Greedy
"""