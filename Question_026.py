# Alimov Abdullokh - solution using stack
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        stack = []
        for i in nums:
            if len(stack) > 0:
                if (stack[-1]) != i:
                    stack.append(i)
            else:
                stack.append(i)
        print(stack)
        print(len(stack))
        return len(stack)
