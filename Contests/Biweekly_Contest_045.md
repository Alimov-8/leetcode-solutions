## Rank 3000/8000, Score 7/17, 2/4 Solved 

<br>

```py
#Question 1   Sum of Unique Elements

class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        isUnique = 0
        sumUnique = 0
        
        for first in nums:
            for items in nums:
                if first == items:
                    isUnique += 1
            if isUnique == 1:
                sumUnique += first
            
            isUnique = 0
        
        return sumUnique
        
    
    
    
#Question 3   Minimum Length of String After Deleting Similar Ends

class Solution:
    def minimumLength(self, s: str) -> int:
        isFound = True
        left = 0
        right = len(s) - 1
        
        while isFound:
            # No Items in s
            if len(s) == 0 or len(s) == 1:
                isFound = False
                
            # If same prefix and suffix
            elif s[left] == s[right] and len(s) > 2:
                
                while s[left] == s[left + 1] and left < right-1:
                    left = left + 1
                    
                while s[right] == s[right - 1] and left < right-1:
                    right = right - 1
                
                s = s[left+1 : right]
            
            elif s[left] == s[right]:    
                s = s[left+1 : right]

            else:   
                isFound = False
            
            left = 0
            right = len(s) - 1

            
        return len(s)
```