class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[]
        for i in range(len(temperatures)):
            found=False
            for j in range(i+1,len(temperatures)):
                if temperatures[i]<temperatures[j]:
                    diff=j-i
                    ans.append(diff)
                    found=True
                    break
            if not found:
                ans.append(0)
                
        return ans
        