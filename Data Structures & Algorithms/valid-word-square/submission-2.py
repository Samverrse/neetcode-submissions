class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for i in range(len(words)):
            for j in range(len(words)):
                for word in words:
                    if word[i]==word[j]:
                        return True
        return False
        