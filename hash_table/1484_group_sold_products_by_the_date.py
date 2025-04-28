"""
LeetCode Question #1484: Group Sold Products by the Date

Problem Statement:
Table: Activities

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| sell_date   | date    |
| product     | varchar |
+-------------+---------+
There is no primary key for this table. It may contain duplicates.
Each row of this table contains the product name and the date it was sold.

Write an SQL query to find for each date the number of different products sold.

The result table should contain the sell_date and the count of different products sold for that date.

Return the result table in any order.

The query result format is in the following example.

Example:
Input:
Activities table:
+------------+------------+
| sell_date  | product    |
+------------+------------+
| 2020-05-30 | Headphone  |
| 2020-05-30 | Pencil     |
| 2020-06-01 | Pencil     |
| 2020-06-02 | Mask       |
| 2020-05-30 | Mask       |
| 2020-06-01 | Mask       |
+------------+------------+

Output:
+------------+----------------+
| sell_date  | num_sold      |
+------------+----------------+
| 2020-05-30 | 3             |
| 2020-06-01 | 2             |
| 2020-06-02 | 1             |
+------------+----------------+
"""

# Python Solution
def group_sold_products_by_date(activities):
    """
    Function to group sold products by date and count the number of unique products sold per date.

    :param activities: List of tuples where each tuple contains (sell_date, product)
    :return: List of tuples where each tuple contains (sell_date, num_sold)
    """
    from collections import defaultdict

    # Dictionary to store unique products for each date
    date_to_products = defaultdict(set)

    # Populate the dictionary
    for sell_date, product in activities:
        date_to_products[sell_date].add(product)

    # Prepare the result
    result = [(sell_date, len(products)) for sell_date, products in date_to_products.items()]
    return result


# Example Test Cases
if __name__ == "__main__":
    # Input data
    activities = [
        ("2020-05-30", "Headphone"),
        ("2020-05-30", "Pencil"),
        ("2020-06-01", "Pencil"),
        ("2020-06-02", "Mask"),
        ("2020-05-30", "Mask"),
        ("2020-06-01", "Mask"),
    ]

    # Expected Output:
    # [
    #     ("2020-05-30", 3),
    #     ("2020-06-01", 2),
    #     ("2020-06-02", 1),
    # ]
    print(group_sold_products_by_date(activities))


# Time and Space Complexity Analysis
"""
Time Complexity:
- Iterating through the `activities` list takes O(n), where n is the number of rows in the input.
- Adding products to the set for each date is an O(1) operation on average.
- Constructing the result list takes O(d), where d is the number of unique dates.

Overall time complexity: O(n + d)

Space Complexity:
- The `date_to_products` dictionary stores up to d keys (unique dates) and their corresponding sets of products.
- In the worst case, the total space used by the sets is O(n), where n is the number of rows in the input.

Overall space complexity: O(n)
"""

# Topic: Hash Table