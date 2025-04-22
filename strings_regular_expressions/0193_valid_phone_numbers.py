"""
LeetCode Question #193: Valid Phone Numbers

Problem Statement:
Given a text file `file.txt` that contains a list of phone numbers (one per line), write a one-liner bash script to print all valid phone numbers.

A valid phone number must appear in one of the following two formats:
1. (xxx) xxx-xxxx
2. xxx-xxx-xxxx
(x represents a digit)

You may assume that the input file will always exist and will contain valid strings.

Example:
Assume that `file.txt` has the following content:
987-123-4567
123 456 7890
(123) 456-7890

Your script should output the following valid phone numbers:
987-123-4567
(123) 456-7890

Note: This is a shell scripting problem, but we will solve it in Python for this exercise.
"""

# Python Solution
import re

def valid_phone_numbers(file_path):
    """
    Reads a file containing phone numbers and prints all valid phone numbers.

    :param file_path: Path to the file containing phone numbers.
    """
    valid_numbers = []
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            # Check if the line matches either of the two valid formats
            if re.match(r'^\(\d{3}\) \d{3}-\d{4}$', line) or re.match(r'^\d{3}-\d{3}-\d{4}$', line):
                valid_numbers.append(line)
    return valid_numbers

# Example Test Cases
if __name__ == "__main__":
    # Create a sample file for testing
    sample_file = "sample_file.txt"
    with open(sample_file, 'w') as f:
        f.write("987-123-4567\n")
        f.write("123 456 7890\n")
        f.write("(123) 456-7890\n")
        f.write("123-45-6789\n")
        f.write("(123)456-7890\n")

    # Call the function and print the results
    result = valid_phone_numbers(sample_file)
    print("Valid Phone Numbers:")
    for number in result:
        print(number)

"""
Expected Output:
Valid Phone Numbers:
987-123-4567
(123) 456-7890
"""

# Time and Space Complexity Analysis
"""
Time Complexity:
- Reading the file: O(n), where n is the number of lines in the file.
- Regex matching: Each line is checked against two regex patterns, which is O(1) per line.
  Therefore, the total time complexity is O(n).

Space Complexity:
- The space used to store valid phone numbers is proportional to the number of valid lines, which is O(k), where k is the number of valid phone numbers.
- The regex patterns themselves use constant space.
  Therefore, the total space complexity is O(k).
"""

# Topic: Strings, Regular Expressions