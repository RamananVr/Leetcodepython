"""
LeetCode Problem #1907: Count Salary Categories

Problem Statement:
You are given a list of integers `salaries` where each integer represents the salary of an employee. 
Your task is to categorize the salaries into three categories:
1. Low salary: salaries less than $50,000.
2. Medium salary: salaries between $50,000 and $100,000 (inclusive).
3. High salary: salaries greater than $100,000.

Return a dictionary with the counts of each category.

Example:
Input: salaries = [45000, 55000, 120000, 75000, 30000, 105000]
Output: {"low": 2, "medium": 2, "high": 2}

Constraints:
- 1 <= len(salaries) <= 10^5
- 0 <= salaries[i] <= 10^6
"""

def count_salary_categories(salaries):
    """
    Categorizes salaries into low, medium, and high categories and returns their counts.

    Args:
    salaries (List[int]): A list of integers representing employee salaries.

    Returns:
    dict: A dictionary with keys "low", "medium", and "high" and their respective counts.
    """
    # Initialize counts for each category
    counts = {"low": 0, "medium": 0, "high": 0}
    
    # Iterate through the salaries and categorize them
    for salary in salaries:
        if salary < 50000:
            counts["low"] += 1
        elif 50000 <= salary <= 100000:
            counts["medium"] += 1
        else:
            counts["high"] += 1
    
    return counts

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    salaries = [45000, 55000, 120000, 75000, 30000, 105000]
    print(count_salary_categories(salaries))  # Output: {"low": 2, "medium": 2, "high": 2}

    # Test Case 2
    salaries = [20000, 40000, 60000, 80000, 100000, 150000]
    print(count_salary_categories(salaries))  # Output: {"low": 2, "medium": 3, "high": 1}

    # Test Case 3
    salaries = [0, 50000, 100000, 100001]
    print(count_salary_categories(salaries))  # Output: {"low": 1, "medium": 2, "high": 1}

    # Test Case 4
    salaries = [1000000]
    print(count_salary_categories(salaries))  # Output: {"low": 0, "medium": 0, "high": 1}

    # Test Case 5
    salaries = []
    print(count_salary_categories(salaries))  # Output: {"low": 0, "medium": 0, "high": 0}

"""
Time Complexity Analysis:
- The function iterates through the list of salaries once, performing constant-time operations for each salary.
- Let n be the length of the salaries list.
- Time Complexity: O(n)

Space Complexity Analysis:
- The function uses a fixed-size dictionary to store the counts, which does not depend on the input size.
- Space Complexity: O(1)

Topic: Arrays
"""