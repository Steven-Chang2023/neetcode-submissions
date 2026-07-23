class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        for num in nums:
            hm[num] = hm.get(num, 0) + 1
        
        freq = [0] * (len(nums)+1)

        for key in hm:
            realf = hm[key]
            if freq[realf] == 0:
                freq[realf] = []
            
            freq[realf].append(key)

        index = len(nums)

        output = []

        subindex = 0
        while len(output) < k:
            if freq[index] == 0:
                index -= 1
            elif subindex < len(freq[index]):
                output.append(freq[index][subindex])
                subindex += 1
            else:
                index -= 1
                subindex = 0
        
        return output

