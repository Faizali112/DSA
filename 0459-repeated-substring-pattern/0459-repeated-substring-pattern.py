class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        rep = ''
        length_s = len(s)

        for i in range (length_s // 2):
            rep += s[i]
            if length_s % len(rep) == 0:
                if rep * (length_s // len(rep)) == s:
                    return True
        return False
        
        