"""
LeetCode Problem #1242: Web Crawler Multithreaded

Problem Statement:
Given a URL `startUrl` and an interface `HtmlParser`, implement a web crawler to crawl all links that are under the same hostname as `startUrl`. 

Return all URLs obtained by your web crawler in any order.

Your crawler should:
1. Start from the page: `startUrl`.
2. Call `HtmlParser.getUrls(url)` to get all URLs from a webpage of a given URL.
3. Use multithreading to crawl multiple URLs simultaneously.

The `HtmlParser` interface is defined as follows:
    interface HtmlParser {
        public List<String> getUrls(String url);
    }

Notes:
- To determine whether a URL is under the same hostname, compare the hostname of the `startUrl` to the hostname of the URL.
- The hostname is the part of the URL between the protocol (e.g., `http://` or `https://`) and the port (e.g., `:80`) or the path (e.g., `/path`).
- A URL may start with "http://" or "https://".
- Assume all URLs use lowercase letters.

Constraints:
- `1 <= urls.length <= 1000`
- `1 <= urls[i].length <= 300`
- `startUrl` is a valid URL.
- The `HtmlParser.getUrls` function may return the same URL multiple times in the list.
- The crawling process should not crawl the same URL twice.
"""

from typing import List
from urllib.parse import urlparse
from concurrent.futures import ThreadPoolExecutor

class Solution:
    def crawl(self, startUrl: str, htmlParser: 'HtmlParser') -> List[str]:
        def get_hostname(url: str) -> str:
            """Extract the hostname from a URL."""
            return urlparse(url).netloc

        def crawl_url(url: str):
            """Crawl a single URL and add its links to the queue if they belong to the same hostname."""
            for next_url in htmlParser.getUrls(url):
                if next_url not in visited and get_hostname(next_url) == hostname:
                    visited.add(next_url)
                    queue.append(next_url)

        # Extract the hostname of the start URL
        hostname = get_hostname(startUrl)
        visited = set([startUrl])  # Set to track visited URLs
        queue = [startUrl]  # Queue for BFS

        # Use ThreadPoolExecutor for multithreading
        with ThreadPoolExecutor() as executor:
            while queue:
                # Submit tasks for all URLs in the current queue
                futures = [executor.submit(crawl_url, url) for url in queue]
                queue = []  # Clear the queue for the next level
                for future in futures:
                    future.result()  # Wait for all tasks to complete

        return list(visited)


# Example Test Cases
class HtmlParser:
    """Mock implementation of HtmlParser for testing purposes."""
    def __init__(self, url_map):
        self.url_map = url_map

    def getUrls(self, url: str) -> List[str]:
        return self.url_map.get(url, [])

# Test Case 1
html_parser = HtmlParser({
    "http://example.com": ["http://example.com/about", "http://example.com/contact"],
    "http://example.com/about": ["http://example.com"],
    "http://example.com/contact": ["http://example.com/about"],
    "http://other.com": ["http://example.com"]
})
solution = Solution()
start_url = "http://example.com"
print(solution.crawl(start_url, html_parser))
# Expected Output: ["http://example.com", "http://example.com/about", "http://example.com/contact"]

# Test Case 2
html_parser = HtmlParser({
    "http://a.com": ["http://a.com/b", "http://a.com/c"],
    "http://a.com/b": ["http://a.com/d"],
    "http://a.com/c": ["http://a.com/d", "http://b.com"],
    "http://a.com/d": []
})
start_url = "http://a.com"
print(solution.crawl(start_url, html_parser))
# Expected Output: ["http://a.com", "http://a.com/b", "http://a.com/c", "http://a.com/d"]

# Time and Space Complexity Analysis
"""
Time Complexity:
- Let N be the total number of URLs and E be the total number of edges (links between URLs).
- Each URL is visited once, and for each URL, we process all its outgoing links.
- Thus, the time complexity is O(N + E).

Space Complexity:
- The space complexity is O(N) for the visited set and the queue.
- Additionally, the ThreadPoolExecutor may use extra memory for managing threads.
- Overall, the space complexity is O(N).

Topic: Multithreading, BFS, Graph
"""