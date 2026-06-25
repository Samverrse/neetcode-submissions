class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        ans=""
        it=iter(s)
        for ch in t:
            if ch not in it:
                ans+=ch
        return len(ans)



         
                    

        