class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        long = 0
        cur = 0

        hm = {}
        l = 0

        for i in range(len(s)):
            if s[i] not in hm:
                hm[s[i]] = 0   
                cur = len(hm)
                long = max(cur, long)
            else:
                while s[i] in hm:
                    hm[s[l]] -= 1
                    if hm[s[l]] == 0:
                        del hm[s[l]]
                    l += 1
                hm[s[i]] = 0
            hm[s[i]] += 1

                
            
        
        return long

            
                
            