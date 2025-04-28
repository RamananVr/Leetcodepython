"""
LeetCode Problem #1268: Search Suggestions System

Problem Statement:
You are given an array of strings `products` and a string `searchWord`. 
The `products` array contains the names of products in a store. You want to design a system that suggests at most three product names from `products` after each character of `searchWord` is typed. Suggested products should have common prefixes with the searchWord. If there are more than three products with a common prefix, return the three lexicographically minimum products.

Return a list of lists of the suggested products after each character of `searchWord` is typed.

Constraints:
- 1 <= products.length <= 1000
- 1 <= products[i].length <= 300
- 1 <= sum(products[i].length) <= 2 * 10^4
- All the strings of `products` are unique.
- products[i] consists of lowercase English letters.
- 1 <= searchWord.length <= 1000
- searchWord consists of lowercase English letters.

Example:
Input: products = ["mobile","mouse","moneypot","monitor","mousepad"], searchWord = "mouse"
Output: [
    ["mobile","moneypot","monitor"],
    ["mobile","moneypot","monitor"],
    ["mouse","mousepad"],
    ["mouse","mousepad"],
    ["mouse","mousepad"]
]
Explanation:
After typing "m", the system suggests ["mobile","moneypot","monitor"].
After typing "mo", the system suggests ["mobile","moneypot","monitor"].
After typing "mou", the system suggests ["mouse","mousepad"].
After typing "mous", the system suggests ["mouse","mousepad"].
After typing "mouse", the system suggests ["mouse","mousepad"].

Follow-up:
Could you optimize your solution to handle large inputs efficiently?
"""

# Python Solution
from typing import List

def suggestedProducts(products: List[str], searchWord: str) -> List[List[str]]:
    # Sort the products lexicographically
    products.sort()
    result = []
    prefix = ""
    
    for char in searchWord:
        prefix += char
        # Filter products that start with the current prefix
        suggestions = [product for product in products if product.startswith(prefix)]
        # Add at most the first three suggestions
        result.append(suggestions[:3])
    
    return result

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    products = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord = "mouse"
    print(suggestedProducts(products, searchWord))
    # Expected Output: [
    #     ["mobile", "moneypot", "monitor"],
    #     ["mobile", "moneypot", "monitor"],
    #     ["mouse", "mousepad"],
    #     ["mouse", "mousepad"],
    #     ["mouse", "mousepad"]
    # ]

    # Test Case 2
    products = ["bags", "baggage", "banner", "box", "cloths"]
    searchWord = "bags"
    print(suggestedProducts(products, searchWord))
    # Expected Output: [
    #     ["baggage", "bags", "banner"],
    #     ["baggage", "bags", "banner"],
    #     ["bags"],
    #     ["bags"]
    # ]

    # Test Case 3
    products = ["havana"]
    searchWord = "havana"
    print(suggestedProducts(products, searchWord))
    # Expected Output: [
    #     ["havana"],
    #     ["havana"],
    #     ["havana"],
    #     ["havana"],
    #     ["havana"],
    #     ["havana"]
    # ]

    # Test Case 4
    products = ["apple", "app", "apricot", "banana"]
    searchWord = "app"
    print(suggestedProducts(products, searchWord))
    # Expected Output: [
    #     ["app", "apple", "apricot"],
    #     ["app", "apple", "apricot"],
    #     ["app", "apple"]
    # ]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Sorting the products array takes O(n log n), where n is the number of products.
- For each character in `searchWord` (length m), we filter the products to find matches with the prefix. 
  In the worst case, this involves checking all n products for each character, resulting in O(m * n).
- Overall time complexity: O(n log n + m * n).

Space Complexity:
- The space complexity is dominated by the storage of the result list, which contains up to m sublists, each with at most 3 products.
- Additional space is used for the prefix string and the filtered suggestions list, but these are relatively small.
- Overall space complexity: O(m + n).

Topic: Strings
"""