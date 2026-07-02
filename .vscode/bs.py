class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    # ── Insert ──────────────────────────────────────────────
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    # ── Search ──────────────────────────────────────────────
    def search(self, value):
        return self._search(self.root, value)

    def _search(self, node, value):
        if node is None:
            return False
        if value == node.value:
            return True
        elif value < node.value:
            return self._search(node.left, value)
        else:
            return self._search(node.right, value)

    # ── Delete ──────────────────────────────────────────────
    def delete(self, value):
        self.root = self._delete(self.root, value)

    def _delete(self, node, value):
        if node is None:
            return None
        if value < node.value:
            node.left = self._delete(node.left, value)
        elif value > node.value:
            node.right = self._delete(node.right, value)
        else:
            # Case 1: No child
            if node.left is None and node.right is None:
                return None
            # Case 2: One child
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            # Case 3: Two children → replace with in-order successor
            successor = self._min_node(node.right)
            node.value = successor.value
            node.right = self._delete(node.right, successor.value)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    # ── Traversals ──────────────────────────────────────────
    def inorder(self):      # Left → Root → Right  (sorted order)
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.value)
            self._inorder(node.right, result)

    def preorder(self):     # Root → Left → Right
        result = []
        self._preorder(self.root, result)
        return result

    def _preorder(self, node, result):
        if node:
            result.append(node.value)
            self._preorder(node.left, result)
            self._preorder(node.right, result)

    def postorder(self):    # Left → Right → Root
        result = []
        self._postorder(self.root, result)
        return result

    def _postorder(self, node, result):
        if node:
            self._postorder(node.left, result)
            self._postorder(node.right, result)
            result.append(node.value)

    # ── Utility ─────────────────────────────────────────────
    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def min_value(self):
        if not self.root:
            return None
        return self._min_node(self.root).value

    def max_value(self):
        node = self.root
        while node and node.right:
            node = node.right
        return node.value if node else None

    def display(self):
        """Simple visual representation of the tree."""
        lines = []
        self._display(self.root, lines, 0)
        print("\n".join(lines))

    def _display(self, node, lines, level):
        if node:
            self._display(node.right, lines, level + 1)
            lines.append(" " * (level * 4) + str(node.value))
            self._display(node.left, lines, level + 1)


# ── Demo ─────────────────────────────────────────────────────
if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [50, 30, 70, 20, 40, 60, 80]
    for v in values:
        bst.insert(v)

    print("=== Binary Search Tree ===\n")
    bst.display()

    print(f"\nInorder   : {bst.inorder()}")
    print(f"Preorder  : {bst.preorder()}")
    print(f"Postorder : {bst.postorder()}")

    print(f"\nHeight    : {bst.height()}")
    print(f"Min value : {bst.min_value()}")
    print(f"Max value : {bst.max_value()}")

    print(f"\nSearch 40 : {bst.search(40)}")
    print(f"Search 99 : {bst.search(99)}")

    bst.delete(30)
    print(f"\nAfter deleting 30 → Inorder: {bst.inorder()}")
    print("\nUpdated tree:")
    bst.display()