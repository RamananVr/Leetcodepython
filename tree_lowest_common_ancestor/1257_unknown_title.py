"""
LeetCode Problem #1257: Smallest Common Region

Problem Statement:
You are given some lists of regions where the first region of each list includes all other regions in that list.

Naturally, if a region X contains another region Y, then X is bigger than Y. Also, by definition, a region X contains itself.

Given two regions: region1 and region2, return the smallest region that contains both of them.

If the regions are represented as a tree, the problem is to find the lowest common ancestor of the two nodes.

Example 1:
Input:
    regions = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"]
    ]
    region1 = "Quebec"
    region2 = "New York"
Output: "North America"

Constraints:
1. The number of regions is in the range [2, 1000].
2. The number of regions[i] is in the range [2, 10].
3. 1 <= regions[i][j].length, region1.length, region2.length <= 20.
4. region1 != region2.
5. region1 and region2 are guaranteed to be in the list of regions.
"""

# Python Solution
def findSmallestRegion(regions, region1, region2):
    # Create a parent mapping for each region
    parent_map = {}
    for region_list in regions:
        parent = region_list[0]
        for child in region_list[1:]:
            parent_map[child] = parent

    # Create a set of ancestors for region1
    ancestors = set()
    while region1 in parent_map:
        ancestors.add(region1)
        region1 = parent_map[region1]
    ancestors.add(region1)  # Add the root region

    # Traverse the ancestors of region2 to find the first common ancestor
    while region2 not in ancestors:
        region2 = parent_map[region2]

    return region2

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    regions = [
        ["Earth", "North America", "South America"],
        ["North America", "United States", "Canada"],
        ["United States", "New York", "Boston"],
        ["Canada", "Ontario", "Quebec"],
        ["South America", "Brazil"]
    ]
    region1 = "Quebec"
    region2 = "New York"
    print(findSmallestRegion(regions, region1, region2))  # Output: "North America"

    # Test Case 2
    regions = [
        ["World", "Asia", "Europe"],
        ["Asia", "China", "India"],
        ["Europe", "Germany", "France"],
        ["China", "Beijing", "Shanghai"],
        ["India", "Delhi", "Mumbai"]
    ]
    region1 = "Shanghai"
    region2 = "Delhi"
    print(findSmallestRegion(regions, region1, region2))  # Output: "Asia"

    # Test Case 3
    regions = [
        ["Global", "RegionA", "RegionB"],
        ["RegionA", "SubRegionA1", "SubRegionA2"],
        ["RegionB", "SubRegionB1", "SubRegionB2"]
    ]
    region1 = "SubRegionA1"
    region2 = "SubRegionB1"
    print(findSmallestRegion(regions, region1, region2))  # Output: "Global"

# Time and Space Complexity Analysis
"""
Time Complexity:
- Building the parent_map takes O(n), where n is the total number of regions across all lists.
- Traversing the ancestors of region1 takes O(h1), where h1 is the height of the tree from region1 to the root.
- Traversing the ancestors of region2 takes O(h2), where h2 is the height of the tree from region2 to the root.
- In the worst case, h1 + h2 = O(n), so the overall time complexity is O(n).

Space Complexity:
- The parent_map dictionary requires O(n) space to store the parent-child relationships.
- The ancestors set requires O(h1) space in the worst case.
- Overall, the space complexity is O(n).
"""

# Topic: Tree, Lowest Common Ancestor