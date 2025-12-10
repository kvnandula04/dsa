class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_char_count = {}

        for c in s:
            if c in s_char_count:
                s_char_count[c] += 1
            else:
                s_char_count[c] = 1

        for c in t:
            if c not in s_char_count:
                return False
            
            s_char_count[c] -= 1

            if s_char_count[c] < 0:
                return False
            
        for c in s_char_count:
            if s_char_count[c] != 0:
                return False
            
        return True