"""
LeetCode Question #194: Transpose File

Problem Statement:
Given a text file `file.txt`, transpose its content. You may assume that each row has the same number of columns and each field is separated by the ' ' (space) character.

For example, if `file.txt` has the following content:
name age
alice 21
ryan 30

Output the following:
name alice ryan
age 21 30

Note:
- You must write a bash script to solve this problem.
- The solution should not use any extra files.

Since this is a shell scripting problem, we will provide a Python simulation of the solution for educational purposes.
"""

# Python Solution to Simulate the Transpose File Problem
def transpose_file(file_content):
    """
    Simulates the transposition of a file's content.

    :param file_content: List of strings, where each string represents a line in the file.
    :return: List of strings, where each string represents a line in the transposed file.
    """
    # Split each line into words and store them in a 2D list
    rows = [line.split() for line in file_content]
    
    # Transpose the 2D list using zip
    transposed = zip(*rows)
    
    # Join each transposed row into a string and return as a list
    return [' '.join(row) for row in transposed]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    file_content_1 = [
        "name age",
        "alice 21",
        "ryan 30"
    ]
    print("Test Case 1 Output:")
    print("\n".join(transpose_file(file_content_1)))
    # Expected Output:
    # name alice ryan
    # age 21 30

    # Test Case 2
    file_content_2 = [
        "a b c",
        "1 2 3",
        "x y z"
    ]
    print("\nTest Case 2 Output:")
    print("\n".join(transpose_file(file_content_2)))
    # Expected Output:
    # a 1 x
    # b 2 y
    # c 3 z

    # Test Case 3
    file_content_3 = [
        "hello world",
        "foo bar"
    ]
    print("\nTest Case 3 Output:")
    print("\n".join(transpose_file(file_content_3)))
    # Expected Output:
    # hello foo
    # world bar

"""
Time and Space Complexity Analysis:

Time Complexity:
- Let `m` be the number of rows and `n` be the number of columns in the file.
- Splitting each line into words takes O(n) for each row, so O(m * n) in total.
- Transposing the 2D list using `zip` takes O(m * n).
- Joining each transposed row into a string takes O(m * n).
- Overall time complexity: O(m * n).

Space Complexity:
- The 2D list `rows` requires O(m * n) space.
- The transposed result also requires O(m * n) space.
- Overall space complexity: O(m * n).

Topic: Strings, Matrix Manipulation
"""