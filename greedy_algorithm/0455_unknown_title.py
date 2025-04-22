"""
LeetCode Problem #455: Assign Cookies

Problem Statement:
Assume you are an awesome parent and want to give your children some cookies. But, you should give each child at most one cookie.

Each child `i` has a greed factor `g[i]`, which is the minimum size of a cookie that the child will be content with; and each cookie `j` has a size `s[j]`. If `s[j] >= g[i]`, we can assign the cookie `j` to the child `i`, and the child `i` will be content. Your goal is to maximize the number of your content children and output the maximum number.

You may assume the greed factor and the size of the cookies are both positive integers.

Example 1:
Input: g = [1,2,3], s = [1,1]
Output: 1
Explanation: You have 3 children and 2 cookies. The greed factors of 3 children are 1, 2, 3. 
And even though you have 2 cookies, since their size is both 1, you can only make the child whose greed factor is 1 content.
You need to output 1.

Example 2:
Input: g = [1,2], s = [1,2,3]
Output: 2
Explanation: You have 2 children and 3 cookies. The greed factors of 2 children are 1, 2. 
You have 3 cookies and their sizes are 1, 2, 3. You can assign the cookie with size 1 to the child with greed factor 1, 
and the cookie with size 2 to the child with greed factor 2. You need to output 2.

Constraints:
- 1 <= g.length <= 3 * 10^4
- 1 <= s.length <= 3 * 10^4
- 1 <= g[i], s[j] <= 2^31 - 1
"""

def findContentChildren(g, s):
    """
    Function to find the maximum number of content children.

    :param g: List[int] - greed factors of children
    :param s: List[int] - sizes of cookies
    :return: int - maximum number of content children
    """
    # Sort both greed factors and cookie sizes
    g.sort()
    s.sort()
    
    # Initialize pointers for children and cookies
    child = 0
    cookie = 0
    
    # Try to satisfy as many children as possible
    while child < len(g) and cookie < len(s):
        if s[cookie] >= g[child]:  # If the cookie can satisfy the child
            child += 1  # Move to the next child
        cookie += 1  # Move to the next cookie
    
    return child

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    g1 = [1, 2, 3]
    s1 = [1, 1]
    print(findContentChildren(g1, s1))  # Output: 1

    # Test Case 2
    g2 = [1, 2]
    s2 = [1, 2, 3]
    print(findContentChildren(g2, s2))  # Output: 2

    # Test Case 3
    g3 = [10, 9, 8, 7]
    s3 = [5, 6, 7, 8]
    print(findContentChildren(g3, s3))  # Output: 2

    # Test Case 4
    g4 = [1, 2, 3]
    s4 = [3]
    print(findContentChildren(g4, s4))  # Output: 1

"""
Time Complexity Analysis:
- Sorting the greed factors (g) takes O(n log n), where n is the length of g.
- Sorting the cookie sizes (s) takes O(m log m), where m is the length of s.
- The while loop iterates at most O(n + m) times, as we traverse both lists once.
- Overall time complexity: O(n log n + m log m).

Space Complexity Analysis:
- The sorting operations use O(log n) and O(log m) space for the sorting algorithms.
- No additional data structures are used, so the space complexity is O(1) apart from the input and output.
- Overall space complexity: O(1).

Topic: Greedy Algorithm
"""