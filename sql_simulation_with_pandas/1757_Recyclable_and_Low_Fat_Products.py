"""
LeetCode Problem #1757: Recyclable and Low Fat Products

Problem Statement:
Table: Products

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| low_fats    | enum    |
| recyclable  | enum    |
+-------------+---------+
product_id is the primary key for this table.
low_fats column is an ENUM of type ('Y', 'N') where 'Y' means the product is low fat, and 'N' means it is not.
recyclable column is an ENUM of type ('Y', 'N') where 'Y' means the product is recyclable, and 'N' means it is not.

Write an SQL query to find the ids of products that are both low fat and recyclable.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Products table:
+------------+----------+------------+
| product_id | low_fats | recyclable |
+------------+----------+------------+
| 1          | Y        | N          |
| 2          | Y        | Y          |
| 3          | N        | Y          |
| 4          | Y        | Y          |
+------------+----------+------------+

Output:
+------------+
| product_id |
+------------+
| 2          |
| 4          |
+------------+
"""

# Python Solution (Simulating SQL Query with Pandas)

import pandas as pd

def recyclable_and_low_fat_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Filters the products DataFrame to find products that are both low fat and recyclable.

    Args:
    products (pd.DataFrame): A DataFrame containing product_id, low_fats, and recyclable columns.

    Returns:
    pd.DataFrame: A DataFrame containing product_id of products that are both low fat and recyclable.
    """
    # Filter the DataFrame for rows where low_fats == 'Y' and recyclable == 'Y'
    result = products[(products['low_fats'] == 'Y') & (products['recyclable'] == 'Y')]
    
    # Select only the product_id column
    return result[['product_id']]

# Example Test Cases

if __name__ == "__main__":
    # Example input DataFrame
    data = {
        "product_id": [1, 2, 3, 4],
        "low_fats": ["Y", "Y", "N", "Y"],
        "recyclable": ["N", "Y", "Y", "Y"]
    }
    products = pd.DataFrame(data)
    
    # Expected output: DataFrame with product_id 2 and 4
    expected_output = pd.DataFrame({"product_id": [2, 4]})
    
    # Run the function
    output = recyclable_and_low_fat_products(products)
    
    # Print the output
    print("Output:")
    print(output)
    print("\nExpected Output:")
    print(expected_output)
    
    # Verify correctness
    assert output.equals(expected_output), "Test case failed!"

"""
Time and Space Complexity Analysis:

Time Complexity:
- Filtering the DataFrame using conditions (low_fats == 'Y' and recyclable == 'Y') is O(n), 
  where n is the number of rows in the DataFrame.

Space Complexity:
- The space complexity is O(k), where k is the number of rows that satisfy the conditions 
  (low_fats == 'Y' and recyclable == 'Y'). This is the size of the resulting DataFrame.

Topic: SQL Simulation with Pandas
"""