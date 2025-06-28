"""
LeetCode Problem 2752: Customers Who Never Order

Given two tables, customers and orders, write a SQL query to find all customers who never placed an order.

Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+

id is the primary key column for this table.
Each row of this table indicates the ID and name of a customer.

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key column for this table.
customerId is a foreign key of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.

Example 1:
Input: 
Customers table:
+----+-------+
| id | name  |
+----+-------+
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |
+----+-------+

Orders table:
+----+------------+
| id | customerId |
+----+------------+
| 1  | 3          |
| 2  | 1          |
+----+------------+

Output: 
+-------+
| name  |
+-------+
| Henry |
| Max   |
+-------+

Explanation: Henry (ID 2) and Max (ID 4) never placed any orders.

Note: This is a classic SQL problem that's often used to test LEFT JOIN and NOT EXISTS concepts.
Since this is primarily an SQL problem, we'll also provide Python implementations for practice.

Constraints:
- 1 <= Customers.id, Orders.id <= 1000
- All IDs are unique within their respective tables
"""

from typing import List, Dict, Set


def find_customers_never_ordered(customers: List[Dict], orders: List[Dict]) -> List[str]:
    """
    Find customers who never placed an order using set operations.
    
    Args:
        customers: List of customer dictionaries with 'id' and 'name'
        orders: List of order dictionaries with 'id' and 'customerId'
        
    Returns:
        List of customer names who never ordered
        
    Time Complexity: O(n + m) where n = customers, m = orders
    Space Complexity: O(m) for storing customer IDs who ordered
    """
    # Get set of customer IDs who placed orders
    ordered_customer_ids = {order['customerId'] for order in orders}
    
    # Find customers who never ordered
    never_ordered = []
    for customer in customers:
        if customer['id'] not in ordered_customer_ids:
            never_ordered.append(customer['name'])
    
    return never_ordered


def find_customers_never_ordered_dict(customers: List[Dict], orders: List[Dict]) -> List[str]:
    """
    Find customers who never ordered using dictionary lookup.
    
    Args:
        customers: List of customer dictionaries
        orders: List of order dictionaries
        
    Returns:
        List of customer names who never ordered
        
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    # Create customer lookup dictionary
    customer_dict = {customer['id']: customer['name'] for customer in customers}
    
    # Get set of customer IDs who placed orders
    ordered_customer_ids = {order['customerId'] for order in orders}
    
    # Find customers who never ordered
    never_ordered = []
    for customer_id, name in customer_dict.items():
        if customer_id not in ordered_customer_ids:
            never_ordered.append(name)
    
    return never_ordered


def find_customers_never_ordered_join(customers: List[Dict], orders: List[Dict]) -> List[str]:
    """
    Simulate LEFT JOIN approach.
    
    Args:
        customers: List of customer dictionaries
        orders: List of order dictionaries
        
    Returns:
        List of customer names who never ordered
        
    Time Complexity: O(n * m) worst case without optimization
    Space Complexity: O(1) excluding output
    """
    never_ordered = []
    
    for customer in customers:
        # Check if this customer has any orders
        has_order = False
        for order in orders:
            if order['customerId'] == customer['id']:
                has_order = True
                break
        
        if not has_order:
            never_ordered.append(customer['name'])
    
    return never_ordered


def find_customers_never_ordered_pandas(customers_data: List[Dict], orders_data: List[Dict]) -> List[str]:
    """
    Pandas-based solution (requires pandas library).
    
    Args:
        customers_data: Customer data
        orders_data: Orders data
        
    Returns:
        List of customer names who never ordered
    """
    try:
        import pandas as pd
        
        # Create DataFrames
        customers_df = pd.DataFrame(customers_data)
        orders_df = pd.DataFrame(orders_data)
        
        # Left join customers with orders
        merged = customers_df.merge(orders_df, left_on='id', right_on='customerId', how='left')
        
        # Filter customers with no orders (NaN in customerId after join)
        never_ordered = merged[merged['customerId'].isna()]['name'].tolist()
        
        return never_ordered
    except ImportError:
        # Fallback to set-based solution
        return find_customers_never_ordered(customers_data, orders_data)


class SQLSimulator:
    """
    Simulate SQL operations for educational purposes.
    """
    
    def __init__(self):
        self.customers = []
        self.orders = []
    
    def load_customers(self, customers: List[Dict]):
        """Load customer data."""
        self.customers = customers
    
    def load_orders(self, orders: List[Dict]):
        """Load order data."""
        self.orders = orders
    
    def execute_not_exists_query(self) -> List[str]:
        """
        Simulate: SELECT name FROM customers c WHERE NOT EXISTS 
        (SELECT 1 FROM orders o WHERE o.customerId = c.id)
        """
        result = []
        for customer in self.customers:
            # Check if NOT EXISTS (subquery)
            exists = any(order['customerId'] == customer['id'] for order in self.orders)
            if not exists:
                result.append(customer['name'])
        return result
    
    def execute_left_join_query(self) -> List[str]:
        """
        Simulate: SELECT c.name FROM customers c LEFT JOIN orders o 
        ON c.id = o.customerId WHERE o.customerId IS NULL
        """
        result = []
        for customer in self.customers:
            # Simulate LEFT JOIN
            joined_orders = [order for order in self.orders if order['customerId'] == customer['id']]
            
            # WHERE o.customerId IS NULL (no matching orders)
            if not joined_orders:
                result.append(customer['name'])
        
        return result
    
    def execute_not_in_query(self) -> List[str]:
        """
        Simulate: SELECT name FROM customers WHERE id NOT IN 
        (SELECT customerId FROM orders WHERE customerId IS NOT NULL)
        """
        # Get all customer IDs from orders (excluding NULL)
        order_customer_ids = {order['customerId'] for order in self.orders 
                             if order['customerId'] is not None}
        
        result = []
        for customer in self.customers:
            if customer['id'] not in order_customer_ids:
                result.append(customer['name'])
        
        return result


# Test cases
def test_find_customers_never_ordered():
    """Test the find_customers_never_ordered function with various inputs."""
    
    test_cases = [
        {
            "customers": [
                {"id": 1, "name": "Joe"},
                {"id": 2, "name": "Henry"},
                {"id": 3, "name": "Sam"},
                {"id": 4, "name": "Max"}
            ],
            "orders": [
                {"id": 1, "customerId": 3},
                {"id": 2, "customerId": 1}
            ],
            "expected": ["Henry", "Max"],
            "description": "Example 1: Two customers never ordered"
        },
        {
            "customers": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ],
            "orders": [
                {"id": 1, "customerId": 1},
                {"id": 2, "customerId": 2}
            ],
            "expected": [],
            "description": "All customers have orders"
        },
        {
            "customers": [
                {"id": 1, "name": "Alice"},
                {"id": 2, "name": "Bob"}
            ],
            "orders": [],
            "expected": ["Alice", "Bob"],
            "description": "No orders at all"
        },
        {
            "customers": [
                {"id": 1, "name": "SingleCustomer"}
            ],
            "orders": [
                {"id": 1, "customerId": 1}
            ],
            "expected": [],
            "description": "Single customer with order"
        },
        {
            "customers": [
                {"id": 1, "name": "LonelyCustomer"}
            ],
            "orders": [],
            "expected": ["LonelyCustomer"],
            "description": "Single customer without order"
        }
    ]
    
    for i, test in enumerate(test_cases):
        customers = test["customers"]
        orders = test["orders"]
        expected = test["expected"]
        
        # Test set-based solution
        result1 = find_customers_never_ordered(customers, orders)
        print(f"Test {i+1}: {test['description']}")
        print(f"  Customers: {[c['name'] for c in customers]}")
        print(f"  Orders by customer IDs: {[o['customerId'] for o in orders]}")
        print(f"  Expected: {expected}")
        print(f"  Set-based: {result1}")
        
        # Test dictionary solution
        result2 = find_customers_never_ordered_dict(customers, orders)
        print(f"  Dictionary: {result2}")
        
        # Test join simulation
        result3 = find_customers_never_ordered_join(customers, orders)
        print(f"  Join simulation: {result3}")
        
        # Test SQL simulator
        simulator = SQLSimulator()
        simulator.load_customers(customers)
        simulator.load_orders(orders)
        
        result4 = simulator.execute_not_exists_query()
        print(f"  NOT EXISTS: {result4}")
        
        result5 = simulator.execute_left_join_query()
        print(f"  LEFT JOIN: {result5}")
        
        result6 = simulator.execute_not_in_query()
        print(f"  NOT IN: {result6}")
        
        # Verify results (order might differ, so sort for comparison)
        assert sorted(result1) == sorted(expected), f"Set-based failed for test {i+1}"
        assert sorted(result2) == sorted(expected), f"Dictionary failed for test {i+1}"
        assert sorted(result3) == sorted(expected), f"Join simulation failed for test {i+1}"
        assert sorted(result4) == sorted(expected), f"NOT EXISTS failed for test {i+1}"
        assert sorted(result5) == sorted(expected), f"LEFT JOIN failed for test {i+1}"
        assert sorted(result6) == sorted(expected), f"NOT IN failed for test {i+1}"
        
        print(f"  ✓ All solutions passed!")
        print()


if __name__ == "__main__":
    test_find_customers_never_ordered()

"""
SQL Solutions:

1. Using NOT EXISTS:
SELECT c.name 
FROM customers c 
WHERE NOT EXISTS (
    SELECT 1 FROM orders o WHERE o.customerId = c.id
);

2. Using LEFT JOIN:
SELECT c.name 
FROM customers c 
LEFT JOIN orders o ON c.id = o.customerId 
WHERE o.customerId IS NULL;

3. Using NOT IN:
SELECT name 
FROM customers 
WHERE id NOT IN (
    SELECT customerId FROM orders WHERE customerId IS NOT NULL
);

Complexity Analysis:

1. Set-based (find_customers_never_ordered):
   - Time Complexity: O(n + m) - one pass through each table
   - Space Complexity: O(m) - set of customer IDs who ordered

2. Dictionary-based (find_customers_never_ordered_dict):
   - Time Complexity: O(n + m) - build dictionary + check orders
   - Space Complexity: O(n + m) - customer dictionary + order set

3. Join Simulation (find_customers_never_ordered_join):
   - Time Complexity: O(n * m) - nested loops without optimization
   - Space Complexity: O(1) - excluding output

Key Insights:
- Classic SQL problem testing understanding of JOINs and subqueries
- Multiple valid SQL approaches: NOT EXISTS, LEFT JOIN, NOT IN
- NOT EXISTS is often most efficient for this type of query
- LEFT JOIN with NULL check is intuitive and widely used
- NOT IN requires careful handling of NULL values

Performance Considerations:
- NOT EXISTS typically performs better than NOT IN for large datasets
- LEFT JOIN is often optimized well by SQL engines
- Proper indexing on join columns is crucial for performance

Topics: SQL, Database Queries, Set Operations, Joins, Subqueries
"""
