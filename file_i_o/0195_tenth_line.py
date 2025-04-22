"""
LeetCode Question #195: Tenth Line

Problem Statement:
Given a text file `file.txt`, print just the 10th line of the file.

Note:
1. If the file contains less than 10 lines, output nothing.
2. Each line in the file ends with a newline character.

Example:
Assume that `file.txt` has the following content:
Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10

Your script should output:
Line 10

Constraints:
- The file `file.txt` is guaranteed to have at most 10^3 lines.
- Each line in the file is guaranteed to have at most 10^3 characters.

"""

# Solution:
# The solution uses Python to read the file line by line and prints the 10th line if it exists.

def print_tenth_line(file_path: str) -> None:
    """
    Prints the 10th line of the file if it exists, otherwise prints nothing.

    :param file_path: Path to the file to read.
    """
    try:
        with open(file_path, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            # Check if there are at least 10 lines
            if len(lines) >= 10:
                # Print the 10th line (index 9 because of 0-based indexing)
                print(lines[9].strip())
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example Test Cases:
# To test this function, create a file named 'file.txt' with the following content:
# Line 1
# Line 2
# Line 3
# Line 4
# Line 5
# Line 6
# Line 7
# Line 8
# Line 9
# Line 10

# Test Case 1: File with 10 lines
# Expected Output: Line 10
print("Test Case 1:")
print_tenth_line('file.txt')

# Test Case 2: File with less than 10 lines
# Create a file named 'file_short.txt' with the following content:
# Line 1
# Line 2
# Line 3
# Expected Output: (nothing)
print("\nTest Case 2:")
print_tenth_line('file_short.txt')

# Test Case 3: File does not exist
# Expected Output: Error: File 'non_existent_file.txt' not found.
print("\nTest Case 3:")
print_tenth_line('non_existent_file.txt')

# Time and Space Complexity Analysis:
# Time Complexity:
# - Reading the file line by line takes O(n), where n is the number of lines in the file.
# - Accessing the 10th line is O(1).
# - Overall time complexity: O(n).

# Space Complexity:
# - Storing all lines in memory takes O(n), where n is the number of lines in the file.
# - Overall space complexity: O(n).

# Topic: File I/O