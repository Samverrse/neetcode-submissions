class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        column=len(matrix[0])
        transposed=[]
        for j in range(column):
            newrow=[]
            for i in range(rows):
                newrow.append(matrix[i][j])
            transposed.append(newrow)
        return transposed


        