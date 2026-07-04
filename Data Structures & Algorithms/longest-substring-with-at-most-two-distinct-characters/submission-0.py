class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l=0
        res=0
        mydict={}
        for r in range(len(s)):
            mydict[s[r]]=mydict.get(s[r],0)+1
            while len(mydict)>2:
                mydict[s[l]]-=1
                if mydict[s[l]]==0:
                    del mydict[s[l]]
                l+=1
            res=max(res,r-l+1)
        return res
        

            
        