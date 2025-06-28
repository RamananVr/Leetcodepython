"""
LeetCode Problem 2782: Number of Unique Categories

You are given an integer n and a 2D integer array categories where categories[i] = [type_i, id_i] indicates that the item with id id_i belongs to the category type_i.

Return the number of unique categories. Two categories are considered the same if they have the exact same set of item IDs.

Constraints:
- 1 <= n <= 100
- 1 <= categories.length <= 100
- categories[i].length == 2
- 1 <= type_i, id_i <= 100

Example 1:
Input: n = 3, categories = [[1,1],[1,2],[2,1],[2,3],[3,1]]
Output: 3
Explanation: 
- Category 1 has items {1, 2}
- Category 2 has items {1, 3}  
- Category 3 has items {1}
All three categories have different sets of items, so there are 3 unique categories.

Example 2:
Input: n = 2, categories = [[1,1],[1,2],[2,2],[2,1]]
Output: 1
Explanation:
- Category 1 has items {1, 2}
- Category 2 has items {1, 2}
Both categories have the same set of items, so there is 1 unique category.

Topics: Array, Hash Table, Set Operations
"""

class Solution:
    def numUniqueCategories(self, n: int, categories: list[list[int]]) -> int:
        """
        Approach 1: Group by category and use set comparison
        
        1. Group items by their category type
        2. Convert each group to a set of item IDs
        3. Count unique sets
        
        Time: O(m) where m = len(categories)
        Space: O(n + m) for storing category groups and sets
        """
        from collections import defaultdict
        
        # Group items by category type
        category_items = defaultdict(set)
        
        for category_type, item_id in categories:
            category_items[category_type].add(item_id)
        
        # Convert to frozensets for hashable comparison
        unique_sets = set()
        for items in category_items.values():
            unique_sets.add(frozenset(items))
        
        return len(unique_sets)
    
    def numUniqueCategories_list_comparison(self, n: int, categories: list[list[int]]) -> int:
        """
        Approach 2: Convert to sorted lists for comparison
        
        Group items and convert to sorted lists, then compare.
        
        Time: O(m + k*s*log(s)) where k is number of categories, s is avg items per category
        Space: O(n + m)
        """
        from collections import defaultdict
        
        category_items = defaultdict(set)
        
        for category_type, item_id in categories:
            category_items[category_type].add(item_id)
        
        # Convert to sorted tuples for comparison
        unique_signatures = set()
        for items in category_items.values():
            signature = tuple(sorted(items))
            unique_signatures.add(signature)
        
        return len(unique_signatures)
    
    def numUniqueCategories_string_signature(self, n: int, categories: list[list[int]]) -> int:
        """
        Approach 3: Create string signatures for each category
        
        Convert each category's items to a sorted string representation.
        
        Time: O(m + k*s*log(s))
        Space: O(n + m)
        """
        from collections import defaultdict
        
        category_items = defaultdict(set)
        
        for category_type, item_id in categories:
            category_items[category_type].add(item_id)
        
        # Create string signatures
        signatures = set()
        for items in category_items.values():
            signature = ','.join(map(str, sorted(items)))
            signatures.add(signature)
        
        return len(signatures)
    
    def numUniqueCategories_manual_comparison(self, n: int, categories: list[list[int]]) -> int:
        """
        Approach 4: Manual set comparison
        
        Compare each category's item set with all previously seen sets.
        
        Time: O(k^2 * s) where k is number of categories, s is avg items per category
        Space: O(n + m)
        """
        from collections import defaultdict
        
        category_items = defaultdict(set)
        
        for category_type, item_id in categories:
            category_items[category_type].add(item_id)
        
        # Manual comparison of sets
        unique_categories = []
        
        for items in category_items.values():
            is_unique = True
            for existing_items in unique_categories:
                if items == existing_items:
                    is_unique = False
                    break
            
            if is_unique:
                unique_categories.append(items)
        
        return len(unique_categories)

def test_num_unique_categories():
    """Test the number of unique categories solution with various test cases."""
    solution = Solution()
    
    # Test case 1: All different categories
    assert solution.numUniqueCategories(3, [[1,1],[1,2],[2,1],[2,3],[3,1]]) == 3
    
    # Test case 2: Some categories are the same
    assert solution.numUniqueCategories(2, [[1,1],[1,2],[2,2],[2,1]]) == 1
    
    # Test case 3: Single category
    assert solution.numUniqueCategories(1, [[1,1]]) == 1
    
    # Test case 4: All items in one category
    assert solution.numUniqueCategories(3, [[1,1],[1,2],[1,3]]) == 1
    
    # Test case 5: Each category has one unique item
    assert solution.numUniqueCategories(3, [[1,1],[2,2],[3,3]]) == 3
    
    # Test case 6: Two categories with overlapping but different sets
    assert solution.numUniqueCategories(4, [[1,1],[1,2],[2,1],[2,3]]) == 2
    # Category 1: {1,2}, Category 2: {1,3} - different sets
    
    # Test case 7: Multiple categories with same items
    assert solution.numUniqueCategories(2, [[1,1],[1,2],[2,1],[2,2],[3,1],[3,2]]) == 1
    # All categories have items {1,2}
    
    # Test case 8: Complex case with duplicates
    result8 = solution.numUniqueCategories(4, [
        [1,1],[1,2],      # Category 1: {1,2}
        [2,3],[2,4],      # Category 2: {3,4}
        [3,1],[3,2],      # Category 3: {1,2} - same as category 1
        [4,3],[4,4]       # Category 4: {3,4} - same as category 2
    ])
    assert result8 == 2
    
    # Test case 9: Single item per category, all different
    assert solution.numUniqueCategories(5, [[1,1],[2,2],[3,3],[4,4],[5,5]]) == 5
    
    # Test case 10: Single item per category, some same
    assert solution.numUniqueCategories(3, [[1,1],[2,1],[3,2],[4,2]]) == 2
    # Categories: {1}, {1}, {2}, {2} -> unique: {1}, {2}
    
    # Compare different approaches
    test_cases = [
        (3, [[1,1],[1,2],[2,1],[2,3],[3,1]]),
        (2, [[1,1],[1,2],[2,2],[2,1]]),
        (1, [[1,1]]),
        (3, [[1,1],[1,2],[1,3]]),
        (3, [[1,1],[2,2],[3,3]]),
        (4, [[1,1],[1,2],[2,1],[2,3]]),
        (2, [[1,1],[1,2],[2,1],[2,2],[3,1],[3,2]]),
        (5, [[1,1],[2,2],[3,3],[4,4],[5,5]]),
        (3, [[1,1],[2,1],[3,2],[4,2]])
    ]
    
    for n, categories in test_cases:
        result1 = solution.numUniqueCategories(n, categories)
        result2 = solution.numUniqueCategories_list_comparison(n, categories)
        result3 = solution.numUniqueCategories_string_signature(n, categories)
        result4 = solution.numUniqueCategories_manual_comparison(n, categories)
        assert result1 == result2 == result3 == result4, \
            f"Mismatch for n={n}, categories={categories}: {result1}, {result2}, {result3}, {result4}"
    
    # Test edge cases
    assert solution.numUniqueCategories(1, [[1,1]]) == 1
    assert solution.numUniqueCategories(100, [[1,1],[1,2]]) == 1
    
    print("All number of unique categories tests passed!")

if __name__ == "__main__":
    test_num_unique_categories()
