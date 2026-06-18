class Solution:
    def calPoints(self, operations: List[str]) -> int:
        for i in range (len(operations)):
            if "+" in operations:
                operations.replace(operations[i-1]+operations[i-2])
                if "D" in operations:
                    operation.replace("D",2*operation[i-1])
                    if "C" in operations:
                        operations.remove([i-1])
        return sum(operations)



            

        