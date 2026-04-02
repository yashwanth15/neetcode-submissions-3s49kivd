# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxd=0
        def dfs(root):
            nonlocal maxd
            if not root:
                return 0
            leftd=dfs(root.left)
            rightd=dfs(root.right)
            maxd=max(maxd,leftd+rightd)
            return 1+max(leftd,rightd)
        dfs(root)
        return maxd
        