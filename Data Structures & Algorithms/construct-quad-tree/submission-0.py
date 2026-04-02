"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def quad(size, r, c):
            # If size == 1, this is a leaf node
            if size == 1:
                return Node(grid[r][c]==1, True, None, None, None, None)
            
            half = size//2

            tl = quad(half, r, c)
            tr = quad(half, r, c+half)
            bl = quad(half, r+half, c)
            br = quad(half, r+half, c+half)

            # If all four are leaves and have same value -> merge
            if (tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf and
            tl.val == tr.val == bl.val == br.val):
                return Node(tl.val, True, None, None, None, None)

            # Otherwise internal node
            return Node(True, False, tl, tr, bl, br)
        
        return quad(len(grid), 0, 0)
        