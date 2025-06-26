from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        queue = []
        queue.append(root)

        while queue:
            current = queue.pop(0)

            # swap children
            current.left, current.right = current.right, current.left

            # add children to queue (if not 'None')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return root


def print_tree(inverted_tree):
    if not inverted_tree:
        return
    print(inverted_tree.val)
    print_tree(inverted_tree.left)
    print_tree(inverted_tree.right)


sol = Solution()

# Case 1
tree = TreeNode(
    4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(7, TreeNode(6), TreeNode(9))
)
inverted_tree = sol.invertTree(tree)
print_tree(inverted_tree)
print()

# Case 2
tree = TreeNode(1, TreeNode(2))
inverted_tree = sol.invertTree(tree)
print_tree(inverted_tree)
print()

# Case 3
tree = TreeNode(2, TreeNode(1), TreeNode(3))
inverted_tree = sol.invertTree(tree)
print_tree(inverted_tree)
print()

# Case 4
tree = TreeNode()
inverted_tree = sol.invertTree(tree)
print_tree(inverted_tree)
print()
