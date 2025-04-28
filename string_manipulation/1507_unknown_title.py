"""
LeetCode Problem #1507: Reformat Date

Problem Statement:
Given a date string in the form Day Month Year, where:
- Day is in the format "1st", "2nd", "3rd", or "4th", ..., "31st".
- Month is in the format "January", "February", ..., "December".
- Year is in the format "YYYY".

Convert the date string to the format "YYYY-MM-DD", where:
- YYYY is the year.
- MM is the two-digit month.
- DD is the two-digit day.

Constraints:
- The given dates are guaranteed to be valid, so no need to validate them.
- The input date string will always follow the format described above.

Example:
Input: date = "20th Oct 2052"
Output: "2052-10-20"

Input: date = "6th Jun 1933"
Output: "1933-06-06"

Input: date = "26th May 1960"
Output: "1960-05-26"
"""

def reformatDate(date: str) -> str:
    # Mapping of month names to their respective numbers
    month_map = {
        "January": "01", "February": "02", "March": "03", "April": "04",
        "May": "05", "June": "06", "July": "07", "August": "08",
        "September": "09", "October": "10", "November": "11", "December": "12"
    }
    
    # Split the input date into its components
    day, month, year = date.split()
    
    # Extract the numeric part of the day (remove "st", "nd", "rd", "th")
    day = ''.join(filter(str.isdigit, day))
    
    # Format the day to be two digits
    day = day.zfill(2)
    
    # Get the numeric month from the month_map
    month = month_map[month]
    
    # Combine year, month, and day into the desired format
    return f"{year}-{month}-{day}"

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    date1 = "20th Oct 2052"
    print(reformatDate(date1))  # Expected Output: "2052-10-20"
    
    # Test Case 2
    date2 = "6th Jun 1933"
    print(reformatDate(date2))  # Expected Output: "1933-06-06"
    
    # Test Case 3
    date3 = "26th May 1960"
    print(reformatDate(date3))  # Expected Output: "1960-05-26"
    
    # Additional Test Case
    date4 = "1st Jan 2000"
    print(reformatDate(date4))  # Expected Output: "2000-01-01"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Splitting the input string into components takes O(1) since the input format is fixed and small.
- Filtering the numeric part of the day takes O(d), where d is the length of the day string (at most 4 characters).
- Looking up the month in the dictionary takes O(1) since the dictionary has a fixed size of 12 entries.
- Combining the components into the final format takes O(1).
Overall, the time complexity is O(1).

Space Complexity:
- The space used by the month_map dictionary is fixed (12 entries).
- The function uses a constant amount of additional space for intermediate variables.
Overall, the space complexity is O(1).

Topic: String Manipulation
"""