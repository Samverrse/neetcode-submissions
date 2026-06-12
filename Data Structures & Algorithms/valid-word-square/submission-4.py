class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words[i])):
                for word in words:
                    for ch in word:
                        if i==j and ch[i][j]==ch[j][i]:
                            return True
        return False
        