class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mz = 0
        sz = 0
        l = 0

        cur = ord('A')
        
        for i in range(26):
            tar = chr(cur + i)
            tc = 0 # keep count of target in window
            l = 0


            for j in range(len(s)):
                ws = j - l + 1

                if tar == s[j]:
                    tc += 1
                

                if ws - tc > k:
                    if tar == s[l]:
                        tc -= 1
                    l += 1
                
                sz = j -l + 1
            mz = max(mz, sz)


                #ws = j - l + 1
                #if tar == s[j]: 
                #    tc += 1
                #while (j - l + 1) - tc > k :
                #    if tar == s[l]:
                #        tc -= 1
                #    l += 1
                
                #mz = max(mz, j - l + 1)




        return mz


                    
                    
                
        
            


           

        


            



       

