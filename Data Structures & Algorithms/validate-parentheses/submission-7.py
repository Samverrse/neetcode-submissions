class Solution:
    def isValid(self, s: str) -> bool:
        mylist=[]
        mydict={"[":"]","{":"}","(":")"}
        for i in range(len(s)):
            if s[i] in mydict:
                mylist.append(s[i])
            else:
                if len(mylist)==0:
                    return False
                if mydict[mylist[-1]]==s[i]:
                    mylist.pop()
                    
                else:
                    return False
        return len(mylist)==0
                