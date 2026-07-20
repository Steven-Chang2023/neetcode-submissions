class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}

        res = 0
        maxf = 0
        l = 0

        for i in range(len(s)):
            if s[i] not in counts:
                counts[s[i]] = 0
            counts[s[i]] += 1

            maxf = max(maxf, counts[s[i]])

            while (i - l + 1) - maxf > k:
                counts[s[l]] -= 1
                l += 1

            res = max(res, i - l + 1)

        return res




                    
                    
                
        
            


           

        


            



       

