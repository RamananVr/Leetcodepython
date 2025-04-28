"""
LeetCode Question #1600: Throne Inheritance

Problem Statement:
A kingdom consists of a king, his children, and their descendants. Every person in the kingdom has a unique name. The king is initially the only person in the kingdom. Later, new people are born into the kingdom, and some people die. A person's birth and death affect the order of inheritance of the throne.

Implement the `ThroneInheritance` class:
- `ThroneInheritance(string kingName)` Initializes an object of the `ThroneInheritance` class. The name of the king is given as `kingName`. The king is initially alive.
- `void birth(string parentName, string childName)` Indicates that `childName` was born to `parentName`. The child becomes the next descendant of the parent in the order of inheritance.
- `void death(string name)` Indicates that `name` is dead. The death of a person does not affect the order of inheritance except that the dead person is excluded from the inheritance order.
- `List<string> getInheritanceOrder()` Returns a list representing the current order of inheritance excluding dead people.

Constraints:
- 1 <= kingName.length, parentName.length, childName.length, name.length <= 15
- All input strings are unique.
- 1 <= number of calls to `birth`, `death`, and `getInheritanceOrder` <= 10^5
- `kingName`, `parentName`, `childName`, and `name` consist of lowercase English letters only.
- `death` will only be called with the name of a person who is alive.

"""

class ThroneInheritance:
    def __init__(self, kingName: str):
        """
        Initializes the ThroneInheritance object with the king's name.
        """
        self.king = kingName
        self.family_tree = {kingName: []}  # Adjacency list to represent the family tree
        self.dead = set()  # Set to track dead people

    def birth(self, parentName: str, childName: str) -> None:
        """
        Adds a child to the parent's list of descendants.
        """
        if parentName not in self.family_tree:
            self.family_tree[parentName] = []
        self.family_tree[parentName].append(childName)
        self.family_tree[childName] = []  # Initialize the child's descendants list

    def death(self, name: str) -> None:
        """
        Marks a person as dead.
        """
        self.dead.add(name)

    def getInheritanceOrder(self) -> list:
        """
        Returns the current order of inheritance excluding dead people.
        """
        order = []

        def dfs(name):
            if name not in self.dead:
                order.append(name)
            for child in self.family_tree[name]:
                dfs(child)

        dfs(self.king)
        return order


# Example Test Cases
if __name__ == "__main__":
    # Initialize the ThroneInheritance object
    ti = ThroneInheritance("king")

    # Births
    ti.birth("king", "andy")
    ti.birth("king", "bob")
    ti.birth("king", "catherine")
    ti.birth("andy", "matthew")
    ti.birth("bob", "alex")
    ti.birth("bob", "asha")

    # Deaths
    ti.death("bob")

    # Get inheritance order
    print(ti.getInheritanceOrder())  # Expected: ['king', 'andy', 'matthew', 'catherine', 'alex', 'asha']

"""
Time and Space Complexity Analysis:

1. `__init__`:
   - Time Complexity: O(1)
   - Space Complexity: O(1)

2. `birth`:
   - Time Complexity: O(1) (Adding a child to the parent's list and initializing the child's list)
   - Space Complexity: O(1) (Adding a new entry to the family tree)

3. `death`:
   - Time Complexity: O(1) (Adding a name to the dead set)
   - Space Complexity: O(1)

4. `getInheritanceOrder`:
   - Time Complexity: O(n), where n is the total number of people in the family tree. This is because we perform a DFS traversal of the family tree.
   - Space Complexity: O(n), due to the recursion stack and the storage of the inheritance order.

Overall:
- Time Complexity: O(n) for `getInheritanceOrder`, O(1) for other operations.
- Space Complexity: O(n), where n is the total number of people in the family tree.

Topic: Tree Traversal
"""