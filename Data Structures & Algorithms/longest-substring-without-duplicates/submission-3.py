class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hm = {}
        # hash each character when re-encounter calculate longest
        longest = 0
        current_len = 0
        window_start = 0
        #abcdeb
        for i in range(len(s)):
            
            if s[i] in hm and window_start <= hm[s[i]]:
                window_start = hm[s[i]] + 1
                current_len = i - hm[s[i]]
                hm[s[i]] = i
                
            else:
                current_len += 1
                if current_len > longest:
                    longest = current_len
                hm[s[i]] = i
            print("l:" + str(longest) + " c:" +str(current_len))
        
        return longest
            