# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count=0
        def dfs(node,highest):
            nonlocal count
            if not node:
                return
            if node.val >= highest:
                count+=1
                highest=node.val
            dfs(node.left,highest)
            dfs(node.right,highest)
        
        dfs(root, float("-inf"))
        return count

        