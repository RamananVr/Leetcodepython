"""
LeetCode Question #1491: Average Salary Excluding the Minimum and Maximum Salary

Problem Statement:
You are given an array of unique integers `salary` where `salary[i]` is the salary of the ith employee.
Return the average salary of employees excluding the minimum and maximum salary. Answers within 10^-5 of the actual answer will be accepted.

Constraints:
- 3 <= salary.length <= 100
- 1000 <= salary[i] <= 10^6
- All the integers in `salary` are unique.

Example:
Input: salary = [4000, 3000, 1000, 2000]
Output: 2500.00000
Explanation: Minimum salary and maximum salary are 1000 and 4000 respectively. 
Average salary excluding minimum and maximum is (2000+3000)/2 = 2500.

Input: salary = [1000, 2000, 3000]
Output: 2000.00000
Explanation: Minimum salary and maximum salary are 1000 and 3000 respectively. 
Average salary excluding minimum and maximum is (2000)/1 = 2000.
"""

# Python Solution
def average(salary):
    """
    Calculate the average salary excluding the minimum and maximum salary.

    :param salary: List[int] - List of unique integers representing salaries.
    :return: float - Average salary excluding the minimum and maximum.
    """
    # Exclude the minimum and maximum salary
    min_salary = min(salary)
    max_salary = max(salary)
    total_salary = sum(salary) - min_salary - max_salary
    
    # Calculate the average
    num_employees = len(salary) - 2
    return total_salary / num_employees

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    salary1 = [4000, 3000, 1000, 2000]
    print(average(salary1))  # Expected Output: 2500.00000

    # Test Case 2
    salary2 = [1000, 2000, 3000]
    print(average(salary2))  # Expected Output: 2000.00000

    # Test Case 3
    salary3 = [6000, 5000, 4000, 3000, 2000, 1000]
    print(average(salary3))  # Expected Output: 3500.00000

    # Test Case 4
    salary4 = [8000, 7000, 6000, 5000]
    print(average(salary4))  # Expected Output: 6500.00000

# Time and Space Complexity Analysis
"""
Time Complexity:
- Calculating the minimum and maximum salary takes O(n), where n is the length of the salary list.
- Calculating the sum of the salary list also takes O(n).
- Overall, the time complexity is O(n).

Space Complexity:
- The solution uses a constant amount of extra space, so the space complexity is O(1).
"""

# Topic: Arrays