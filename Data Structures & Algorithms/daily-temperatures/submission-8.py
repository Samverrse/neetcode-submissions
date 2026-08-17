class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[]
        for i in range(len(temperatures)-1):
            diff=0
            for j in range(i+1,len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    diff=j-i
                    break
            ans.append(diff)
        ans.append(0)
        return ans
        
                

        