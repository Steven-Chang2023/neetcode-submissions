class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm  = {}
        for word in strs:
            freq = [0] * 26
            for letter in word:
                freq[ord(letter) - ord('a')] += 1
            val = tuple(freq)

            if val not in hm:
                hm[val]= [word]
            else:
                hm[val].append(word)
        output = []
        for key in hm:
            output.append(hm[key])

        return output