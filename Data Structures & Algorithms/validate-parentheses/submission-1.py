class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        dict={"]":"[","}":"{",")":"("}
        for ch in s:
            if ch in dict:
                if stack and stack[-1]==dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
        
                
             