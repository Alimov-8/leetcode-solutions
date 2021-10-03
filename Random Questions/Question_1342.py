class Solution:
    def numberOfSteps (self, num: int) -> int:
        ans = 0
        while(num > 0):
            if num%2==0:
                num = int(num/2)
                ans +=1
            else: 
                num -= 1
                ans +=1
                
        return ans
            
