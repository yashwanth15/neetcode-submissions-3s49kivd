# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # bfs
        q=deque([root])
        res=[]
        while q:
            right=q[-1]
            if right:
                res.append(right.val)
            n=len(q)
            for _ in range(n):
                node=q.popleft()
                if node and node.left:
                    q.append(node.left)
                if node and node.right:
                    q.append(node.right)
        return res
        