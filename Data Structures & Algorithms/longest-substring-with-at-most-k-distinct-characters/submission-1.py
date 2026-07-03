class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        res=0
        l=0
        mydict={}
        for r in range(len(s)):
            mydict[s[r]]=mydict.get(s[r],0)+1
            while len(mydict)>k:
                mydict[s[l]]-=1
                if mydict[s[l]]==0:
                    del mydict[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res    
