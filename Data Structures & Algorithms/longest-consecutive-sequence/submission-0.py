class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        hm = {}

        hashed = set(nums)

        max_c = 0

        for guy in hashed:
            if guy not in hm:
                cur = guy
                count = 1
                while cur + 1 in hashed:
                    if cur + 1 in hm:
                        count += hm[cur + 1]
                        break
                    else:
                        count += 1
                        cur += 1

                
                hm[guy] = count
                max_c = max(count, max_c)

        return max_c
        