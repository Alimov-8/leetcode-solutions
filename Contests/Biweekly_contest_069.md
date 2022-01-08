# Alimov-8 | Biweekly Contest 69

## Rank: 4394/15120	 	
## Score: 12	
#

## Question 1

```py
# Time: 7 minutes
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title_list = title.split()
        answer = []
        for i in title_list:
            if len(i) > 2:
                answer.append(i.capitalize())
            else:
                answer.append(i.lower())
        return " ".join(answer)
```


## Question 2

```py
# Time: 30-35 minutes
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        
        lst = []

        while head is not None:
            lst.append(head.val)
            head = head.next
            
            
        n = len(lst)
        i = list(range(n//2))
        
        # find pairs
        d = {}
        for j in i:
            d[n-1-j] = j
            
        # max twin sum
        
        maxSum = 0
        
        for k in d.keys():
            curSum = lst[k]+lst[d[k]]
            if curSum > maxSum:
                maxSum = curSum
                
        return maxSum
        
```


## Question 3

```py
# Time: 23-25 minutes
class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        d = {}
        is_same = True  # 'aa' case
        answer = 0
        for word in words:                
            if word[::-1] in d.keys():
                answer = answer + 4
                if d[word[::-1]] > 2:
                    d[word[::-1]] -= 2
                else:
                    del d[word[::-1]]
            else:
                if word in d.keys():
                    d[word] += 2
                else:
                    d[word] = 2
                    
        for key in d.keys():
            if key[0] == key[1]:
                answer = answer + 2
                break
            
        return answer
```