"""
LeetCode Question #1236: Web Crawler

Problem Statement:
You are given a URL `startUrl` representing the starting point of a web crawl. To crawl a web page, you perform the following steps:

1. Call `HtmlParser.getUrls(url)` to get all URLs from a webpage of a given URL.
2. The function returns a list of all URLs from that webpage in any order.
3. Your task is to implement a web crawler to crawl all pages that belong to the same hostname as the `startUrl`. 

Return all URLs obtained by your web crawler in any order.

Your crawler should:
- Start from the page: `startUrl`
- Explore only the web pages of the same hostname as `startUrl`.

As a reminder:
- To extract the hostname from a URL, you can use the following method:
  `hostname = startUrl.split('/')[2]`
- URLs are strings that follow the format `http://hostname/path/`.

The `HtmlParser` interface is defined as follows:
```python
class HtmlParser:
    def getUrls(self, url: str) -> List[str]:
        pass
```

Constraints:
- `1 <= urls.length <= 1000`
- `1 <= urls[i].length <= 300`
- `startUrl` is a valid URL.
- Hostname is a valid hostname.
- All URLs follow the HTTP protocol, i.e., they start with `"http://"`.

"""

from typing import List, Set

# Solution
class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url: str) -> str:
            """Extract the hostname from a URL."""
            return url.split('/')[2]

        # Extract the hostname of the start URL
        start_hostname = get_hostname(startUrl)
        
        # Use a set to keep track of visited URLs
        visited: Set[str] = set()
        visited.add(startUrl)
        
        # Use a queue for BFS
        queue = [startUrl]
        
        while queue:
            current_url = queue.pop(0)
            # Get all URLs from the current page
            for url in htmlParser.getUrls(current_url):
                # Check if the URL belongs to the same hostname and is not visited
                if url not in visited and get_hostname(url) == start_hostname:
                    visited.add(url)
                    queue.append(url)
        
        # Return all visited URLs as a list
        return list(visited)

# Example Test Cases
class MockHtmlParser:
    """Mock implementation of HtmlParser for testing purposes."""
    def __init__(self, url_map: dict):
        self.url_map = url_map

    def getUrls(self, url: str) -> List[str]:
        return self.url_map.get(url, [])

if __name__ == "__main__":
    # Mock data
    url_map = {
        "http://example.com/": ["http://example.com/a", "http://example.com/b", "http://example.org/"],
        "http://example.com/a": ["http://example.com/"],
        "http://example.com/b": ["http://example.com/c"],
        "http://example.com/c": [],
        "http://example.org/": ["http://example.org/a"],
    }
    htmlParser = MockHtmlParser(url_map)
    
    # Test case 1
    startUrl = "http://example.com/"
    solution = Solution()
    result = solution.crawl(startUrl, htmlParser)
    print(sorted(result))  # Expected: ['http://example.com/', 'http://example.com/a', 'http://example.com/b', 'http://example.com/c']

    # Test case 2
    startUrl = "http://example.org/"
    result = solution.crawl(startUrl, htmlParser)
    print(sorted(result))  # Expected: ['http://example.org/', 'http://example.org/a']

"""
Time Complexity:
- Let `n` be the total number of URLs and `e` be the total number of edges (links between URLs).
- In the worst case, we visit each URL once and process all its outgoing links.
- Thus, the time complexity is O(n + e).

Space Complexity:
- The space complexity is O(n) for the `visited` set and the BFS queue.

Topic: Graph Traversal (BFS)
"""