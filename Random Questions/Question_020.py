#Alimov Abdullokh (I solved it using stack which I learned in IUT Data Structres Courese)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = ["K"]
        for i in s:
            if (i == "(" or i == "[" or i == "{"):
                stack.append(i) # just push
            else:
                if stack[-1] == "(" and i == ")": 
                    stack.pop()
                elif stack[-1] == "{" and i == "}": 
                    stack.pop()
                elif stack[-1] == "[" and i == "]": 
                    stack.pop()
                else:
                    return False      
        stack.pop()
        if len(stack) == 0 :
            return True
        
