class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans=[]
        for i in range(len(words)):
            if words[i] in words[i+1:]:
                ans.append(words[i])
        return ans

        