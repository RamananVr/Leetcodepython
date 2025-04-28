"""
LeetCode Problem #946: Validate Stack Sequences

Problem Statement:
Given two integer arrays `pushed` and `popped` each with distinct values, return `true` if this could have been the result of a sequence of push and pop operations on an initially empty stack, or `false` otherwise.

Constraints:
- `1 <= pushed.length <= 1000`
- `0 <= pushed[i] <= 1000`
- All the elements of `pushed` are unique.
- `popped.length == pushed.length`
- `popped` is a permutation of `pushed`.

Example 1:
Input: pushed = [1,2,3,4,5], popped = [4,5,3,2,1]
Output: true
Explanation: We might do the following sequence:
push(1), push(2), push(3), push(4), pop() -> 4,
push(5), pop() -> 5, pop() -> 3, pop() -> 2, pop() -> 1

Example 2:
Input: pushed = [1,2,3,4,5], popped = [4,3,5,1,2]
Output: false
Explanation: 1 cannot be popped before 2.

"""

def validateStackSequences(pushed, popped):
    """
    Validate if the given pushed and popped sequences are valid stack operations.

    :param pushed: List[int] - The sequence of elements pushed onto the stack.
    :param popped: List[int] - The sequence of elements popped from the stack.
    :return: bool - True if the sequences are valid, False otherwise.
    """
    stack = []
    pop_index = 0

    for num in pushed:
        stack.append(num)  # Push the current number onto the stack
        # Check if the top of the stack matches the next number to pop
        while stack and stack[-1] == popped[pop_index]:
            stack.pop()  # Pop the top of the stack
            pop_index += 1  # Move to the next number in the popped sequence

    # If the stack is empty, all operations were valid
    return not stack


# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 5, 3, 2, 1]
    print(validateStackSequences(pushed, popped))  # Output: True

    # Test Case 2
    pushed = [1, 2, 3, 4, 5]
    popped = [4, 3, 5, 1, 2]
    print(validateStackSequences(pushed, popped))  # Output: False

    # Test Case 3
    pushed = [1]
    popped = [1]
    print(validateStackSequences(pushed, popped))  # Output: True

    # Test Case 4
    pushed = [1, 2, 3]
    popped = [3, 2, 1]
    print(validateStackSequences(pushed, popped))  # Output: True

    # Test Case 5
    pushed = [1, 2, 3]
    popped = [1, 3, 2]
    print(validateStackSequences(pushed, popped))  # Output: True


"""
Time and Space Complexity Analysis:

Time Complexity:
- The algorithm iterates through the `pushed` list once, performing O(1) operations for each element.
- The `while` loop pops elements from the stack, but each element is pushed and popped at most once.
- Therefore, the time complexity is O(n), where n is the length of the `pushed` list.

Space Complexity:
- The algorithm uses a stack to simulate the push and pop operations.
- In the worst case, the stack can grow to the size of the `pushed` list.
- Therefore, the space complexity is O(n), where n is the length of the `pushed` list.

Topic: Stack
"""