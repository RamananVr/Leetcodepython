"""
LeetCode Question #1677: Product's Price for Each Store

Problem Statement:
You are given a table, Products, with the following structure:

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key column for this table.
Each row in this table indicates the price of a product in 3 different stores: store1, store2, and store3.

Write an SQL query to rearrange the Products table so that each row has (product_id, store, price). 
The store column is a string (store1, store2, store3) and the price column is the price of the product in that store.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Products table:
+------------+--------+--------+--------+
| product_id | store1 | store2 | store3 |
+------------+--------+--------+--------+
| 1          | 100    | 200    | 300    |
| 2          | 400    | 500    | 600    |
+------------+--------+--------+--------+

Output:
+------------+--------+-------+
| product_id | store  | price |
+------------+--------+-------+
| 1          | store1 | 100   |
| 1          | store2 | 200   |
| 1          | store3 | 300   |
| 2          | store1 | 400   |
| 2          | store2 | 500   |
| 2          | store3 | 600   |
+------------+--------+-------+
"""

# Solution in Python (using pandas for demonstration purposes)

import pandas as pd

def rearrange_products(products: pd.DataFrame) -> pd.DataFrame:
    """
    Rearranges the Products table so that each row has (product_id, store, price).
    
    Args:
    products (pd.DataFrame): Input DataFrame with columns ['product_id', 'store1', 'store2', 'store3'].
    
    Returns:
    pd.DataFrame: Output DataFrame with columns ['product_id', 'store', 'price'].
    """
    # Melt the DataFrame to transform columns into rows
    result = products.melt(id_vars=['product_id'], 
                           value_vars=['store1', 'store2', 'store3'], 
                           var_name='store', 
                           value_name='price')
    return result

# Example Test Cases

if __name__ == "__main__":
    # Input DataFrame
    products = pd.DataFrame({
        'product_id': [1, 2],
        'store1': [100, 400],
        'store2': [200, 500],
        'store3': [300, 600]
    })
    
    # Expected Output DataFrame
    expected_output = pd.DataFrame({
        'product_id': [1, 1, 1, 2, 2, 2],
        'store': ['store1', 'store2', 'store3', 'store1', 'store2', 'store3'],
        'price': [100, 200, 300, 400, 500, 600]
    })
    
    # Run the function
    output = rearrange_products(products)
    
    # Print the result
    print("Input:")
    print(products)
    print("\nOutput:")
    print(output)
    print("\nExpected Output:")
    print(expected_output)
    
    # Check if the output matches the expected output
    assert output.equals(expected_output), "Test case failed!"
    print("\nTest case passed!")

# Time and Space Complexity Analysis

"""
Time Complexity:
- Melting the DataFrame involves iterating over the rows and columns to reshape the data.
- If there are `n` rows and `m` columns in the input DataFrame, the time complexity is O(n * m).

Space Complexity:
- The space complexity is O(n * m) for the output DataFrame, as it contains the same number of elements as the input DataFrame.

Overall, the solution is efficient for small to medium-sized datasets.

Topic: SQL Transformation / DataFrame Manipulation
"""