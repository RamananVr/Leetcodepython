"""
LeetCode Problem #811: Subdomain Visit Count

Problem Statement:
A website domain "discuss.leetcode.com" consists of various subdomains. At the top level, we have "com", 
at the next level, we have "leetcode.com", and at the lowest level, "discuss.leetcode.com". When we visit 
a domain like "discuss.leetcode.com", we will also visit the parent domains "leetcode.com" and "com" 
implicitly.

A count-paired domain is a domain that has an associated visit count, such as "9001 discuss.leetcode.com". 
It means the domain "discuss.leetcode.com" was visited 9001 times.

Given a list of count-paired domains `cpdomains`, return a list of the count-paired domains of each 
subdomain in the input. You may return the answer in any order.

Example 1:
Input: cpdomains = ["9001 discuss.leetcode.com"]
Output: ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]

Explanation:
We will visit "discuss.leetcode.com" 9001 times, "leetcode.com" 9001 times, and "com" 9001 times.

Example 2:
Input: cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
Output: ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]

Explanation:
We will visit "google.mail.com" 900 times, "mail.com" 900 times, and "com" 900 times.
"yahoo.com" gets 50 visits and "com" gets an additional 50 visits.
"intel.mail.com" gets 1 visit, "mail.com" gets an additional 1 visit, and "com" gets an additional 1 visit.
"wiki.org" gets 5 visits, and "org" gets 5 visits.

Constraints:
1. 1 <= cpdomains.length <= 100
2. 1 <= cpdomains[i].length <= 100
3. cpdomains[i] follows the format "{count} {domain}".
4. The count is in the range [1, 10^4].
5. The domain consists of lowercase English letters, digits, and '-' or '.'.
6. The domain will not have leading or trailing spaces.
7. The number of subdomains for any domain will not exceed 100.
"""

from collections import defaultdict

def subdomainVisits(cpdomains):
    """
    Function to calculate the visit count for each subdomain.

    Args:
    cpdomains (List[str]): List of count-paired domains.

    Returns:
    List[str]: List of count-paired subdomains with their visit counts.
    """
    domain_counts = defaultdict(int)

    for cpdomain in cpdomains:
        count, domain = cpdomain.split()
        count = int(count)
        subdomains = domain.split('.')
        
        # Generate all subdomains
        for i in range(len(subdomains)):
            subdomain = '.'.join(subdomains[i:])
            domain_counts[subdomain] += count

    # Format the result as required
    return [f"{count} {domain}" for domain, count in domain_counts.items()]

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    cpdomains1 = ["9001 discuss.leetcode.com"]
    print(subdomainVisits(cpdomains1))  # Output: ["9001 leetcode.com", "9001 discuss.leetcode.com", "9001 com"]

    # Test Case 2
    cpdomains2 = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
    print(subdomainVisits(cpdomains2))  # Output: ["901 mail.com", "50 yahoo.com", "900 google.mail.com", "5 wiki.org", "5 org", "1 intel.mail.com", "951 com"]

    # Test Case 3
    cpdomains3 = ["10 a.b.c", "20 b.c", "30 c"]
    print(subdomainVisits(cpdomains3))  # Output: ["10 a.b.c", "30 b.c", "60 c"]

"""
Time Complexity Analysis:
- Splitting each domain into subdomains takes O(L), where L is the average length of a domain.
- For each domain in cpdomains, we process up to O(L) subdomains.
- Thus, the total time complexity is O(N * L), where N is the number of domains in cpdomains.

Space Complexity Analysis:
- We use a dictionary to store the counts for each subdomain. In the worst case, we store up to O(N * L) subdomains.
- Thus, the space complexity is O(N * L).

Topic: Hash Table, String Manipulation
"""