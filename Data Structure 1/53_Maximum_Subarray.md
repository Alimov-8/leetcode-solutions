# Leetcode 53. Max Sub Array
## Kadane's Algorithm to Maximum Sum Subarray Problem
```py
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = 0 
        max_sum = nums[0]
        for i in nums:
            cur_sum = max(i, cur_sum + i)
            
            if cur_sum > max_sum:
                max_sum = cur_sum
            
        return max_sum
```

 <img src="sources/Kadane's Algorithm.png"
     alt=""
     style="float: left; margin-right: 10px; margin-top: 5px; margin: 10px;" />  