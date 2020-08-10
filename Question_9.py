"""
Solution for #9 Palindrome Number 
I have tried to solve this question with more easy and understandable way
But there are more solutions and you can try to find by yorself 
"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
		# Now we just make int -> str and check with its opposite view 
		# if its sam ethan it will be True otherwise False
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False