"""
Solution for #7 Reverse Integer
"""

class Solution:
    def reverse(self, x: int) -> int:
        if x > (2**31 -1) or x < (-2**31):
            return 0
        if x >= 0:
            a = 0
            while x != 0:
                a = a * 10 + x % 10
                x = x // 10
            if a <= (2**31 - 1):
                return a
            return 0
        else:
            b = 0
            while x != 0:
                b = b * 10 + (x % -10)
                x = -(x // -10)
            if b >= (-2**31):
                return b
            return 0