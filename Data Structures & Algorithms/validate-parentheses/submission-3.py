class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mydict={"(":")","[":"]","{":"}"}
        for i in range(len(s)):
            if s[i] in mydict:
                stack.append(s[i])
            else:
                if len(stack)==0:
                    return False
                if mydict[stack[-1]]==s[i]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0