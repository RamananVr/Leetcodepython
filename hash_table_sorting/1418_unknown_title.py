"""
LeetCode Problem #1418: Display Table of Food Orders in a Restaurant

Problem Statement:
Given the array orders, where orders[i] = [customerNamei, tableNumberi, foodItemi], 
return the restaurant's "display table". The "display table" is a table that shows 
the number of each food item being ordered at each table. The first row should be 
the header, with food items sorted in lexicographical order. The first column should 
be the table numbers sorted in numerical order.

Each cell in the table should contain the number of times that food item was ordered 
at that table.

Input:
- orders: List[List[str]], where each order is represented as [customerName, tableNumber, foodItem].

Output:
- List[List[str]], representing the display table.

Constraints:
- 1 <= orders.length <= 500
- orders[i].length == 3
- 1 <= customerName.length, foodItem.length <= 20
- customerName and foodItem consist of lowercase and uppercase English letters.
- tableNumber is a string of integers between 1 and 500.

Example:
Input: orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],
                 ["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
Output: [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
         ["3","0","2","1","0"],
         ["5","0","1","0","1"],
         ["10","1","0","0","0"]]
"""

# Solution
from collections import defaultdict

def displayTable(orders):
    # Step 1: Extract all unique food items and sort them lexicographically
    food_items = sorted({order[2] for order in orders})
    
    # Step 2: Create a mapping of table numbers to food item counts
    table_food_count = defaultdict(lambda: defaultdict(int))
    for _, table, food in orders:
        table_food_count[int(table)][food] += 1
    
    # Step 3: Sort table numbers numerically
    sorted_tables = sorted(table_food_count.keys())
    
    # Step 4: Build the display table
    header = ["Table"] + food_items
    display_table = [header]
    
    for table in sorted_tables:
        row = [str(table)] + [str(table_food_count[table][food]) for food in food_items]
        display_table.append(row)
    
    return display_table

# Example Test Cases
if __name__ == "__main__":
    orders1 = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],
               ["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
    print(displayTable(orders1))
    # Expected Output:
    # [["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],
    #  ["3","0","2","1","0"],
    #  ["5","0","1","0","1"],
    #  ["10","1","0","0","0"]]

    orders2 = [["James","1","Fried Chicken"],["Laura","2","Fried Chicken"],["Laura","2","Water"]]
    print(displayTable(orders2))
    # Expected Output:
    # [["Table","Fried Chicken","Water"],
    #  ["1","1","0"],
    #  ["2","1","1"]]

# Time and Space Complexity Analysis
# Time Complexity:
# - Extracting unique food items: O(n), where n is the number of orders.
# - Sorting food items: O(f log f), where f is the number of unique food items.
# - Iterating through orders to populate table_food_count: O(n).
# - Sorting table numbers: O(t log t), where t is the number of unique tables.
# - Constructing the display table: O(t * f), as we iterate through each table and food item.
# Overall: O(n + f log f + t log t + t * f)

# Space Complexity:
# - Storage for food_items: O(f).
# - Storage for table_food_count: O(t * f), as we store counts for each table-food combination.
# Overall: O(t * f)

# Topic: Hash Table, Sorting