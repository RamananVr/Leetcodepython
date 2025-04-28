"""
LeetCode Problem #1993: Operations on Tree

Problem Statement:
You are given a tree with `n` nodes numbered from `0` to `n - 1` in the form of a parent array `parent` where `parent[i]` is the parent of the `i-th` node. The root node is `0`, so `parent[0] = -1` since it has no parent. Each node has a lock state that is initially `unlocked`.

Implement a class `LockingTree` that has the following methods:

1. `LockingTree(int[] parent)`: Constructs the tree with the given parent array.
2. `bool lock(int num, int user)`: Locks the node `num` for the user `user`. If the node is already locked, the operation fails and returns `False`. Otherwise, the node is locked and the operation returns `True`.
3. `bool unlock(int num, int user)`: Unlocks the node `num` for the user `user`. If the node is not locked by the user `user`, the operation fails and returns `False`. Otherwise, the node is unlocked and the operation returns `True`.
4. `bool upgrade(int num, int user)`: Upgrades the node `num` for the user `user`. To upgrade a node:
   - The node must be unlocked.
   - It must have at least one locked descendant (by any user).
   - It must not have any locked ancestors.
   If the upgrade is successful, the node is locked for the user `user`, and all its descendants are unlocked. The operation returns `True`. Otherwise, it returns `False`.

Constraints:
- `n == parent.length`
- `2 <= n <= 2000`
- `0 <= parent[i] <= n - 1` for all `i != 0`
- `parent[0] == -1`
- `0 <= num <= n - 1`
- `1 <= user <= 10^4`
- At most `2000` calls will be made to any function.

"""

from collections import defaultdict, deque

class LockingTree:
    def __init__(self, parent: list[int]):
        self.parent = parent
        self.locked = {}  # Dictionary to store locked nodes and their users
        self.children = defaultdict(list)  # Adjacency list for children of each node
        for child, par in enumerate(parent):
            if par != -1:
                self.children[par].append(child)

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False  # Node is already locked
        self.locked[num] = user  # Lock the node for the user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False  # Node is not locked by this user
        del self.locked[num]  # Unlock the node
        return True

    def upgrade(self, num: int, user: int) -> bool:
        # Check if the node is unlocked
        if num in self.locked:
            return False

        # Check if the node has any locked ancestors
        current = num
        while current != -1:
            if current in self.locked:
                return False
            current = self.parent[current]

        # Check if the node has at least one locked descendant
        has_locked_descendant = False
        queue = deque([num])
        to_unlock = []  # List of descendants to unlock
        while queue:
            node = queue.popleft()
            if node in self.locked:
                has_locked_descendant = True
                to_unlock.append(node)
            queue.extend(self.children[node])

        if not has_locked_descendant:
            return False

        # Perform the upgrade: lock the node and unlock all its descendants
        self.locked[num] = user
        for node in to_unlock:
            del self.locked[node]
        return True


# Example Test Cases
if __name__ == "__main__":
    # Initialize the tree
    parent = [-1, 0, 0, 1, 1, 2, 2]
    tree = LockingTree(parent)

    # Test lock
    assert tree.lock(2, 10) == True  # Lock node 2 for user 10
    assert tree.lock(2, 20) == False  # Node 2 is already locked

    # Test unlock
    assert tree.unlock(2, 20) == False  # Node 2 is not locked by user 20
    assert tree.unlock(2, 10) == True  # Unlock node 2 for user 10

    # Test upgrade
    assert tree.lock(4, 15) == True  # Lock node 4 for user 15
    assert tree.lock(5, 25) == True  # Lock node 5 for user 25
    assert tree.upgrade(0, 5) == True  # Upgrade node 0 for user 5
    assert tree.lock(4, 15) == True  # Node 4 is unlocked, so it can be locked again

    print("All test cases passed!")

"""
Time Complexity:
- `lock` and `unlock`: O(1) since they involve dictionary operations.
- `upgrade`: O(n) in the worst case, as it may need to traverse all ancestors and descendants of the node.

Space Complexity:
- O(n) for storing the parent array and the adjacency list of children.

Topic: Tree, BFS, HashMap
"""