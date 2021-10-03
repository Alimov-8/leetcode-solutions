"""
Solution for #13 Roman to Ineteger
"""
class Solution:
    def romanToInt(self, s: str) -> int:
        char_val = {
            "I" : 1,
            "IV" : 4,
            "V" : 5,
            "IX" : 9,
            "X" : 10,
            "XL" : 40,
            "L" : 50,
            "XC" : 90,
            "C" : 100,
            "CD" : 400,
            "D" : 500,
            "CM" : 900,
            "M" : 1000
        }

        i = 0
        result = 0

        while i < len(s):
            first = s[i]
            if i+1 < len(s):
                second = s[i + 1]
                two_elems = first + second
                if two_elems in char_val:
                    result += char_val[two_elems]
                    i += 2
                    continue
                else:
                    result += char_val[first]
                    i += 1
                    continue
            else:
                result += char_val[first]
                i += 1
                continue

        return result
