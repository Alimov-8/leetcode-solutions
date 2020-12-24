class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # if list empty return empty string
        if len(strs)==0:
            return ""
    
        # Find lenght of shortest string in the list 
        length = 10000 # defoult value
        finalAnswer = "kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk"
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
