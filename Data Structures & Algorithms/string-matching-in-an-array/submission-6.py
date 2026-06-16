class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        sortit=sorted(words,key=len)
        for i in range(len(sortit)):
            if any(sortit[i] in word for word in sortit[i+1:]):
                ans.append(sortit[i])
        return ans

            

        