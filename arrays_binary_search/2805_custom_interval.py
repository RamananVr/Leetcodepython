"""
LeetCode Problem 2805: Custom Interval

Design a data structure that supports adding intervals and querying for the number of intervals that contain a given point.

Implement the CustomInterval class:
- CustomInterval() Initializes the object.
- void addInterval(int left, int right) Adds the interval [left, right] to the data structure.
- int query(int point) Returns the number of intervals that contain the point.

An interval [left, right] contains point if left <= point <= right.

Constraints:
- 1 <= left <= right <= 10^9
- 1 <= point <= 10^9
- At most 10^5 calls will be made to addInterval and query.

Example 1:
Input:
["CustomInterval", "addInterval", "addInterval", "query", "query", "query"]
[[], [1, 3], [2, 6], [2], [5], [7]]
Output:
[null, null, null, 2, 1, 0]

Explanation:
CustomInterval customInterval = new CustomInterval();
customInterval.addInterval(1, 3); // Add interval [1, 3]
customInterval.addInterval(2, 6); // Add interval [2, 6]
customInterval.query(2); // return 2, intervals [1, 3] and [2, 6] contain point 2
customInterval.query(5); // return 1, interval [2, 6] contains point 5
customInterval.query(7); // return 0, no interval contains point 7
"""

class CustomInterval:
    """
    Approach 1: Simple List with Linear Search
    
    Store intervals in a list and check each interval for queries.
    
    Time Complexity: 
    - addInterval: O(1)
    - query: O(n)
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.intervals = []
    
    def addInterval(self, left, right):
        self.intervals.append((left, right))
    
    def query(self, point):
        count = 0
        for left, right in self.intervals:
            if left <= point <= right:
                count += 1
        return count

class CustomIntervalOptimized:
    """
    Approach 2: Coordinate Compression + Difference Array
    
    Use coordinate compression and difference array for efficient queries.
    
    Time Complexity:
    - addInterval: O(log n) amortized
    - query: O(log n)
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.events = []  # (coordinate, delta)
        self.compressed = False
        self.coords = []
        self.diff_array = []
    
    def addInterval(self, left, right):
        self.events.append((left, 1))      # Start of interval
        self.events.append((right + 1, -1)) # End of interval (exclusive)
        self.compressed = False  # Need to recompress
    
    def _compress(self):
        """Compress coordinates and build difference array"""
        if self.compressed:
            return
        
        # Get all unique coordinates
        coords_set = set()
        for coord, _ in self.events:
            coords_set.add(coord)
        
        self.coords = sorted(coords_set)
        coord_to_idx = {coord: i for i, coord in enumerate(self.coords)}
        
        # Build difference array
        self.diff_array = [0] * len(self.coords)
        for coord, delta in self.events:
            if coord in coord_to_idx:
                self.diff_array[coord_to_idx[coord]] += delta
        
        # Convert to prefix sum for actual counts
        for i in range(1, len(self.diff_array)):
            self.diff_array[i] += self.diff_array[i-1]
        
        self.compressed = True
    
    def query(self, point):
        self._compress()
        
        # Binary search for the rightmost coordinate <= point
        left, right = 0, len(self.coords) - 1
        result_idx = -1
        
        while left <= right:
            mid = (left + right) // 2
            if self.coords[mid] <= point:
                result_idx = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return self.diff_array[result_idx] if result_idx >= 0 else 0

class CustomIntervalSegmentTree:
    """
    Approach 3: Segment Tree with Coordinate Compression
    
    Use segment tree for range updates and point queries.
    
    Time Complexity:
    - addInterval: O(log n)
    - query: O(log n)
    Space Complexity: O(n)
    """
    
    def __init__(self):
        self.intervals = []
        self.tree = None
        self.coords = []
        self.built = False
    
    def addInterval(self, left, right):
        self.intervals.append((left, right))
        self.built = False
    
    def _build_tree(self):
        """Build segment tree with coordinate compression"""
        if self.built:
            return
        
        # Compress coordinates
        coords_set = set()
        for left, right in self.intervals:
            coords_set.add(left)
            coords_set.add(right)
            coords_set.add(right + 1)  # For exclusive end
        
        self.coords = sorted(coords_set)
        n = len(self.coords)
        
        # Build segment tree
        self.tree = [0] * (4 * n)
        self.lazy = [0] * (4 * n)
        
        # Add all intervals to tree
        for left, right in self.intervals:
            left_idx = self._get_index(left)
            right_idx = self._get_index(right)
            self._update_range(0, 0, n-1, left_idx, right_idx, 1)
        
        self.built = True
    
    def _get_index(self, coord):
        """Get index of coordinate in compressed array"""
        left, right = 0, len(self.coords) - 1
        while left <= right:
            mid = (left + right) // 2
            if self.coords[mid] == coord:
                return mid
            elif self.coords[mid] < coord:
                left = mid + 1
            else:
                right = mid - 1
        return left - 1  # Largest coordinate <= coord
    
    def _push(self, node, start, end):
        """Push lazy updates down"""
        if self.lazy[node] != 0:
            self.tree[node] += self.lazy[node]
            if start != end:
                self.lazy[2*node+1] += self.lazy[node]
                self.lazy[2*node+2] += self.lazy[node]
            self.lazy[node] = 0
    
    def _update_range(self, node, start, end, l, r, val):
        """Update range [l, r] with value val"""
        self._push(node, start, end)
        if start > r or end < l:
            return
        
        if start >= l and end <= r:
            self.lazy[node] += val
            self._push(node, start, end)
            return
        
        mid = (start + end) // 2
        self._update_range(2*node+1, start, mid, l, r, val)
        self._update_range(2*node+2, mid+1, end, l, r, val)
    
    def _query_point(self, node, start, end, idx):
        """Query value at index idx"""
        if start == end:
            self._push(node, start, end)
            return self.tree[node]
        
        self._push(node, start, end)
        mid = (start + end) // 2
        if idx <= mid:
            return self._query_point(2*node+1, start, mid, idx)
        else:
            return self._query_point(2*node+2, mid+1, end, idx)
    
    def query(self, point):
        self._build_tree()
        if not self.coords:
            return 0
        
        idx = self._get_index(point)
        if idx < 0 or self.coords[idx] > point:
            return 0
        
        return self._query_point(0, 0, len(self.coords)-1, idx)

class CustomIntervalBST:
    """
    Approach 4: Binary Search Tree with Intervals
    
    Use balanced BST to store intervals sorted by start time.
    
    Time Complexity:
    - addInterval: O(log n)
    - query: O(n) worst case, O(log n) average
    Space Complexity: O(n)
    """
    
    class IntervalNode:
        def __init__(self, left, right):
            self.left_val = left
            self.right_val = right
            self.max_right = right
            self.left_child = None
            self.right_child = None
    
    def __init__(self):
        self.root = None
    
    def addInterval(self, left, right):
        self.root = self._insert(self.root, left, right)
    
    def _insert(self, node, left, right):
        if not node:
            return self.IntervalNode(left, right)
        
        # Update max_right
        node.max_right = max(node.max_right, right)
        
        if left <= node.left_val:
            node.left_child = self._insert(node.left_child, left, right)
        else:
            node.right_child = self._insert(node.right_child, left, right)
        
        return node
    
    def query(self, point):
        return self._search(self.root, point)
    
    def _search(self, node, point):
        if not node:
            return 0
        
        count = 0
        
        # Check current interval
        if node.left_val <= point <= node.right_val:
            count += 1
        
        # Search left subtree if it might contain point
        if node.left_child and node.left_child.max_right >= point:
            count += self._search(node.left_child, point)
        
        # Search right subtree if it might contain point
        if node.right_child and node.left_val <= point:
            count += self._search(node.right_child, point)
        
        return count

# Test cases
def test_custom_interval():
    test_cases = [
        {
            "operations": ["CustomInterval", "addInterval", "addInterval", "query", "query", "query"],
            "inputs": [[], [1, 3], [2, 6], [2], [5], [7]],
            "expected": [None, None, None, 2, 1, 0]
        },
        {
            "operations": ["CustomInterval", "addInterval", "addInterval", "addInterval", "query", "query"],
            "inputs": [[], [1, 5], [3, 7], [6, 10], [4], [8]],
            "expected": [None, None, None, None, 2, 1]
        }
    ]
    
    approaches = [
        ("Simple List", CustomInterval),
        ("Optimized", CustomIntervalOptimized),
        ("Segment Tree", CustomIntervalSegmentTree),
        ("BST", CustomIntervalBST)
    ]
    
    for approach_name, CustomIntervalClass in approaches:
        print(f"Testing {approach_name} approach:")
        
        for i, test_case in enumerate(test_cases):
            print(f"  Test Case {i+1}:")
            
            obj = None
            results = []
            
            for j, (op, inp) in enumerate(zip(test_case["operations"], test_case["inputs"])):
                if op == "CustomInterval":
                    obj = CustomIntervalClass()
                    results.append(None)
                elif op == "addInterval":
                    obj.addInterval(inp[0], inp[1])
                    results.append(None)
                elif op == "query":
                    result = obj.query(inp[0])
                    results.append(result)
            
            print(f"    Results: {results}")
            print(f"    Expected: {test_case['expected']}")
            print(f"    ✓ Passed: {results == test_case['expected']}")
        
        print()

if __name__ == "__main__":
    test_custom_interval()

"""
Topics: Arrays, Binary Search, Segment Tree, Data Structure Design
Difficulty: Medium

Key Insights:
1. Simple approach stores intervals and searches linearly
2. Coordinate compression reduces space for sparse coordinates
3. Segment tree provides efficient range updates and queries
4. BST with max_right enables pruning during search
5. Trade-off between insert and query performance

Companies: Google, Microsoft, Amazon, Bloomberg
"""
