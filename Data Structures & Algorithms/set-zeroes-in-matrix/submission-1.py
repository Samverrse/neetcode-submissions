class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows,col=len(matrix),len(matrix[0])
        marks=[[matrix[r][c] for c in range(col)]for r in range(rows)]
        for r in range(rows):
            for c in range(col):
                if matrix[r][c]==0:
                    for c1 in range(col):
                        marks[r][c1]=0
                    for r1 in range(rows):
                        marks[r1][c]=0
        for r in range(rows):
            for c in range(col):
                matrix[r][c]=marks[r][c]
