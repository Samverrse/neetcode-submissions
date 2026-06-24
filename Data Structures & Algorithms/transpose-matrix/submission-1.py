class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows=len(matrix)
        column=len(matrix[0])
        transposed=[]
        for i in range(column):
            newrow=[]
            for j in range(rows):
                newrow.append(matrix[j][i])
            transposed.append(newrow)
        return transposed


        