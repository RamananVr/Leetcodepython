"""
LeetCode Question #1693: Daily Leads and Partners

Problem Statement:
You are given a table, `DailyLeadsAndPartners`, with two columns:
- `date_id` (DATE): The date of the record.
- `partner_id` (INTEGER): The ID of the partner.

Write an SQL query to find the daily percentage of leads for each partner rounded to 2 decimal places. The percentage of leads for a partner is calculated as:
    (Number of leads for the partner on a given day / Total leads on that day) * 100

Return the result table in any order.

The result format should be:
- `date_id` (DATE): The date of the record.
- `partner_id` (INTEGER): The ID of the partner.
- `percentage` (DECIMAL): The percentage of leads for the partner rounded to 2 decimal places.

Example:
Input:
DailyLeadsAndPartners table:
+------------+------------+
| date_id    | partner_id |
+------------+------------+
| 2020-12-01 | 1          |
| 2020-12-01 | 2          |
| 2020-12-01 | 1          |
| 2020-12-02 | 1          |
| 2020-12-02 | 2          |
| 2020-12-02 | 3          |
| 2020-12-02 | 1          |
+------------+------------+

Output:
+------------+------------+------------+
| date_id    | partner_id | percentage |
+------------+------------+------------+
| 2020-12-01 | 1          | 66.67      |
| 2020-12-01 | 2          | 33.33      |
| 2020-12-02 | 1          | 50.00      |
| 2020-12-02 | 2          | 25.00      |
| 2020-12-02 | 3          | 25.00      |
+------------+------------+------------+
"""

# Python Solution (Simulating the SQL Query with Pandas)

import pandas as pd

def calculate_daily_percentage(data):
    """
    Calculate the daily percentage of leads for each partner.

    Args:
    data (pd.DataFrame): A DataFrame containing 'date_id' and 'partner_id' columns.

    Returns:
    pd.DataFrame: A DataFrame with 'date_id', 'partner_id', and 'percentage' columns.
    """
    # Group by date_id and partner_id to count the number of leads for each partner on each day
    partner_leads = data.groupby(['date_id', 'partner_id']).size().reset_index(name='lead_count')
    
    # Group by date_id to calculate the total leads for each day
    daily_total_leads = partner_leads.groupby('date_id')['lead_count'].transform('sum')
    
    # Calculate the percentage for each partner
    partner_leads['percentage'] = (partner_leads['lead_count'] / daily_total_leads * 100).round(2)
    
    # Return the result
    return partner_leads[['date_id', 'partner_id', 'percentage']]

# Example Test Cases

if __name__ == "__main__":
    # Input Data
    data = pd.DataFrame({
        'date_id': ['2020-12-01', '2020-12-01', '2020-12-01', '2020-12-02', '2020-12-02', '2020-12-02', '2020-12-02'],
        'partner_id': [1, 2, 1, 1, 2, 3, 1]
    })
    
    # Expected Output
    expected_output = pd.DataFrame({
        'date_id': ['2020-12-01', '2020-12-01', '2020-12-02', '2020-12-02', '2020-12-02'],
        'partner_id': [1, 2, 1, 2, 3],
        'percentage': [66.67, 33.33, 50.00, 25.00, 25.00]
    })
    
    # Calculate Output
    output = calculate_daily_percentage(data)
    
    # Print Results
    print("Input Data:")
    print(data)
    print("\nCalculated Output:")
    print(output)
    print("\nExpected Output:")
    print(expected_output)
    print("\nTest Passed:", output.equals(expected_output))

"""
Time and Space Complexity Analysis:

1. Time Complexity:
   - Grouping by `date_id` and `partner_id` takes O(n), where n is the number of rows in the input data.
   - Calculating the total leads per day and transforming the data also takes O(n).
   - Overall, the time complexity is O(n).

2. Space Complexity:
   - The space complexity is O(n) for storing intermediate results (grouped data and transformed data).

Topic: SQL Simulation / Data Manipulation with Pandas
"""