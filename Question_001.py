"""
Solution for the #1 Question in the LeetCode.com Web Site

------------------

list = [2,7,11,15]
target = 9
target = 2+7

Answer: 0,1 
 
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Creating Dictionary to save index of possible value
		# In the first loop it will be {7:0} 
		possible_nums = {}
        
        for i in range(len(nums)):
            if nums[i] in possible_nums:
                return possible_nums[nums[i]], i
            else:    
                possible_nums[target-nums[i]] = i
				
