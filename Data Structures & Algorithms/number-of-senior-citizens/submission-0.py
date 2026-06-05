class Solution:
    def countSeniors(self, details: List[str]) -> int:
        num=0
        for det in details:
            age=int(det[11:13])
            if age > 60:
                num+=1
        return num

        