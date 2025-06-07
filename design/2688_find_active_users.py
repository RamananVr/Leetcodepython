"""
LeetCode Question #2688: Find Active Users

Problem Statement:
Table: Users
+---------------+----------+
| Column Name   | Type     |
+---------------+----------+
| user_id       | int      |
| item          | varchar  |
| created_at    | datetime |
| amount        | int      |
+---------------+----------+
This table may contain duplicate rows.
Each row includes the user id, the item they ordered, the date they ordered it, and the amount they paid.

An active user is a user that has made at least 2 orders in a 7-day window.

Write an SQL query to find all active users.

Return the result in any order.

Examples:
Example 1:
Input: 
Users table:
+---------+----------+---------------------+--------+
| user_id | item     | created_at          | amount |
+---------+----------+---------------------+--------+
| 1       | apple    | 2022-03-01 00:00:00 | 10     |
| 1       | orange   | 2022-03-03 00:00:00 | 10     |
| 1       | banana   | 2022-03-04 00:00:00 | 5      |
| 1       | orange   | 2022-03-07 00:00:00 | 10     |
| 1       | banana   | 2022-03-08 00:00:00 | 5      |
| 2       | apple    | 2022-03-01 00:00:00 | 10     |
| 2       | banana   | 2022-03-10 00:00:00 | 5      |
| 3       | apple    | 2022-03-01 00:00:00 | 10     |
| 3       | orange   | 2022-03-02 00:00:00 | 10     |
| 4       | apple    | 2022-03-01 00:00:00 | 10     |
+---------+----------+---------------------+--------+

Output: 
+---------+
| user_id |
+---------+
| 1       |
| 3       |
+---------+

Explanation: 
User 1: 
- Made 4 orders on 2022-03-01, 2022-03-03, 2022-03-04, 2022-03-07, 2022-03-08.
- Has multiple 7-day windows with at least 2 orders:
  - Window 2022-03-01 to 2022-03-07: 4 orders
  - Window 2022-03-02 to 2022-03-08: 4 orders

User 2: Made only 1 order in any 7-day window.
User 3: Made 2 orders on 2022-03-01 and 2022-03-02 (within 7 days).
User 4: Made only 1 order.

Constraints:
- 1 <= user_id <= 100
- item contains only lowercase letters.
- created_at is between 2022-01-01 and 2022-12-31.
- 1 <= amount <= 1000
"""

# This is a SQL problem, but we'll provide Python simulation and SQL solutions

def find_active_users(users_data):
    """
    Python simulation to find active users.
    
    Args:
        users_data: List of tuples (user_id, item, created_at, amount)
    
    Returns:
        List of active user_ids
    """
    from collections import defaultdict
    from datetime import datetime, timedelta
    
    # Group orders by user
    user_orders = defaultdict(list)
    
    for user_id, item, created_at, amount in users_data:
        # Convert string to datetime if needed
        if isinstance(created_at, str):
            created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        
        user_orders[user_id].append(created_at)
    
    active_users = set()
    
    # Check each user for activity
    for user_id, order_dates in user_orders.items():
        order_dates.sort()
        
        # Check all possible 7-day windows
        for i in range(len(order_dates)):
            count_in_window = 0
            base_date = order_dates[i]
            
            for j in range(i, len(order_dates)):
                if order_dates[j] <= base_date + timedelta(days=6):
                    count_in_window += 1
                else:
                    break
            
            if count_in_window >= 2:
                active_users.add(user_id)
                break
    
    return sorted(list(active_users))

def create_sql_solution():
    """
    Returns the SQL solution using self-join approach.
    """
    sql_query = """
    SELECT DISTINCT u1.user_id
    FROM Users u1
    JOIN Users u2 ON u1.user_id = u2.user_id 
                  AND u1.created_at != u2.created_at
                  AND u2.created_at BETWEEN u1.created_at 
                                        AND DATE_ADD(u1.created_at, INTERVAL 6 DAY)
    ORDER BY u1.user_id;
    """
    return sql_query

def create_alternative_sql_solutions():
    """
    Alternative SQL approaches.
    """
    
    # Solution 1: Using window functions
    solution1 = """
    WITH user_windows AS (
        SELECT 
            user_id,
            created_at,
            COUNT(*) OVER (
                PARTITION BY user_id 
                ORDER BY created_at 
                RANGE BETWEEN CURRENT ROW 
                AND INTERVAL 6 DAY FOLLOWING
            ) as orders_in_window
        FROM Users
    )
    SELECT DISTINCT user_id
    FROM user_windows
    WHERE orders_in_window >= 2
    ORDER BY user_id;
    """
    
    # Solution 2: Using correlated subquery
    solution2 = """
    SELECT DISTINCT user_id
    FROM Users u1
    WHERE (
        SELECT COUNT(*)
        FROM Users u2
        WHERE u2.user_id = u1.user_id
        AND u2.created_at BETWEEN u1.created_at 
                               AND DATE_ADD(u1.created_at, INTERVAL 6 DAY)
    ) >= 2
    ORDER BY user_id;
    """
    
    # Solution 3: Using EXISTS
    solution3 = """
    SELECT DISTINCT u1.user_id
    FROM Users u1
    WHERE EXISTS (
        SELECT 1
        FROM Users u2
        WHERE u2.user_id = u1.user_id
        AND u2.created_at != u1.created_at
        AND u2.created_at BETWEEN u1.created_at 
                               AND DATE_ADD(u1.created_at, INTERVAL 6 DAY)
    )
    ORDER BY user_id;
    """
    
    # Solution 4: Using LAG/LEAD window functions
    solution4 = """
    WITH user_order_gaps AS (
        SELECT 
            user_id,
            created_at,
            LAG(created_at) OVER (PARTITION BY user_id ORDER BY created_at) as prev_order,
            LEAD(created_at) OVER (PARTITION BY user_id ORDER BY created_at) as next_order
        FROM Users
    )
    SELECT DISTINCT user_id
    FROM user_order_gaps
    WHERE (prev_order IS NOT NULL AND DATEDIFF(created_at, prev_order) <= 6)
       OR (next_order IS NOT NULL AND DATEDIFF(next_order, created_at) <= 6)
    ORDER BY user_id;
    """
    
    return {
        "window_function": solution1,
        "correlated_subquery": solution2,
        "exists": solution3,
        "lag_lead": solution4
    }

def analyze_user_activity_patterns(users_data):
    """
    Detailed analysis of user activity patterns.
    """
    from collections import defaultdict, Counter
    from datetime import datetime, timedelta
    
    user_stats = defaultdict(lambda: {
        'total_orders': 0,
        'total_amount': 0,
        'unique_items': set(),
        'order_dates': [],
        'max_orders_in_7_days': 0,
        'first_order': None,
        'last_order': None,
        'active_periods': []
    })
    
    # Process all orders
    for user_id, item, created_at, amount in users_data:
        if isinstance(created_at, str):
            created_at = datetime.strptime(created_at, '%Y-%m-%d %H:%M:%S')
        
        stats = user_stats[user_id]
        stats['total_orders'] += 1
        stats['total_amount'] += amount
        stats['unique_items'].add(item)
        stats['order_dates'].append(created_at)
        
        if stats['first_order'] is None or created_at < stats['first_order']:
            stats['first_order'] = created_at
        if stats['last_order'] is None or created_at > stats['last_order']:
            stats['last_order'] = created_at
    
    # Analyze activity patterns
    for user_id, stats in user_stats.items():
        order_dates = sorted(stats['order_dates'])
        
        # Find maximum orders in any 7-day window
        max_in_window = 0
        active_periods = []
        
        for i in range(len(order_dates)):
            count = 0
            window_start = order_dates[i]
            window_end = window_start + timedelta(days=6)
            
            for j in range(i, len(order_dates)):
                if order_dates[j] <= window_end:
                    count += 1
                else:
                    break
            
            max_in_window = max(max_in_window, count)
            
            if count >= 2:
                active_periods.append((window_start, window_end, count))
        
        stats['max_orders_in_7_days'] = max_in_window
        stats['active_periods'] = active_periods
        stats['is_active'] = max_in_window >= 2
        stats['activity_level'] = (
            'High' if max_in_window >= 4 else
            'Medium' if max_in_window >= 2 else
            'Low'
        )
        
        # Calculate average days between orders
        if len(order_dates) > 1:
            total_days = (order_dates[-1] - order_dates[0]).days
            stats['avg_days_between_orders'] = total_days / (len(order_dates) - 1)
        else:
            stats['avg_days_between_orders'] = 0
        
        # Convert sets to lists for easier display
        stats['unique_items'] = list(stats['unique_items'])
    
    return dict(user_stats)

def create_advanced_analytics_queries():
    """
    Advanced analytics queries for user behavior analysis.
    """
    
    queries = {
        # User activity summary
        "activity_summary": """
        WITH user_activity AS (
            SELECT 
                user_id,
                COUNT(*) as total_orders,
                SUM(amount) as total_spent,
                COUNT(DISTINCT item) as unique_items,
                MIN(created_at) as first_order,
                MAX(created_at) as last_order,
                DATEDIFF(MAX(created_at), MIN(created_at)) as customer_lifespan_days
            FROM Users
            GROUP BY user_id
        ),
        active_check AS (
            SELECT DISTINCT u1.user_id
            FROM Users u1
            JOIN Users u2 ON u1.user_id = u2.user_id 
                          AND u1.created_at != u2.created_at
                          AND u2.created_at BETWEEN u1.created_at 
                                                AND DATE_ADD(u1.created_at, INTERVAL 6 DAY)
        )
        SELECT 
            ua.*,
            CASE WHEN ac.user_id IS NOT NULL THEN 'Active' ELSE 'Inactive' END as activity_status
        FROM user_activity ua
        LEFT JOIN active_check ac ON ua.user_id = ac.user_id
        ORDER BY ua.total_orders DESC;
        """,
        
        # Most popular items among active users
        "active_user_preferences": """
        WITH active_users AS (
            SELECT DISTINCT u1.user_id
            FROM Users u1
            JOIN Users u2 ON u1.user_id = u2.user_id 
                          AND u1.created_at != u2.created_at
                          AND u2.created_at BETWEEN u1.created_at 
                                                AND DATE_ADD(u1.created_at, INTERVAL 6 DAY)
        )
        SELECT 
            u.item,
            COUNT(*) as order_count,
            COUNT(DISTINCT u.user_id) as unique_active_users,
            SUM(u.amount) as total_revenue
        FROM Users u
        JOIN active_users au ON u.user_id = au.user_id
        GROUP BY u.item
        ORDER BY order_count DESC;
        """,
        
        # Activity timeline analysis
        "activity_timeline": """
        WITH daily_activity AS (
            SELECT 
                DATE(created_at) as order_date,
                COUNT(DISTINCT user_id) as active_users,
                COUNT(*) as total_orders,
                SUM(amount) as daily_revenue
            FROM Users
            GROUP BY DATE(created_at)
        )
        SELECT 
            order_date,
            active_users,
            total_orders,
            daily_revenue,
            LAG(active_users) OVER (ORDER BY order_date) as prev_day_users,
            ROUND(
                (active_users - LAG(active_users) OVER (ORDER BY order_date)) * 100.0 / 
                LAG(active_users) OVER (ORDER BY order_date), 2
            ) as user_growth_rate
        FROM daily_activity
        ORDER BY order_date;
        """
    }
    
    return queries

# Test Cases
if __name__ == "__main__":
    # Test data from the example
    test_data = [
        (1, 'apple', '2022-03-01 00:00:00', 10),
        (1, 'orange', '2022-03-03 00:00:00', 10),
        (1, 'banana', '2022-03-04 00:00:00', 5),
        (1, 'orange', '2022-03-07 00:00:00', 10),
        (1, 'banana', '2022-03-08 00:00:00', 5),
        (2, 'apple', '2022-03-01 00:00:00', 10),
        (2, 'banana', '2022-03-10 00:00:00', 5),
        (3, 'apple', '2022-03-01 00:00:00', 10),
        (3, 'orange', '2022-03-02 00:00:00', 10),
        (4, 'apple', '2022-03-01 00:00:00', 10)
    ]
    
    expected_result = [1, 3]
    
    print("Testing Python simulation:")
    result = find_active_users(test_data)
    print("Result:", result)
    print("Expected:", expected_result)
    print("Match:", result == expected_result)
    
    print("\nMain SQL Solution:")
    print(create_sql_solution())
    
    print("\nAlternative SQL Solutions:")
    alternatives = create_alternative_sql_solutions()
    for name, query in alternatives.items():
        print(f"\n{name.replace('_', ' ').title()}:")
        print(query)
    
    print("\nUser Activity Pattern Analysis:")
    analysis = analyze_user_activity_patterns(test_data)
    for user_id, stats in analysis.items():
        print(f"\nUser {user_id}:")
        print(f"  Total orders: {stats['total_orders']}")
        print(f"  Total amount: ${stats['total_amount']}")
        print(f"  Unique items: {stats['unique_items']}")
        print(f"  Max orders in 7 days: {stats['max_orders_in_7_days']}")
        print(f"  Activity level: {stats['activity_level']}")
        print(f"  Is active: {stats['is_active']}")
        if stats['active_periods']:
            print(f"  Active periods: {len(stats['active_periods'])}")
    
    print("\nAdvanced Analytics Queries:")
    advanced_queries = create_advanced_analytics_queries()
    for name, query in advanced_queries.items():
        print(f"\n{name.replace('_', ' ').title()}:")
        print(query)

"""
Time and Space Complexity Analysis:

Python Simulation:
Time Complexity: O(n²) - for each user, check all order pairs
Space Complexity: O(n) - storing orders per user

SQL Self-Join:
Time Complexity: O(n²) - join operation on date ranges
Space Complexity: O(n) - intermediate join results

Window Function Approach:
Time Complexity: O(n log n) - sorting within partitions
Space Complexity: O(n) - window function memory

Correlated Subquery:
Time Complexity: O(n²) - subquery for each row
Space Complexity: O(1) - no additional storage

Key SQL Concepts:
1. Self-joins for comparing rows within same table
2. Date arithmetic (DATE_ADD, INTERVAL)
3. Window functions with range frames
4. Correlated subqueries for row-wise analysis
5. EXISTS for efficient existence checks

Performance Optimization:
- Index on (user_id, created_at) is crucial
- Window functions often more efficient than self-joins
- DISTINCT eliminates duplicate user_ids
- Consider partitioning for large datasets

Business Applications:
- Customer segmentation and targeting
- Retention analysis and churn prediction
- Marketing campaign effectiveness
- Product recommendation systems
- User engagement measurement

Advanced Metrics:
- Customer lifetime value (CLV)
- Purchase frequency analysis
- Seasonal behavior patterns
- Cross-selling opportunities
- User journey mapping

Topic: SQL, Database Queries, Window Functions, User Analytics, Retention Analysis
"""
