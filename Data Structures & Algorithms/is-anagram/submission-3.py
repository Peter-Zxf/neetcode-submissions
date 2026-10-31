class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def toInt(s:str) -> int:
            str_xor = 0
            char_sum = 0
            for char in s:
                c = ord(char)
                str_xor ^= c
                char_sum += c**2
            return str_xor + char_sum
        return toInt(s) == toInt(t)