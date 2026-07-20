class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dict_1={}
        for ch1 in s:
            dict_1[ch1]=dict_1.get(ch1,0)+1
        news="".join(wordDict)
        dict_2={}
        for ch2 in news:
            dict_2[ch2]=dict_2.get(ch2,0)+1
        if dict_1==dict_2:
            return True
        return False





        