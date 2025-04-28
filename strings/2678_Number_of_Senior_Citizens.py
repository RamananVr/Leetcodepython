"""
LeetCode Problem #2678: Number of Senior Citizens

Problem Statement:
You are given a 0-indexed array of strings `details`. Each string in `details` has a length of 15 and represents the details of a passenger. The system divides the string into three parts:
- The first 10 characters represent the passenger's ID.
- The next 2 characters represent the passenger's age.
- The last 3 characters represent the passenger's seat number.

Return the number of passengers who are senior citizens. A person is considered a senior citizen if their age is greater than or equal to 60.

Example 1:
Input: details = ["123456789012345", "987654321059876", "111111111160111"]
Output: 2
Explanation: 
- The first passenger's age is 12, which is less than 60.
- The second passenger's age is 59, which is less than 60.
- The third passenger's age is 60, which is equal to or greater than 60.
Thus, there are 2 senior citizens.

Example 2:
Input: details = ["555555555560555", "444444444461444"]
Output: 2
Explanation:
- Both passengers have ages greater than or equal to 60.
Thus, there are 2 senior citizens.

Constraints:
- 1 <= details.length <= 100
- details[i].length == 15
- details[i] consists of digits only.

"""

# Python Solution
def countSeniors(details):
    """
    Counts the number of senior citizens (age >= 60) in the given list of passenger details.

    :param details: List[str] - A list of strings where each string represents passenger details.
    :return: int - The number of senior citizens.
    """
    senior_count = 0
    for detail in details:
        age = int(detail[11:13])  # Extract the age from the 12th and 13th characters
        if age >= 60:
            senior_count += 1
    return senior_count

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    details1 = ["123456789012345", "987654321059876", "111111111160111"]
    print(countSeniors(details1))  # Output: 2

    # Test Case 2
    details2 = ["555555555560555", "444444444461444"]
    print(countSeniors(details2))  # Output: 2

    # Test Case 3
    details3 = ["000000000012000", "111111111059111", "222222222058222"]
    print(countSeniors(details3))  # Output: 0

    # Test Case 4
    details4 = ["333333333360333", "444444444462444", "555555555559555"]
    print(countSeniors(details4))  # Output: 2

    # Test Case 5
    details5 = ["123456789060123"]
    print(countSeniors(details5))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- The function iterates through the `details` list once, and for each string, it performs a constant-time operation to extract and compare the age.
- Let n = len(details). The time complexity is O(n).

Space Complexity:
- The function uses a constant amount of extra space for variables like `senior_count` and `age`.
- The space complexity is O(1).
"""

# Topic: Strings