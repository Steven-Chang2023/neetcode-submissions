class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        target = {}

        for letter in s1:
            if letter not in target:
                target[letter] = 0
            target[letter] += 1
        
        window = {}

        l = 0

        for r in range(len(s2)):
            window[s2[r]] = window.get(s2[r], 0) + 1
            if r - l + 1 > len(s1):
                window[s2[l]] -= 1
                if window[s2[l]] == 0:
                    window.pop(s2[l])
                l += 1
            
            if window == target:
                return True
    
        return False