class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            l_status = ((ord('A') <= ord(s[l]) and ord('Z') >= ord(s[l])) or 
                    (ord('a') <= ord(s[l]) and ord('z') >= ord(s[l])) or
                    (ord('0') <= ord(s[l]) and ord('9') >= ord(s[l]))
                )
            r_status = ((ord('A') <= ord(s[r]) and ord('Z') >= ord(s[r])) or 
                    (ord('a') <= ord(s[r]) and ord('z') >= ord(s[r]))
                    or
                    (ord('0') <= ord(s[l]) and ord('9') >= ord(s[l]))
                )

            if not l_status and not r_status:
                l += 1
                r -= 1
            elif not l_status:
                l += 1
            elif not r_status:
                r -= 1
            else:
                if s[l].upper() != s[r].upper():
                    return False
                l += 1
                r -= 1
        return True