"""
LeetCode Problem #551: Student Attendance Record I

Problem Statement:
You are given a string `s` representing an attendance record for a student. The record only contains the following three characters:
- 'A': Absent.
- 'L': Late.
- 'P': Present.

A student is eligible for an attendance award if they meet both of the following criteria:
1. The student was absent ('A') for strictly fewer than 2 days total.
2. The student was never late ('L') for 3 or more consecutive days.

Return `True` if the student is eligible for an attendance award, or `False` otherwise.

Constraints:
- 1 <= len(s) <= 1000
- `s` consists only of characters 'A', 'L', and 'P'.
"""

def checkRecord(s: str) -> bool:
    """
    Determines if a student is eligible for an attendance award based on their attendance record.

    :param s: A string representing the attendance record.
    :return: True if the student is eligible for an award, False otherwise.
    """
    # Check if the number of 'A's is less than 2
    if s.count('A') >= 2:
        return False
    
    # Check if there are 3 or more consecutive 'L's
    if 'LLL' in s:
        return False
    
    return True

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1: Eligible for award
    s1 = "PPALLP"
    print(checkRecord(s1))  # Expected output: True

    # Test Case 2: Not eligible due to 2 absences
    s2 = "PPALLA"
    print(checkRecord(s2))  # Expected output: False

    # Test Case 3: Not eligible due to 3 consecutive late days
    s3 = "PPALLL"
    print(checkRecord(s3))  # Expected output: False

    # Test Case 4: Eligible with no absences or late days
    s4 = "PPPPP"
    print(checkRecord(s4))  # Expected output: True

    # Test Case 5: Not eligible due to both 2 absences and 3 consecutive late days
    s5 = "AALLLPA"
    print(checkRecord(s5))  # Expected output: False

"""
Time Complexity Analysis:
- Counting the number of 'A's in the string takes O(n), where n is the length of the string.
- Checking for the substring 'LLL' also takes O(n) in the worst case.
- Therefore, the overall time complexity is O(n).

Space Complexity Analysis:
- The solution uses O(1) additional space as it only performs string operations without using extra data structures.

Topic: Strings
"""