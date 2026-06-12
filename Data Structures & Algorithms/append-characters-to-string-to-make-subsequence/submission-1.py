class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans=""
        it=iter(s)
        for i in range(len(t)):
            if t[i] not in it:
                ans=t[i+1:]
        return len(ans)



         
                    

        