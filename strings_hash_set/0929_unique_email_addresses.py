"""
LeetCode Question #929: Unique Email Addresses

Problem Statement:
Every email consists of a local name and a domain name, separated by the '@' sign. For example, in alice@leetcode.com, 
alice is the local name, and leetcode.com is the domain name.

Besides lowercase letters, the email may contain '.' or '+'.

- If you add periods ('.') between some characters in the local name part of an email address, mail sent there will be 
  forwarded to the same address without dots in the local name. For example, "alice.z@leetcode.com" and "alicez@leetcode.com" 
  forward to the same email address.
- If you add a plus ('+') in the local name, everything after the first plus sign will be ignored. This allows certain 
  emails to be filtered. For example, "m.y+name@email.com" will be forwarded to "my@email.com".
- (Note that this rule does not apply to domain names.)

Given an array of strings emails where we send one email to each email[i], return the number of different addresses 
that actually receive mails.

Example 1:
Input: emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.

Example 2:
Input: emails = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
Output: 3

Constraints:
- 1 <= emails.length <= 100
- 1 <= emails[i].length <= 100
- email[i] consists of lowercase English letters, '+', '.', and '@'.
- Each emails[i] contains exactly one '@' character.
"""

# Solution
def numUniqueEmails(emails):
    """
    Function to calculate the number of unique email addresses that actually receive mails.

    :param emails: List[str] - List of email addresses
    :return: int - Number of unique email addresses
    """
    unique_emails = set()

    for email in emails:
        local, domain = email.split('@')
        # Remove everything after '+' in the local name
        local = local.split('+')[0]
        # Remove all '.' in the local name
        local = local.replace('.', '')
        # Combine the processed local name with the domain
        unique_emails.add(local + '@' + domain)

    return len(unique_emails)

# Example Test Cases
if __name__ == "__main__":
    # Test Case 1
    emails1 = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails1))  # Output: 2

    # Test Case 2
    emails2 = ["a@leetcode.com", "b@leetcode.com", "c@leetcode.com"]
    print(numUniqueEmails(emails2))  # Output: 3

    # Test Case 3
    emails3 = ["test.email+alex@leetcode.com", "test.email.leet+alex@code.com"]
    print(numUniqueEmails(emails3))  # Output: 2

    # Test Case 4
    emails4 = ["test.email+alex@leetcode.com", "test.email@leetcode.com"]
    print(numUniqueEmails(emails4))  # Output: 1

# Time and Space Complexity Analysis
"""
Time Complexity:
- Splitting the email into local and domain parts takes O(n) for each email, where n is the length of the email string.
- Processing the local name (splitting by '+', removing '.', and concatenating) also takes O(n).
- Adding the processed email to the set takes O(1) on average.
- Overall, for m emails, the complexity is O(m * n), where m is the number of emails and n is the average length of an email.

Space Complexity:
- The space complexity is O(m * n) in the worst case, where m is the number of emails and n is the average length of an email.
  This accounts for storing all unique email addresses in the set.
"""

# Topic: Strings, Hash Set