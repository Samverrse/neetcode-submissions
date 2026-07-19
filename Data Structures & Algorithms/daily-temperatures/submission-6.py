class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans=[]
        for i in range(len(temperatures)-1):
            mylist=temperatures[i+1:]
            for n in mylist:
                if temperatures[i]<n:
                    diff=temperatures.index(n)-i
                    print(diff)
                    break
                else:
                    diff=0
            ans.append(diff)
        ans.append(0)
                
        return ans
                

        