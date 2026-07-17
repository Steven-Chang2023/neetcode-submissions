class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for word in strs:
            counts = [0] * 26
            for letter in word:
                counts[ord(letter) - ord('a')] += 1
            counts = tuple(counts)
            if counts in hm:
                hm[counts].append(word)
            else:
                hm[counts] = [word]
        
        output = []
        for value in hm.values():
            output.append(value)
    
        return output