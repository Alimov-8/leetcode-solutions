class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if list empty return empty string
        if len(strs)==0:
            return ""
    
        # Find lenght of shortest string in the list 
        length = 10000 # defoult value
        finalAnswer = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
        answer = ""
        
        for i in strs: # Check all values
            if len(i) < length:
                length = len(i)
                shortStr = i # take shortest element in the list
        
        for i in strs: # Next loop
            answer = ""
            j = 0
            while (j < int(len(shortStr))): #Take longest common prefic between two strings
                  if shortStr[j] == i[j]:
                    answer = answer + shortStr[j]
                    j=j+1
                  else:
                    j = len(shortStr)
                
            if len(finalAnswer) > len(answer): # check this prefix shortest in the list?
                finalAnswer = answer

        
        return finalAnswer
    
    
    
    # Another solution but idea same (shortest version of my algorithm)
    '''class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: # constraint includes len(strs)==0
            return ''
        shortest = min(strs,key=len)
        for i,c in enumerate(shortest):
            for words in strs:
                if words[i]!=c:
                    return shortest[:i] # upto but not including mismatched ith character
        return shortest'''
