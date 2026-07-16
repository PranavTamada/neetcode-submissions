class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        b = {"}":"{","]":'[',")":"("}
        for i in s:
            if i in ['[','{','(']:
                stack.append(i)
            else:
                if stack and b[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return not stack 
