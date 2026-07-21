class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l = [0] * 26
        c = 0
        for le in s:
            l[ord(le) - ord('a')] += 1
            c += 1

        for le in t:
            if l[ord(le) - ord('a')] == 0:
                return False
            else:
                l[ord(le) - ord('a')] -= 1
                c -= 1

        if c != 0:
            return False

        return True

        
