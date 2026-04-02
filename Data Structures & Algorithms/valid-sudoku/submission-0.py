
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
       row=defaultdict(set) #map of sets
       col=defaultdict(set) #map of sets
       box=defaultdict(set) #map of sets
       num=0
       for i in range(9):
        for j in range(9):
            num=board[i][j]
            if(num=="."):
                continue
            if(num in row[i] or
            num in col[j] or
            num in box[(int(i/3),int(j/3))]):
                return False
            else:
                row[i].add(num)
                col[j].add(num)
                box[(int(i/3),int(j/3))].add(num)
       return True

        