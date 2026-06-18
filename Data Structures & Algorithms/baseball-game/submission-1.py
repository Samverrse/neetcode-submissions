class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score=[]
        for op in operations:
            if op=="+":
                score.append(operations[-1]+operations[-2])
            elif op=="D":
                score.append(2*op[-1])
            elif op=="C":
                score.pop()
            else:
                score.append(int(op))
        return sum(score)


            

        