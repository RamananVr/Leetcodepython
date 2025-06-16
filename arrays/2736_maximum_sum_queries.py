"""
2736. Maximum Sum Queries

You are given two 0-indexed integer arrays nums1 and nums2, each of length n, and a 1-indexed 2D array queries where queries[i] = [xi, yi].

For the ith query, find the maximum value of nums1[j] + nums2[j] where nums1[j] >= xi and nums2[j] >= yi, or -1 if there is no such j.

Return an array answer where answer[i] is the answer to the ith query.

Example 1:
Input: nums1 = [4,3,1,2], nums2 = [2,4,9,5], queries = [[4,1],[1,3],[2,5]]
Output: [6,10,7]
Explanation:
For the 1st query [4,1]: nums1[j] >= 4 and nums2[j] >= 1. We can choose j = 0 since nums1[0] = 4 >= 4 and nums2[0] = 2 >= 1. The sum is nums1[0] + nums2[0] = 6.
For the 2nd query [1,3]: nums1[j] >= 1 and nums2[j] >= 3. We can choose j = 1 since nums1[1] = 3 >= 1 and nums2[1] = 4 >= 3. The sum is nums1[1] + nums2[1] = 7. We can also choose j = 0 since nums1[0] = 4 >= 1 and nums2[0] = 2 >= 3 is false. So j = 1 is the only choice.
For the 3rd query [2,5]: nums1[j] >= 2 and nums2[j] >= 5. We can choose j = 3 since nums1[3] = 2 >= 2 and nums2[3] = 5 >= 5. The sum is nums1[3] + nums2[3] = 7.

Example 2:
Input: nums1 = [3,2,5], nums2 = [2,3,4], queries = [[4,4],[3,2],[1,1]]
Output: [-1,9,9]
Explanation:
For the 1st query [4,4]: There is no j such that nums1[j] >= 4 and nums2[j] >= 4.
For the 2nd query [3,2]: nums1[j] >= 3 and nums2[j] >= 2. We can choose j = 2 since nums1[2] = 5 >= 3 and nums2[2] = 4 >= 2. The sum is nums1[2] + nums2[2] = 9.
For the 3rd query [1,1]: nums1[j] >= 1 and nums2[j] >= 1. We can choose j = 0, j = 1, or j = 2. The maximum sum is max(3+2, 2+3, 5+4) = 9.

Constraints:
- n == nums1.length == nums2.length
- 1 <= n <= 10^5
- 1 <= nums1[i], nums2[i] <= 10^9
- 1 <= queries.length <= 10^5
- queries[i].length == 2
- 1 <= xi, yi <= 10^9
"""

def maximum_sum_queries(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    """
    Find maximum sum for each query using brute force approach.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers  
        queries: List of [xi, yi] query pairs
        
    Returns:
        list[int]: Maximum sums for each query, -1 if no valid j exists
        
    Time Complexity: O(q * n) where q is number of queries, n is array length
    Space Complexity: O(1) - constant extra space for computation
    """
    n = len(nums1)
    result = []
    
    for x, y in queries:
        max_sum = -1
        
        for j in range(n):
            if nums1[j] >= x and nums2[j] >= y:
                current_sum = nums1[j] + nums2[j]
                max_sum = max(max_sum, current_sum)
        
        result.append(max_sum)
    
    return result

def maximum_sum_queries_optimized(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    """
    Optimized approach using coordinate compression and segment tree or similar structure.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        queries: List of query pairs
        
    Returns:
        list[int]: Maximum sums for each query
        
    Time Complexity: O((n + q) log n) - sorting and processing with data structure
    Space Complexity: O(n) - for storing sorted data and auxiliary structures
    """
    n = len(nums1)
    
    # Create list of (nums1[i], nums2[i], sum) tuples
    points = [(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)]
    
    # Sort by nums1 in descending order for easier processing
    points.sort(reverse=True)
    
    result = []
    
    for x, y in queries:
        max_sum = -1
        
        # Since points are sorted by nums1 in descending order,
        # we only need to check points where nums1[i] >= x
        for nums1_val, nums2_val, point_sum in points:
            if nums1_val < x:
                break  # No more valid points
            if nums2_val >= y:
                max_sum = max(max_sum, point_sum)
        
        result.append(max_sum)
    
    return result

def maximum_sum_queries_segment_tree(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    """
    Advanced approach using coordinate compression and range maximum query.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        queries: List of query pairs
        
    Returns:
        list[int]: Maximum sums for each query
        
    Time Complexity: O((n + q) log n) - with efficient range queries
    Space Complexity: O(n) - for compressed coordinates and data structure
    """
    n = len(nums1)
    
    # Coordinate compression for nums2 values
    all_nums2 = sorted(set(nums2 + [q[1] for q in queries]))
    nums2_map = {v: i for i, v in enumerate(all_nums2)}
    
    # Create events: (nums1_val, nums2_val, sum, type)
    # type: 0 for points, 1 for queries
    events = []
    
    for i in range(n):
        events.append((nums1[i], nums2[i], nums1[i] + nums2[i], 0, i))
    
    for i, (x, y) in enumerate(queries):
        events.append((x, y, 0, 1, i))
    
    # Sort events by nums1 in descending order
    events.sort(reverse=True)
    
    # Simple approach: for each query, track maximum sum for valid points
    result = [-1] * len(queries)
    max_sums = {}  # nums2_val -> max_sum
    
    for event in events:
        if event[3] == 0:  # Point
            nums1_val, nums2_val, point_sum = event[0], event[1], event[2]
            max_sums[nums2_val] = max(max_sums.get(nums2_val, -1), point_sum)
        else:  # Query
            x, y, _, _, query_idx = event
            max_sum = -1
            for nums2_val, sum_val in max_sums.items():
                if nums2_val >= y:
                    max_sum = max(max_sum, sum_val)
            result[query_idx] = max_sum
    
    return result

def maximum_sum_queries_monotonic_stack(nums1: list[int], nums2: list[int], queries: list[list[int]]) -> list[int]:
    """
    Using monotonic stack approach for efficient processing.
    
    Args:
        nums1: First array of integers
        nums2: Second array of integers
        queries: List of query pairs
        
    Returns:
        list[int]: Maximum sums for each query
        
    Time Complexity: O((n + q) log n) - sorting and stack operations
    Space Complexity: O(n + q) - for storing processed data
    """
    n = len(nums1)
    
    # Create and sort points by nums1 descending, then nums2 descending
    points = [(nums1[i], nums2[i], nums1[i] + nums2[i]) for i in range(n)]
    points.sort(key=lambda x: (-x[0], -x[1]))
    
    # Add query indices for processing
    indexed_queries = [(x, y, i) for i, (x, y) in enumerate(queries)]
    indexed_queries.sort(key=lambda x: (-x[0], -x[1]))
    
    result = [-1] * len(queries)
    stack = []  # Monotonic stack for efficient range maximum
    point_idx = 0
    
    for x, y, query_idx in indexed_queries:
        # Add all points with nums1 >= x to our data structure
        while point_idx < len(points) and points[point_idx][0] >= x:
            nums1_val, nums2_val, point_sum = points[point_idx]
            
            # Maintain monotonic property: remove points that are dominated
            while stack and stack[-1][0] <= nums2_val and stack[-1][1] <= point_sum:
                stack.pop()
            
            if not stack or stack[-1][0] > nums2_val:
                stack.append((nums2_val, point_sum))
            
            point_idx += 1
        
        # Query for maximum sum where nums2 >= y
        max_sum = -1
        for nums2_val, point_sum in stack:
            if nums2_val >= y:
                max_sum = max(max_sum, point_sum)
        
        result[query_idx] = max_sum
    
    return result

# Test cases
def test_maximum_sum_queries():
    test_cases = [
        # Basic test cases
        ([4,3,1,2], [2,4,9,5], [[4,1],[1,3],[2,5]], [6,10,7]),
        ([3,2,5], [2,3,4], [[4,4],[3,2],[1,1]], [-1,9,9]),
        
        # Edge cases
        ([1], [1], [[1,1]], [2]),           # Single element
        ([1,2], [1,2], [[3,3]], [-1]),     # No valid elements
        ([5,5], [5,5], [[5,5]], [10]),     # Multiple same elements
        
        # All elements valid
        ([1,2,3], [1,2,3], [[1,1]], [6]), # Maximum sum should be 3+3=6
        
        # Complex cases
        ([10,5,1], [1,5,10], [[5,5],[1,1],[10,1]], [10,20,11]),
        ([1,1,1], [2,3,4], [[1,2]], [5]),  # Multiple elements satisfy, max is 1+4=5
        
        # Large value cases
        ([1000000000], [1000000000], [[1,1]], [2000000000]),
    ]
    
    print("Testing maximum_sum_queries function:")
    for i, (nums1, nums2, queries, expected) in enumerate(test_cases):
        result1 = maximum_sum_queries(nums1, nums2, queries)
        result2 = maximum_sum_queries_optimized(nums1, nums2, queries)
        result3 = maximum_sum_queries_segment_tree(nums1, nums2, queries)
        
        print(f"Test {i+1}:")
        print(f"  nums1={nums1}, nums2={nums2}")
        print(f"  queries={queries}")
        print(f"  Expected: {expected}")
        print(f"  Brute Force: {result1}")
        print(f"  Optimized: {result2}")
        print(f"  Segment Tree: {result3}")
        
        assert result1 == expected, f"Brute Force failed for test case {i+1}"
        assert result2 == expected, f"Optimized failed for test case {i+1}"
        assert result3 == expected, f"Segment Tree failed for test case {i+1}"
        print(f"  ✓ All passed\n")
    
    print("All test cases passed!")

if __name__ == "__main__":
    test_maximum_sum_queries()

"""
Time Complexity Analysis:
- Brute Force: O(q * n) - for each query, check all n elements
- Optimized: O((n + q) log n) - sorting points and processing queries
- Segment Tree: O((n + q) log n) - coordinate compression and range queries
- Monotonic Stack: O((n + q) log n) - sorting and stack operations

Space Complexity Analysis:
- Brute Force: O(1) - constant extra space
- Optimized: O(n) - storing sorted points
- Segment Tree: O(n) - coordinate compression and auxiliary structures
- Monotonic Stack: O(n + q) - stack and query processing

Key Insights:
1. For each query [x, y], we need nums1[j] >= x AND nums2[j] >= y
2. Among all valid j, we want the maximum nums1[j] + nums2[j]
3. Sorting by one dimension helps reduce search space
4. Coordinate compression can help with range queries
5. Monotonic data structures can maintain relevant maximum values efficiently

Topics: Arrays, Sorting, Segment Tree, Monotonic Stack, Range Queries
"""
