# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node: Optional[TreeNode]):
            if not node:
                return 0
            else:
                left_height = dfs(node.left)
                right_height = dfs(node.right)

                if left_height == -1 or right_height == -1:
                    return -1

                diff = abs(left_height - right_height)

                if diff > 1:
                    return -1
                else:
                    return 1 + max(left_height, right_height)

        return dfs(root) != -1